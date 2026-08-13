# Failure scenarios a schema cannot catch

Structural validation checks that a manifest is well formed and that stated numbers clear the floors in BES 0001. Everything below passes validation and still breaks conformance. A verifier checks these by hand, and §11.6 exists so that nobody mistakes a green check for an assessment.

| Scenario | Why validation misses it | How a verifier checks it |
|----------|--------------------------|--------------------------|
| An undisclosed spending path spends with one key | Both check layers read the paths the deployment declared. Neither can see a branch that was never listed | Derive the published descriptor under §2.2, reconstruct the on chain output including any Taproot output key and tree commitment, and compare. The `invalid_recovery_path_below_floor` vector catches a declared weak path, never an undeclared one |
| A Taproot key path bypasses the script path | Nothing structural distinguishes them | §2.6 makes the deployment declare, per path, whether the threshold is script enforced or produced by aggregate signing. §2.7 requires a published unspendable internal key derivation where the key path is disabled, and §2.8 forbids presenting an aggregate signing threshold as consensus enforced. Check the derivation yourself against the output key |
| Threshold exceeds participant count | Structural validation enforces floors per field, not relationships between them | `check_invariants.py` catches this one. Run both layers |
| A stated weakest condition that no path actually offers | Both numbers are individually plausible | `check_invariants.py` requires the weakest condition to name a real path and match that path's own m and n |
| Five guardians, one controlling entity | The domain table is attested, not investigated | `check_invariants.py` checks the arithmetic of the table under §3.5 and §3.6. Whether the table names every real dependency is documentary, and is where a false claim is most likely to survive |
| Guardians in several countries, one legal reach | Country count is structural, coercive reach is not | Read the coercion analysis under §3.7 and its stated residual uncertainty. A deployment claiming to have proved no jurisdiction can reach m is overclaiming, and §3.7 forbids it |
| One party holding two authorization shares | The manifest asserts one share each | Match guardian identities against signatures over time. §3.1 makes the shares count once |
| Rehearsals listed but never run | The array records claims | Read the published results required by §9.4, including failures. No failure ever recorded is itself a signal |
| A simulated scenario presented as observed | Both look identical in a list | §9.5 requires each scenario be marked observed or simulated. A fee market spike is always simulated |
| A revoked key that still controls coins | Revocation is a statement | §9.7 forbids publishing revocation as complete until the coins move. Check the chain for coins under the new policy |
| A deviation that exists but is not registered | A missing entry is structurally valid | Compare the evidence package against the standard. An undeclared deviation makes the claim false under §11.4 |
| A claim carrying a stronger label than what backs it | Labels are free text at the claim level | Reclassify each claim yourself. Look for anything asserting consensus control over an organizational fact |
| Committed evidence never opened | A commitment is structurally complete | §7.2 requires the opening, or a stated reason it will never come. An indefinite commitment is an unverifiable claim |
| Conformant manifest, mission already abandoned | Mission drift is not machine checkable | Read the payment record against the constitution. This is only checkable over time |
| Legal wrapper named but unenforceable | The field records a name | Read the instrument and ask counsel in that jurisdiction. §10.3 means this is never a guarantee |
| Custody operated badly by a conformant deployment | Out of scope by design | §12.1. This standard requires that a recovery plan exist, be rehearsed, and be reported, and requires the verification procedure be published under §7.5. It does not assess any of them. Ask which operational standard the deployment names under §12.2 and §9.2 |

The pattern: the two check layers tell you what a deployment asserts and whether its own numbers agree with each other, the chain tells you what actually happened, and between them sit the documentary, legal, and governance claims, which is most of the surface and all of the trust.
