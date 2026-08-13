# Failure scenarios a schema cannot catch

Structural validation checks that a manifest is well formed and that stated numbers clear the floors in BES 0001. Everything below passes validation and still breaks conformance. A verifier checks these by hand, and §11.6 exists so that nobody mistakes a green check for an assessment.

| Scenario | Why validation misses it | How a verifier checks it |
|----------|--------------------------|--------------------------|
| An undisclosed spending path spends with one key | The manifest asserts a policy; validation reads the assertion | Derive addresses from the published descriptor under §2.1 and inspect every branch. This is the failure that makes all the others irrelevant |
| A Taproot key path bypasses the script path | Nothing structural distinguishes them | Read the full policy. §2.2 requires the weakest condition to be stated, so compare the stated value against the actual branches |
| Threshold exceeds guardian count | Validation enforces floors per field, not relationships between them | Read both numbers together. A threshold above the count is unspendable |
| Five guardians, one controlling entity | Correlated control is attested, not proven | Check ownership, employer, funding, and counsel independently. §3.3 is where a false claim is most likely to survive |
| Guardians in three countries, one legal reach | Country count is structural, coercive reach is not | Ask which single order or actor could compel enough guardians. §3.5 requires this analysis, not the country count |
| One party holding two authorization shares | The manifest asserts one share each | Match guardian identities against signatures over time. §3.1 makes the shares count once |
| Rehearsals listed but never run | The array records claims | Read the recorded results required by §9.3, including failures. No failure ever recorded is itself a signal |
| A simulated scenario presented as observed | Both look identical in a list | §9.4 requires simulated scenarios to be marked. A fee spike rehearsed on a test network is always simulated |
| A revoked key that still controls coins | Revocation is a statement | §9.6 requires a rotation transaction. Check the chain for coins moved to the new policy |
| A deviation that exists but is not registered | A missing entry is structurally valid | Compare the evidence package against the standard. An undeclared deviation makes the claim false under §11.4 |
| A claim carrying a stronger label than what backs it | Labels are free text at the claim level | Reclassify each claim yourself. Look for anything asserting consensus control over an organizational fact |
| Committed evidence never opened | A commitment is structurally complete | §7.2 requires the opening, or a stated reason it will never come. An indefinite commitment is an unverifiable claim |
| Conformant manifest, mission already abandoned | Mission drift is not machine checkable | Read the payment record against the constitution. This is only checkable over time |
| Legal wrapper named but unenforceable | The field records a name | Read the instrument and ask counsel in that jurisdiction. §10.3 means this is never a guarantee |
| Custody operated badly by a conformant deployment | Out of scope by design | §12.1. BES 0001 does not assess custody operations. Ask which operational standard the deployment names under §12.2 |

The pattern: validation tells you what a deployment asserts, the chain tells you what happened, and between them sit the documentary, legal, and governance claims, which is most of the surface and all of the trust.
