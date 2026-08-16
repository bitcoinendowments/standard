# Constitution of Lighthouse Endowment

Adopted 2026 08 13. Version 0.2.

> **Fictional.** Lighthouse does not exist, holds no funds, and has no guardians. It exists to show what the template in `../../templates/` looks like with every placeholder decided, and to test whether BES 0001 is specific enough to build a real constitution on. No part of it has been reviewed by counsel. Its legal structure, including the Cayman Islands trust in 10A, is an illustration chosen to make the example concrete, not a recommendation of any structure or jurisdiction. Read it. Do not adopt it.

## 0. Relationship to BES 0001

This constitution was drafted against BES 0001 at its current editor's draft. That reference is informational. This document is complete in itself, and nothing in BES 0001 governs Lighthouse except as written out below.

## 1. Mission (Tier One)

Lighthouse Endowment exists to preserve a permanent reserve of bitcoin and to spend from it to fund organizations that give people living under capital controls, hyperinflation, or financial surveillance practical access to permissionless money, through open source tools, education, and documentation.

Lighthouse does not fund political campaigns and holds no assets other than bitcoin and the operating cash disclosed in 6.4. No administrator, guardian, or auditor may receive any payment, grant, gift, or benefit beyond the disclosed compensation fixed under section 7.

## 2. Spending policy and control

2.1 Lighthouse publishes the complete spending policy for every coin it controls, including the network, the descriptor, key origin information sufficient for watch only verification, every key path, script path, and recovery branch, and every timelock. The policy is published at the evidence package address in 9.1, and is sufficient for any party to reconstruct the exact on chain output, including the Taproot output key and script tree commitment.

2.2 The weakest authorization condition across every path is 3 of 5. The recovery branch, which becomes available after an 18 month timelock, is also 3 of 5. No path authorizes a spend under a weaker condition.

2.3 Receive addresses are derived from the published policy and verified against that derivation before publication.

2.4 Coins are not held by any third party custodian or on any exchange.

2.5 No party without an authorization share can influence, delay, or block a spend. Lighthouse runs its own coordinator and publishes its version.

## 3. Guardians

3.1 Lighthouse has 5 guardian organizations. Each holds exactly one authorization share. Each runs its own internal two of three process before contributing its single signature, and that internal process creates no additional share.

3.2 For each guardian, Lighthouse publishes the controlling entity, the funding source, the jurisdiction of legal residence, the physical location where it differs, the signing device and software stack, the backup facility, the coordinator and communication dependencies, and the recovery dependencies.

3.3 Lighthouse publishes, for every spending path, a table naming each correlated failure domain, the dependency it rests on, and the guardians it contains, aggregated through any shared parent dependency. Every control, compromise, or coercion domain contains at most 2 guardians. Every unavailability domain contains at most 2 guardians.

3.4 Lighthouse publishes a coercion analysis covering legal residence, physical location, controlling entities, beneficial control, and cross border dependencies. The five guardians are resident in five jurisdictions on four continents, and no two share a parent, a funder, a signing stack, a backup facility, or counsel. Lighthouse does not claim this proves no jurisdiction can reach 3 guardians. Two of the five sit in states with a mutual legal assistance treaty, which is the largest single coercion domain at 2 guardians, and that residual uncertainty is published rather than argued away.

3.5 This analysis is republished annually and after any change of guardian, signing stack, or recovery arrangement.

3.6 Disclosed risk, in Lighthouse's own numbers: loss of 2 guardians does not stop spending, and 3 guardians acting together can spend against the mission. Both figures apply to the primary path and to the recovery branch, which is why the recovery branch was set at the same threshold rather than a lower one.

3.7 Guardian succession. If a guardian is unreachable across at least two independent channels for 180 consecutive days, the remaining guardians may vote, at 3 of the remaining guardians, to designate a replacement satisfying 3.2 to 3.4. The threshold stays at 3 however many seats are vacant, so succession remains possible while spending still is. This replaces a seat. It does not move coins and carries no automatic transfer of control. The vote, the contact attempts, and the replacement's disclosure are published.

## 4. Rule engine

4.1 Parameter updates within bounds fixed by this constitution apply automatically and are logged. Logic changes require 3 of 5 guardian approval followed by 30 days of public notice. Emergency patches that narrow, never widen, what the engine approves may be approved by 3 of 5 within 48 hours, with public disclosure and full review within 30 days.

4.2 Guardians may revert to the last reviewed version at any time at 3 of 5, with no delay on a rollback.

4.3 Guardians sign only against a hash pinned engine version and attest to the version they run.

4.4 The rule engine constrains nothing that 3 guardians cannot override by signing a different valid transaction. It is published as a software control and never as one Bitcoin enforces.

## 5. Beneficiaries (Tier Two)

5.1 Eligible beneficiaries are nonprofit or mission aligned organizations, five years old or younger from their own founding, that operate open source financial software, run bitcoin or financial privacy education programs, or document the effects of capital controls or currency collapse for the populations described in section 1.

5.2 A single beneficiary may not receive more than 8 percent of a year's distribution pool.

5.3 Administration screens applications against these criteria and publishes accepted and rejected applications with reasons, subject to the publication classes in section 9. Administration has no discretion to add criteria.

## 6. Spending

6.1 Each year Lighthouse distributes 4 percent of the trailing 3 year average treasury value, measured in USD, converted to bitcoin at the time of distribution.

6.2 This is spending from principal. Bitcoin generates no yield on its own. The 4 percent rate assumes ongoing donations and treasury appreciation will exceed the payout over time. It is a discipline rule, not a guarantee, and this assumption is restated in every annual report.

6.3 Coins are not lent, pledged as collateral, rehypothecated, or converted into any wrapped or synthetic representation of bitcoin.

6.4 Lighthouse holds up to nine months of operating cash in a bank account in the trust's jurisdiction, for administration and audit costs. Size and counterparty are published annually.

## 7. Administration

7.1 Administration is a paid team, compensation fixed annually by guardians at 3 of 5 and published.

7.2 No administrator holds an authorization share. Administration may not change a rule at any tier, select or exclude a beneficiary outside section 5, suppress or delay a failed check, or make a payment final without guardian signatures.

7.3 Every administrator action is published as automatic and reproducible, an unverified claim, or a judgment call with a recorded justification.

7.4 Reconciliation of the published payment record is performed by an external accountant who is neither an administrator nor a guardian.

## 8. Payment procedure

8.1 Administration publishes, or publishes a commitment to, each payment request with its supporting evidence before any guardian signs.

8.2 Where a request is committed rather than published in full, the opening is published once disclosure is no longer harmful, or the reason it never will be is stated. Lighthouse expects to use commitments for grants to organizations operating under surveillance.

8.3 Where an automatic check is claimed, the checking software, its version, and its inputs are published so any party can rerun it.

8.4 Each guardian reaches its own decision on each request and does not delegate it to administration, to the coordinator, or to another guardian. The procedure guardians follow to verify a transaction before signing is published in the evidence package and follows no operational standard, because none yet exists that Lighthouse could name.

8.5 Three signatures are required. The transaction identifier and supporting record are published once the payment confirms.

8.6 Missing or unclear evidence stops the payment. There is no path to completion that skips a check.

## 9. Evidence and publication classes

9.1 Lighthouse publishes and maintains an evidence package at `https://example.invalid/lighthouse/evidence`, with a control value and an evidence value on every claim.

9.2 Each item carries one publication class. The spending policy, guardian disclosures, correlated control analysis, risk statement, and confirmed payment identifiers are public. Beneficiary applications are redacted. Grants to organizations operating under surveillance are committed and opened later, or never, under 8.2. Beneficiary identity documents are restricted to the external auditor under the retention policy in 9.5.

9.3 Nothing is published that would expose a beneficiary or guardian to physical, legal, or financial harm.

9.4 For each item that is not public, Lighthouse states what an outside party consequently cannot verify. Specifically: an outsider cannot verify that a committed grant went to an eligible beneficiary, and must rely on the external auditor's report for that class of payment.

9.5 Beneficiary identity documents are destroyed 24 months after the final payment to that beneficiary. Guardian disclosures are retained for the life of the endowment.

## 10. Continuity

10.1 Lighthouse holds a documented recovery plan that its guardians executed end to end on signet before funds were received. The plan follows no operational custody standard, because none yet exists that Lighthouse could name.

10.2 The plan is rehearsed annually and after any change of guardian roster, spending policy, signing software, or signing hardware. Results are published including failures. Each scenario is marked observed or simulated. A mainnet fee spike is always simulated, because no test network reproduces a mainnet fee market.

10.3 A compromised key is treated as compromised until the coins it controls have been moved to a policy that excludes it. Guardian replacement took 41 days in the most recent rehearsal.

## 10A. Legal wrapper

10A.1 Every judgment this constitution cannot settle by rule, including whether a beneficiary is real and whether the mission is being served, is made by the guardian federation at 3 of 5, on the record, with reasons published under section 9.

10A.2 Lighthouse uses a STAR purpose trust in the Cayman Islands. The trust holds the mission as its stated purpose and is the nominal legal holder of the treasury's interest. The five guardian organizations remain separately incorporated in their own jurisdictions and are bound to this constitution by a guardian membership agreement, which is a contract rather than ownership or control. Trustee language uses certification vocabulary throughout: the trustee certifies conformance and does not authorize spending.

10A.3 The wrapper is not a guarantee that any duty is enforceable. Enforcement depends on a court's cooperation. It carries no authority to override sections 1 through 10A. If its jurisdiction requires something this constitution forbids, the conflict is disclosed publicly and referred to counsel, never resolved silently.

10A.4 Whether a Cayman STAR trustee's role can lawfully be limited to certification rather than discretionary governance is exactly the question a real organization must put to its own counsel. Lighthouse is fictional and has asked nobody.

## 11. Amendment

11.1 Tier One, being the mission, the private benefit prohibition, the control requirements in section 2, and this section 11, requires 5 of 5 guardians and 180 days of public notice.

11.2 Tier Two, being beneficiary criteria, guardian succession, and the rate and window in 6.1, requires 4 of 5 guardians and 60 days of public notice.

11.3 Tier Three items, being the annual pool calculation and payee additions meeting the fixed criteria in section 5, apply automatically and are logged.

11.4 No tier is easier to amend than the tier above it, and Tier Two differs from Tier One in both threshold and notice period.

11.5 No provision of this constitution is permanent. Every provision states its tier in the register at 11A.

## 11A. Tier register

Every provision of this constitution states its tier here. A provision not listed is Tier One, so that an omission is never the easier path.

| Provisions | Tier |
|------------|------|
| 1, 2.1 to 2.5, 3.1 to 3.5, 7.2, 9.1 to 9.5, 10.1 to 10.3, 10A, 11, 11A, 12 | Tier One |
| 3.6, 3.7, 4, 5, 6.1, 6.2, 8 | Tier Two |
| 6.4, and any numeric parameter that updates under a formula fixed above | Tier Three |

## 12. Dissolution

12.1 If guardians determine, at the Tier One threshold, that the mission has become impossible or unlawful to pursue, remaining funds transfer to one or more successor organizations pursuing a substantially similar mission, selected by the same vote and published with reasons. No guardian, administrator, or auditor may be a successor or receive dissolution proceeds.

12.2 What the legal instrument requires on dissolution: transfer under 12.1, controlled by section 12 of this constitution read together with the guardian membership agreement and the trust instrument described in 10A.2.

12.3 What the spending policy permits on dissolution: any 3 guardians are technically able to spend contrary to 12.2. Nothing in the spending policy prevents it. The constraint is contractual and reputational, and it depends on a court's cooperation, which is the honest description of what protects the funds at that moment.

## 13. Conformance claim

Lighthouse Endowment states that it is conformant with BES 0001 at its current editor's draft.

* Unmet MUST clauses: none.
* Declined SHOULD clauses: none.

Custody operations follow no operational custody standard, and remain unassessed. BES 0001 §12.2 requires that this be said plainly rather than left to inference, and BES 0001 §12.1 forbids Lighthouse from presenting its conformance as evidence that its custody is soundly operated.

> Note for readers: a real deployment reaching this line with nothing declared should be read with more suspicion, not less. Nine disclosure factors, a domain table that survives aggregation, a coercion analysis, five publication classes, and a legal wrapper rarely all land cleanly on a first attempt, and §11.2 exists so that saying so costs nothing.
