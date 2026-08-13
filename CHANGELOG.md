# Changelog

All notable changes to this standard are recorded here. Format follows the release rules in `VERSIONING.md`. Releases are immutable once tagged.

## Unreleased, editor's draft

No release has been tagged. Clause identifiers are not frozen and may change without notice until the first release. Nothing here should be cited in a binding instrument yet.

Current state of the draft:

* `spec/BES_0001_core_standard.md`, scoped to governance and conformance, with a minimum custody interface in §2 and §12.
* Two label fields per clause, CONTROL and EVIDENCE, replacing the earlier single label, which allowed organizational facts to be presented as enforced by Bitcoin.
* Strict conformance. An unmet MUST means nonconformant. Two defined claims, conformant and based on with declared deviations.
* Custody expressed as a complete spending policy across every path, rather than a threshold on one script.
* Independence expressed as correlated failure domains measured against the weakest authorization condition, rather than a checklist of six shared factors.
* All risk arithmetic parameterized to a deployment's own m and n, per spending path.
* Evidence publication classes, so auditability does not require exposing beneficiaries or guardians.
* Correlated failure domains expressed as a published table per path, aggregated through shared parent dependencies, with the two size tests stated as arithmetic against m and n rather than as fixed numbers.
* A coercion analysis with stated residual uncertainty, replacing a claim that no jurisdiction can reach the threshold, which cannot be proved.
* A second check layer, `tests/check_invariants.py`, for the cross field arithmetic no JSON Schema can express.
* Continuity requirements that a recovery plan exist, be executed, be rehearsed on a cadence, and be reported, with each scenario marked observed or simulated. What the plan contains is operational and deliberately out of scope.

Known limitations:

* The threat model records analysis, not adversarial test results.
* BES 0002, covering operational custody, does not exist. §12.2 requires a deployment to say so plainly rather than let the gap disappear.
* No legal review has been completed in any jurisdiction.

### Provenance

The first draft of this standard was reviewed before any release, and that review changed it structurally. The single label model, the conformance semantics, the custody scope, and the independence rule were all replaced as a result. A second review of the rewrite found that the custody scope split had been asserted in the scope statement while the clauses still standardized operational custody, and that the tier ordering rule forbade the configuration its own recommended profile used. Both are corrected here. The reviews are the reason no release was tagged from either draft.
