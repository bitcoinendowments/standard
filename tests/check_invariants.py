#!/usr/bin/env python3
# Copyright 2026 Bitcoin Chiang Mai Ltd Co
# Licensed under the Apache License, Version 2.0. See LICENSE_CODE in the repository root.
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
    by_name = {p["name"]: p for p in paths}
    weakest = sp["weakest_authorization"]

    for p in paths:
        if p["threshold"] > p["participants"]:
            problems.append(
                f"path {p['name']}: threshold {p['threshold']} exceeds participants "
                f"{p['participants']}, which is unspendable")
        if len(p["roster"]) != p["participants"]:
            problems.append(
                f"path {p['name']}: roster lists {len(p['roster'])} parties but participants says "
                f"{p['participants']}")

    # The weakest condition belongs to one real path. It is never a synthesis of the
    # smallest m across paths with the largest n, because that pair may describe no
    # path that exists.
    weakest_path = by_name.get(weakest["path"])
    if weakest_path is None:
        problems.append(
            f"weakest authorization names path {weakest['path']}, which is not in the published policy")
    else:
        if weakest["m"] != weakest_path["threshold"] or weakest["n"] != weakest_path["participants"]:
            problems.append(
                f"weakest authorization says {weakest['m']} of {weakest['n']} but path "
                f"{weakest_path['name']} is {weakest_path['threshold']} of {weakest_path['participants']}")
        smallest = min(p["threshold"] for p in paths)
        if weakest_path["threshold"] != smallest:
            weaker = [p["name"] for p in paths if p["threshold"] == smallest]
            problems.append(
                f"weakest authorization names path {weakest_path['name']} at threshold "
                f"{weakest_path['threshold']}, but {', '.join(weaker)} authorizes at {smallest}. "
                f"Section 2.3 wants the weakest route, not the headline one")

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
                f"unavailable, but n minus m for this path is {expected_unavailable}")
        if r["collusion_set"] != p["threshold"]:
            problems.append(
                f"path {name}: risk statement says {r['collusion_set']} guardians can spend against "
                f"the mission, but this path's threshold is {p['threshold']}")
    for name in stated:
        if name not in by_name:
            problems.append(f"risk statement names path {name}, which is not in the published policy")

    guardian_count = manifest["guardians"]["count"]
    largest_roster = max(len(p["roster"]) for p in paths)
    if guardian_count < largest_roster:
        problems.append(
            f"guardian count {guardian_count} is smaller than the largest path roster "
            f"{largest_roster}. Section 3.1 counts a party once however many shares it holds")

    # Domain membership is counted per path, against that path's own roster and its own
    # m and n. A guardian who cannot participate in a path cannot compromise it.
    for d in manifest["guardians"].get("domains", []):
        for path_name in d["paths"]:
            p = by_name.get(path_name)
            if p is None:
                problems.append(f"domain {d['name']} names path {path_name}, which does not exist")
                continue
            members = [g for g in d["guardians"] if g in p["roster"]]
            size = len(members)
            if size == 0:
                continue
            m, n = p["threshold"], p["participants"]
            if d["kind"] in ("control", "compromise", "coercion") and size >= m:
                problems.append(
                    f"domain {d['name']} ({d['kind']}, {d['dependency']}) holds {size} of path "
                    f"{path_name}'s roster, reaching its threshold of {m}. Section 3.5 requires fewer than m")
            if d["kind"] == "unavailability" and size >= n - m + 1:
                problems.append(
                    f"domain {d['name']} ({d['dependency']}) can disable {size} of path {path_name}'s "
                    f"roster, making its threshold unreachable. Section 3.6 requires fewer than {n - m + 1}")

    # An enabled key path is an ordinary path entry, so that weakest path selection,
    # risk arithmetic, and domain membership all apply to it. The Taproot object holds
    # only enabled state and the unspendable internal key proof.
    key_path = sp.get("key_path", {})
    if key_path.get("enabled") is False:
        if not key_path.get("unspendable_internal_key_proof"):
            problems.append(
                "key path is disabled but no unspendable internal key derivation is published. "
                "Section 2.7 requires it, because an enabled key path nobody mentions is the most "
                "consequential undisclosed path there is")
        for p in paths:
            if p["enforcement"] == "aggregate_signing":
                problems.append(
                    f"path {p['name']} declares aggregate signing while the key path is marked "
                    f"disabled. Section 2.6 and section 2.8 disagree with each other here")
    if key_path.get("enabled") is True:
        named = key_path.get("path")
        if not named:
            problems.append(
                "key path is enabled but names no entry in paths. Section 2.8 requires it be "
                "published as a path with its own threshold, participants, and roster")
        elif named not in by_name:
            problems.append(f"key path names path {named}, which is not in the published policy")
        elif by_name[named]["enforcement"] != "aggregate_signing":
            problems.append(
                f"key path names path {named}, which declares enforcement "
                f"{by_name[named]['enforcement']} rather than aggregate_signing. Section 2.6")
        elif not by_name[named].get("aggregate_protocol"):
            problems.append(f"path {named} is the aggregate signing key path but names no protocol. Section 2.8")

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
