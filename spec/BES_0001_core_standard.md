# BES 0001: Core Standard for a Native Bitcoin Endowment

Release 0.1.0. Status: Draft. Not legal advice. See `../DISCLAIMER.md`.

## How to read this document

Every normative statement has a permanent clause identifier, for example `§4.2`. Clause identifiers are never renumbered and never reused. A clause that is withdrawn is marked withdrawn in place, in §13, together with the release that withdrew it. A deployment may cite a clause and a release together, for example "conformant with BES 0001 §4.2 at release 0.1.0", and that citation remains meaningful for as long as the release exists.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are used only in the sense defined in §1.2. They appear nowhere else in this repository in a casual sense.

Every normative clause carries a verification label in brackets stating what actually backs it. The labels are defined in §1.3. A reader skimming a section should be able to see the proportion of BITCOIN claims to LEGAL and GOVERNANCE claims without reading the detail. That visible ratio is deliberate.

## §1. Scope and interpretation

**§1.1** This standard defines how a Bitcoin endowment holds and distributes funds so that money movement is provably correct, control is shared among multiple independent parties, and any process that could be abused is slow, visible, and logged. [GOVERNANCE]

**§1.2** In this document, MUST and MUST NOT state an absolute requirement for conformance. SHOULD and SHOULD NOT state a strong recommendation that a deployment MAY decline only by disclosing the deviation under §12.3. MAY states an option with no conformance consequence either way. [GOVERNANCE]

**§1.3** Every normative clause carries exactly one verification label. BITCOIN means enforced by transaction and script rules and validated under network consensus. SOFTWARE means checked or executed by software that any party can reproduce. DOCUMENTARY means it depends on evidence someone submitted. LEGAL means it depends on a jurisdiction and a court. GOVERNANCE means it depends on people following their own stated process. [GOVERNANCE]

**§1.4** This standard does not make an endowment trustless. It defines where trust is required, how that trust is distributed, and how it is disclosed. A deployment MUST NOT describe itself as trustless on the basis of conformance with this standard. [GOVERNANCE]

**§1.5** This standard applies to a deployment, meaning one specific endowment adopting it through its own constitution. Nothing in this standard is adopted by reference. A deployment MUST hold its own constitution as an independent document. [DOCUMENTARY]

## §2. Definitions

Terms used in this document are defined in `glossary.md`. The glossary is informative, not normative. Where the glossary and this document conflict, this document governs.

## §3. Custody and signing

**§3.1** Endowment funds MUST be held in a multisignature arrangement requiring at least three signatures from at least five distinct signing keys. A deployment MAY require more keys or a higher threshold. It MUST NOT require fewer. [BITCOIN]

**§3.2** The signing threshold MUST be committed in the output script that holds endowment funds. A threshold that exists only in a written policy is not enforced by Bitcoin and MUST NOT be described as if it were. [BITCOIN]

**§3.3** Endowment funds MUST NOT be held by a third party custodian, on an exchange, or under any arrangement where a single party can move funds unilaterally. [BITCOIN]

**§3.4** Each guardian MUST hold exactly one signing key. One person or entity holding two keys reduces the effective threshold and MUST be treated as a single guardian for every count in this standard. [DOCUMENTARY]

**§3.5** Any spending restriction a deployment claims Bitcoin enforces, including timelocks and thresholds, MUST be committed in script. Restrictions enforced only by a rule engine or by policy MUST be labeled SOFTWARE or GOVERNANCE in the deployment's evidence package, never BITCOIN. [BITCOIN]

## §4. Guardian independence

**§4.1** No two guardians may share an owner or controlling entity, a country of legal residence, a key storage system or password manager, a backup custodian, legal counsel, or a cloud or hosting account. A deployment MUST document how each of these six is satisfied. [DOCUMENTARY]

**§4.2** Guardians MUST be resident in at least three distinct countries. [DOCUMENTARY]

**§4.3** Geographic spread alone is insufficient. A deployment's independence claim MUST be evaluated on shared ownership, shared software and vendors, and shared legal exposure, not on country count. [DOCUMENTARY]

**§4.4** A deployment MUST state plainly in its evidence package that the loss of any two guardians does not stop fund movement, and that collusion among any three or more guardians could move funds against the mission. This disclosure MUST NOT be minimized, footnoted, or omitted. [GOVERNANCE]

**§4.5** The maintainers of this standard MUST NOT serve as guardians for any deployment that adopts it. [GOVERNANCE]

## §5. Separation of roles

**§5.1** A guardian MUST NOT also serve as an administrator. [GOVERNANCE]

**§5.2** An administrator MAY prepare paperwork, draft unsigned payment proposals, publish evidence package updates, and communicate with beneficiaries. [GOVERNANCE]

**§5.3** An administrator MUST NOT sign or move funds, change a rule at any tier, select or exclude a beneficiary outside the criteria fixed in the constitution, suppress a failed compliance check, or make any payment final without guardian signatures. [BITCOIN]

**§5.4** Every administrator action MUST be published as one of three types: automatic and independently provable, based on a claim not yet independently verified, or a judgment call requiring guardian approval with a recorded justification. [DOCUMENTARY]

**§5.5** A deployment SHOULD assign reconciliation of the published record to a party who is neither an administrator nor a guardian. [GOVERNANCE]

## §6. Asset and spending policy

**§6.1** A deployment MUST state, before funds are received, whether spending draws from principal, from new donations, or from separately disclosed income. Bitcoin produces no yield on its own and a deployment MUST NOT present it as if it does. [DOCUMENTARY]

**§6.2** A deployment MUST state its annual spending rule as a formula, including the measurement window used to value the endowment. [DOCUMENTARY]

**§6.3** Endowment funds MUST NOT be lent, used as collateral, rehypothecated, or converted into a wrapped or synthetic representation of bitcoin, unless the constitution names the practice explicitly, states the counterparty risk, and assigns the decision to Tier One under §7.1. [GOVERNANCE]

**§6.4** A deployment SHOULD hold its reserve in bitcoin held directly under §3, and MUST disclose any portion held otherwise, including the reason and the counterparty. [DOCUMENTARY]

## §7. Rule tiers and amendment

**§7.1** Every rule in a deployment's constitution MUST be assigned to exactly one of three tiers. Tier One covers the mission, the prohibition on personal profit by administrators and guardians, and the procedure for amending Tier One itself. Tier Two covers beneficiary criteria and spending limits. Tier Three covers routine numeric parameters that update under a formula fixed in the constitution. [GOVERNANCE]

**§7.2** Tier One amendments MUST require the deployment's highest vote threshold and its longest public notice period. Tier Two amendments MUST require a lower threshold and a shorter notice period than Tier One, and both MUST be deliberately slow. Tier Three parameters MAY update automatically and MUST be logged publicly when they do. [GOVERNANCE]

**§7.3** This standard does not set the specific vote counts or notice periods. Those belong in the constitution. See `../profiles/` for starting configurations. [GOVERNANCE]

**§7.4** A deployment MUST NOT label any rule permanent or unamendable. Every rule MUST state its tier and the exact procedure required to change it. [GOVERNANCE]

**§7.5** A deployment is never required to adopt a new release of this standard. Its own constitution governs whether and when it updates. [GOVERNANCE]

## §8. Payment procedure

**§8.1** An administrator MUST publish a payment request with its supporting evidence and the verification label for each claim, before any guardian signs. [DOCUMENTARY]

**§8.2** Any outside party MUST be able to rerun the automatic checks against the published request and the constitution and reach the same result. [SOFTWARE]

**§8.3** Each guardian MUST independently review the request and the unsigned transaction against the published evidence and the constitution before signing. [GOVERNANCE]

**§8.4** At least the threshold set under §3.1 MUST sign before broadcast. [BITCOIN]

**§8.5** The signed payment and its full supporting record MUST be published. [DOCUMENTARY]

**§8.6** If any required evidence is missing, unclear, or fails a check, the payment MUST NOT proceed. There MUST be no default path to completion that skips a check. [GOVERNANCE]

## §9. Evidence package

**§9.1** A deployment MUST publish and maintain a public evidence package. [DOCUMENTARY]

**§9.2** The evidence package MUST contain the release of this standard in use, the deployment's own constitution, the guardian count and threshold, the guardian identities or pseudonymous identifiers sufficient to check §4.1, a complete record of past payments, and any audit results with the auditor named. [DOCUMENTARY]

**§9.3** Every claim in the evidence package MUST carry one of the five verification labels defined in §1.3. A claim MUST NOT be presented under a stronger label than the one that actually backs it. [DOCUMENTARY]

**§9.4** The evidence package MUST NOT publish personal information about beneficiaries or guardians that would put them at risk. Proof of compliance MUST be achievable without it. [DOCUMENTARY]

**§9.5** The evidence package MUST state the residual risks the deployment accepts, including those in §4.4 and any deviation disclosed under §12.3. [GOVERNANCE]

## §10. Recovery and rehearsal

**§10.1** Before receiving endowment funds, a deployment MUST rehearse, on a test network, at least the following: a guardian who stops responding, a guardian key compromise, a lost backup, a malicious or unavailable coordinator, and a fee spike that prevents timely settlement. [SOFTWARE]

**§10.2** The result of each rehearsal MUST be recorded in the evidence package, including anything that failed. [DOCUMENTARY]

**§10.3** A deployment MUST rehearse guardian replacement and MUST state how long a replacement takes in practice. [GOVERNANCE]

**§10.4** Any provision that transfers control automatically after a period of guardian silence MUST define a trigger period long enough to exclude ordinary missed communication, MUST require a verification step before activation, and MUST have been tested and recorded under §10.2 before adoption. [SOFTWARE]

## §11. Legal wrapper

**§11.1** Bitcoin cannot verify a mission, confirm a beneficiary is real, or resolve a dispute. A deployment MUST name the people and the process responsible for every judgment Bitcoin cannot make. [GOVERNANCE]

**§11.2** A deployment SHOULD adopt a legal wrapper in a named jurisdiction so that fiduciary duty, contract, and dissolution are enforceable. [LEGAL]

**§11.3** A deployment MUST NOT present a legal wrapper as a guarantee. Enforcement depends on a court's cooperation and MUST be labeled LEGAL. [LEGAL]

**§11.4** A deployment MUST state what happens to the funds if the wrapper entity is dissolved, and which clause of which document controls that outcome. [LEGAL]

## §12. Conformance

**§12.1** A deployment MAY state that it is conformant with a specific release of this standard. The statement MUST name the exact release. [DOCUMENTARY]

**§12.2** A conformance statement is a checkable claim made by the deployment. It is not issued, reviewed, or endorsed by the maintainers of this standard. [GOVERNANCE]

**§12.3** A deployment that declines a SHOULD, or that deviates from any MUST, MUST disclose the deviation, the clause identifier, and the reason in its evidence package. An undisclosed deviation makes a conformance statement false. [DOCUMENTARY]

**§12.4** Conformance describes evidence against this specification. It does not establish solvency, honesty, investment prudence, legal validity, or future compliance. [GOVERNANCE]

**§12.5** Conformance MUST be verifiable by an outside party using `../schemas/` and `../tests/` without contacting the deployment or the maintainers. [SOFTWARE]

## §13. Withdrawn clauses

None. When a clause is withdrawn, its identifier is listed here with the release that withdrew it and the reason. Withdrawn identifiers are never reused.
