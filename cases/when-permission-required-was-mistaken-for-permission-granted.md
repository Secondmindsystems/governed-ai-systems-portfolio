# When “Permission Required” Was Mistaken for “Permission Granted”

## Fix the guardrail, not the evidence

A repository gate produced two false-positive authorization findings. One
record said execution permission was still required; the other preserved an
earlier state in which implementation permission had been withheld. Neither
record granted current authority. The same refusal separately reported a
receipt-write error.

The integration stayed blocked. The refusal and source records remained
intact. A five-file repair corrected the evaluated classifier behavior and
replayed the recorded 127-path staged surface. The repaired gate returned
allow on that replay; this result did not authorize integration, commit, or
any downstream action.

## At a Glance

| Question | Answer |
| --- | --- |
| What failed? | The gate treated one unmet permission condition and one historical withheld-permission record as present-authority overclaims; the same refusal separately recorded a receipt-write error. |
| What did the system do? | Preserved the refusal, investigated the two findings, and kept the integration blocked. |
| What changed? | One classifier, two existing test modules, and two evidence records. |
| What stayed untouched? | Both records that triggered the false findings. |
| What proved the repair? | 88 focused tests, 200 subtests, a 58-case internal authorization-state review against recorded artifact hashes, and two recorded staged-state gate evaluations. |
| What remains unproven? | Production reliability, external validation, broad adversarial robustness, and a universal full-suite pass. |

## The Two-Sided Guardrail Problem

A useful guardrail must survive two opposite tests:

```text
valid boundary
-> correct refusal
-> recovery through an already permitted route

defective control interpretation
-> incorrect refusal
-> preserve the stop
-> repair the control
-> replay the recorded staged surface
```

The first protects the system from unauthorized movement. The second preserves
useful work while a defective control is repaired, then checks that the
declared fail-closed cases still block in the evaluated fixture set.

## The Authorization-State Classifier Was Wrong

The gate was supposed to stop repository changes that claimed more authority
than the evidence supported.

It found two records containing authority-related language and blocked the
integration. That fail-closed response was appropriate under uncertainty. The
problem was what the classifier thought the records meant.

One record said a future execution permission was still required. The other
was a historical checkpoint showing that implementation permission had been
withheld. Neither record granted current authority.

The original refusal recorded two authorization-classification findings plus one
separate fail-closed receipt-storage internal error. This case does not rewrite
that multi-cause refusal as a single-cause event.

## Why Keyword Matching Was Not Enough

The gate had to distinguish the role a permission statement played under its
declared rules, not merely detect permission-related words.

> Permission words are not permission states.

These statements use similar words but imply different actions:

| Meaning | Operational consequence |
| --- | --- |
| Required | Permission is necessary and has not yet been supplied. |
| Requested | A decision is pending. |
| Denied | A qualified authority rejected the action. |
| Absent | No qualifying permission record exists. |
| Granted | The record matches a recognized operative grant shape. That classification alone does not authorize execution. |
| Ambiguous | The record cannot support a deterministic conclusion. |
| Specifically bounded historical state | A narrowly identified or expired record can be treated as non-operative only when the declared rules prove it cannot grant present authority; otherwise it remains ambiguous. |

Only a qualifying current grant can satisfy this classifier's
authority-evidence condition. Permission to execute remains a separate
downstream decision.

```text
required != granted
requested != granted
denied != granted
absent != granted
ambiguous != granted
historical != current grant
```

## Why Bypass Was the Wrong Repair

An incorrect refusal does not make bypass legitimate.

Disabling the gate, suppressing the finding, or rewriting the records would
have erased the evidence needed to understand the failure. The repair instead
followed one rule:

> Correct the control that interpreted the evidence. Do not alter the
> evidence to satisfy the control.

The integration remained blocked until a five-file repair scope had been
recorded.

## The Five-Path Repair

The repair changed exactly five paths:

- one gate implementation;
- two existing test modules;
- one adjudication record;
- one validation record.

Neither source record that triggered the false findings was edited. No
filename allowlist was added. No global authority rule was disabled. No gate
bypass, runtime permission, downstream execution authority, product change,
or commit permission was created by the repair record.

The classifier was changed to distinguish the evaluated non-grant and grant
shapes while continuing to block unsupported, malformed, contradictory, or
ambiguous authority-bearing fixtures.

## Verification

### 1. Focused repair tests

The focused suite completed:

- 88 tests passed;
- 200 subtests passed;
- 0 failures;
- 0 errors;
- 0 skips.

### 2. Internal authorization-state review

The validation record reports that an internal authorization-state review
evaluated 58 declared cases against recorded gate and test hashes without
mutating state.

Result: **58 of 58 passed**.

The commit-preserved record does not independently prove reviewer role
separation or third-party validation.

### 3. Replay of the recorded staged surface

The recorded 127-path staged surface was replayed after the repair. The
retained evidence proves the path-list identity and both triggering blobs, but
does not preserve a tree identity for every pre-repair blob.

Result:

```text
decision: allow
blocking findings: 0
structured authority blocks: 0
internal errors: 0
```

### 4. Evaluation of the final repaired state

The final 132-path surface—the preserved integration plus the five repair
paths—was then evaluated by the live local gate.

Result:

```text
decision: allow
blocks: 0
internal errors: 0
bypass used: no
```

## What Did Not Pass

The broader test evidence still contained:

- eight known baseline failures in the repository-control suite;
- one inherited historical failure in an adjacent suite.

Those failures remained visible. The repair introduced no new
repair-linked failures in the broader repository-control run, but it did not
turn the whole system into a passing system.

The supported conclusion is:

> The identified authorization-state classification defect was repaired in the evaluated
> repository state.

The unsupported conclusion is:

> The entire system passed.

## Repository Record

The repaired integration was later recorded as a two-parent merge commit on a
dedicated integration branch. At the last internal verification, that commit
was not part of the repository’s local mainline.

The exact private Git identity remains in the sealed derivation map. Publishing
an unresolvable private commit identifier would create the appearance of
public inspectability without providing it.

## Engineering Capabilities Demonstrated

- structured authorization-state classification;
- policy and controls as code;
- fail-closed repository governance;
- false-positive control repair;
- five-file repair scope;
- immutable historical-evidence preservation;
- deterministic regression testing;
- recorded staged-state replay;
- internal authorization-state review against recorded artifact hashes;
- residual-failure reporting;
- Git lineage awareness;
- disciplined claim qualification.

## Why This Matters for AI Systems

Agent authorization increasingly depends on interpreting what a policy or
record actually permits. A system that only detects permission-related words
can fail in both directions:

1. allow an action that was never authorized; or
2. block a lawful action because a record merely discussed permission.

This case demonstrates the second failure mode and, within the evaluated
fixtures and repository states, a repair that retained the declared
fail-closed protections.

That pattern is relevant to:

- AI governance engineering;
- agent authorization;
- policy-engine development;
- controls-as-code;
- AI platform gates;
- evaluation and auditability;
- secure AI enablement;
- technical responsible-AI programs.

## Claim Boundary

This case demonstrates a bounded, repository-local repair of one
authority-classification defect. It does not establish:

- enterprise production reliability;
- regulatory compliance or certification;
- broad adversarial robustness;
- a universal full-suite pass;
- independent proof of the original repair authorization beyond the
  adjudication record;
- external third-party validation;
- customer adoption;
- commercial impact.

The sanitized claim record is
[PSR-AUTHORITY-SEMANTICS-v0.1.json](../evidence/public-safe-receipts/PSR-AUTHORITY-SEMANTICS-v0.1.json).
The [public evidence index](../evidence/EVIDENCE_INDEX.md) lists the atomic
claims and limitations.

## Authorship and AI Use

Tavio Lawrence defined the intended behavior, authority distinctions, repair
boundaries, acceptance conditions, evidence requirements, and claim limits.
AI agents performed bounded implementation, analysis, drafting, and
internal review under those controls.

Internal agent review is not represented as independent third-party
validation.
