# tests

Vectors an outside party can run to check a conformance claim without contacting the deployment or the maintainers.

```
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/valid_standard_five_guardian.json
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/invalid_threshold_below_floor.json
```

The first must pass. The second must fail, at `custody.signing_threshold`. A vector named `invalid_` that passes validation is a bug in the schema, not a passing test.

## What these vectors do not catch

`failure_scenarios.md`, in this folder, lists the conformance failures that no schema can detect, and what a human verifier has to do instead. That list is longer than this one, which is the honest shape of the problem.

Released under Apache License 2.0, in `../LICENSE_CODE`.
