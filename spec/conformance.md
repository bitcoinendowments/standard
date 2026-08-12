# Conformance

## What a conformance statement is

A deployment may publish a statement that it is conformant with a named release of this standard. The statement is a claim made by the deployment about itself. It is not issued, reviewed, approved, or endorsed by the maintainers of this standard. There is no registry, no certification, and no authority here that decides who counts as a real Bitcoin endowment.

The value of the statement comes entirely from being checkable by someone else.

## The required form

A conformance statement must name the exact release, list every disclosed deviation by clause identifier, and point to the evidence package where each claim can be checked.

```
This deployment states conformance with BES 0001 at release 0.1.0.
Disclosed deviations: §4.2 (guardians resident in two countries, not three), §5.5 (no independent reconciler).
Evidence package: <location>
```

An undisclosed deviation makes the statement false. Disclosure costs nothing and is always available, which is why nothing here is worth concealing.

## How an outside party checks it

1. Read the named release of `BES_0001_core_standard.md`. Releases are immutable, so the text checked is the text claimed.
2. Validate the deployment manifest against `../schemas/deployment_manifest.schema.json`.
3. Run the vectors in `../tests/vectors/` against the deployment's published payment requests.
4. For each clause, check the claim against its verification label. A BITCOIN claim is checked against the chain. A SOFTWARE claim is checked by reproducing the software. A DOCUMENTARY claim is checked against a submitted record, which means deciding whether to trust the submitter. A LEGAL claim is checked by reading the instrument and, if it matters, asking a lawyer. A GOVERNANCE claim can only be checked against a history of behavior over time.
5. Compare the disclosed deviations against what the evidence actually shows.

Step 4 is where most of the judgment lives. The labels exist so that a reader knows which kind of judgment each claim requires, not to make judgment unnecessary.

## What conformance does not establish

Not solvency. Not honesty. Not investment prudence. Not legal validity in any jurisdiction. Not future compliance. Not that the mission is worthwhile or that the beneficiaries are real.

A deployment can be fully conformant and still be a bad endowment. This standard makes a narrow set of properties checkable. It does not make an organization good.
