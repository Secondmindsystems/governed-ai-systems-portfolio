# Two Controlled Provider Tests

The same review service crossed real provider interfaces in two separate
tests. They must not be described as one simultaneous production workflow.

## Episode A: Stripe Test Mode

In a deployed test environment, Stripe test mode processed checkout and
webhook events, created temporary test access, and issued a one-time access
token. The raw token was not stored, and no real customer was charged.

Gemini remained simulated during this episode. The test was accompanied by
101 passing backend and tool tests.

## Episode B: One Deployed Gemini Call

In a later test, a deployed Cloud Run service made one authorized Gemini call
and stored a review receipt and provider-usage record in Firestore.

Stripe was not live during this episode. The service returned to simulated
mode afterward. The test was accompanied by 118 passing backend and tool
tests.

See [PPR-01 through PPR-07](../evidence/EVIDENCE_INDEX.md#two-controlled-provider-tests).

## Why It Matters

The work moved beyond simulated providers without turning a bounded test into
standing live operation.

The useful engineering pattern is:

```text
declare the test boundary
-> enable one real provider surface
-> exercise the planned behavior
-> preserve evidence
-> restore simulated mode
-> state what was not proved
```

## Claim Ceiling

The portfolio may show two separate controlled provider tests built on the
same review service: one Stripe test-mode workflow and one later deployed
Gemini call.

It may not combine them into a simultaneous live customer journey.

## Limitations

- Stripe operated only in test mode.
- Synthetic identities were used.
- No real customer charge occurred.
- Only one deployed Gemini call is claimed.
- The episodes did not establish continuous service.
- No customer use, revenue, adoption, production reliability, or market
  validation is established.
- Restoring simulated mode after one test is not evidence of a universal
  rollback system.

## Capabilities Demonstrated

- cloud deployment and provider integration;
- API and webhook implementation;
- temporary-access handling;
- evidence persistence;
- test-environment control;
- restoration to simulated mode;
- disciplined separation of technical proof from business proof.

## Third-Party Names

Stripe, Gemini, Cloud Run, and Firestore are named only to identify the
interfaces exercised. Their inclusion does not imply endorsement,
partnership, or certification.
