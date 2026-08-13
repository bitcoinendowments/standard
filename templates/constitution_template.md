# Constitution of <ORGANIZATION NAME>

Adopted <YYYY MM DD>. Version <X.Y>.

> **How to use this template.** Replace every value in angle brackets. Read the note under each section before choosing, because most of these are trades rather than settings. Delete the notes before adopting.
>
> This document must stand on its own. BES 0001 §1.6 forbids a constitution from incorporating the standard by reference or providing that the standard governs where the constitution is silent, because a governing document that depends on a file in someone else's repository is not a governing document. Copy in what you want. Then you own it.
>
> Have your own counsel review the completed document before you rely on it. See `../DISCLAIMER.md`.

## 0. Relationship to BES 0001

This constitution was drafted against BES 0001 at release <RELEASE>. That reference is informational. This document is complete in itself, and nothing in BES 0001 governs <ORGANIZATION NAME> except to the extent it is written out below.

<ORGANIZATION NAME> publishes its conformance claim under section 13.

## 1. Mission (Tier One)

<ORGANIZATION NAME> exists to <MISSION IN ONE SENTENCE>.

<ORGANIZATION NAME> does not <EXCLUDED ACTIVITIES>. No administrator, guardian, or auditor may receive any payment, grant, gift, or benefit beyond the disclosed compensation fixed under section 7.

> *Note.* This is the hardest thing here to change and the thing everything else serves. Write it so a stranger in twenty years can tell whether a given payment fits it. A mission broad enough to permit anything permits drift.

## 2. Spending policy and control

2.1 <ORGANIZATION NAME> publishes the complete spending policy for every coin it controls, including the network, the descriptor, key origin information sufficient for watch only verification, every key path, script path, and recovery branch, and every timelock. The policy is published at <LOCATION>.

2.2 The weakest authorization condition across every path is <M> of <N>. No path, including any recovery branch, authorizes a spend under a weaker condition.

2.3 Receive addresses are derived from the published policy and verified against that derivation before publication. The derivation method is published at <LOCATION>.

2.4 Coins are not held by any third party custodian or on any exchange.

2.5 The following parties can influence, delay, or block a spend without holding an authorization share: <COORDINATOR OR SERVICES, or "none">.

> *Note.* Section 2.2 is the number that describes your actual security, and it is the one people get wrong. A five of seven primary path with a two key recovery branch is a two key endowment. Work out the weakest route before writing anything here, and publish the policy so a stranger can check your answer rather than take it.

## 3. Guardians

3.1 <ORGANIZATION NAME> has <N> guardians. Each holds exactly one authorization share. A party holding more than one share counts as one guardian for every count in this constitution.

3.2 For each guardian, <ORGANIZATION NAME> publishes the beneficial owner or controlling entity, the employer or funding source, the jurisdiction of legal residence, the signing device and software stack, the backup facility, the coordinator and communication dependencies, and the recovery dependencies.

3.3 No single correlated failure domain across those factors controls <M> guardians, and none can disable enough guardians to make <M> unreachable.

3.4 No single coercive jurisdiction can reach <M> guardians by legal order or physical reach.

3.5 This analysis is republished at least annually and after any change of guardian, signing stack, or recovery arrangement.

3.6 Disclosed risk, in this deployment's own numbers: loss of <N minus M> guardians does not stop spending, and <M> guardians acting together can spend against the mission. Where a path differs, each is stated separately: <PER PATH FIGURES>.

3.7 Guardian succession. If a guardian is unreachable across at least two independent channels for <DAYS> consecutive days, the remaining guardians may vote, at <SUCCESSION THRESHOLD>, to designate a replacement satisfying 3.2 to 3.4. This replaces a seat. It does not move coins and carries no automatic transfer of control. The vote, the contact attempts, and the replacement's disclosure are published.

> *Note.* Counting countries is not the analysis. Five guardians in three countries can satisfy 3.4 or fail it badly, depending on where they sit and who can reach them. Ask which single actor, order, employer, or supply chain could reach or disable <M>, and answer that question in writing.

## 4. Rule engine (optional)

4.1 Parameter updates within bounds already fixed by this constitution apply automatically and are logged. Logic changes require guardian approval at <THRESHOLD> followed by <DAYS> days of public notice. Emergency patches that narrow, never widen, what the engine will approve may be approved by <THRESHOLD> within <HOURS> hours, with public disclosure and full review within <DAYS> days.

4.2 Guardians may revert to the last reviewed version at any time at <THRESHOLD>, with no delay on a rollback.

4.3 Guardians sign only against a hash pinned engine version and attest to the version they run.

4.4 The rule engine constrains nothing that guardians cannot override by signing a different valid transaction. It is published as a software control and never as one Bitcoin enforces.

> *Note.* Delete this section if you do not run an engine.

## 5. Beneficiaries (Tier Two)

5.1 Eligible beneficiaries are <ELIGIBILITY CRITERIA>.

5.2 A single beneficiary may not receive more than <PERCENT> of a year's distribution pool.

5.3 Administration screens applications against these criteria and publishes accepted and rejected applications with reasons, subject to the publication classes in section 9. Administration has no discretion to add criteria.

## 6. Spending

6.1 Each year <ORGANIZATION NAME> distributes <RATE> of the trailing <WINDOW> average treasury value, measured in <UNIT OF ACCOUNT>, converted at the time of distribution.

6.2 This is spending from <PRINCIPAL / NEW DONATIONS / DISCLOSED INCOME>. Bitcoin generates no yield on its own. The rate assumes <ASSUMPTION>. It is a discipline rule, not a guarantee, and this assumption is restated in every annual report.

6.3 Coins are not lent, pledged as collateral, rehypothecated, or converted into any wrapped or synthetic representation of bitcoin.

6.4 Assets other than the endowment coins, including operating cash: <HOLDINGS, PURPOSE, SIZE, COUNTERPARTY, or "none">.

> *Note.* The unit of account matters more than the rate. Measuring in fiat makes the payout stable in fiat and variable in bitcoin. A longer window smooths volatility and slows your response to a real change in circumstances.

## 7. Administration

7.1 Administration is <PAID / VOLUNTEER>, compensation fixed annually by guardians at <THRESHOLD> and published.

7.2 No administrator holds an authorization share. Administration may not change a rule at any tier, select or exclude a beneficiary outside section 5, suppress or delay a failed check, or make a payment final without guardian signatures.

7.3 Every administrator action is published as automatic and reproducible, an unverified claim, or a judgment call with a recorded justification.

7.4 <OPTIONAL: reconciliation of the published record is performed by <PARTY>, who is neither an administrator nor a guardian.>

## 8. Payment procedure

8.1 Administration publishes, or publishes a commitment to, each payment request with its supporting evidence before any guardian signs.

8.2 Where a request is committed rather than published in full, the opening is published once disclosure is no longer harmful, or the reason it never will be is stated.

8.3 Where an automatic check is claimed, the checking software, its version, and its inputs are published so any party can rerun it.

8.4 Each guardian independently reviews the unsigned transaction against the published request and this constitution before signing, including recipients, amounts, fees, inputs, change, locktime, and the policy path being satisfied, on a device independent of the coordinator that produced it.

8.5 <M> signatures are required. The transaction identifier and supporting record are published once the payment confirms.

8.6 Missing or unclear evidence stops the payment. There is no path to completion that skips a check.

## 9. Evidence and publication classes

9.1 <ORGANIZATION NAME> publishes and maintains an evidence package at <LOCATION>, with a control value and an evidence value on every claim.

9.2 Each item carries one publication class: public, redacted, committed, delayed, or restricted to a named auditor under a stated retention policy.

9.3 Nothing is published that would expose a beneficiary or guardian to physical, legal, or financial harm.

9.4 For each item that is not public, <ORGANIZATION NAME> states what an outside party consequently cannot verify, and makes no claim that outsiders can check a fact its own publication class conceals.

9.5 The retention policy for beneficiary and guardian data is published at <LOCATION>.

## 10. Recovery

10.1 <ORGANIZATION NAME> holds a documented recovery plan, executable on mainnet, covering watch only restoration, construction of a rotation transaction, verification on independent devices, loss of the coordinator, isolation of a compromised device, fee estimation and fee bumping, coin availability, chain monitoring, confirmation depth and reorganization response, backup integrity testing, and an emergency communication path.

10.2 The plan is rehearsed before funds are received, at least annually thereafter, and after any change of guardian roster, spending policy, signing software, or signing hardware. Results are published, including failures, and scenarios that were simulated rather than observed are marked as such.

10.3 A compromised key is treated as compromised until the coins it controls have been moved to a policy that excludes it. A declaration alone is not a remedy.

## 11. Amendment

11.1 Tier One, being the mission, the private benefit prohibition, the control requirements in section 2, and this section 11, requires <TIER ONE THRESHOLD> and <TIER ONE DAYS> days of public notice.

11.2 Tier Two, being beneficiary criteria, the spending rate and window, and guardian count or threshold, requires <TIER TWO THRESHOLD> and <TIER TWO DAYS> days of public notice.

11.3 Tier Three items apply automatically and are logged.

11.4 No tier is easier to amend than the tier above it, and Tier Two differs from Tier One in threshold, notice period, or both.

11.5 No provision of this constitution is permanent. Every section states its tier.

## 12. Dissolution

12.1 If guardians determine, at the Tier One threshold, that the mission has become impossible or unlawful to pursue, remaining funds transfer to <SUCCESSOR CRITERIA>, selected by the same vote and published with reasons. No guardian, administrator, or auditor may be a successor or receive dissolution proceeds.

12.2 What the legal instrument requires on dissolution: <REQUIREMENT>, controlled by <DOCUMENT AND CLAUSE>.

12.3 What the spending policy permits on dissolution: <M> guardians are technically able to spend contrary to 12.2. <STATE ANY CONSTRAINT THAT ACTUALLY PREVENTS THIS, OR STATE THAT THERE IS NONE>.

> *Note.* Sections 12.2 and 12.3 usually have different answers, and publishing only the first is the comfortable half of the truth. A legal outcome depends on a court's cooperation. A spending policy does not.

## 13. Conformance claim

<ORGANIZATION NAME> states that it is <CONFORMANT WITH / BASED ON> BES 0001 at release <RELEASE>.

Unmet MUST clauses: <NONE, or a list with clause identifiers and reasons>.
Declined SHOULD clauses: <NONE, or a list with clause identifiers and reasons>.

Custody operations follow <OPERATIONAL CUSTODY STANDARD AND RELEASE, or "no operational custody standard, and remain unassessed">.

> *Note.* If any MUST is unmet, the claim is "based on", not "conformant". That claim is respectable and common. A conformance claim resting on an undeclared or waived requirement is neither.
