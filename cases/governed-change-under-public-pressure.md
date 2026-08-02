# What Happened When We Put a Public AI-Governance Control Under External and Adversarial Pressure

Status: `CASE IN PROGRESS — OUTSIDER RESULT PENDING`

## Thirty-second version

The public Governed Change demo already shows one proposed repository change
moving from BLOCK to a bounded repair and then PASS under CAP, a Path Gate, a
Claims Gate, and hash-linked receipts.

The next test is harder: can someone outside the construction and review team
clone it, understand it, reproduce its fixed identities, and report where it
works or becomes confusing?

The public-validation successor is now published. It adds an exact
reproduction packet, a structured return form, a 15-case adversarial pack, and
bounded local timing evidence. Its first GitHub Actions run after publication
passed. No outsider result has been received. This page therefore records a
public test in progress, not an external-validation result.

## Problem

A repository can be technically runnable while still failing as public proof.
The commands may be unclear, failure cases may be scattered across tests, and
the author may mistake an internal rerun for independent evidence.

The practical question is:

> Can a reviewer who did not build this prototype run it from a clean public
> clone, see the same BLOCK → repair → PASS result, and explain what CAP and
> PASS do—and do not—mean?

## My role

I defined the public-validation objective, authority boundary, evidence
requirements, fixed identity checks, claim limits, and the distinction between
internal reproduction and outsider evidence. AI agents implemented and
reviewed bounded changes under those controls.

## Constraints

- Preserve the existing replay identity, receipt IDs, receipt hashes, and
  canonical replay size.
- Do not turn local timings into production or comparative claims.
- Do not describe “available to reproduce” as “independently reproduced.”
- Do not expose private repository machinery or internal source evidence.
- Keep publication, outreach, organization-profile changes, and repository
  pinning behind separate operator decisions.

## Architecture under test

```text
clean public clone
-> six-contract validation
-> BLOCK → repair → PASS demo
-> five-run replay identity check
-> named adversarial pressure pack
-> full test suite
-> structured PASS / FAIL / CONFUSED return
```

## Critical decisions

### Make confusion a valid result

The return form accepts `PASS`, `FAIL`, or `CONFUSED`. A confusing explanation
is evidence about the public product even when the code behaves correctly.

### Reuse the real negative tests

The adversarial pack names existing contract and failure tests instead of
copying their logic into a decorative second suite. It covers stale context,
revoked or expired authority, path attacks, policy drift, skipped gates,
prohibited claims, missing evidence, malformed input, unexpected gate states,
and gate-order invariance.

### Separate gate timing from repair timing

The local timing tool measures a lineage-free PASS evaluation separately from
the integrated BLOCK → repair → PASS process. It does not pretend revision 2
can bypass its required prior BLOCK receipt.

## What failed

The first timing-tool run failed closed for exactly that reason: it tried to
measure the repaired revision without supplying its prior receipt. The tool was
repaired before any timing result was accepted. A second defect expected a
human-readable demo string while the CLI correctly emitted JSON; that check
was also repaired before measurement.

These failures are useful because they show the evidence tooling being held to
the same lineage and output contracts as the demonstration.

## Verification completed locally

- 15/15 named adversarial cases passed.
- 76/76 full product-local tests passed.
- Six-contract validation passed.
- The integrated demo preserved BLOCK → repair → PASS.
- Five-run replay remained byte-identical at 25,194 canonical bytes.
- Replay identity remained
  `sha256:10a2135e3e8127ab8ed9d17759d8507e424d0aba2ad73afaa183bf9cf00778f4`.
- BLOCK receipt hash remained
  `sha256:1a2dd8d031b21da78390bbbcdb626bbdfa89ba628520194de17d69607fc9f505`.
- PASS receipt hash remained
  `sha256:54346099dfef791368c87c2b259e6399ebb683ec4a37e90880c0d05989e6e8d8`.

The fixed identities and local results above are now published at demo commit
[`13a9e8bd8b6aebaeca174a7d49d22f9a6226ac48`](https://github.com/Secondmindsystems/governed-change-demo/commit/13a9e8bd8b6aebaeca174a7d49d22f9a6226ac48).
The corresponding [public GitHub Actions run](https://github.com/Secondmindsystems/governed-change-demo/actions/runs/30767977358)
completed successfully. Neither publication nor CI success is outsider
reproduction.

## Result

The public-validation workband produced a published, reproducible proof packet.
The external result is unresolved.

This section will be updated only after:

1. an identifiable outsider returns the required environment, commit,
   commands, output, fixed identities, and relationship disclosure; and
2. the returned packet is checked for internal consistency.

## Limitations

- No outsider reproduction has been recorded.
- No customer, market, security, compliance, production, deployment, capacity,
  or scalability conclusion is supported.
- Local timings are not production benchmarks or comparative performance
  claims.
- The prototype evaluates declared fixture snapshots; it does not execute live
  repository changes.
- Publication and public CI do not establish independent outsider
  reproduction.

## Next evidence event

Invite one person outside construction and review to return a structured
`PASS`, `FAIL`, or `CONFUSED` report. Outreach remains separately authorized;
this case does not create that authority. Until a return is received, the
truthful state is:

> Anyone can verify the published demo. Recorded outsider reproduction remains
> pending.

The public evidence-return door is
[Governed Change Demo issue #1](https://github.com/Secondmindsystems/governed-change-demo/issues/1).
