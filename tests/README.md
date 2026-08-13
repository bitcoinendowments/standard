# tests

Two layers of check an outside party can run against a published manifest. Neither proves conformance, and §11.6 says so normatively.

## Layer one, structure

```
check-jsonschema --schemafile schemas/deployment_manifest.schema.json tests/vectors/valid_conformant.json
```

Every field on its own: presence, type, and the §2.5 floor applied to each declared script path.

The schema is plain JSON Schema 2020-12, so any implementation works and `check-jsonschema` is only one convenient wrapper. With no CLI installed:

```
python3 -c "import json,jsonschema,sys; jsonschema.Draft202012Validator(json.load(open('schemas/deployment_manifest.schema.json'))).validate(json.load(open(sys.argv[1])))" tests/vectors/valid_conformant.json
```

## Layer two, cross field arithmetic

```
python3 tests/check_invariants.py tests/vectors/valid_conformant.json
```

Comparisons a JSON Schema cannot express: that the stated weakest authorization really is the smallest threshold across paths, that each path's risk arithmetic matches its own m and n, that no correlated failure domain reaches m or disables the threshold, that a threshold does not exceed its participant count, and that a conformance claim is not published beside an unmet MUST.

## The vectors

| Vector | Expected |
|--------|----------|
| `vectors/valid_conformant.json` | passes both layers |
| `vectors/valid_based_on_with_deviations.json` | passes both layers |
| `vectors/invalid_recovery_path_below_floor.json` | fails layer one at `spending_policy.paths` |
| `vectors/invalid_conformant_claim_with_unmet_must.json` | fails layer one at `conformance.unmet_musts` |
| `vectors/invalid_domain_reaches_threshold.json` | passes layer one, fails layer two at §3.5 |
| `vectors/invalid_risk_arithmetic_mismatch.json` | passes layer one, fails layer two at §3.10 |
| `vectors/invalid_synthesized_weakest_pair.json` | passes layer one, fails layer two at §2.3 |
| `vectors/invalid_key_path_without_proof.json` | passes layer one, fails layer two at §2.7 |
| `vectors/valid_enabled_key_path.json` | passes both layers |
| `vectors/invalid_key_path_undeclared_weakest.json` | passes layer one, fails layer two at §2.3 |

Most of these exist to make the point that structure alone is not enough. A manifest can be perfectly formed and still describe an endowment where one vendor can compromise the threshold, or state a weakest condition of three of seven when no three of seven path exists, or disable a Taproot key path without publishing anything that proves it.

`vectors/invalid_key_path_undeclared_weakest.json` is the one worth reading. It publishes a three of five threshold signed key path and a four of seven script recovery path, then names the script path as its weakest route. The script path is the larger number and the smaller claim. An enabled key path is an ordinary path under §2.8, so it competes for weakest like any other, and the check names it.

Every figure in layer two is evaluated against one real path. The checker never combines the smallest threshold in the policy with the largest participant count, because that pair can describe a path nobody operates.

A vector named `invalid_` that passes both layers is a bug in the checks, not a passing test.

## What neither layer catches

**Path completeness.** Both layers read the paths a deployment declared. Neither can tell you a Taproot branch was omitted. That requires deriving the published descriptor under §2.2 and comparing it against the chain, by hand, and it is the failure that makes every other control decoration.

`failure_scenarios.md`, in this folder, lists the rest.

The aggregate protocol named in the two key path vectors is deliberately generic. A three of five key path needs a threshold signing construction, not an aggregate multisignature such as MuSig2, which is n of n. §2.9 makes that a requirement rather than a footnote, and the construction itself belongs to BES 0002.

Note on the manifest template: `../templates/deployment_manifest_template.json` is structurally illustrative. Its placeholders are not dates, so a validator asserting formats will reject it, correctly.

Released under Apache License 2.0, in `../LICENSE_CODE`.
