# Public Evidence Index

Status: `PUBLIC`

Last reviewed: 2026-08-02

The repository containing this packet is public. The machine-readable receipts
retain the artifact status recorded when they were created; that historical
candidate status is provenance, not a claim that this repository remains
unpublished.

## How to Read This Index

Each public claim has:

- a public evidence identifier;
- one bounded statement;
- an evidence class;
- the environment in which the event occurred;
- a limitation that travels with the claim.

The exact private source crosswalk remains sealed. Public identifiers do not
reveal private paths, commits, branch names, raw receipts, private control
implementation, private control topology, or bypass-relevant details.

## Evidence Classes

**Live-context evidence** means the behavior ran against a real local gate,
runtime, hook, deployment, or provider interface. It does not automatically
mean production, customer-facing operation, or external validation.

**Repeated local evidence** means focused tests or controlled local executions
reproduced the behavior. It is not a production reliability benchmark.

**Working artifact** means an implemented document or software artifact exists
and received bounded verification.

## The Agent That Obeyed the Brake

| Public ID | Supported statement | Evidence class | Environment | Required limitation |
| --- | --- | --- | --- | --- |
| `PBR-01` | During one repository task, an active pre-commit gate blocked one proposed file change. | Live context | Local repository | One cooperative event; not a many-agent or adversarial study. |
| `PBR-02` | The agent did not bypass the gate. It reverted the edit and left both the file and gate unchanged. | Live context | Local repository | Cooperative compliance does not prove that a hostile actor cannot bypass the control. |
| `PBR-03` | A recovery route already defined in the task plan let the agent complete the five-change scope without gaining new permission, and 13 focused tests passed. | Repeated local | Local repository | The focused tests do not establish general agent safety or product reliability. |

Machine-readable summary:
[PSR-BRAKE-v0.1.json](public-safe-receipts/PSR-BRAKE-v0.1.json)

## Authorization Before Inference

| Public ID | Supported statement | Evidence class | Environment | Required limitation |
| --- | --- | --- | --- | --- |
| `PAI-01` | The local runtime checked one-use permission before contacting the model and allowed exactly one authorized call. | Live context | Same-machine runtime | Local and non-production; no remote provider or external action. |
| `PAI-02` | After the permission was used, the runtime rejected a second attempt before sending another model request. | Live context | Same-machine runtime | One consumed-permission path does not establish broad hostile-caller resistance. |
| `PAI-03` | The answer remained review-only text and could not authorize or execute another action. | Live context | Same-machine runtime | No downstream action system was exercised. |
| `PAI-04` | Seventy focused tests passed before the local, non-production run. | Repeated local | Same-machine runtime | The suites are not a production reliability benchmark. |
| `PAI-05` | A separate earlier local smoke test produced the expected non-empty response, then stopped a second attempt before another model request was sent. | Repeated local | Same-machine runtime | Two episodes are corroboration, not a statistical reliability study. |

Machine-readable summary:
[PSR-AUTHORIZATION-v0.1.json](public-safe-receipts/PSR-AUTHORIZATION-v0.1.json)

## Two Controlled Provider Tests

| Public ID | Supported statement | Evidence class | Environment | Required limitation |
| --- | --- | --- | --- | --- |
| `PPR-01` | In a deployed test environment, Stripe test mode processed checkout and webhook events, created temporary test access, and issued a one-time access token without charging a real customer or storing the raw token. | Live context | Deployed provider test | Test mode and synthetic identities only. |
| `PPR-02` | During the Stripe test, Gemini remained simulated rather than making a real model call. | Live context | Deployed provider test | The payment and model-provider tests did not run simultaneously. |
| `PPR-03` | The Stripe test was accompanied by 101 passing backend and tool tests. | Repeated local | Provider-integration test state | The tests do not establish production reliability. |
| `PPR-04` | A deployed Cloud Run test made one authorized Gemini call and stored the review receipt and provider-usage record in Firestore. | Live context | Deployed provider test | One call does not establish continuous service or customer use. |
| `PPR-05` | During the Gemini test, Stripe was not live, and the AI service returned to simulated mode afterward. | Live context | Deployed provider test | One restoration event is not a general rollback system. |
| `PPR-06` | The deployed Gemini test was accompanied by 118 passing tool and backend tests. | Repeated local | Provider-integration test state | The tests do not establish continuous production reliability. |
| `PPR-07` | The system completed two separate provider tests: a Stripe test-mode workflow and, later, one deployed Gemini call. Gemini and Stripe were not live together in either cited test. | Live context | Two deployed test episodes | The two episodes may not be presented as one simultaneous live workflow. |

Machine-readable summary:
[PSR-PROVIDERS-v0.1.json](public-safe-receipts/PSR-PROVIDERS-v0.1.json)

## When “Permission Required” Was Mistaken for “Permission Granted”

| Public ID | Supported statement | Evidence class | Environment | Required limitation |
| --- | --- | --- | --- | --- |
| `PAS-01` | A live local repository gate blocked a 127-path staged integration after classifying two authority-related records as authority overclaims; the same refusal also recorded a separate receipt-storage defect. | Live context | Local repository | The original refusal recorded two authorization-classification findings plus one separate fail-closed receipt-storage internal error; it must not be presented as a single-cause event. |
| `PAS-02` | Adjudication found that one record described permission still required and the other preserved a historical state in which permission had been withheld; neither record was a current permission grant. | Working artifact | Local repository | This conclusion is bounded to the two adjudicated records. |
| `PAS-03` | The repair changed exactly five paths: one gate implementation, two existing test modules, and two evidence records; neither triggering source record was edited. | Working artifact | Local repository | The adjudication records bound the five-file repair scope; independent proof of the original repair authorization beyond the adjudication record was not preserved in the cited commit. |
| `PAS-04` | The repaired classifier distinguished required, requested, denied, absent, granted, and ambiguous authority states, and recognized specifically bounded historical states as non-operative, while retaining fail-closed treatment for unsupported or ambiguous authority. | Repeated local | Local repository | The authorization-state coverage is bounded to the implemented fixtures, rules, and evaluated repository state. |
| `PAS-05` | The focused repair suite passed 88 tests and 200 subtests with zero failures, errors, or skips. | Repeated local | Local repository | Focused passing tests are not a production reliability benchmark. |
| `PAS-06` | The validation record reports that an internal authorization-state review passed all 58 declared cases against recorded gate and test hashes without mutating state. | Repeated local | Local repository | The commit-preserved record does not independently prove reviewer role separation or third-party validation. |
| `PAS-07` | After repair, replay of the recorded 127-path staged surface returned allow with zero blocking findings, zero structured authority blocks, and zero internal errors. | Live context | Local repository | The replay result is bounded to the recorded 127-path staged surface and repaired local gate. |
| `PAS-08` | The final 132-path staged state returned allow with zero blocks, zero internal errors, and no gate bypass. | Live context | Local repository | A passing local gate result did not itself authorize a commit, downstream execution, runtime activation, deployment, or external action. |
| `PAS-09` | Eight known repository-control baseline failures and one inherited historical failure in an adjacent suite remained visible; no universal full-suite pass was claimed. | Repeated local | Local repository | The authority repair resolved its identified defect without resolving those residual failures. |
| `PAS-10` | The repaired integration was later recorded in a two-parent merge commit on a dedicated integration branch that was not part of the local mainline at internal verification on 2026-07-29. | Working artifact | Local repository | The earlier repair receipt neither authorized nor performed that later commit. |

Machine-readable summary:
[PSR-AUTHORITY-SEMANTICS-v0.1.json](public-safe-receipts/PSR-AUTHORITY-SEMANTICS-v0.1.json)

## Sentence-Level Evidence Method

| Public ID | Supported statement | Evidence class | Environment | Required limitation |
| --- | --- | --- | --- | --- |
| `PEM-01` | The 25 engineering-event claims shown in this candidate have public identifiers and private derivation entries recording their reviewed source claims, evidence class, execution setting, and required limitation. | Working artifact | Local repository | The derivation records and their review are internal; this mapping does not independently prove the underlying events. |

Machine-readable summary:
[PSR-EVIDENCE-METHOD-v0.2.json](public-safe-receipts/PSR-EVIDENCE-METHOD-v0.2.json)

The sanitized derivative hashes and claim-to-receipt mapping are recorded in
[index.json](index.json). These hashes identify the public-safe candidates;
they do not expose or substitute for the sealed private source identities.

The [sanitized packet integrity checker](verification/README.md) checks all five
sanitized receipts, their 26 claim identifiers, claim-level boundary fields,
and the hashes declared in the index. Its pass state is limited to sanitized
packet integrity; it does not evaluate the private events.

## Review Independence

The underlying events and this public transformation received internal review.
No case is presented as independently validated by a third party.

## Market Outcome

`NONE`

The evidence establishes technical events. It does not establish customer
adoption, revenue, measured business improvement, or market fit.
