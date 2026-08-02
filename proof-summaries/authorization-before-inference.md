# Authorization Before Inference

## Result

A local, non-production AI runtime checked one-use permission before sending a
model request. It allowed one local call, consumed the permission, and stopped
a second attempt before another request was sent.

The returned answer remained review-only text. It produced no tool call and no
external effect.

## Why It Matters

In this design, the permission check occurs before model transport, so the
blocked second attempt never reached the model:

```text
one-use permission
-> permission check
-> model request
-> candidate text
-> separate action authority
```

The model’s ability to generate text did not grant permission to run another
model request or take an action.

## Evidence

- One authorized local model call occurred after the permission check.
- The one-use permission was consumed.
- A second attempt stopped before another model request.
- The answer remained inert, review-only text.
- Seventy focused tests passed before the operator-facing run.
- A separate earlier smoke test exercised the same one-use boundary.

See [PAI-01 through PAI-05](../evidence/EVIDENCE_INDEX.md#authorization-before-inference).

## Claim Ceiling

One local, loopback-only, non-production runtime enforced one-use permission
before model transport and kept returned text separate from action authority.

## Limitations

- The model ran on the same machine.
- No remote provider was exercised.
- No browsing, retrieval, tool use, or external action occurred.
- Two local episodes are corroborating evidence, not a reliability study.
- The result does not establish resistance to hostile callers or production
  readiness.

## Capabilities Demonstrated

- authorization-system design;
- local-model runtime integration;
- one-use permission consumption;
- pre-transport blocking;
- inert-output handling;
- deterministic test engineering.
