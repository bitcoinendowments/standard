# Threat model

Release 0.1.0.

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

**A guardian goes silent.** Below the threshold, spending continues. At or above it, spending halts until replacement. BES 0001 §10.3 requires that replacement be rehearsed and its real duration published, because an untested replacement procedure is the most common way this scenario becomes permanent.

**A guardian key is compromised.** One key is insufficient. The compromise must be detected, disclosed, and the key rotated. Detection is the weak link, and it is a GOVERNANCE claim, not a BITCOIN one.

**Guardians collude at the threshold.** Funds move against the mission and Bitcoin validates the transaction as correct, because it is correct. Nothing in this design prevents it. §4.1 makes it harder to arrange, §4.4 requires it be stated out loud, and §11 is where a legal wrapper may create consequences afterward. Consequences afterward are not prevention.

**The administrator commits fraud.** Blocked from signing by §5.3, blocked from choosing beneficiaries outside fixed criteria by §5.3, and exposed by the publication requirements in §5.4 and §8.1. The residual path is a well documented fraudulent request that guardians approve without independent review, which is why §8.3 puts the review duty on each guardian individually.

**The coordinator turns malicious.** It can present a transaction that does not match the published request. The defence is each guardian verifying the transaction independently rather than trusting the interface presenting it. This is a GOVERNANCE property and it degrades quietly as a deployment gets busy.

**Legal seizure or compulsion.** A guardian may be compelled in their own jurisdiction. §4.2 spreads guardians across at least three countries so no single order reaches the threshold. Whether that holds depends entirely on which countries.

**The wrapper entity fails or is dissolved.** §11.4 requires the outcome to be stated in advance, in a named document, before it matters.

**A fee spike prevents timely settlement.** Rehearsed under §10.1. An endowment that has never seen this in testing will meet it during a crisis.

**Backups fail together.** §4.1 prohibits a shared backup custodian and a shared key storage system. Correlated backup loss is the failure mode that has ended real treasuries, and it is a DOCUMENTARY claim, meaning someone has to actually check it rather than assert it.

## Residual risk, stated plainly

Loss of any two guardians does not stop fund movement. Collusion among three or more can move funds against the mission. A rule engine can be bypassed by guardians signing a different valid transaction unless the restriction is committed in script. A legal wrapper depends on a court's cooperation. Detection of a compromised key depends on people paying attention.

A deployment that finds these unacceptable should raise its threshold, not describe the risk differently.
