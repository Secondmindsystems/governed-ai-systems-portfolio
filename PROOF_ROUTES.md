# Requirement → claim → evidence → limit

Tavio Lawrence's focus is agentic AI systems and controls: permission checks,
evaluation, developer safeguards, and inspectable execution evidence. This is
a responsibility-based navigation page, not a claim of employment seniority.

## Choose the responsibility you need to evaluate

| Responsibility | Start with | Proof mode | What remains unproven here |
| --- | --- | --- | --- |
| Evaluate agent actions against explicit constraints | [Governed Change demo](https://github.com/Secondmindsystems/governed-change-demo) | PUBLIC_DEMONSTRATION: separately runnable synthetic example | Production agent reliability and reproduction of the private systems |
| Check authorization before a model request | [Authorization before inference](proof-summaries/authorization-before-inference.md) | PUBLIC_HISTORICAL_EVIDENCE: sanitized first-party account | Public reproduction of the original runtime |
| Recover from a refused repository change | [The agent that obeyed the brake](cases/agent-obeyed-the-brake.md) | PUBLIC_HISTORICAL_EVIDENCE: bounded cooperative episode | Protection against a malicious or non-cooperative agent |
| Diagnose and repair an authorization classifier | [Permission required versus granted](cases/when-permission-required-was-mistaken-for-permission-granted.md) | PUBLIC_HISTORICAL_EVIDENCE: internal repair and replay | Universal correctness or production qualification |
| Integrate providers under controlled test conditions | [Two controlled provider tests](proof-summaries/two-controlled-provider-tests.md) | PUBLIC_HISTORICAL_EVIDENCE: separate bounded provider tests | Simultaneous provider operation, customer adoption, or production scale |
| Verify an evidence packet's internal consistency | [Verification instructions](evidence/verification/README.md) | PUBLIC_REPRODUCTION route for the packet checker only | Authenticity or reproduction of the underlying private events |

Proof-mode labels describe the object being inspected. Publicly readable
historical evidence can still be first-party evidence. A runnable synthetic
demonstration is not a reproduction of a private implementation. An available
reproduction route does not mean an outside person has run it.

## A ten-minute review route

This is a suggested time budget, not measured human-comprehension evidence.

1. Select one responsibility above and read its case and limitation.
2. For historical cases, follow their pointers into the [evidence index](evidence/EVIDENCE_INDEX.md). For the synthetic example, stay in the separate demo repository and inspect its proof and reproduction artifacts. For packet integrity, use the checker's own instructions and result.
3. Run the [packet checker](evidence/verification/README.md) if evaluating packet integrity, or follow the separate demo repository's instructions if evaluating synthetic behavior.
4. Read [claim boundaries](CLAIM_BOUNDARIES.md) and [authorship and AI use](methods/AUTHORSHIP_AND_AI_USE.md).
5. State which bounded claim the evidence supports and which stronger claim it does not.

For failure analysis, start with the authorization-classifier repair. For
production hiring, ask separately about sustained operation, incidents,
customer exposure, team responsibilities, and employment history; these
cannot be inferred from this packet.

## Opportunity decisions

Route existing evidence before proposing new credential work. If a role needs
production-scale operation rather than local or bounded-test behavior, a
clear explanation is not a substitute for that missing evidence. Conversely,
do not require another implementation merely because an existing proof was
hard to find.

Questions or challenges: use the [contact section](README.md#contact).
