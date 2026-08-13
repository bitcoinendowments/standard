# spec

The normative standard. This folder is the only place in the repository where MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY carry their defined meaning.

| File | Purpose |
|------|---------|
| `BES_0001_core_standard.md` | The requirements. Governance and conformance, plus the minimum custody interface it depends on |
| `glossary.md` | Informative definitions. Where it conflicts with the standard, the standard governs |
| `threat_model.md` | What this design does and does not defend against |
| `conformance.md` | The two claims a deployment may make, and how an outside party checks one |

**Status.** Editor's draft. No release is tagged and no clause identifier is frozen. Identifiers become permanent at the first tagged release.

**Scope.** BES 0001 covers governance, roles, amendment, evidence, and claims. Operational custody, meaning key lifecycle, transaction review discipline, fee and coin policy, chain monitoring, supply chain, and incident response, is the subject of BES 0002, which does not exist yet. Conformance with BES 0001 does not establish custody safety, and §12 says so normatively rather than in a footnote.

**What does not belong here.** Organization specific numbers, recommended configurations, and anything an adopter would edit. Configurations belong in `../profiles/`. Editable documents belong in `../templates/`.
