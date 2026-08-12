# Contributing

Issues and pull requests are welcome from anyone. You do not need permission, an introduction, or an affiliation.

## Three lanes

Every change goes through exactly one of these.

**Editorial.** Typos, formatting, broken links, clearer phrasing that changes no meaning. Open a pull request. Merged quickly.

**Clarification.** Wording that changes what a requirement is understood to mean, without changing what it requires. Open a pull request, state in the description that no normative change is intended, and a maintainer must confirm that explicitly before merge. If a reviewer thinks the meaning changed, it becomes a normative change instead.

**Normative.** Anything that adds, removes, or alters a requirement, or that changes a verification label. Requires a numbered proposal in `proposals/`, a public comment period of at least thirty days, and a recorded decision. See `proposals/0000_template.md`.

When in doubt, the change is normative. The cost of an unnecessary proposal is thirty days. The cost of a silent normative change is that every existing conformance statement quietly becomes unreliable.

## Writing a proposal

Copy `proposals/0000_template.md` and number it with the next unused number. The template has six sections and the last one matters most: **who is worse off if this is adopted.** Reviewers read that section first. A proposal that claims nobody is worse off is usually a proposal that has not been thought through, since almost every tightening of a requirement excludes someone who was previously conformant.

## House style

The style rules exist because the audience includes lawyers, trustees, and engineers who have no reason to trust us yet.

• MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY carry the meaning in BES 0001 §1.2 and appear nowhere else in a casual sense.
• Every normative clause carries exactly one verification label.
• Never write trustless, unhackable, guaranteed, immutable governance, revolutionary, or institutional grade.
• Prefer mechanism verbs: enforced by, depends on, requires trusting, can be bypassed when. Avoid a bare "secured by", which hides which verification category is doing the work.
• The spec is impersonal and describes what a deployment does. The README is second person and describes what a reader can do.
• Dates are absolute and in ISO form.
• State a limit in the same register as the capability it limits.
• Give reasons, not authority. Nothing here is true because it is written down.

## Clause identifiers

Never renumber a clause. Never reuse a withdrawn identifier. A pull request that renumbers clauses will be rejected regardless of merit, because outside documents cite these identifiers.

## Reporting a security issue

See `SECURITY.md`. Do not open a public issue for a vulnerability in a live deployment.

## Licensing of contributions

Contributions to the specification, profiles, templates, and examples are accepted under CC0 1.0. Contributions to schemas, tests, and code are accepted under Apache License 2.0. By opening a pull request you confirm you have the right to contribute the work under those terms.
