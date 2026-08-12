# Constitution of <ORGANIZATION NAME>

Adopted <YYYY MM DD>. Version <X.Y>.

> **How to use this template.** Replace every value in angle brackets. Read the note under each section before choosing a number, because most of these choices trade safety against speed and there is no setting that avoids the trade. Delete the notes before adopting. When you are done you own this document. It is not adopted by reference, and nothing about it links back to the repository it came from.
>
> Have your own counsel review the completed document before you rely on it. See `../DISCLAIMER.md`.

## 0. Adoption

<ORGANIZATION NAME> adopts BES 0001 at release <RELEASE>. Where this constitution is silent, BES 0001 governs. Where this constitution sets a value BES 0001 leaves open, this constitution controls. Where this constitution deviates from BES 0001, the deviation is listed in section 12 with its clause identifier.

> *Note.* Name an exact release, never "the latest version". Releases are immutable, so a reader can check the text you actually adopted. You are never required to upgrade.

## 1. Mission (Tier One)

<ORGANIZATION NAME> exists to <MISSION IN ONE SENTENCE>.

<ORGANIZATION NAME> does not <EXCLUDED ACTIVITIES>. No administrator, guardian, or auditor may receive any payment, grant, gift, or benefit beyond the disclosed compensation fixed under section 6.

> *Note.* This is the hardest thing here to change and the thing everything else serves. Write it so that a stranger in twenty years can tell whether a given payment fits it. A mission broad enough to permit anything permits drift.

## 2. Beneficiaries (Tier Two)

2.1 Eligible beneficiaries are <ELIGIBILITY CRITERIA>.

2.2 A single beneficiary may not receive more than <PERCENT> of a year's distribution pool.

2.3 Administration screens applications against these criteria and publishes accepted and rejected applications with reasons, under BES 0001 §5.4. Administration has no discretion to add criteria. Any change to eligibility is a Tier Two amendment.

> *Note.* The concentration cap in 2.2 protects against a single relationship quietly becoming the endowment's purpose. A low cap forces breadth and raises administrative cost. A high cap does the reverse.

## 3. Spending (Tier Two for the formula, Tier Three for its output)

3.1 Each year <ORGANIZATION NAME> distributes <RATE> of the trailing <WINDOW> average treasury value, measured in <UNIT OF ACCOUNT>, converted at the time of distribution.

3.2 This is spending from <PRINCIPAL / NEW DONATIONS / DISCLOSED INCOME>, per BES 0001 §6.1. Bitcoin generates no yield on its own. The rate in 3.1 assumes <ASSUMPTION>. It is a discipline rule, not a guarantee, and this assumption is restated in every annual report.

3.3 The averaging calculation and the resulting pool are Tier Three, computed automatically and logged. The rate itself and the averaging window are Tier Two.

> *Note.* The unit of account matters more than the rate. Measuring in fiat makes the payout stable in fiat and variable in bitcoin. Measuring in bitcoin does the opposite. A longer averaging window smooths volatility and slows the response to a real change in circumstances.

## 4. Guardians

4.1 <ORGANIZATION NAME> is secured by <COUNT> guardians, <THRESHOLD> signatures required to move funds. BES 0001 §3.1 sets the floor at five guardians and three signatures.

4.2 Each guardian holds exactly one signing key, per BES 0001 §3.4. <IF GUARDIANS ARE ORGANIZATIONS: each guardian organization runs its own internal signing process before contributing its single signature. The treasury script recognizes one signature per organization, never an individual.>

4.3 Independence under BES 0001 §4.1 is attested annually and published: no shared parent or controlling entity, no shared country of legal residence, no shared key storage system, no shared backup custodian, no shared counsel, no shared cloud or hosting account. Guardians are resident in at least <COUNTRY COUNT> countries. Attestations are DOCUMENTARY evidence, not proof.

4.4 Guardian succession. If a guardian is unreachable across at least two independent channels for <DAYS> consecutive days, the remaining guardians may vote, at <SUCCESSION THRESHOLD>, to designate a replacement meeting 4.3. This replaces a seat. It does not move funds and carries no automatic transfer of treasury control. The vote, the contact attempts, and the replacement's independence attestation are published.

4.5 Disclosed risk, per BES 0001 §4.4: loss of any <COUNT MINUS THRESHOLD> guardians does not stop fund movement, and collusion among any <THRESHOLD> guardians could move funds against the mission.

> *Note.* Raising the threshold reduces collusion risk and increases the chance of deadlock when people are unavailable. The succession period in 4.4 must be long enough to exclude illness, travel, and ordinary silence, and short enough that a lost seat does not become permanent. Whatever you choose, BES 0001 §10.3 requires you to rehearse the replacement and publish how long it actually took.

## 5. Rule engine (optional)

5.1 Parameter updates within bounds already fixed by this constitution apply automatically and are logged. Logic changes require guardian approval at <THRESHOLD> followed by a <DAYS> day public notice period. Emergency patches that narrow, never widen, what the engine will approve may be approved by <THRESHOLD> within <HOURS> hours, with public disclosure and full review within <DAYS> days.

5.2 Guardians may revert to the last reviewed version at any time at <THRESHOLD>, with no delay on a rollback.

5.3 Guardians sign only against a hash pinned engine version and attest to the version they are running.

> *Note.* A rule engine is a SOFTWARE control, not a BITCOIN one, per BES 0001 §3.5. Guardians can always sign a different valid transaction. Describe it as a check that makes mistakes visible, never as a restriction Bitcoin enforces. Delete this section entirely if you do not run one.

## 6. Administration

6.1 Administration is <PAID / VOLUNTEER>, compensation fixed annually by guardians at <THRESHOLD> and published. Administration prepares applications, drafts unsigned payment proposals, publishes reports, and communicates with beneficiaries.

6.2 Administration may not sign or move funds, change a rule at any tier, select or exclude a beneficiary outside section 2, suppress a failed check, or make a payment final without guardian signatures.

6.3 Every administrator action is published as automatic, unverified claim, or judgment call, per BES 0001 §5.4.

6.4 <OPTIONAL: reconciliation of the published record is performed by <PARTY>, who is neither an administrator nor a guardian.>

## 7. Payment procedure

<ORGANIZATION NAME> follows BES 0001 §8 exactly. Administration publishes a request with evidence and verification labels, any party may rerun the automatic checks, administration prepares the unsigned transaction, each guardian independently reviews before signing, <THRESHOLD> signatures are required to broadcast, and the signed payment with its full record is published. Missing or unclear evidence stops the payment. There is no default path to completion.

## 8. Legal wrapper

8.1 <ORGANIZATION NAME> uses <STRUCTURE> in <JURISDICTION>.

8.2 The wrapper carries no authority to override sections 1 through 7. If the wrapper's jurisdiction requires something this constitution forbids, the conflict is disclosed publicly and referred to counsel. It is not resolved silently.

8.3 If the wrapper entity is dissolved, <OUTCOME>, controlled by <DOCUMENT AND CLAUSE>.

> *Note.* This section is a LEGAL claim under BES 0001 §11.3. It depends on a court's cooperation and must never be presented as a guarantee. This is the section most in need of counsel in your own jurisdiction.

## 9. Evidence package

<ORGANIZATION NAME> publishes and maintains everything required by BES 0001 §9, at <LOCATION>, with a verification label on every claim. Personal information that could put a beneficiary or guardian at risk is excluded, using pseudonymous or hashed identifiers where a public claim must remain checkable.

## 10. Amendment

10.1 Tier One changes, being the mission, the private benefit prohibition, the guardian minimum, and this amendment procedure itself, require <TIER ONE THRESHOLD> and <TIER ONE DAYS> days of public notice.

10.2 Tier Two changes, being beneficiary criteria, the spending rate and window, and guardian count or threshold, require <TIER TWO THRESHOLD> and <TIER TWO DAYS> days of public notice.

10.3 Tier Three items apply automatically and are logged.

10.4 No provision of this constitution is permanent, per BES 0001 §7.4. Every section states its tier.

## 11. Dissolution

If guardians determine, at the Tier One threshold, that the mission has become impossible or unlawful to pursue, remaining funds transfer to <SUCCESSOR CRITERIA>, selected by the same Tier One vote and published with reasons. No guardian, administrator, or auditor may be a successor or receive dissolution proceeds.

## 12. Conformance and disclosed deviations

<ORGANIZATION NAME> states conformance with BES 0001 at release <RELEASE>.

Disclosed deviations: <NONE, or a list of clause identifiers with the reason for each>.

> *Note.* An undisclosed deviation makes the conformance statement false. Disclosure costs nothing.
