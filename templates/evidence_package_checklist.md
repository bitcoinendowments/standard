# Evidence package checklist

Everything BES 0001 §8 requires, in the order it is easiest to assemble. Each item names its clause and the two label fields it carries. Every item also needs a publication class under §8.4: public, redacted, committed, delayed, or restricted.

## Spending policy, first and most important

* [ ] Complete policy for every coin controlled: network, descriptor or equivalent, key origins sufficient for watch only verification, every key path, script path, and recovery branch, and every timelock. §2.1, GOVERNANCE and DOCUMENTARY
* [ ] Enough policy detail to reconstruct the exact on chain output, including a Taproot output key and script tree commitment. §2.2, SOFTWARE and REPRODUCIBLE
* [ ] The weakest authorization condition across all paths, stated as the smallest set of parties that can spend by any route. §2.3, GOVERNANCE and DOCUMENTARY
* [ ] A statement that no undisclosed path spends under a weaker condition. §2.4, GOVERNANCE with CHAIN and DOCUMENTARY
* [ ] The method by which anyone can derive your receive addresses from the published policy. §2.12, SOFTWARE and REPRODUCIBLE
* [ ] Confirmation that each receive address was verified against that derivation before publication. §2.13, GOVERNANCE and REPRODUCIBLE
* [ ] For each path, whether its threshold is enforced by script or produced by aggregate signing. §2.6
* [ ] If the Taproot key path is disabled, the derivation proving the internal key is unspendable. §2.7
* [ ] If it is enabled, the aggregate protocol, its participant set, and its threshold, published as a software or governance control and never as consensus enforced. §2.8
* [ ] Any party other than a guardian able to influence, delay, or block a spend. §2.15, GOVERNANCE and DOCUMENTARY

If you publish nothing else, publish this. Every other control in the standard is decoration if a single party can spend by a path nobody was shown.

## Guardians

* [ ] All nine factors per guardian: beneficial owner, employer or funding source, jurisdiction, physical location, signing stack, backup facility, coordinator dependency, communication dependency, recovery dependency. §3.2, GOVERNANCE and DOCUMENTARY
* [ ] The domain table, per path: each domain named, its shared dependency, and the guardians in it, aggregated through common parents. §3.3 and §3.4
* [ ] Confirmation that every control, compromise, or coercion domain holds fewer than m guardians. §3.5
* [ ] Confirmation that every unavailability domain holds fewer than n minus m plus one. §3.6
* [ ] The coercion analysis, with residual uncertainty stated rather than a claim of proof. §3.7, LEGAL and DOCUMENTARY
* [ ] Your own risk arithmetic, per path, in your own m and n: how many can go missing, how many acting together can spend against the mission. §3.10, GOVERNANCE and DOCUMENTARY

## Roles

* [ ] Confirmation that no administrator holds an authorization share. §4.2, GOVERNANCE with CHAIN and DOCUMENTARY
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

## Continuity

The contents of a recovery plan are operational and out of scope here. What this standard requires is that one exists, has been executed, is rehearsed, and is reported.

* [ ] A documented recovery plan your guardians have executed end to end at least once. §9.1
* [ ] The operational standard that plan follows, or a statement that it follows none. §9.2
* [ ] Date of the most recent rehearsal, at least annual and after any change. §9.3
* [ ] Results of every rehearsal, including failures. §9.4
* [ ] Each scenario marked observed or simulated. §9.5
* [ ] How long guardian replacement took when rehearsed. §9.6

## Legal

* [ ] The wrapper and jurisdiction, or a statement that there is none. §10.2, LEGAL and DOCUMENTARY
* [ ] What the legal instrument requires on dissolution. §10.4
* [ ] Whether the guardians are technically able to disregard that outcome, and what if anything prevents it. §10.5, GOVERNANCE with CHAIN and DOCUMENTARY

These last two are usually different answers. Publishing only the first is the comfortable half of the truth.

## Payment authorization

* [ ] Each request published or committed before any guardian signs. §7.1
* [ ] The procedure your guardians follow to verify a transaction, and the operational standard it follows if any. §7.5

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
