#!/usr/bin/env python3
"""Cross field checks a JSON Schema cannot express.

Structural validation checks each field on its own. These checks compare fields
against each other, which is where several of the errors BES 0001 exists to catch
actually live. Run both:

    check-jsonschema --schemafile schemas/deployment_manifest.schema.json <manifest>
    python3 tests/check_invariants.py <manifest>

Neither proves conformance. Both check assertions the deployment made about
itself. Path completeness in particular cannot be checked here at all: it
requires deriving the published descriptor and comparing it against the chain.
See tests/failure_scenarios.md.

Licensed under Apache License 2.0, in LICENSE_CODE.
"""
import json
import sys


def check(manifest):
    """Return a list of invariant violations. Empty means every check passed."""
    problems = []
    sp = manifest["spending_policy"]
    paths = sp["paths"]
    weakest = sp["weakest_authorization"]

    for p in paths:
        if p["threshold"] > p["participants"]:
            problems.append(
                f"path {p['name']}: threshold {p['threshold']} exceeds participants "
                f"{p['participants']}, which is unspendable")

    min_threshold = min(p["threshold"] for p in paths)
    if weakest["m"] != min_threshold:
        problems.append(
            f"weakest authorization m is {weakest['m']} but the smallest path threshold "
            f"is {min_threshold}. BES 0001 section 2.3 requires the weakest, not the headline")

    max_participants = max(p["participants"] for p in paths)
    if weakest["n"] != max_participants:
        problems.append(
            f"weakest authorization n is {weakest['n']} but the largest path participant "
            f"count is {max_participants}")

    guardian_count = manifest["guardians"]["count"]
    if guardian_count != weakest["n"]:
        problems.append(
            f"guardian count {guardian_count} does not match n {weakest['n']}. Section 3.1 "
            f"counts a party once however many shares it holds")

    by_name = {p["name"]: p for p in paths}
    stated = {r["path"]: r for r in manifest["risk_statement"]["per_path"]}
    for name, p in by_name.items():
        if name not in stated:
            problems.append(f"path {name} has no risk statement. Section 3.10 requires one per path")
            continue
        r = stated[name]
        expected_unavailable = p["participants"] - p["threshold"]
        if r["unavailable_tolerated"] != expected_unavailable:
            problems.append(
                f"path {name}: risk statement says {r['unavailable_tolerated']} guardians may be "
                f"unavailable, but n minus m is {expected_unavailable}")
        if r["collusion_set"] != p["threshold"]:
            problems.append(
                f"path {name}: risk statement says {r['collusion_set']} guardians can spend against "
                f"the mission, but the path threshold is {p['threshold']}")
    for name in stated:
        if name not in by_name:
            problems.append(f"risk statement names path {name}, which is not in the published policy")

    for d in manifest["guardians"].get("domains", []):
        size = len(d["guardians"])
        for path_name in d["paths"]:
            p = by_name.get(path_name)
            if p is None:
                problems.append(f"domain {d['name']} names path {path_name}, which does not exist")
                continue
            m, n = p["threshold"], p["participants"]
            if d["kind"] in ("control", "compromise", "coercion") and size >= m:
                problems.append(
                    f"domain {d['name']} ({d['kind']}, {d['dependency']}) contains {size} guardians "
                    f"on path {path_name}, reaching the threshold of {m}. Section 3.5 requires fewer than m")
            if d["kind"] == "unavailability" and size >= n - m + 1:
                problems.append(
                    f"domain {d['name']} ({d['dependency']}) can disable {size} guardians on path "
                    f"{path_name}, making the threshold unreachable. Section 3.6 requires fewer than "
                    f"{n - m + 1}")

    conf = manifest["conformance"]
    if conf["claim"] == "conformant" and conf["unmet_musts"]:
        problems.append(
            "claim is conformant while unmet MUST clauses are listed. Section 11.2 permits only "
            "'based on with declared deviations' in that case")

    custody = manifest["custody_operations"]
    if custody["assessed"] and not custody.get("standard"):
        problems.append(
            "custody operations are marked assessed but no standard is named. Section 12.2 requires "
            "a named standard and release, or a plain statement that custody is unassessed")

    return problems


def main(argv):
    if len(argv) < 2:
        print("usage: check_invariants.py <manifest.json> [<manifest.json> ...]")
        return 2
    failed = False
    for path in argv[1:]:
        with open(path) as handle:
            problems = check(json.load(handle))
        if problems:
            failed = True
            print(f"FAIL {path}")
            for problem in problems:
                print(f"  {problem}")
        else:
            print(f"ok   {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
