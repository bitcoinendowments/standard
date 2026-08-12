# Changelog

All notable changes to this standard are recorded here. Format follows the release rules in `VERSIONING.md`. Releases are immutable once tagged.

## 0.1.0 (unreleased)

**Migration impact for existing deployments:** none. This is the first release.

First public draft.

Added:

• `spec/BES_0001_core_standard.md`, the normative standard, with permanent clause identifiers and one verification label per clause.
• `spec/glossary.md`, `spec/threat_model.md`, `spec/conformance.md`.
• `profiles/profile_standard_five_guardian.md`, one starting configuration.
• `templates/constitution_template.md`, `templates/deployment_manifest_template.json`, `templates/evidence_package_checklist.md`.
• `examples/lighthouse/`, one fully worked fictional deployment.
• `schemas/deployment_manifest.schema.json` and `tests/vectors/`.
• Governance, contributing, versioning, and disclaimer documents.

Known limitations at this release:

• The threat model records analysis, not adversarial test results. Stress testing against guardian loss, guardian collusion, legal dispute, and technical failure is scheduled and will run in the open.
• No legal review has been completed in any jurisdiction.
