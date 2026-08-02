#!/usr/bin/env python3
"""Fail-closed integrity checks for the sanitized public evidence packet.

This verifier checks public-safe derivative files only. It does not inspect
private repository evidence, rerun the original engineering tests, or create
third-party validation.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


VERIFIER_ID = "PUBLIC_EVIDENCE_PACKET_VERIFIER_v0.3"
RESULT_SCHEMA = "public-evidence-verification-result.v0.2"
INDEX_SCHEMA = "public-evidence-index.v0.2"
RECEIPT_SCHEMA = "public-safe-receipt.v0.2"
ARTIFACT_STATUS = "PUBLIC_SAFE_CANDIDATE_NOT_PUBLISHED"
REVIEW_RELATIONSHIP = "INTERNAL_REVIEW_ONLY"
MARKET_OUTCOME = "NONE"
CURRENT_REPOSITORY_STATE = "PUBLIC"

ALLOWED_TECHNICAL_CLASSES = {
    "CONCEPT",
    "WORKING_ARTIFACT",
    "REPEATED_LOCAL",
    "LIVE_CONTEXT",
}
ALLOWED_EXTERNALITIES = {
    "LOCAL_REPOSITORY",
    "LOOPBACK_RUNTIME",
    "DEPLOYED_PROVIDER",
    "EXTERNAL_USER",
}
REQUIRED_CLAIM_FIELDS = {
    "public_claim_id",
    "statement",
    "technical_evidence_class",
    "execution_externality",
    "required_limitation",
    "claim_ceiling",
    "review_relationship",
    "market_outcome_state",
    "prohibited_inferences",
}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )


def load_json_object(
    path: Path, label: str, errors: list[str]
) -> tuple[dict[str, Any] | None, bytes | None]:
    try:
        payload = path.read_bytes()
    except OSError as exc:
        errors.append(f"{label} could not be read: {exc}")
        return None, None

    try:
        parsed = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label} is not valid UTF-8 JSON: {exc}")
        return None, payload

    if not isinstance(parsed, dict):
        errors.append(f"{label} must contain one JSON object")
        return None, payload

    return parsed, payload


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(nonempty_string(item) for item in value)
    )


def add_input(
    inputs: list[dict[str, str]], candidate_root: Path, path: Path, digest: str
) -> None:
    inputs.append(
        {
            "path": path.relative_to(candidate_root).as_posix(),
            "sha256": digest,
        }
    )


def packet_snapshot(inputs: list[dict[str, str]]) -> str:
    """Hash the verified input manifest without including the output result."""
    digest = hashlib.sha256()
    for item in sorted(inputs, key=lambda value: value["path"]):
        digest.update(item["path"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(item["sha256"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def validate_claim(
    claim: Any,
    receipt_id: str,
    position: int,
    observed_claim_ids: set[str],
    errors: list[str],
) -> str | None:
    label = f"{receipt_id} claim {position}"
    if not isinstance(claim, dict):
        errors.append(f"{label} must be an object")
        return None

    missing = sorted(REQUIRED_CLAIM_FIELDS - set(claim))
    if missing:
        errors.append(f"{label} missing fields: {', '.join(missing)}")

    claim_id = claim.get("public_claim_id")
    if not nonempty_string(claim_id):
        errors.append(f"{label} has an invalid public_claim_id")
        return None

    for field in ("statement", "required_limitation", "claim_ceiling"):
        if not nonempty_string(claim.get(field)):
            errors.append(f"{claim_id} has an invalid {field}")

    if claim.get("technical_evidence_class") not in ALLOWED_TECHNICAL_CLASSES:
        errors.append(f"{claim_id} has an invalid technical_evidence_class")

    if claim.get("execution_externality") not in ALLOWED_EXTERNALITIES:
        errors.append(f"{claim_id} has an invalid execution_externality")

    if claim.get("review_relationship") != REVIEW_RELATIONSHIP:
        errors.append(f"{claim_id} has an invalid review_relationship")

    if claim.get("market_outcome_state") != MARKET_OUTCOME:
        errors.append(f"{claim_id} has an invalid market_outcome_state")

    if not nonempty_string_list(claim.get("prohibited_inferences")):
        errors.append(f"{claim_id} must declare prohibited_inferences")

    if claim_id in observed_claim_ids:
        errors.append(f"duplicate public claim identifier: {claim_id}")
    observed_claim_ids.add(claim_id)
    return claim_id


def build_result(
    *,
    errors: list[str],
    inputs: list[dict[str, str]],
    receipt_results: list[dict[str, Any]],
    claim_count: int,
) -> dict[str, Any]:
    return {
        "schema_version": RESULT_SCHEMA,
        "verifier": VERIFIER_ID,
        "generated_at_utc": utc_now(),
        "decision": (
            "SANITIZED_PACKET_INTEGRITY_PASS"
            if not errors
            else "SANITIZED_PACKET_INTEGRITY_FAIL"
        ),
        "validation_scope": "SANITIZED_DERIVATIVE_ONLY",
        "underlying_event_proof": "NOT_EVALUATED",
        "independent_validation": "NONE",
        "publication_state": CURRENT_REPOSITORY_STATE,
        "publication_authority": "NOT_GRANTED_BY_VERIFIER",
        "receipt_count": len(receipt_results),
        "public_claim_count": claim_count,
        "checks": receipt_results,
        "verified_inputs": sorted(inputs, key=lambda item: item["path"]),
        "evidence_packet_snapshot_sha256": packet_snapshot(inputs),
        "snapshot_scope": (
            "Verifier source, public evidence index, and indexed sanitized "
            "receipt bytes; the generated result is excluded to avoid a "
            "self-referential hash."
        ),
        "errors": errors,
        "proof_boundary": (
            "Verifies sanitized packet integrity, claim metadata, and declared "
            "boundaries only; it does not prove the underlying private "
            "repository events."
        ),
    }


def run() -> tuple[dict[str, Any], int]:
    candidate_root = Path(__file__).resolve().parents[1]
    evidence_root = (candidate_root / "evidence").resolve()
    verifier_path = Path(__file__).resolve()
    index_path = evidence_root / "index.json"

    errors: list[str] = []
    inputs: list[dict[str, str]] = []
    receipt_results: list[dict[str, Any]] = []
    observed_claim_ids: set[str] = set()

    try:
        add_input(
            inputs,
            candidate_root,
            verifier_path,
            sha256_file(verifier_path),
        )
    except OSError as exc:
        errors.append(f"verifier source could not be hashed: {exc}")

    index, index_payload = load_json_object(index_path, "evidence index", errors)
    if index_payload is not None:
        add_input(
            inputs,
            candidate_root,
            index_path,
            sha256_bytes(index_payload),
        )

    if index is None:
        if not errors:
            errors.append("evidence index is unavailable")
        result = build_result(
            errors=errors,
            inputs=inputs,
            receipt_results=receipt_results,
            claim_count=0,
        )
        return result, 1

    if index.get("schema_version") != INDEX_SCHEMA:
        errors.append("evidence index schema_version is missing or unsupported")
    if index.get("artifact_status") != ARTIFACT_STATUS:
        errors.append("evidence index has an unexpected artifact_status")
    if index.get("current_repository_state") != CURRENT_REPOSITORY_STATE:
        errors.append("evidence index has an unexpected current_repository_state")
    if index.get("market_outcome") != MARKET_OUTCOME:
        errors.append("evidence index has an invalid market_outcome boundary")

    entries = index.get("receipts")
    if not isinstance(entries, list) or not entries:
        errors.append("evidence index must declare at least one receipt")
        entries = []

    for position, entry in enumerate(entries, start=1):
        entry_label = f"index receipt {position}"
        if not isinstance(entry, dict):
            errors.append(f"{entry_label} must be an object")
            continue

        receipt_id = entry.get("receipt_id")
        relative_path = entry.get("path")
        expected_hash = entry.get("sha256")
        expected_claim_ids = entry.get("public_claim_ids")

        if not nonempty_string(receipt_id):
            errors.append(f"{entry_label} has an invalid receipt_id")
            continue
        if not nonempty_string(relative_path):
            errors.append(f"{receipt_id} has an invalid path")
            continue
        if not (
            nonempty_string(expected_hash)
            and len(expected_hash) == 64
            and all(char in "0123456789abcdef" for char in expected_hash)
        ):
            errors.append(f"{receipt_id} has an invalid SHA-256 value")
        if not isinstance(expected_claim_ids, list) or not all(
            nonempty_string(item) for item in expected_claim_ids
        ):
            errors.append(f"{receipt_id} has an invalid public_claim_ids list")
            expected_claim_ids = []

        receipt_path = (evidence_root / relative_path).resolve()
        try:
            receipt_path.relative_to(evidence_root)
        except ValueError:
            errors.append(f"path escapes evidence root: {relative_path}")
            continue

        receipt, receipt_payload = load_json_object(
            receipt_path, f"receipt {receipt_id}", errors
        )
        if receipt_payload is None:
            continue

        actual_hash = sha256_bytes(receipt_payload)
        add_input(inputs, candidate_root, receipt_path, actual_hash)
        if actual_hash != expected_hash:
            errors.append(f"hash mismatch: {receipt_id}")

        if receipt is None:
            continue

        if receipt.get("schema_version") != RECEIPT_SCHEMA:
            errors.append(f"unsupported receipt schema: {receipt_id}")
        if receipt.get("receipt_id") != receipt_id:
            errors.append(f"receipt identity mismatch: {receipt_id}")
        if receipt.get("artifact_status") != ARTIFACT_STATUS:
            errors.append(f"unexpected artifact status: {receipt_id}")
        if receipt.get("review_relationship") != REVIEW_RELATIONSHIP:
            errors.append(f"review boundary missing: {receipt_id}")
        if receipt.get("market_outcome") != MARKET_OUTCOME:
            errors.append(f"market outcome boundary missing: {receipt_id}")
        if receipt.get("private_source_material_included") is not False:
            errors.append(f"private-source boundary missing: {receipt_id}")

        claims = receipt.get("public_claims")
        if not isinstance(claims, list) or not claims:
            errors.append(f"{receipt_id} must contain public_claims")
            claims = []

        receipt_claim_ids: list[str] = []
        for claim_position, claim in enumerate(claims, start=1):
            claim_id = validate_claim(
                claim,
                receipt_id,
                claim_position,
                observed_claim_ids,
                errors,
            )
            if claim_id is not None:
                receipt_claim_ids.append(claim_id)

        if receipt_claim_ids != expected_claim_ids:
            errors.append(f"claim mapping mismatch: {receipt_id}")

        receipt_results.append(
            {
                "receipt_id": receipt_id,
                "sha256": actual_hash,
                "sha256_match": actual_hash == expected_hash,
                "public_claim_count": len(receipt_claim_ids),
                "claim_metadata_complete": all(
                    isinstance(claim, dict)
                    and REQUIRED_CLAIM_FIELDS.issubset(claim)
                    for claim in claims
                ),
                "boundary_fields_present": all(
                    [
                        receipt.get("review_relationship")
                        == REVIEW_RELATIONSHIP,
                        receipt.get("market_outcome") == MARKET_OUTCOME,
                        receipt.get("private_source_material_included") is False,
                    ]
                ),
            }
        )

    result = build_result(
        errors=errors,
        inputs=inputs,
        receipt_results=receipt_results,
        claim_count=len(observed_claim_ids),
    )
    return result, 0 if not errors else 1


def main() -> int:
    try:
        result, exit_code = run()
    except Exception as exc:  # Fail closed even on an unexpected verifier defect.
        result = {
            "schema_version": RESULT_SCHEMA,
            "verifier": VERIFIER_ID,
            "generated_at_utc": utc_now(),
            "decision": "SANITIZED_PACKET_INTEGRITY_FAIL",
            "validation_scope": "SANITIZED_DERIVATIVE_ONLY",
            "underlying_event_proof": "NOT_EVALUATED",
            "independent_validation": "NONE",
            "publication_state": CURRENT_REPOSITORY_STATE,
            "publication_authority": "NOT_GRANTED_BY_VERIFIER",
            "receipt_count": 0,
            "public_claim_count": 0,
            "checks": [],
            "verified_inputs": [],
            "evidence_packet_snapshot_sha256": hashlib.sha256(b"").hexdigest(),
            "snapshot_scope": "Unavailable because the verifier failed closed.",
            "errors": [f"unexpected verifier failure: {type(exc).__name__}: {exc}"],
            "proof_boundary": (
                "No evidence conclusion is available because the verifier "
                "failed closed."
            ),
        }
        exit_code = 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
