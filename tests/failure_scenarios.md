# Failure scenarios a schema cannot catch

Schema validation checks that a manifest is well formed and that the numbers clear the floors in BES 0001. Everything below passes validation and still breaks conformance. A verifier has to check these by hand, and knowing that is the point of publishing the list.

| Scenario | Why the schema misses it | How a verifier checks it |
|----------|--------------------------|--------------------------|
| Threshold exceeds guardian count | The schema enforces floors on each field, not the relationship between them | Read both numbers together. A threshold above the count is unspendable |
| `threshold_committed_in_script` asserted but false | It is a DOCUMENTARY claim in the manifest | Derive the address from the published script and compare it against the chain. Only then is it a BITCOIN claim |
| Five guardians, one controlling entity | Independence is attested, not proven | Check ownership, employment, and counsel independently. This is where a false conformance claim is most likely to survive |
| Guardians in three countries who share an IT department | §4.2 is satisfied while §4.1 and §4.3 are not | Check all six independence tests. Country count is the weakest of them |
| One person holding two keys | The manifest asserts one key each | Match guardian identities against signatures on published transactions over time |
| Rehearsals listed but never run | The array only records claims | Read the published rehearsal results required by §10.2, including what failed. No failures ever recorded is itself a signal |
| A deviation that exists but is not listed | A missing entry is structurally valid | Compare the evidence package against the checklist. An undisclosed deviation makes the statement false under §12.3 |
| A claim carrying a stronger label than what backs it | Labels are free text at the claim level | Reclassify each claim yourself. A rule engine restriction labeled BITCOIN is the common case, and §3.5 exists because of it |
| Administrator and guardian are the same person under two names | Both booleans read false | Compare identities across roles in the evidence package |
| Conformant manifest, mission already abandoned | Nothing about mission drift is machine checkable | Read the payment record against section 1 of the constitution. This is a GOVERNANCE claim and it can only be checked over time |
| Legal wrapper named but unenforceable in practice | The field records a name | Read the instrument. Ask counsel in that jurisdiction. §11.3 means this is never a guarantee |

The pattern: the schema tells you what a deployment asserts, and the chain tells you what actually happened. Between those two sit the DOCUMENTARY, LEGAL, and GOVERNANCE claims, which is most of the interesting surface and all of the trust.
