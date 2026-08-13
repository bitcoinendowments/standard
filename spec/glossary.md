# Glossary

Informative. Where this glossary conflicts with `BES_0001_core_standard.md`, the standard governs.

This glossary serves two readers who arrive from opposite directions: a lawyer or treasurer who does not work with Bitcoin, and an engineer who does not work with charity governance. Terms from both sides are defined here.

**Authorization share.** One participation in a deployment's spending policy, held by one guardian. Backups are copies of the same share, not additional ones. A party holding two shares counts once toward every threshold, under BES 0001 §3.1.

**Administrator.** A person or team handling daily operations who cannot move funds. Proposes payments, prepares records, talks to beneficiaries. See BES 0001 §5.

**Beneficiary.** A recipient of endowment spending, qualifying under criteria fixed in the constitution rather than chosen at an administrator's discretion.

**Broadcast.** Publishing a signed transaction to the Bitcoin network so that it can be included in a block. Before broadcast a transaction moves nothing.

**Constitution.** The document specific to one endowment covering its mission, beneficiaries, spending rules, and its own amendment procedure. Built on this standard, owned by the organization, not adopted by reference.

**Deployment.** One specific endowment that has adopted this standard.

**Endowment.** A fund held for the long term where spending is governed by a rule rather than by discretion.

**Evidence package.** The public record through which a deployment shows it follows its constitution and this standard. See BES 0001 §9.

**Guardian.** A person or independent entity holding exactly one signing key required to move endowment funds.

**Multisignature, or multisig.** A Bitcoin arrangement where funds can only move when a set number of separate keys sign. Three of five means any three of the five key holders together can move funds, and any two together cannot.

**Principal.** The original endowment capital, as distinct from income or new donations.

**Profile.** An opinionated starting configuration, such as five guardians at a three of five threshold. A recommendation, never a requirement of the standard.

**PSBT.** Partially Signed Bitcoin Transaction. The file format that lets an unsigned transaction be passed between guardians so each can add a signature independently, without any of them handling another's key.

**Rule engine.** Software that checks a payment request against the constitution's rules before guardians sign. It can refuse to produce a request, but it cannot stop guardians from signing a different valid transaction, so its output is a SOFTWARE claim, never a BITCOIN one.

**Script.** The spending conditions committed inside a Bitcoin transaction output. Conditions written in script are enforced by every node on the network. Conditions written only in a document are not.

**Threshold.** The number of signatures required to move funds.

**Timelock.** A condition committed in script that prevents funds from moving until a stated time or block height. Enforced by the network, not by policy.

**CONTROL and EVIDENCE.** The two fields every normative clause carries. CONTROL says what constrains behavior: CONSENSUS, SOFTWARE, LEGAL, or GOVERNANCE. EVIDENCE says how an outsider checks it: CHAIN, REPRODUCIBLE, or DOCUMENTARY. They do not move together, which is why there are two.

**Correlated failure domain.** Anything that could cause several guardians to fail, be compromised, or be compelled at once: a shared owner, employer, funding source, jurisdiction, signing stack, backup facility, coordinator, or recovery dependency. BES 0001 §3.3 to §3.5 measure these against the number of guardians needed to spend.

**Descriptor.** A text expression of a wallet's spending policy, from which anyone can derive the addresses and check the conditions. Publishing it is what makes a custody claim checkable rather than asserted.

**Publication class.** How an evidence item is disclosed: public, redacted, committed, delayed, or restricted. BES 0001 §8.4 exists so that auditability does not require exposing a beneficiary to harm.

**Spending path.** One route by which coins can be spent. A policy may have several: a primary path, a recovery branch, a key path. The one that matters is the weakest, under BES 0001 §2.2.

**Verification basis.** A single derived label for lay readers, computed by weakest link across a claim's evidence values, never by strongest component. A claim resting on consensus plus documentary attribution derives to DOCUMENTARY. It is never called BITCOIN.

**Weakest authorization condition.** The smallest set of parties that can authorize a spend by any route in the published policy. This number, not the one on the impressive path, is a deployment's real security.

**Wrapper, or legal wrapper.** The legal entity, such as a trust or foundation, that gives the arrangement standing in a court. Necessary for anything Bitcoin cannot evaluate. See BES 0001 §11.
