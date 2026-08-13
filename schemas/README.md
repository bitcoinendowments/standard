# schemas

Machine checkable structure for a deployment's published manifest.

| File | Validates |
|------|-----------|
| `deployment_manifest.schema.json` | The manifest a deployment publishes in its evidence package |

Validate with any JSON Schema 2020-12 implementation:

```
check-jsonschema --schemafile schemas/deployment_manifest.schema.json examples/lighthouse/deployment_manifest.json
```

**What this schema can check.** Structure, presence, types, the floor in BES 0001 §2.5 applied to every declared script path, that each path declares whether its threshold is script enforced or produced by aggregate signing, that an enabled key path names the path entry describing it, that all nine correlated control factors are disclosed, that a domain table and per path rosters exist, and that a conformance claim is not published alongside an unmet MUST.

**What it cannot check.** Relationships between fields. A threshold larger than its participant count, a stated weakest condition that is not the smallest path threshold, risk arithmetic that contradicts m and n, and a correlated domain large enough to reach the threshold all validate cleanly here. Those are checked by `../tests/check_invariants.py`, which is the second layer and should always be run alongside this one. That layer also evaluates every figure against one real path, rather than synthesizing a threshold and participant count that may describe no path in the policy.

It also cannot check whether any stated fact is true. The domain table is an assertion until someone investigates ownership and employment, and the path list is an assertion until someone derives the descriptor under §2.2 and compares it against the chain.

Under §11.6 a deployment must not present a passing validation as evidence of conformance. The schema tells you what a deployment asserts. `../tests/failure_scenarios.md` tells you what to check yourself.

Schemas and tests are released under Apache License 2.0, in `../LICENSE_CODE`.
