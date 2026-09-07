# Tavio Lawrence

## AI Systems & Harness Engineer

I build harnesses around AI models that shape how they reason, use context, stay within boundaries, evaluate their work, recover from failure, and produce evidence about what they did.

Those harnesses operate around the model rather than changing its weights. They give the same underlying AI more structure for handling complex work: reasoning guidance, behavioral constraints, authority, evaluation, continuity, and evidence.

My public work includes a
[runnable change-evaluation demo](https://github.com/Secondmindsystems/governed-change-demo),
a [local Git safeguard](https://github.com/Secondmindsystems/ai-protected-paths)
that requires approval for selected file paths, and engineering case studies
showing how I investigated failures and repaired controls.

The repository is structured as a navigation system, designed to route you
from the responsibility or capability you want to evaluate to the work and
evidence that matter.

**[Start with a responsibility or capability →](PROOF_ROUTES.md)**

![Governed execution flow](assets/governed-execution-flow.svg)

My work focuses on a practical question:

> What can we build around an AI model to make more of its capability usable in real work?

The cases show different parts of that problem: how agents handle boundaries, how authorization affects execution, how useful work can continue after a refusal, how failures are evaluated and repaired, and how evidence about those decisions is preserved.

For a runnable public example, see
[One Change, Two Gates, One Receipt](https://github.com/Secondmindsystems/governed-change-demo).

## Selected Applied Systems Work

### [Translate institutional rules into controls](https://github.com/Secondmindsystems/mark-cuban-pbm-contract-contribution-repost)

This work examines how purchaser protections in Mark Cuban's open-source PBM agreement can change as the agreement moves through procurement, negotiation, completed exhibits, implementation, and later amendments.

We developed a controlled-adaptation approach for surfacing material deviations, deciding them explicitly, and reconciling the completed agreement against what was approved.

**[Mark Cuban reposted our resulting contribution on LinkedIn.](https://www.linkedin.com/analytics/post/urn:li:activity:7500402183310565376/?resultType=RESHARES)**

[Inspect the analysis, delivered artifacts, and evidence →](https://github.com/Secondmindsystems/mark-cuban-pbm-contract-contribution-repost)

## Start Here

Exploring a capability or hiring for a specific responsibility? Use the
[work and evidence routes](PROOF_ROUTES.md) to find a relevant example
and see what you can inspect or run.

### [The Agent That Obeyed the Brake](cases/agent-obeyed-the-brake.md)

In one local execution, an active repository control refused a proposed change. The agent did not
bypass the control. It reverted the edit and finished the bounded task through
a recovery route already defined in the plan.

**Why it matters:** the agent remained useful after encountering a boundary without inventing new permission.

## Supporting Engineering Evidence

### Operational Campaign case

#### [Persistent Campaigns Without Authority Expansion](cases/persistent-campaigns-without-authority-expansion.md)

A bounded local Codex intake path was adversarially repaired, rechecked,
exercised with one campaign-shaped and one ordinary objective, and accepted
with a documented Windows path limitation. It was published after separate
internal claim and IP review and explicit operator authorization.

### [Authorization Before Inference](proof-summaries/authorization-before-inference.md)

A local AI runtime checked one-use permission before contacting a model,
allowed one call, consumed that permission, and stopped the next attempt before
another model request was sent.

**Capability shown:** authorization design, local-model integration, and
separation between generated text and permission to act.

### [Two Controlled Provider Tests](proof-summaries/two-controlled-provider-tests.md)

A review service completed two separate provider tests: a Stripe test-mode
workflow and, later, one deployed Gemini call. The providers were not live
together, and the service returned to simulated mode after the model test.

**Capability shown:** cloud and provider integration with explicit test
boundaries, evidence persistence, and restoration to simulated mode.

### Technical Deep Dive — Failure-Preserving Integration

#### [When “Permission Required” Was Mistaken for “Permission Granted”](cases/when-permission-required-was-mistaken-for-permission-granted.md)

A local repository gate misclassified two non-grant records: one said execution
permission was still required, while the other preserved an earlier state in
which implementation permission had been withheld. The same refusal recorded
a separate receipt-write error. The integration stayed blocked while the
refusal and source records were preserved. A five-path repair corrected the
evaluated classifier behavior, replayed the recorded 127-path staged surface,
and then evaluated the final 132-path staged state.

**Capability shown:** structured authorization-state classification,
controls-as-code, bounded control repair, staged-state replay, and
residual-failure reporting.

## Why This Matters to Teams

A capable model is only one part of a working AI system. The harness around it shapes what context it receives, how work is structured, how it handles boundaries, what happens when something fails, how results are evaluated, and what evidence comes back.

The systems in this portfolio demonstrate parts of that surrounding structure across separate implementations: an agent recovering after a refused action, permission being checked before a model request, controls being repaired without erasing the failure that exposed the defect, and provider interactions being tested under explicit conditions.

I build that surrounding structure so agents can carry useful work through boundaries, failures, and review.

## Demonstrated Capabilities

| Capability | Evidence |
| --- | --- |
| Harness and agent-system design | Across separate implementations, the public work demonstrates parts of the structure around AI models: behavior, authority, evaluation, recovery, continuity, and evidence. |
| Structured behavior around tasks | [Behavior Profiles](https://github.com/Secondmindsystems/Behavior-Profiles) makes task boundaries, allowed actions, stopping conditions, and completion reporting explicit for AI coding agents. |
| Authority before consequence | Permission was checked before a local model request was sent. |
| Controls that affect real work | A live pre-commit gate blocked one proposed repository change. |
| Bounded refusal and authorized recovery | A blocked edit was reverted and the task continued only through a route already present in the plan. |
| Continuity across longer work | [Persistent Campaigns Without Authority Expansion](cases/persistent-campaigns-without-authority-expansion.md) documents a bounded local path that preserved revisioned state across re-entry while keeping authority transitions explicit. |
| Structured authorization-state classification | A repository control was repaired to distinguish present-state permission meanings and specifically bounded historical records. |
| Failure-preserving control repair | The incorrect refusal and triggering records remained intact while the control and its focused evidence surfaces were repaired. |
| Generated output kept inert | Local model output remained review-only text with no tool call or external effect. |
| Cloud and API implementation | Separate Stripe test-mode and deployed Gemini tests crossed real provider interfaces. |
| Deterministic evaluation | The public work includes fixed fixtures, focused tests, replay checks, structural checks, and structured evidence. |
| Evidence-producing workflows | Cases preserve execution results, failures, receipts, and scoped evidence so later claims can be traced back to what actually happened. |

Each case includes its own focused tests and scoped evidence record.

## Evidence at Two Speeds

If you have thirty seconds, read the flagship case.

If you are reviewing the evidence trail, inspect:

- the [public evidence index](evidence/EVIDENCE_INDEX.md);
- the [execution-under-pressure architecture](architecture/governed-execution-under-pressure.md);
- the machine-readable receipts (which preserve their historical candidate
  status) in
  `evidence/public-safe-receipts/`;
- the [evidence method](methods/EVIDENCE_METHOD.md);
- the [claim boundaries](CLAIM_BOUNDARIES.md).

You can also run the
[sanitized packet integrity checker](evidence/verification/README.md), which checks
sanitized receipt hashes, claim identifiers, and claim-level boundary fields.
It fails closed on malformed or missing inputs and emits hashes for its source,
index, receipts, and verified packet snapshot. It verifies the internal
integrity of this public packet.

Anyone can independently verify the published evidence packet:

```text
git clone https://github.com/Secondmindsystems/governed-ai-systems-portfolio.git
cd governed-ai-systems-portfolio
python tools/verify_public_evidence.py
```

The expected decision is `SANITIZED_PACKET_INTEGRITY_PASS`, covering five
sanitized receipts and 26 public claims. This repository makes independent
verification possible. A recorded outsider reproduction remains pending until
an identifiable reviewer returns the environment, commit, command, and result.

## Work in Progress

### [What Happened When We Put a Public AI-Governance Control Under External and Adversarial Pressure](cases/governed-change-under-public-pressure.md)

The runnable Governed Change demo publishes an outsider reproduction route, a
named adversarial test pack, bounded local timing evidence, and a passing
public GitHub Actions run. This case remains explicitly in progress until an
identifiable outsider returns a result.

**Current evidence:** published runnable artifacts, local adversarial and
timing results, and public CI success.

## Contact

I'm open to engineering roles, consulting, and technical collaboration involving AI harnesses, agentic systems, reasoning and behavior infrastructure, evaluation, context and runtime architecture, developer tooling, and governed AI execution.

**[secondmindsystems@gmail.com](mailto:secondmindsystems@gmail.com)**

Also reachable through the
[Second Mind Systems GitHub profile](https://github.com/Secondmindsystems).

## Use of These Materials

© Second Mind Systems. Published for inspection and evaluation. No license is
granted to copy, modify, redistribute, or reuse these materials except as
permitted by law.
