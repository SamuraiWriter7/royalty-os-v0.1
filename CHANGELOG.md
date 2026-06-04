# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight versioning model during the early draft phase.

---

## [v0.1.0-candidate] - 2026-06-04

### Added

* Added initial Royalty OS v0.1 implementation documentation.

  * `docs/royalty-os-implementation.md`

* Added core Royalty OS v0.1 specification.

  * `spec/royalty-os-v0.1.yaml`

* Added minimum value circulation example.

  * `examples/value-circulation.example.yaml`

* Added JSON Schema for Royalty OS records.

  * `schemas/royalty-os.schema.json`

* Added example validation script.

  * `scripts/validate_examples.py`

* Added GitHub Actions workflow for automated validation.

  * `.github/workflows/validate-royalty-os.yml`

* Added README documentation reflecting the Royalty OS v0.1 repository structure, validation flow, implementation stages, and design philosophy.

  * `README.md`

### Defined

* Defined Royalty OS as a Trace-to-Value Circulation Architecture for the AI age.

* Defined the core conceptual flow:

```text
Origin
  ↓
Trace Record
  ↓
Reference Event
  ↓
Value Signal
  ↓
Allocation Rule
  ↓
Return / Recognition
```

* Defined the relationship between Trace Protocol and Royalty OS:

```text
Trace Protocol
= records origin and lineage

Royalty OS
= connects recorded origin to value circulation
```

* Defined the minimum viable implementation structure:

```text
docs/royalty-os-implementation.md
spec/royalty-os-v0.1.yaml
examples/value-circulation.example.yaml
schemas/royalty-os.schema.json
scripts/validate_examples.py
.github/workflows/validate-royalty-os.yml
```

### Validation

* Added schema-based validation for `examples/value-circulation.example.yaml`.

* Added support for validating Royalty OS records against `schemas/royalty-os.schema.json`.

* Added GitHub Actions validation on:

  * push
  * pull request
  * manual workflow dispatch

### Notes

This candidate release establishes the first minimum viable implementation of Royalty OS.

The current version focuses on non-monetary value circulation, including:

* citation
* linkback
* conceptual attribution
* version lineage
* repository reference
* origin recognition

Monetary compensation, licensing automation, tokenized rewards, AI usage-based compensation, and legal enforcement remain future extensions.

---

## [v0.1.0-draft] - 2026-06-04

### Added

* Drafted the initial Royalty OS concept.
* Established the third epicenter structure:

  * Epicenter Network
  * Trace Protocol
  * Royalty OS
* Defined Royalty OS as the value circulation layer that connects Trace Protocol to recognition, attribution, evaluation, and future compensation.

### Notes

This draft introduced Royalty OS as the third epicenter following:

```text
Epicenter Network
  ↓
Trace Protocol
  ↓
Royalty OS
```
