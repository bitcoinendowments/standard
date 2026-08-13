# schemas

Machine checkable structure for a deployment's published manifest.

| File | Validates |
|------|-----------|
| `deployment_manifest.schema.json` | The manifest a deployment publishes in its evidence package |

Validate with any JSON Schema 2020-12 implementation:

```
check-jsonschema --schemafile schemas/deployment_manifest.schema.json examples/lighthouse/deployment_manifest.json
```

**What this schema can check.** Structure, presence, types, the floors in BES 0001 §2.4 applied to every declared spending path, that all eight correlated control factors are disclosed, and that a conformance claim is not published alongside an unmet MUST.

**What it cannot check.** Whether any stated fact is true. `no_undisclosed_weaker_path` is an assertion until someone derives the policy and looks. `control_ceiling_met` is an assertion until someone investigates ownership and employment. It also cannot compare fields the way a reader can, so a threshold larger than its participant count validates cleanly.

Under §11.6 a deployment must not present a passing validation as evidence of conformance. The schema tells you what a deployment asserts. `../tests/failure_scenarios.md` tells you what to check yourself.

Schemas and tests are released under Apache License 2.0, in `../LICENSE_CODE`.
