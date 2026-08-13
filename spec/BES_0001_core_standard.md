# BES 0001: Governance and Conformance Standard for a Native Bitcoin Endowment

**Editor's draft. No release has been published and no clause identifier is frozen.** Identifiers become permanent at the first tagged release and not before. Until then, clauses may be renumbered, merged, or split without notice. Do not cite this document in a binding instrument yet.

Not legal advice. See `../DISCLAIMER.md`.

**What this standard covers.** Governance, roles, amendment, evidence, and the claims a deployment is permitted to make. It also requires a deployment to disclose its complete spending policy and its correlated control analysis, because a governance claim about distributed authority is meaningless without them.

**What this standard does not cover.** Operational custody. Key generation, device handling, transaction verification procedure, backup integrity, fee and coin policy, chain monitoring, software supply chain, and incident response are the subject of BES 0002, which does not exist yet. This document does not enumerate those requirements, does not assess them, and conformance with it says nothing about whether a deployment operates its custody competently. Where this standard requires that something exist, be rehearsed, or be published, the content of that thing is operational and out of scope. See §12.

## How to read this document

Every normative statement sits in a numbered clause and states one testable proposition. Where a requirement has two parts a verifier would check differently, it is two clauses.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are used only as defined in §1.2, and nowhere else in this repository in a casual sense.

### The two label fields

Every normative clause carries two fields, because the mechanism that enforces a requirement and the evidence a verifier uses to check it are different questions, and conflating them is how a standard ends up calling an organizational fact a Bitcoin fact.

**CONTROL. What actually constrains behavior.**

| Value | Meaning |
|-------|---------|
| CONSENSUS | A Bitcoin node will reject a transaction that violates it |
| SOFTWARE | Software refuses or flags it, and can be bypassed by anyone able to sign |
| LEGAL | A court or regulator may enforce it |
| GOVERNANCE | Only people following their own stated process enforce it |

**EVIDENCE. How an outside party checks the claim.**

| Value | Meaning |
|-------|---------|
| CHAIN | Verifiable against the block chain by anyone |
| REPRODUCIBLE | Verifiable by rerunning published software on published inputs |
| DOCUMENTARY | Depends on a record someone submitted, which means deciding whether to trust the submitter |

A clause may list more than one evidence value. `CHAIN + DOCUMENTARY` means the chain proves part of the claim and a submitted record supplies the rest.

**The test for CONSENSUS.** If evaluating the sentence requires knowing an identity, a disclosure, a classification, or an intention, its control is not CONSENSUS, however much chain evidence supports it. Bitcoin enforces authorization conditions over keys. It does not know who holds a key, what role that person occupies, whether a key was stolen, or whether anything was published.

**Derived verification basis.** Where a single label is needed for a lay reader, it is derived by weakest link, never by strongest component. CHAIN is stronger than REPRODUCIBLE, which is stronger than DOCUMENTARY. A claim resting on consensus plus documentary attribution derives to DOCUMENTARY. The derived value is called the verification basis. It is never called BITCOIN, because a claim that Bitcoin verifies an organizational fact is false however it is presented.

Worked example. A three of five spend has CONTROL CONSENSUS and EVIDENCE CHAIN. That is a claim about keys. The claim that those five keys belong to five independent guardians is a different clause, with CONTROL GOVERNANCE and EVIDENCE DOCUMENTARY, and its verification basis is DOCUMENTARY. Keeping them apart is the entire point of the two fields.

Terms are defined in `glossary.md`, which is informative. Where the glossary and this document conflict, this document governs.

## §1. Scope, interpretation, and conformance vocabulary

**§1.1** This standard defines how a Bitcoin endowment governs itself so that authority is distributed, the claims it makes are checkable, and any process that could be abused is slow, visible, and logged. [GOVERNANCE | DOCUMENTARY]

**§1.2** MUST and MUST NOT state an absolute requirement. A deployment that does not meet a MUST is nonconformant, whether or not it discloses the fact. SHOULD and SHOULD NOT state a strong recommendation that a deployment MAY decline by disclosing the decision under §11.4. MAY states an option with no conformance consequence. [GOVERNANCE | DOCUMENTARY]

**§1.3** Disclosure does not cure an unmet MUST. A deployment that discloses a MUST level deviation is honest and nonconformant, and MUST use the vocabulary in §11.2 rather than claiming conformance. [GOVERNANCE | DOCUMENTARY]

**§1.4** This standard does not make an endowment trustless. It defines where trust is required, how it is distributed, and how it is disclosed. A deployment MUST NOT describe itself as trustless on the basis of this standard. [GOVERNANCE | DOCUMENTARY]

**§1.5** A deployment MUST hold its own constitution as a complete, independent document that can be read and enforced without reference to this standard. [GOVERNANCE | DOCUMENTARY]

**§1.6** A constitution MUST NOT incorporate this standard by reference, and MUST NOT provide that this standard governs matters on which the constitution is silent. Where a deployment wants a requirement of this standard, it copies the requirement into its constitution. [GOVERNANCE | DOCUMENTARY]

## §2. Spending policy and effective control

This section is the minimum custody interface this standard depends on. It requires disclosure and sets one floor. It does not standardize how custody is operated, which is §12.

**§2.1** A deployment MUST publish the complete spending policy for every coin it controls, covering the network, the descriptor or equivalent policy expression, key origin information sufficient for watch only verification, every key path, script path, and recovery branch, and every timelock. [GOVERNANCE | DOCUMENTARY]

**§2.2** The published policy MUST be sufficient for an outside party to reconstruct the exact on chain output that holds the coins, including, where Taproot is used, the output key and the commitment to the script tree. A list of asserted paths is not evidence that the list is complete. [SOFTWARE | REPRODUCIBLE]

**§2.3** A deployment MUST state the weakest authorization condition across all paths in its published policy, expressed as the smallest set of parties that can authorize a spend by any route. [GOVERNANCE | DOCUMENTARY]

**§2.4** A deployment MUST NOT operate an undisclosed path that authorizes a spend under a condition weaker than the one stated under §2.3. [GOVERNANCE | CHAIN + DOCUMENTARY]

**§2.5** Every script path in the published policy, including every recovery branch, MUST commit a spending condition requiring signatures satisfying at least three of at least five distinct keys. [CONSENSUS | CHAIN]

**§2.6** A deployment MUST declare, for each path, whether its threshold is enforced by consensus, meaning it is committed in script, or produced by an off chain aggregate signing protocol such as a Taproot key path using multiparty signing. [GOVERNANCE | DOCUMENTARY]

**§2.7** Where a deployment does not use the Taproot key path, the internal key MUST be a provably unspendable point, and the deployment MUST publish the derivation that proves it. An enabled key path nobody mentions is the most consequential undisclosed path there is. [CONSENSUS | CHAIN]

**§2.8** Where a deployment does use an aggregate or threshold signing protocol on the key path, the participant set and threshold MUST be published, MUST itself be at least three of at least five participants, and MUST be published with CONTROL SOFTWARE or GOVERNANCE. Bitcoin sees one signature for one output key and enforces nothing about how it was produced, so a deployment MUST NOT present an aggregate signing threshold as enforced by consensus. [GOVERNANCE | DOCUMENTARY]

**§2.9** The keys or participants in each path MUST map to at least five distinct parties, each holding exactly one authorization share, each independent under §3. [GOVERNANCE | DOCUMENTARY]

**§2.10** Every authorization condition a deployment claims Bitcoin enforces MUST be committed in the spending condition of the coins it applies to. [CONSENSUS | CHAIN]

**§2.11** A restriction enforced by a rule engine, a coordinator, or a policy document MUST NOT be described as enforced by Bitcoin, and MUST be published with CONTROL SOFTWARE or GOVERNANCE. [GOVERNANCE | DOCUMENTARY]

**§2.12** A deployment MUST publish a method by which any party can derive its receive addresses from the published policy. [SOFTWARE | REPRODUCIBLE]

**§2.13** A deployment MUST verify a receive address against that derivation before publishing it for donations. [GOVERNANCE | REPRODUCIBLE]

**§2.14** Endowment coins MUST NOT be held by a third party custodian or on an exchange. [GOVERNANCE | DOCUMENTARY]

**§2.15** A deployment MUST disclose any arrangement under which a party other than its guardians can influence, delay, or block a spend, including coordinator services and signing service providers. [GOVERNANCE | DOCUMENTARY]

## §3. Guardians and correlated control

**§3.1** A guardian is a party holding one authorization share in the published spending policy. A party holding more than one share counts as one guardian for every count in this standard, and its shares count once toward every threshold. [GOVERNANCE | DOCUMENTARY]

**§3.2** A deployment MUST identify, for each guardian, its beneficial owner or controlling entity, its employer or funding source where one exists, its jurisdiction of legal residence, its physical location where it differs from that jurisdiction, its signing device and software stack, its backup facility, its coordinator and communication dependencies, and its recovery dependencies. [GOVERNANCE | DOCUMENTARY]

**§3.3** A correlated failure domain is a named set of guardians sharing a dependency capable of common control, common compromise, common coercion, or common unavailability. A deployment MUST publish, for every spending path, a table naming each domain, the dependency it rests on, and the guardians it contains. [GOVERNANCE | DOCUMENTARY]

**§3.4** Domains MUST be aggregated where they share a parent dependency. Several domains that are individually small but reachable through one vendor, funder, or legal authority are one domain for the tests in §3.5 and §3.6. [GOVERNANCE | DOCUMENTARY]

**§3.5** For every spending path, every control or compromise domain MUST contain fewer than m guardians, where m is the threshold for that path. [GOVERNANCE | DOCUMENTARY]

**§3.6** For every spending path, every unavailability domain MUST contain fewer than n minus m plus one guardians, so that no single domain can make the threshold unreachable. [GOVERNANCE | DOCUMENTARY]

**§3.7** A deployment MUST publish a coercion analysis covering known legal residence, physical location, controlling entities, beneficial control, and cross border dependencies, and MUST state the residual uncertainty that remains. A deployment MUST NOT claim it has proved that no jurisdiction can reach m guardians, because jurisdictions cooperate and exert extraterritorial and physical pressure, and that negative cannot be proved. [LEGAL | DOCUMENTARY]

**§3.8** Residence or jurisdiction counts MUST NOT be presented as satisfying §3.5, §3.6, or §3.7. They are one input to the analysis. [GOVERNANCE | DOCUMENTARY]

**§3.9** The tables and analysis required by §3.3 through §3.7 MUST be republished at least annually and after any change of guardian, signing stack, or recovery arrangement. [GOVERNANCE | DOCUMENTARY]

**§3.10** A deployment MUST state, using its own values of m and n and covering every spending path, how many guardians can become unavailable before spending halts, being n minus m, and how many acting together can authorize a spend against the mission, being m. Where paths differ, each path MUST be stated separately. This disclosure MUST NOT be minimized, footnoted, or omitted. [GOVERNANCE | DOCUMENTARY]

## §4. Roles and separation

**§4.1** A guardian MUST NOT also serve as an administrator. [GOVERNANCE | DOCUMENTARY]

**§4.2** An administrator MUST NOT hold an authorization share in the spending policy. [GOVERNANCE | CHAIN + DOCUMENTARY]

**§4.3** An administrator MUST NOT change a rule at any tier. [GOVERNANCE | DOCUMENTARY]

**§4.4** An administrator MUST NOT select or exclude a beneficiary outside the criteria fixed in the constitution. [GOVERNANCE | DOCUMENTARY]

**§4.5** An administrator MUST NOT suppress, delay, or omit a failed compliance check from the record. [GOVERNANCE | DOCUMENTARY]

**§4.6** An administrator MAY prepare paperwork, draft unsigned transactions, publish evidence, and communicate with beneficiaries. [GOVERNANCE | DOCUMENTARY]

**§4.7** Every administrator action MUST be published as one of three types: automatic and reproducible, based on a claim not yet independently verified, or a judgment call requiring guardian approval with a recorded justification. [GOVERNANCE | DOCUMENTARY]

**§4.8** A deployment SHOULD assign reconciliation of the published record to a party who is neither an administrator nor a guardian. [GOVERNANCE | DOCUMENTARY]

## §5. Asset and spending policy

**§5.1** A deployment MUST state, before it receives funds, whether spending draws from principal, from new donations, or from separately disclosed income. [GOVERNANCE | DOCUMENTARY]

**§5.2** A deployment MUST NOT represent bitcoin as producing yield on its own. [GOVERNANCE | DOCUMENTARY]

**§5.3** A deployment MUST state its spending rule as a formula, including the measurement window and the unit of account used to value the endowment. [GOVERNANCE | DOCUMENTARY]

**§5.4** Endowment coins MUST NOT be lent, pledged as collateral, rehypothecated, or converted into a wrapped or synthetic representation of bitcoin. A deployment that does any of these is nonconformant, however it discloses the fact. [GOVERNANCE | DOCUMENTARY]

**§5.5** A deployment MAY hold assets other than its endowment coins, including operating cash, and MUST disclose each holding, its purpose, its size relative to the endowment, and its counterparty. [GOVERNANCE | DOCUMENTARY]

## §6. Rule tiers and amendment

**§6.1** A deployment's constitution MUST define exactly three tiers: Tier One covering the mission, the prohibition on personal profit by administrators and guardians, and the procedure for amending Tier One; Tier Two covering beneficiary criteria and spending limits; Tier Three covering routine numeric parameters that update under a formula fixed in the constitution. [GOVERNANCE | DOCUMENTARY]

**§6.2** Every rule in the constitution MUST state its tier. [GOVERNANCE | DOCUMENTARY]

**§6.3** Each tier MUST publish its approval threshold and its public notice period as explicit values. [GOVERNANCE | DOCUMENTARY]

**§6.4** Tier One's approval threshold MUST be greater than or equal to Tier Two's, and Tier One's notice period MUST be greater than or equal to Tier Two's, with at least one of the two strictly greater. [GOVERNANCE | DOCUMENTARY]

**§6.5** Tier Three parameters MAY update automatically, and MUST be logged publicly when they do. [SOFTWARE | REPRODUCIBLE]

**§6.6** A deployment MUST NOT label any rule permanent or unamendable. [GOVERNANCE | DOCUMENTARY]

**§6.7** A deployment is never required to adopt a later release of this standard. [GOVERNANCE | DOCUMENTARY]

## §7. Payment authorization

This section governs who decides and what is published. How a guardian technically verifies a transaction is operational and belongs to the standard named under §12.2.

**§7.1** An administrator MUST publish or commit to a payment request, with its supporting evidence classified under §8, before any guardian signs. [GOVERNANCE | DOCUMENTARY]

**§7.2** Where a request is published as a commitment rather than in full under §8.4, the deployment MUST publish the opening of that commitment once disclosure is no longer harmful, or state why it never will be. [GOVERNANCE | DOCUMENTARY]

**§7.3** Where a deployment claims an automatic check, it MUST publish the checking software, its version, and its inputs, so that any party can rerun the check and reach the same result. [SOFTWARE | REPRODUCIBLE]

**§7.4** Each guardian MUST reach its own decision on each request, and MUST NOT delegate that decision to an administrator, to a coordinator, or to another guardian. [GOVERNANCE | DOCUMENTARY]

**§7.5** A deployment MUST publish the procedure its guardians follow to verify a transaction before signing, and MUST identify the operational standard, if any, that procedure conforms to. This standard does not specify that procedure. [GOVERNANCE | DOCUMENTARY]

**§7.6** A transaction spending endowment coins MUST satisfy a committed spending condition meeting §2.5, or, where the key path is used, a signature over the output key produced under the arrangement declared in §2.8. [CONSENSUS | CHAIN]

**§7.6.1** The path used MUST be one whose party mapping under §2.9 meets the condition stated under §2.3. Consensus knows the keys and the condition satisfied. It does not know which parties held them, so this comparison is made by a reader against the published mapping, not by a node. [GOVERNANCE | DOCUMENTARY]

**§7.7** The transaction identifier and the record supporting a payment MUST be published once the payment confirms, subject to the evidence classes in §8. [GOVERNANCE | DOCUMENTARY]

**§7.8** If required evidence is missing, unclear, or fails a check, the payment MUST NOT proceed. A deployment MUST NOT operate any path that completes a payment without passing every check. [GOVERNANCE | DOCUMENTARY]

## §8. Evidence, publication, and privacy

**§8.1** A deployment MUST publish and maintain an evidence package. [GOVERNANCE | DOCUMENTARY]

**§8.2** The evidence package MUST contain the release of this standard in use, the constitution, the published spending policy under §2.1, the weakest authorization condition under §2.3, the domain tables and analysis under §3.3 through §3.7, the disclosure under §3.10, the record of past payments, and any audit results with the auditor named. [GOVERNANCE | DOCUMENTARY]

**§8.3** Every claim in the evidence package MUST carry a CONTROL value and an EVIDENCE value, and MUST NOT be published under a stronger value than the one that actually backs it. [GOVERNANCE | DOCUMENTARY]

**§8.4** Every item in the evidence package MUST be assigned one publication class: public, meaning disclosed in full; redacted, meaning disclosed with identified fields removed; committed, meaning a salted commitment is published and the opening withheld; delayed, meaning full disclosure occurs after a stated period; or restricted, meaning disclosed only to a named independent auditor under a stated retention policy. [GOVERNANCE | DOCUMENTARY]

**§8.5** A deployment MUST NOT publish information about a beneficiary or guardian that would expose them to physical, legal, or financial harm, and MUST use a class under §8.4 that avoids it. [GOVERNANCE | DOCUMENTARY]

**§8.6** A deployment MUST state, for each item that is not public, what an outside party consequently cannot verify. A conformance claim MUST NOT assert that outsiders can verify a fact that its own publication class prevents them from seeing. [GOVERNANCE | DOCUMENTARY]

**§8.7** A deployment MUST publish its retention policy for beneficiary and guardian data. [GOVERNANCE | DOCUMENTARY]

**§8.8** The evidence package MUST state the residual risks the deployment accepts, including those under §3.7 and §3.10 and any deviation disclosed under §11.4. [GOVERNANCE | DOCUMENTARY]

## §9. Continuity

This section requires that recovery capability exist, be exercised, and be reported. It does not specify what a recovery plan contains, which is operational and belongs to the standard named under §12.2.

**§9.1** Before receiving funds, a deployment MUST hold a documented recovery plan that its guardians have executed end to end at least once. [GOVERNANCE | DOCUMENTARY]

**§9.2** A deployment MUST identify the operational standard its recovery plan follows, or state that it follows none. [GOVERNANCE | DOCUMENTARY]

**§9.3** A deployment MUST rehearse its recovery plan at least annually, and after any change of guardian roster, spending policy, signing software, or signing hardware. [GOVERNANCE | DOCUMENTARY]

**§9.4** A deployment MUST publish the result of each rehearsal, including anything that failed. [GOVERNANCE | DOCUMENTARY]

**§9.5** A deployment MUST mark each rehearsed scenario as observed or simulated. A scenario that cannot be reproduced outside mainnet, including a fee market spike, is simulated. [GOVERNANCE | DOCUMENTARY]

**§9.6** A deployment MUST publish how long guardian replacement took when rehearsed. [GOVERNANCE | DOCUMENTARY]

**§9.7** A deployment MUST NOT publish the revocation of a compromised key as a completed remedy until the coins that key controlled have been moved to a policy excluding it. [GOVERNANCE | CHAIN + DOCUMENTARY]

**§9.8** Any provision that transfers control after a period of guardian silence MUST state its trigger period as an explicit value, MUST require a verification step before activation, and MUST have been rehearsed and published under §9.4. [GOVERNANCE | DOCUMENTARY]

**§9.9** Where such a provision is enforced by a timelocked spending path, the timelock MUST be committed in the spending condition. [CONSENSUS | CHAIN]

## §10. Legal wrapper

**§10.1** A deployment MUST name the people and the process responsible for every judgment Bitcoin cannot make, including whether a beneficiary is real and whether the mission is being served. [GOVERNANCE | DOCUMENTARY]

**§10.2** A deployment SHOULD adopt a legal wrapper in a named jurisdiction. [LEGAL | DOCUMENTARY]

**§10.3** A deployment MUST NOT present a legal wrapper as a guarantee that any duty is enforceable. Enforcement depends on a court's cooperation. [LEGAL | DOCUMENTARY]

**§10.4** A deployment MUST state what the legal instrument requires on dissolution, and which clause of which document controls it. [LEGAL | DOCUMENTARY]

**§10.5** A deployment MUST state separately whether the guardians holding authorization shares are technically able to spend contrary to the outcome required under §10.4, and what, if anything, prevents it. [GOVERNANCE | CHAIN + DOCUMENTARY]

## §11. Conformance

**§11.1** A deployment that meets every MUST in this standard MAY state that it is conformant with a named release. The statement MUST name the exact release. [GOVERNANCE | DOCUMENTARY]

**§11.2** A deployment that does not meet every MUST MUST NOT claim conformance. It MAY state that it is based on a named release of this standard, with declared deviations. These are the only two claims this standard defines. [GOVERNANCE | DOCUMENTARY]

**§11.3** A conformance claim is made by the deployment about itself. It is not issued, reviewed, or endorsed by the maintainers of this standard. [GOVERNANCE | DOCUMENTARY]

**§11.4** A deployment MUST publish a deviation register listing every declined SHOULD and every unmet MUST, each with its clause identifier and reason. [GOVERNANCE | DOCUMENTARY]

**§11.5** The structure of a deployment's published manifest MUST be machine validatable against the schema for the release it names. [SOFTWARE | REPRODUCIBLE]

**§11.6** Structural validation checks assertions, not conformance. A deployment MUST NOT present a passing schema validation as evidence of conformance. Conformance requires chain, documentary, governance, and legal review by a reader. [GOVERNANCE | DOCUMENTARY]

**§11.7** Conformance describes evidence against this specification. It does not establish solvency, honesty, investment prudence, custody competence, legal validity, or future compliance. [GOVERNANCE | DOCUMENTARY]

## §12. Interface to operational custody

**§12.1** This standard evaluates governance and evidence claims. It does not establish operational custody safety. A deployment MUST NOT present conformance with this standard as evidence that its custody operations are sound. [GOVERNANCE | DOCUMENTARY]

**§12.2** A deployment MUST either name the operational custody standard and exact release it follows, or state plainly that its custody operations are outside the scope of this standard and remain unassessed. [GOVERNANCE | DOCUMENTARY]

**§12.3** Conformance with this standard MUST NOT be presented as conformance with any operational custody standard. The two are claimed separately. [GOVERNANCE | DOCUMENTARY]

**§12.4** The custody interface this standard depends on is §2 in full, together with §7.5, §9.1, and §9.2. These require disclosure, existence, and identification. None of them specify how custody is operated, and this standard MUST NOT be read as standardizing operational practice. [GOVERNANCE | DOCUMENTARY]

## §13. Clause status register

While this document is an editor's draft, no clause is frozen and this register is empty.

At the first tagged release, every clause enters this register with status `active`. Thereafter each clause carries exactly one status, and the register is the machine readable record of which:

| Status | Meaning |
|--------|---------|
| `active` | In force at this release |
| `amended` | Text changed at a stated release, identifier retained, meaning may have changed |
| `withdrawn` | No longer in force from a stated release. Identifier never reused |

An amendment that changes what a clause requires is a MAJOR change under `../VERSIONING.md` and requires a proposal. A clause is never renumbered after the first release.
