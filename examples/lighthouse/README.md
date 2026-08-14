# Lighthouse Endowment (fictional)

A worked example of BES 0001 at its current editor's draft.

| File | What it is |
|------|------------|
| `constitution.md` | The template in `../../templates/` with every placeholder decided |
| `deployment_manifest.json` | The matching machine checkable manifest |

Lighthouse is fictional. Its mission, guardians, jurisdiction, and numbers were invented to exercise the standard. The Cayman Islands structure in section 10A is illustrative and has not been reviewed by counsel in any jurisdiction.

Validate the manifest:

```sh
check-jsonschema --schemafile ../../schemas/deployment_manifest.schema.json deployment_manifest.json
```
