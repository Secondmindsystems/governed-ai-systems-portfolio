# Start with the work you need to evaluate

I build agentic AI systems and the controls around them: permission checks, evaluation, developer safeguards, provider boundaries, and evidence showing what a system actually did.

The repository is structured as a navigation system, designed to route you from the responsibility you need to evaluate to the work and evidence that matter.

If you’re evaluating a specific engineering responsibility, start with the closest match below.

## Choose what you want to evaluate

| What you want to evaluate | Start here | What you can inspect |
| --- | --- | --- |
| Whether agent actions can be checked against explicit constraints | [Governed Change Demo](https://github.com/Secondmindsystems/governed-change-demo) | A runnable synthetic demo with deterministic PASS/BLOCK/HOLD behavior, automated tests, repair cases, replay checks, and execution receipts |
| Whether authorization is checked before a model request | [Authorization before inference](proof-summaries/authorization-before-inference.md) | First-party build records showing one-use permission checked before model transport and blocked on reuse |
| Whether an agent can stop cleanly when a repository action is refused | [The agent that obeyed the brake](cases/agent-obeyed-the-brake.md) | Refusal, recovery, and preserved evidence from one cooperative agent’s repository-change attempt |
| Whether an authorization failure can be diagnosed and repaired | [Permission required versus granted](cases/when-permission-required-was-mistaken-for-permission-granted.md) | The original failure, targeted repair, tests, and replay—with unresolved failures kept visible |
| Whether cloud services and APIs can be integrated under controlled conditions | [Two controlled provider tests](proof-summaries/two-controlled-provider-tests.md) | First-party records of separate Stripe test-mode and Cloud Run/Gemini tests, including recorded results and Firestore receipts |
| Whether sensitive repository paths can require explicit approval before a commit proceeds | [AI Protected Paths](https://github.com/Secondmindsystems/ai-protected-paths) | A local Git safeguard with configurable protected paths, one-use approvals, tests, installation instructions, and release-validation records |
| Whether the published evidence packet is internally consistent | [Verification instructions](evidence/verification/README.md) | A checker you can run to verify receipt hashes and claim mappings against the published packet |

Some links lead to runnable public code; others document work in private systems. Those build records are first-party accounts. The packet checker verifies published records, not the private events behind them. Each linked page explains its limits.

## A ten-minute review

Choose one route; you don’t need to read the whole portfolio.

1. Pick the responsibility closest to what you care about.
2. Open the linked case or implementation.
3. Inspect the evidence attached to it.
4. If the route is runnable, follow its instructions and compare your results. Try Git-hook tools in a disposable repository. For private-build records, follow the references into the [evidence index](evidence/EVIDENCE_INDEX.md).
5. Read [what the portfolio establishes and its limitations](CLAIM_BOUNDARIES.md), along with [how I worked with AI](methods/AUTHORSHIP_AND_AI_USE.md).

By the end, you should know what the work demonstrates and what would need additional evidence. Ten minutes is a suggested review budget, not a measured completion time.

If you’re interested in failure analysis, start with [Permission required versus granted](cases/when-permission-required-was-mistaken-for-permission-granted.md).

## Discuss a role or ask for more evidence

For production responsibilities, ask about sustained operation, incidents, customer exposure, team responsibilities, and deployment history separately. Local tests and controlled deployments do not establish those on their own.

Questions or challenges: use the [contact section](README.md#contact).
