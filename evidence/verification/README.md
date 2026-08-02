# Verify the Public Evidence Packet

Use Python 3.10 or later. From the candidate repository root, run the
following command in PowerShell, Command Prompt, macOS Terminal, or a Linux
shell:

```text
python tools/verify_public_evidence.py
```

The verifier uses only the Python standard library. It checks:

- the SHA-256 hash of each sanitized receipt;
- the receipt-to-claim mapping;
- duplicate public claim identifiers;
- required claim-level evidence, limitation, ceiling, review, outcome, and
  prohibited-inference fields;
- the internal-review and no-market-outcome boundaries;
- the declaration that private source material is not included;
- its own source hash, the evidence-index hash, and a deterministic snapshot
  hash for the files it verified.

Malformed, missing, or unsupported inputs produce a controlled failure result
instead of an unhandled traceback.

Expected result for this candidate:

```text
decision: SANITIZED_PACKET_INTEGRITY_PASS
receipts: 5
public claims: 26
```

When reporting an independent reproduction, include the operating system,
Python version, repository commit, exact command, exit code, and decision.
Until an identifiable reviewer returns that packet, independent verification
is available but recorded outsider reproduction remains pending.

The captured local result is
[VERIFICATION_RESULT_v0_2.json](VERIFICATION_RESULT_v0_2.json).

## Proof Boundary

This is a reproducible integrity check for the public evidence packet.

It does not prove the underlying private repository events, independently
re-run the original engineering tests, or create third-party validation.
It grants no disclosure or publication authority.
