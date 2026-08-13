# Threat model

Editor's draft. No release tagged.

**Status: analysis only.** Nothing in this document has been adversarially tested. The stress test against guardian loss, guardian collusion, legal dispute, and technical failure is scheduled and will run in the open, with results recorded here. Until then, treat every mitigation below as a design intention rather than a demonstrated property. This is the one document in this repository that cannot be quietly fixed later, so its untested status is stated first rather than in a footnote.

## What this design is trying to prevent

One party moving endowment funds alone. Silent drift away from the founding mission. Fraud by whoever handles daily operations. A single point of failure in custody, jurisdiction, or software. Risk that exists but was never written down.

## What this design cannot prevent

Collusion at or above the signing threshold. A court order in a jurisdiction where a guardian or the wrapper entity is exposed. A mission that was badly chosen. Beneficiaries who are real, documented, and undeserving. Loss of funds through operational error by the required number of guardians acting in good faith.

## Actors

**Guardians.** Hold one key each. Assumed competent and honest individually, and capable of collusion collectively.
**Administrators.** Hold no keys. Assumed to have the strongest incentive and the most frequent opportunity for fraud, which is why §5 removes their ability to act alone.
**Coordinator software.** Assembles unsigned transactions. Assumed potentially malicious or unavailable.
**Outside verifiers.** Assumed adversarial, which is the point. The evidence package is designed for a hostile reader.
**Standard maintainers.** Assumed capturable, which is why §4.5 bars them from serving as guardians and why the license permits anyone to fork without permission.

## Scenarios

**A guardian goes silent.** A deployment tolerates n minus m unavailable guardians before spending halts, per spending path. §9.5 requires that replacement be rehearsed and its real duration published, because an untested replacement procedure is the most common way this scenario becomes permanent.

**A guardian key is compromised.** One key is insufficient at any conformant threshold. The compromise must be detected, disclosed, and the coins moved to a policy that excludes the key. §9.6 exists because a declaration of revocation changes nothing: an attacker holding a share keeps it until the coins move. Detection is the weak link and it is a governance property, not a chain enforced one.

**Guardians collude at the threshold.** Any m guardians can move funds against the mission, and Bitcoin validates the transaction as correct, because it is correct. Nothing in this design prevents it. §3.3 makes it harder to arrange, §3.7 requires the real number be stated out loud using the deployment's own m and n, and §10 is where a legal wrapper may create consequences afterward. Consequences afterward are not prevention.

**The administrator commits fraud.** Blocked from signing by §5.3, blocked from choosing beneficiaries outside fixed criteria by §5.3, and exposed by the publication requirements in §5.4 and §8.1. The residual path is a well documented fraudulent request that guardians approve without independent review, which is why §8.3 puts the review duty on each guardian individually.

**The coordinator turns malicious.** It can present a transaction that does not match the published request. The defence is each guardian verifying the transaction independently rather than trusting the interface presenting it. This is a GOVERNANCE property and it degrades quietly as a deployment gets busy.

**Legal seizure or compulsion.** A guardian may be compelled in their own jurisdiction. §3.5 requires that no single coercive jurisdiction reach m guardians by legal order or physical reach. Counting countries does not satisfy this. Three countries where one actor can reach three guardians is worse than two countries where nobody can reach m.

**The wrapper entity fails or is dissolved.** §10.4 requires the legal outcome to be stated in advance in a named document, and §10.5 separately requires the deployment to state whether the guardians are technically able to disregard it. Those two answers are frequently different, and publishing only the first is the more comfortable half of the truth.

**A fee spike prevents timely settlement.** Rehearsed under §9.3, and necessarily simulated rather than observed, since a test network cannot reproduce a mainnet fee market. §9.4 requires that a simulated scenario be marked as simulated, so nobody later mistakes a rehearsal for evidence.

**An undisclosed spending path exists.** A three of five script path sits alongside a key path or recovery branch that spends with less. Every other control in this document is decoration if this is true. §2.1 requires the complete policy be published, §2.2 requires the weakest condition be stated, and §2.3 forbids anything weaker existing undisclosed. A verifier who checks nothing else should check this.

**A coordinator substitutes a receive address.** Donations flow to an address that does not belong to the endowment. §2.7 requires that addresses be derivable from the published policy and verified before publication.

**Backups fail together.** §3.2 requires backup facility and signing stack be disclosed per guardian, and §3.4 forbids any single domain disabling enough guardians to make the threshold unreachable. Correlated backup loss is the failure mode that has ended real treasuries, and it rests on documentary evidence, meaning someone has to check it rather than accept the assertion.

## Residual risk, stated plainly

Every statement here is parameterized by a deployment's own m and n, per §3.7, and by every spending path separately. Loss of n minus m guardians does not stop fund movement. Collusion among m can move funds against the mission. A rule engine can be bypassed by guardians signing a different valid transaction unless the restriction is committed in the spending condition. A legal wrapper depends on a court's cooperation. Detection of a compromised key depends on people paying attention, and until the coins move, a compromised key still works.

This standard governs governance and evidence. It does not assess custody operations, per §12.1, so nothing here should be read as saying a conformant deployment holds its keys competently.

A deployment that finds these unacceptable should raise its threshold or narrow its paths, not describe the risk differently.
