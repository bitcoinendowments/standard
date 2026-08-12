# Profile: standard five guardian

A starting configuration, not a requirement. Every value below is a choice, and each one is stated with what it costs.

## Configuration

| Parameter | Value | BES 0001 clause |
|-----------|-------|-----------------|
| Guardians | 5 | §3.1 |
| Signing threshold | 3 of 5 | §3.1 |
| Guardian countries | at least 3 | §4.2 |
| Spending rate | 4 percent of trailing 3 year average | §6.2 |
| Spending source | principal | §6.1 |
| Tier One amendment | 5 of 5, 180 days notice | §7.2 |
| Tier Two amendment | 4 of 5, 60 days notice | §7.2 |
| Tier Three | automatic, logged | §7.2 |
| Guardian succession trigger | 180 days unreachable across 2 channels | §10.3 |
| Rehearsal before funding | required | §10.1 |

## Why these values

**Five guardians at three of five** is the BES floor. It survives the loss of two guardians and fails to collusion by three. Below five, a single loss puts the treasury one absence away from deadlock. Above five, coordination cost rises faster than the security benefit for most organizations, and finding genuinely independent guardians gets harder, which is the constraint that actually binds.

**Three countries** rather than five keeps the guardian search realistic while ensuring no single jurisdiction can compel the threshold. The country count is the weakest of the six independence tests in §4.1 and should never be the one an organization leans on.

**Four percent of a trailing three year average** is borrowed from conventional endowment practice, and the borrowing is the point: it is a familiar discipline rule that a board and an auditor already understand. In a bitcoin treasury it behaves differently, because the measurement unit is volatile and there is no yield. This is spending from principal. A three year window smooths the volatility enough that a single bad year does not force a cut, and slowly enough that a genuine change in circumstances takes years to show up in the payout.

**Unanimous Tier One with 180 days notice** makes the mission effectively unchangeable without every guardian agreeing and the public watching for half a year. That is the intent. The cost is real: if one guardian is unreachable, Tier One cannot change at all, including in a case where changing it is obviously right.

**Four of five Tier Two with 60 days** allows beneficiary criteria and spending parameters to evolve at the speed an operating organization needs, while still requiring a supermajority and enough notice for an outside objection to arrive.

**180 days for succession** is long enough to exclude illness, travel, and ordinary silence. It is uncomfortably long during a real emergency, which is the trade being made, and it is why §10.3 requires rehearsing replacement and publishing how long it actually takes.

## When not to use this profile

**A small foundation** that cannot find five genuinely independent guardians should not pretend otherwise. Five signers who share an office, an IT department, and a lawyer are one point of trust wearing five hats. Fewer guardians with real independence, disclosed as a deviation from §3.1 under §12.3, is more honest than five nominal ones.

**A treasury that must spend predictably in fiat terms** should not use a bitcoin denominated trailing average without stating clearly what happens in a year when the payout falls by half.

**An organization expecting a contested amendment** should think hard before adopting unanimous Tier One. Consider four of five with a longer notice period instead, and write down why.
