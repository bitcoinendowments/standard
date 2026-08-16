# templates

Documents an adopting organization edits and makes its own. Copy them out, fill them in, and delete the guidance notes.

| File | Purpose |
|------|---------|
| `constitution_template.md` | The governing document. Placeholders in angle brackets, with a note under each section stating the trade being made |
| `deployment_manifest_template.json` | The machine checkable summary of a deployment, validated against `../schemas/deployment_manifest.schema.json` |
| `evidence_package_checklist.md` | What must be published under BES 0001 §8, in a form you can work through |

`deployment_manifest_template.json` is structurally illustrative, not a valid deployment instance. Its placeholders are not dates, addresses, or names, so a validator configured to assert formats will reject them, correctly. Fill it in before validating it.

Nothing here is adopted by reference. When you finish, you own the document and it does not depend on this repository continuing to exist.

Have your own counsel review a completed constitution before relying on it. See `../DISCLAIMER.md`.
