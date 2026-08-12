# spec

The normative standard. This folder is the only place in the repository where MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY carry their defined meaning.

| File | Purpose |
|------|---------|
| `BES_0001_core_standard.md` | The requirements. Permanent clause identifiers, one verification label per clause |
| `glossary.md` | Informative definitions. Where it conflicts with the standard, the standard governs |
| `threat_model.md` | What this design does and does not defend against |
| `conformance.md` | How a deployment states conformance and how an outside party checks it |

**What does not belong here.** Organization specific numbers, recommended configurations, and anything an adopter would edit. Configurations belong in `../profiles/`. Editable documents belong in `../templates/`.
