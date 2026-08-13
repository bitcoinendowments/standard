# Profile: standard five guardian

A starting configuration, not a requirement. Every value is a choice, and each is stated with what it costs.

## Configuration

| Parameter | Value | BES 0001 clause |
|-----------|-------|-----------------|
| Guardians (n) | 5 | §2.9 |
| Weakest authorization condition (m) | 3 of 5, on every path | §2.3, §2.5 |
| Taproot key path | disabled, with published unspendable internal key | §2.7 |
| Alternate or recovery paths | none weaker than 3 of 5 | §2.4 |
| Control, compromise, and coercion domains | at most 2 guardians each | §3.5 |
| Unavailability domains | at most 2 guardians each | §3.6 |
| Spending rule | 4 percent of trailing 3 year average | §5.3 |
| Spending source | principal | §5.1 |
| Tier One amendment | 5 of 5, 180 days notice | §6.3 |
| Tier Two amendment | 4 of 5, 60 days notice | §6.3, §6.4 |
| Tier Three | automatic, logged | §6.5 |
| Guardian succession trigger | 180 days unreachable across 2 channels | §9.6 |
| Rehearsal cadence | before funding, then annually and on any change | §9.1, §9.3 |

## Why these values

**Five guardians at three of five, on every path.** This is the §2.5 floor. It survives the loss of two and fails to collusion by three. The words "on every path" carry more weight than the ratio: a three of five script path protects nothing if a key path or a recovery branch spends with fewer. Below five guardians, one loss puts the treasury a single absence from deadlock. Above five, coordination cost rises faster than the security benefit, and finding genuinely uncorrelated guardians gets harder, which is the constraint that actually binds.

**Domain sizes rather than a country count.** At three of five, a control, compromise, or coercion domain must contain at most two guardians, since three reaches the threshold. An unavailability domain must also contain at most two, since three would leave fewer than three available. Both numbers fall out of §3.5 and §3.6 at this configuration, and both change if you change m or n, which is why the standard states them as arithmetic rather than as a number.

Domains aggregate through a common parent under §3.4. Two guardians sharing a hardware vendor and two others sharing the same vendor's firmware supplier are one domain of four, not two of two. This is the step most deployments will get wrong, and `../tests/check_invariants.py` checks the arithmetic once the table is honest.

Countries are one input to §3.7, never the analysis itself. Five guardians in three countries can be safe or badly exposed depending on where the three sit and who can reach them.

**Four percent of a trailing three year average** is borrowed from conventional endowment practice, and the borrowing is deliberate: a board and an auditor already understand it. In a bitcoin treasury it behaves differently, because the unit of account is volatile and there is no yield. A three year window smooths volatility enough that one bad year does not force a cut, and slowly enough that a real change in circumstances takes years to show up in the payout.

**Unanimous Tier One with 180 days notice** makes the mission unchangeable without every guardian agreeing and the public watching for half a year. The cost is real: one unreachable guardian means Tier One cannot change at all, including when changing it is obviously right.

**Four of five Tier Two with 60 days** satisfies §6.4, which requires Tier One to be no easier than Tier Two in either dimension, with at least one strictly harder. Here both are strictly harder. A deployment that prefers five of five for both tiers with 180 days for Tier One and 60 for Tier Two is equally conformant, since only one dimension needs to be strictly greater.

**180 days for succession** is long enough to exclude illness, travel, and ordinary silence, and uncomfortably long in a real emergency. That is the trade. §9.6 requires publishing how long replacement actually took when rehearsed, which is the number that matters.

## When not to use this profile

**An organization that cannot find five uncorrelated guardians** should not pretend otherwise. Five signers sharing an office, an IT department, and a lawyer are one point of trust wearing five hats. Such an organization is nonconformant with §2.9, and the honest path is the "based on BES 0001, with declared deviations" claim under §11.2, not a conformance claim with an asterisk. That claim is respectable. A conformance claim that quietly depends on a waiver is not.

**A treasury that must spend predictably in fiat terms** should not adopt a bitcoin denominated trailing average without stating what happens in a year when the payout halves.

**An organization expecting a contested amendment** should think hard before unanimous Tier One, and consider four of five with a longer notice period instead, recording why.
