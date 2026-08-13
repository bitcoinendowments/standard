# Evidence package checklist

Everything BES 0001 §8 requires, in the order it is easiest to assemble. Each item names its clause and the two label fields it carries. Every item also needs a publication class under §8.4: public, redacted, committed, delayed, or restricted.

## Spending policy, first and most important

* [ ] Complete policy for every coin controlled: network, descriptor or equivalent, key origins sufficient for watch only verification, every key path, script path, and recovery branch, and every timelock. §2.1, GOVERNANCE and DOCUMENTARY
* [ ] The weakest authorization condition across all paths, stated as the smallest set of parties that can spend by any route. §2.2, GOVERNANCE and DOCUMENTARY
* [ ] A statement that no undisclosed path spends under a weaker condition. §2.3, CONSENSUS with CHAIN and DOCUMENTARY
* [ ] The method by which anyone can derive your receive addresses from the published policy. §2.7, SOFTWARE and REPRODUCIBLE
* [ ] Any party other than a guardian able to influence, delay, or block a spend. §2.9, GOVERNANCE and DOCUMENTARY

If you publish nothing else, publish this. Every other control in the standard is decoration if a single party can spend by a path nobody was shown.

## Guardians

* [ ] All eight factors per guardian: beneficial owner, employer or funding source, jurisdiction, signing stack, backup facility, coordinator dependency, communication dependency, recovery dependency. §3.2, GOVERNANCE and DOCUMENTARY
* [ ] The correlated control analysis: no domain reaches m, no domain disables the threshold, no single coercive jurisdiction reaches m. §3.3 to §3.6, GOVERNANCE and DOCUMENTARY
* [ ] Your own risk arithmetic, per path, in your own m and n: how many can go missing, how many acting together can spend against the mission. §3.7, GOVERNANCE and DOCUMENTARY

## Roles

* [ ] Confirmation that no administrator holds an authorization share. §4.2, CONSENSUS with CHAIN and DOCUMENTARY
* [ ] Every administrator action classified as automatic, unverified claim, or judgment call. §4.7, GOVERNANCE and DOCUMENTARY
* [ ] Who reconciles the record, if anyone. §4.8, GOVERNANCE and DOCUMENTARY

## Money

* [ ] Spending source: principal, new donations, or disclosed income. §5.1
* [ ] Spending formula, measurement window, and unit of account. §5.3
* [ ] Confirmation that no coins are lent, pledged, rehypothecated, or wrapped. §5.4
* [ ] Any other assets held, with purpose, size, and counterparty. §5.5

## Governance

* [ ] The constitution, complete and readable without this standard. §1.5
* [ ] Each tier's threshold and notice period as explicit values. §6.3

## Recovery

* [ ] The recovery plan, executable on mainnet. §9.1, §9.2
* [ ] Results of every rehearsal, including failures. §9.3
* [ ] Which scenarios were simulated rather than observed. §9.4
* [ ] How long guardian replacement actually took. §9.5
* [ ] Date of the most recent rehearsal. §9.7

## Legal

* [ ] The wrapper and jurisdiction, or a statement that there is none. §10.2, LEGAL and DOCUMENTARY
* [ ] What the legal instrument requires on dissolution. §10.4
* [ ] Whether the guardians are technically able to disregard that outcome. §10.5, CONSENSUS with CHAIN and DOCUMENTARY

These last two are usually different answers. Publishing only the first is the comfortable half of the truth.

## Claims

* [ ] Which operational custody standard you follow, or a plain statement that custody operations are unassessed. §12.2
* [ ] Your claim: conformant, or based on with declared deviations. §11.1, §11.2
* [ ] The deviation register: every unmet MUST and every declined SHOULD, with clause and reason. §11.4

## Before publishing

* [ ] Every item has a publication class. §8.4
* [ ] Nothing published would expose a beneficiary or guardian to harm. §8.5
* [ ] A statement of what outsiders consequently cannot verify. §8.6
* [ ] Your data retention policy. §8.7
* [ ] No claim carries a stronger CONTROL or EVIDENCE value than what actually backs it. §8.3
* [ ] If any MUST is unmet, the claim says based on, not conformant. §11.2
