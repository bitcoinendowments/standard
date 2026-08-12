# Glossary

Informative. Where this glossary conflicts with `BES_0001_core_standard.md`, the standard governs.

This glossary serves two readers who arrive from opposite directions: a lawyer or treasurer who does not work with Bitcoin, and an engineer who does not work with charity governance. Terms from both sides are defined here.

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

**Verification label.** One of BITCOIN, SOFTWARE, DOCUMENTARY, LEGAL, or GOVERNANCE, stating what actually backs a claim. Defined in BES 0001 §1.3.

**Wrapper, or legal wrapper.** The legal entity, such as a trust or foundation, that gives the arrangement standing in a court. Necessary for anything Bitcoin cannot evaluate. See BES 0001 §11.
