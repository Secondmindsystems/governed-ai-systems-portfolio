# Persistent Campaigns Without Authority Expansion

Status: `PUBLISHED — BOUNDED LOCAL EVIDENCE`

## Thirty-second version

A bounded local Codex intake path was built to distinguish ordinary work from
work that requires persistent state, multiple phases, review cycles, and
explicit authority transitions.

The first implementation was not accepted on design intent alone. It was
subjected to adversarial review, repaired at the root, re-attacked, installed
on one local module/CLI surface, exercised with one campaign-shaped objective
and one ordinary objective, and independently reviewed inside the project.

The result was accepted with a documented limitation: deep Windows state-root
paths can fail before activation. That failure is visible and leaves no
authoritative state residue, but projected-path preflight is not implemented.

## Problem

Long-running AI-assisted work is often managed as a sequence of disconnected
prompts. That creates two opposing risks:

- useful work repeatedly stops for ordinary implementation decisions; or
- continuity is mistaken for permission and the agent silently expands its
  authority.

The engineering question was:

> Can one bounded operating path preserve a goal and revisioned state across
> phases while still returning to the operator at genuine authority
> boundaries?

## My role

I defined the operating objective, authority model, state and re-entry
requirements, acceptance gates, claim ceiling, and sovereign stop conditions.
AI agents performed bounded implementation, adversarial review, repair,
reproduction, and evidence drafting under those controls.

The independent reviews described here were performed by separate internal AI
review roles. They are not third-party validation.

## Public-safe architecture

```text
outcome statement
-> structural classification
-> consolidated authority and state proposal
-> accepted revisioned state
-> governed continuation across phases
-> evidence and independent internal review
-> sovereign stop or accepted closure
```

The implementation separates four concerns:

1. Classification decides whether the objective has campaign-shaped
   structure.
2. Authority decides whether state may be created or changed.
3. Program state preserves accepted truth across re-entry.
4. Review and operator gates decide whether evidence supports transition or
   closure.

Classification cannot create authority. Re-entry cannot widen an accepted
envelope. A successful trial cannot declare its own permanent acceptance.

## What early review rounds found

The initial adapter was directionally correct but did not yet justify
installation. Review pressure exposed defects that mattered to the authority
boundary:

- campaign qualification was too dependent on vocabulary instead of the
  structure of the requested work;
- caller-supplied facts could influence qualification, so their provenance
  needed an explicit trust model;
- interrupted state materialization needed recovery tests for partially
  written lanes; and
- re-entry needed to compare the accepted authority envelope itself, not rely
  on a familiar reference alone.

These findings produced repair, not claim narrowing around an unchanged
implementation.

## Root repairs

The repaired path:

- qualifies work from multiple structural signals such as persistent state,
  cross-session continuity, authority transitions, review cycles, multiple
  actors, and a program-level terminal scope;
- keeps ordinary bounded work in an ordinary workband;
- treats agent-derived and unverified facts as classification-only input that
  cannot carry activation grants;
- requires operator-supplied facts to include a provenance reference and a
  complete authority envelope;
- returns missing grants in one consolidated response;
- denies authority widening before governed work begins;
- recovers exact matching partial materialization while denying mismatched
  state; and
- provides a visible, receipted per-objective bypass.

## Verification

Two internal review seams tested different burdens.

The pre-install review reproduced 67 focused tests. It also simulated a
failure during state materialization, confirmed that no stranded files
remained, verified recovery from both state-only and workband-only partial
lanes, and confirmed that mismatched envelopes were denied.

The post-install review reproduced 72 focused and adjacent tests in fresh
processes. It verified that:

- one campaign-shaped objective re-entered compatible persisted state;
- one ordinary objective remained an ordinary workband and created no state
  root;
- the visible bypass did not invoke the campaign core and emitted a receipt;
- agent-derived and unverified facts could not activate or mutate a campaign;
  and
- rollback remained available through the bypass or an operator-authorized
  revert.

The post-install disposition was `PASS_WITH_LIMITATION`.

## Result

The bounded local module/CLI path was accepted for continued local use after
implementation, adversarial defect discovery, root repair, re-attack, two live
trials, and post-install review.

The supported claim is narrow:

> A bounded local Codex module/CLI intake path was implemented, adversarially
> repaired, independently rechecked inside the project, exercised with one
> campaign-shaped and one ordinary objective, and accepted with a documented
> Windows path limitation.

This is evidence that persistent work and conservative authority can coexist
on the tested local surface. It is not evidence of universal autonomy.

## Limitations

- The tested installation is one local module/CLI path on one qualified
  machine, not every Codex host or user-interface entry path.
- Fact-provenance references are locally asserted and receipted, not
  cryptographically authenticated against a malicious local caller.
- A sufficiently deep Windows state root can return a visible adapter error
  before activation. No authoritative residue was observed, but path-budget
  preflight and recommended-root guidance are not implemented.
- Internal role separation is not identifiable outsider review.
- The evidence does not establish cross-agent installation, production
  readiness, global wiring, deployment, customer use, commercial impact,
  canonical admission, or universal conformance.
- Private implementation source, raw receipts, internal paths, and sovereign
  architecture are not published in this case.

## Next evidence

The next stronger evidence class would require a separately authorized,
identifiable outsider to reproduce a public artifact on different hardware.
This draft does not authorize outreach, private-source disclosure, deployment,
or publication of the private runtime.
