# Bitcoin Endowment Standard

An open specification and toolkit for organizations building a native Bitcoin endowment. It exists to answer one question honestly: what does Bitcoin actually enforce here, and what still depends on people.

This is not a certification authority. Nothing here confers legitimacy by itself. It is not a custody product, not an investment strategy, and not legal advice. It is a starting point and a common vocabulary, published so any organization can adopt it, adapt it, or fork it without asking permission.

**Status: editor's draft. No release is tagged and no clause identifier is frozen.** The threat model in `spec/threat_model.md` has not yet been stress tested. Read `DISCLAIMER.md` before relying on anything here.

**Scope.** This standard covers governance, roles, amendment, evidence, and the claims a deployment may make. It does not standardize or assess operational custody. Key lifecycle, transaction verification procedure, fee and coin policy, chain monitoring, backup integrity, software supply chain, and incident response belong to BES 0002, which does not exist yet.

Where this standard touches custody at all, it requires disclosure rather than practice: publish your complete spending policy, state your weakest authorization condition, publish the procedure your guardians follow, and have a recovery plan that you rehearse and report on. What goes in that procedure and that plan is out of scope, and a deployment states which operational standard it follows or says plainly that its custody operations are unassessed. Conformance here never implies custody safety.

## Read this before anything else

Bitcoin nodes validate signatures and enforce spending conditions, such as signature thresholds and timelocks, when those conditions are actually committed in the spending condition of the coins they apply to. A policy that lives only in a constitution is not enforced by Bitcoin. Bitcoin cannot verify a charitable mission, confirm a beneficiary is real, or resolve a legal dispute.

Two different questions get confused here constantly, so this standard labels every requirement with both answers.

**What actually constrains behavior.**

* **CONSENSUS.** A Bitcoin node rejects a transaction that violates it.
* **SOFTWARE.** Software refuses or flags it, and anyone able to sign can bypass it.
* **LEGAL.** A court or regulator may enforce it.
* **GOVERNANCE.** Only people following their own stated process enforce it.

**How an outside party checks it.**

* **CHAIN.** Verifiable against the block chain by anyone.
* **REPRODUCIBLE.** Verifiable by rerunning published software on published inputs.
* **DOCUMENTARY.** Depends on a record someone submitted, which means deciding whether to trust the submitter.

The two do not move together, and that is the point. A three of five spend is constrained by CONSENSUS, and the chain proves the spending condition was satisfied. Only a submitted record tells you those five keys belong to five independent people. So the claim reads CONSENSUS with evidence CHAIN plus DOCUMENTARY, and where a single word is needed it derives to the weaker one, DOCUMENTARY, never to Bitcoin.

That rule, deriving by the weakest link rather than the strongest component, is what keeps an organizational fact from being presented as a Bitcoin fact. It is the honesty mechanism this whole repository is built around.

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

This standard defines exactly two claims. **Conformant** means every MUST is met. **Based on, with declared deviations** means one or more are not, and each is declared. Disclosure does not cure an unmet requirement, because a standard whose absolute requirements can be waived by mentioning them has no absolute requirements. The second claim is honest, common, and often the right one.

Either claim is made by the deployment about itself. It is not a seal of approval issued by this project. There is no registry here deciding who counts as a real Bitcoin endowment. Competing indexes and independent auditors are expected and welcome.

Conformance describes evidence against this specification. It does not establish solvency, honesty, investment prudence, custody competence, legal validity, or future compliance.

## License

The specification, profiles, templates, and examples are released under **CC0 1.0 Universal**, in `LICENSE`. Jimmy Kostro, the author and copyright holder, dedicates those directories to the public domain and, where any right survives that dedication under local law, will not assert it against any use of them. You may copy, change, translate, or sell them, with no obligation to credit anyone and no permission required. This is deliberate: a charity's counsel needs to paste a template into a legal instrument without an attribution obligation riding along with it.

Schemas, tests, and any code are released under **Apache License 2.0**, in `LICENSE_CODE`, which adds an explicit patent grant. There is no NOTICE file, also deliberate, so redistribution carries nothing to preserve beyond the license itself.

The name of this project is not restricted and using the standard requires nothing from us. That is a statement about the name, not about identity: the general law still forbids claiming that we published, endorsed, or certified work we did not, and nothing in either license says otherwise.

## Contributing and governance

Read `CONTRIBUTING.md` for how changes are made and `GOVERNANCE.md` for who decides and what happens if we stop. Forking this repository is legitimate, expected, and not a hostile act.

Every substantive normative change goes through a public proposal in `proposals/`. Editorial corrections go through reviewed pull requests without a full proposal. All releases are versioned and tagged, never quietly rewritten. Deployments pin an exact release and are never expected to auto upgrade. See `VERSIONING.md`.

## Who publishes this

Published and stewarded by BITCOIN CHIANG MAI Co., Ltd. Authored by Jimmy Kostro, who holds the copyright and has dedicated the specification to the public domain under CC0 1.0.

Neither name is a claim on your deployment. Stewardship decides what this repository says and nothing else, and the license already gives you the right to fork it and drop both names. See `GOVERNANCE.md` and `DISCLAIMER.md`.
