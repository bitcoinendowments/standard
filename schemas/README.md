# schemas

Machine checkable definitions, so an outside party can check a conformance claim without contacting the deployment or the maintainers. This is what BES 0001 §12.5 requires.

| File | Validates |
|------|-----------|
| `deployment_manifest.schema.json` | The manifest a deployment publishes in its evidence package |

Validate with any JSON Schema 2020-12 implementation. For example:

```
check-jsonschema --schemafile schemas/deployment_manifest.schema.json examples/lighthouse/deployment_manifest.json
```

**What a schema can and cannot check.** It checks structure, presence, types, and floors such as a signing threshold of at least three. It cannot check whether a stated fact is true. `threshold_committed_in_script` being `true` is a DOCUMENTARY claim until someone verifies it against the chain, at which point it becomes a BITCOIN claim. The schema tells you what the deployment asserts. Verification is still your job.

Schemas and tests are released under Apache License 2.0, in `../LICENSE_CODE`.
