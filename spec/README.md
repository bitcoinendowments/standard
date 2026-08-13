# spec

The normative standard. This folder is the only place in the repository where MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY carry their defined meaning.

| File | Purpose |
|------|---------|
| `BES_0001_core_standard.md` | The requirements. Governance and conformance, plus the minimum custody interface it depends on |
| `glossary.md` | Informative definitions. Where it conflicts with the standard, the standard governs |
| `threat_model.md` | What this design does and does not defend against |
| `conformance.md` | The two claims a deployment may make, and how an outside party checks one |

**Status.** Editor's draft. No release is tagged and no clause identifier is frozen. Identifiers become permanent at the first tagged release.

**Scope.** BES 0001 covers governance, roles, amendment, evidence, and claims. Where it touches custody it requires disclosure, not practice: §2 requires the complete spending policy be published and its weakest condition stated, §7.5 requires the verification procedure be published, and §9 requires a recovery plan exist, be exercised, and be reported. What belongs inside that procedure and that plan is operational, belongs to BES 0002, and is deliberately absent here. §12 forbids presenting conformance with this document as evidence of custody safety.

**What does not belong here.** Organization specific numbers, recommended configurations, and anything an adopter would edit. Configurations belong in `../profiles/`. Editable documents belong in `../templates/`.
