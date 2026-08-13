# Versioning

**Current state: editor's draft.** No release is tagged, no clause identifier is frozen, and clauses may be renumbered or restructured without notice. Everything below takes effect at the first tagged release. Nothing should be called an immutable release before it has been published once.

Releases are numbered `MAJOR.MINOR.PATCH`. The meanings are defined from the adopting organization's side, not the author's, because the only question that matters is whether a release affects a deployment already in the field.

| Change | Meaning for a deployment already conformant |
|--------|---------------------------------------------|
| **MAJOR** | A deployment that was conformant may no longer be conformant. Action may be required |
| **MINOR** | New optional requirements, new profiles, or clarifications. An existing conformant deployment stays conformant. No action required |
| **PATCH** | Editorial only. Typos, formatting, broken links. No normative change of any kind |

## Rules that do not bend

**Clause identifiers are permanent.** A clause is never renumbered and never reused. A withdrawn clause is marked withdrawn in place in BES 0001 §13, with the release that withdrew it and the reason. This is what lets a constitution written today cite a clause and remain intelligible in ten years.

**Tags are immutable.** A release tag is signed, and once pushed it is never moved, never deleted, and never force pushed. If a release is wrong, the fix is a new release, never a rewrite of the old one.

**Release notes lead with migration impact.** The first paragraph of every release note states what an existing conformant deployment must do, even when the answer is nothing.

**Deployments pin an exact release.** No deployment is expected or required to upgrade. A conformance statement always names a specific release, and that release keeps meaning what it meant when it was published.

## What a release contains

A `CHANGELOG.md` entry, a signed tag, and, for any MINOR or MAJOR release, links to the merged proposals in `proposals/` that produced the change.
