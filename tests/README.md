# tests

Vectors an outside party can run against a published manifest.

```
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/valid_conformant.json
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/valid_based_on_with_deviations.json
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/invalid_recovery_path_below_floor.json
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/invalid_conformant_claim_with_unmet_must.json
```

The two named `valid_` must pass. The two named `invalid_` must fail, the first at `spending_policy.paths` and the second at `conformance.unmet_musts`. A vector named `invalid_` that validates is a bug in the schema, not a passing test.

The two failing vectors encode the errors this standard exists to catch. The first is a recovery path that spends below the stated condition while the primary path looks respectable, which is the failure that makes every other control decoration. The second is a conformance claim published alongside an unmet MUST, which BES 0001 §11.2 forbids.

## What these vectors do not catch

`failure_scenarios.md`, in this folder, lists the conformance failures that no schema can detect and what a human verifier has to do instead. That list is longer than this one, which is the honest shape of the problem. Structural validation checks assertions, never conformance, per §11.6.

Released under Apache License 2.0, in `../LICENSE_CODE`.
