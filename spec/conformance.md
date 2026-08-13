# Conformance

## The two claims this standard defines

**Conformant.** Every MUST is met. The deployment names an exact release.

**Based on, with declared deviations.** One or more MUSTs are not met, and each is declared. This is an honest claim and a common one. It is not conformance.

There is no third state. Disclosure does not cure an unmet MUST, because a standard whose absolute requirements can be waived by mentioning them has no absolute requirements. A deployment that cannot find five independent guardians, or that operates in one jurisdiction, is better served by the second claim than by a conformance claim carrying an asterisk.

Neither claim is issued, reviewed, approved, or endorsed by the maintainers of this standard. There is no registry, no certification, and no authority here deciding who counts as a real Bitcoin endowment.

## The required form

```
This deployment is conformant with BES 0001 at release <release>.
Deviation register: none.
Evidence package: <location>
```

or

```
This deployment is based on BES 0001 at release <release>, with declared deviations.
Unmet MUST clauses: §3.5 (all guardians resident in one jurisdiction).
Declined SHOULD clauses: §4.8 (no independent reconciler).
Evidence package: <location>
```

An undeclared deviation makes either statement false. Declaring one costs nothing.

## What this standard does not evaluate

Operational custody. Key generation, device handling, backup integrity, transaction review discipline, fee and coin policy, chain monitoring, software supply chain, and incident response are outside this document, and a conformance claim says nothing about them. Under §12.2 a deployment states which operational custody standard it follows, or states plainly that its custody operations are unassessed.

## How an outside party checks a claim

1. Read the named release. Releases are immutable, so the text checked is the text claimed.
2. Validate the manifest structure against the schema for that release. This checks assertions, not conformance, under §11.6.
3. Derive the addresses from the published spending policy under §2.1 and compare them against the chain. This is where a distributed authority claim becomes checkable, or fails to.
4. Read the weakest authorization condition under §2.2 and satisfy yourself that no path in the published policy is weaker. A three of five script path means nothing if a key path or a recovery branch spends with one signature.
5. Check the m of n arithmetic under §3.7 against the actual policy, per path.
6. Read the correlated control analysis under §3.6. This is documentary, which means deciding whether to trust the submitter. It is also where a false claim is most likely to survive.
7. Read the publication classes under §8.4 and the statement under §8.6 of what you consequently cannot verify. Treat anything in that statement as unchecked, not as satisfied.
8. Compare the deviation register against what the evidence actually shows.

Steps 3 and 4 are the only ones a stranger can settle alone. Everything else requires a judgment about a record or about people, which is the honest shape of the problem.

## What conformance does not establish

Not solvency. Not honesty. Not investment prudence. Not custody competence. Not legal validity in any jurisdiction. Not future compliance. Not that the mission is worthwhile or that the beneficiaries are real.

A deployment can be fully conformant and still be a bad endowment. This standard makes a narrow set of properties checkable. It does not make an organization good.
