# Profile: standard five guardian

A starting configuration, not a requirement. Every value is a choice, and each is stated with what it costs.

## Configuration

| Parameter | Value | BES 0001 clause |
|-----------|-------|-----------------|
| Guardians (n) | 5 | §2.4 |
| Weakest authorization condition (m) | 3 of 5, on every path | §2.2, §2.4 |
| Alternate or recovery paths | none weaker than 3 of 5 | §2.3 |
| Correlated control ceiling | no domain reaching 3 guardians | §3.3 |
| Availability ceiling | no domain disabling 3 guardians | §3.4 |
| Spending rule | 4 percent of trailing 3 year average | §5.3 |
| Spending source | principal | §5.1 |
| Tier One amendment | 5 of 5, 180 days notice | §6.3 |
| Tier Two amendment | 4 of 5, 60 days notice | §6.3, §6.4 |
| Tier Three | automatic, logged | §6.5 |
| Guardian succession trigger | 180 days unreachable across 2 channels | §9.5 |
| Rehearsal cadence | before funding, then annually and on any change | §9.3, §9.7 |

## Why these values

**Five guardians at three of five, on every path.** This is the §2.4 floor. It survives the loss of two and fails to collusion by three. The words "on every path" carry more weight than the ratio: a three of five script path protects nothing if a key path or a recovery branch spends with fewer. Below five guardians, one loss puts the treasury a single absence from deadlock. Above five, coordination cost rises faster than the security benefit, and finding genuinely uncorrelated guardians gets harder, which is the constraint that actually binds.

**Correlated control ceiling rather than a country count.** The requirement is that no single owner, employer, funding source, jurisdiction, signing stack, backup facility, coordinator, or coercion domain reaches three guardians. Countries are one input. Five guardians in three countries can satisfy §3.5 or violate it, depending on where the three sit and who can reach them. Work the analysis, do not count flags.

**Four percent of a trailing three year average** is borrowed from conventional endowment practice, and the borrowing is deliberate: a board and an auditor already understand it. In a bitcoin treasury it behaves differently, because the unit of account is volatile and there is no yield. A three year window smooths volatility enough that one bad year does not force a cut, and slowly enough that a real change in circumstances takes years to show up in the payout.

**Unanimous Tier One with 180 days notice** makes the mission unchangeable without every guardian agreeing and the public watching for half a year. The cost is real: one unreachable guardian means Tier One cannot change at all, including when changing it is obviously right.

**Four of five Tier Two with 60 days** satisfies §6.4 by differing from Tier One in both dimensions. A deployment that prefers the same threshold as Tier One with a shorter notice period is equally conformant, since §6.4 requires a difference in at least one dimension, not both.

**180 days for succession** is long enough to exclude illness, travel, and ordinary silence, and uncomfortably long in a real emergency. That is the trade. §9.5 requires rehearsing replacement and publishing how long it actually took, which is the number that matters.

## When not to use this profile

**An organization that cannot find five uncorrelated guardians** should not pretend otherwise. Five signers sharing an office, an IT department, and a lawyer are one point of trust wearing five hats. Such an organization is nonconformant with §2.4, and the honest path is the "based on BES 0001, with declared deviations" claim under §11.2, not a conformance claim with an asterisk. That claim is respectable. A conformance claim that quietly depends on a waiver is not.

**A treasury that must spend predictably in fiat terms** should not adopt a bitcoin denominated trailing average without stating what happens in a year when the payout halves.

**An organization expecting a contested amendment** should think hard before unanimous Tier One, and consider four of five with a longer notice period instead, recording why.
