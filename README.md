# Bitcoin Endowment Standard

An open specification and toolkit for organizations building a native Bitcoin endowment. It exists to answer one question honestly: what does Bitcoin actually enforce here, and what still depends on people.

This is not a certification authority. Nothing here confers legitimacy by itself. It is not a custody product, not an investment strategy, and not legal advice. It is a starting point and a common vocabulary, published so any organization can adopt it, adapt it, or fork it without asking permission.

**Status: Draft 0.1.0.** The threat model in `spec/threat_model.md` has not yet been stress tested. Read `DISCLAIMER.md` before relying on anything here.

## Read this before anything else

Bitcoin nodes validate signatures and enforce spending conditions, such as signature thresholds and timelocks, when those conditions are actually committed in the transaction output's script. A policy that lives only in a constitution, and not in that script, is not enforced by Bitcoin. Bitcoin cannot verify a charitable mission, confirm a beneficiary is real, or resolve a legal dispute. Every claim in this repository is labeled with what actually backs it:

• **BITCOIN.** Enforced by transaction and script rules, validated under network consensus. Anyone can verify it against the chain itself.
• **SOFTWARE.** Checked or executed by reproducible software. A rule engine can reject a request locally, but guardians can still bypass it and sign a different valid transaction unless the restriction is committed in script, so this claim is only as strong as the code, inputs, build, and execution environment being genuinely available for anyone to reproduce.
• **DOCUMENTARY.** Depends on evidence someone submitted. Verifiable, but requires trusting a record.
• **LEGAL.** Depends on a jurisdiction and a court's willingness to enforce it.
• **GOVERNANCE.** Depends on people following their own stated process.

BITCOIN claims are independently validated under network consensus. SOFTWARE claims are independently reproducible only when the code, inputs, build, and execution environment are actually available to check, so treat the two as different strengths of proof, not interchangeable ones. The remaining three are where an organization's real institutional character shows up, and this project's job is to make that visible rather than hide it behind the word Bitcoin native.

## Three kinds of document in this repository, and why the difference matters

**The standard, in `spec/`.** This is the normative document, the one that says what a deployment must, must not, should, or may do to call itself conformant. It does not know your organization's mission or beneficiaries. It is deliberately boring and general, the same way a building code is boring and general, so that it can apply to a small foundation and a very large trust without changing shape.

**Profiles, in `profiles/`.** A profile is an opinionated starting configuration, for example five guardians with a three of five signing threshold. A profile is a recommendation sized for a common situation, not a universal rule the standard imposes. An organization with a smaller treasury or a different risk tolerance should pick a different profile, or write its own, without that making it nonconformant.

**Templates, in `templates/`.** A template is the document an organization actually edits: a constitution with placeholders like mission, threshold, and notice period days, ready to be filled in, argued over, and adopted as that organization's own. Templates carry inline comments explaining what each placeholder trades off, so filling one in is a design decision, not a fill in the blank exercise.

Confusing these three is the most common way a standard like this goes wrong. Treating a profile as mandatory turns a recommendation into an unnecessary barrier. Treating a template as the standard means nobody can tell what is actually required versus what one example organization happened to choose. Keeping them in separate folders, with separate purposes stated up front, is a deliberate editorial choice, not a filing convenience.

## Three ways to use this repository

**Understand.** Start with this README and `spec/glossary.md`. You should be able to explain the standard's core idea, Bitcoin secures custody and settlement, governance documents handle everything Bitcoin cannot evaluate, before you touch a template.

**Adopt.** Pick a profile in `profiles/` close to your situation, copy the matching files in `templates/`, and fill them in as your own constitution and deployment manifest. Nothing here is adopted by reference. You are expected to end up with your own document, not a link back to this repository.

**Verify.** Use `schemas/` and the `tests/` test vectors to check that a deployment's manifest, payment requests, and evidence package actually match what it claims to be conformant with. Verification is meant to be something an outside party can do independently, not something this project certifies on anyone's behalf.

## Repository map

| Path | What it holds |
|------|----------------|
| `spec/` | The normative standard, glossary, threat model, and conformance rules |
| `profiles/` | Opinionated starting configurations. Recommendations, not requirements |
| `templates/` | Documents an adopting organization edits and makes its own |
| `examples/` | One fully worked fictional deployment, for reading, not copying blindly |
| `schemas/` | Machine checkable definitions of the manifest and payment request formats |
| `tests/` | Vectors an outside party can run to check a conformance claim |
| `proposals/` | Numbered proposals for every substantive change to the standard |

## What conformance means, and does not mean

A deployment can state it is conformant with a specific, versioned release of this standard, with any deviations disclosed. That statement is a checkable claim, not a seal of approval issued by this project. There is no registry here that decides who counts as a real Bitcoin endowment. Competing indexes and independent auditors are expected and welcome.

Conformance describes evidence against this specification. It does not establish solvency, honesty, investment prudence, legal validity, or future compliance.

## License

The specification, profiles, templates, and examples are released under **CC0 1.0 Universal**, in `LICENSE`. You may copy, change, translate, or sell them, with no obligation to credit anyone and no permission required. This is deliberate: a charity's counsel needs to paste a template into a legal instrument without an attribution obligation riding along with it.

Schemas, tests, and any code are released under **Apache License 2.0**, in `LICENSE_CODE`, which adds an explicit patent grant.

The name of this project is not restricted. Using the standard requires nothing from us.

## Contributing and governance

Read `CONTRIBUTING.md` for how changes are made and `GOVERNANCE.md` for who decides and what happens if we stop. Forking this repository is legitimate, expected, and not a hostile act.

Every substantive normative change goes through a public proposal in `proposals/`. Editorial corrections go through reviewed pull requests without a full proposal. All releases are versioned and tagged, never quietly rewritten. Deployments pin an exact release and are never expected to auto upgrade. See `VERSIONING.md`.
