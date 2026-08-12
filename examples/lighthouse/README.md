# Lighthouse Endowment (fictional)

A worked example of BES 0001 at release 0.1.0.

| File | What it is |
|------|------------|
| `constitution.md` | The template in `../../templates/` with every placeholder decided |
| `deployment_manifest.json` | The matching machine checkable manifest |

Lighthouse is fictional. Its mission, guardians, jurisdiction, and numbers were invented to exercise the standard. The Cayman Islands structure in section 8 is illustrative and has not been reviewed by counsel in any jurisdiction.

Validate the manifest:

```
check-jsonschema --schemafile ../../schemas/deployment_manifest.schema.json deployment_manifest.json
```
