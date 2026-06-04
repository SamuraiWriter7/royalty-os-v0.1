# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight versioning model during the early draft and candidate phases.

---

## [v0.1.0-candidate] - 2026-06-04

### Added

* Added initial Royalty OS v0.1 implementation documentation.

  * `docs/royalty-os-implementation.md`

* Added positioning document for Royalty OS.

  * `docs/positioning.md`

* Added comparison matrix for adjacent systems and fields.

  * `docs/comparison-matrix.md`

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

* Added citation metadata.

  * `CITATION.cff`

* Added README documentation reflecting the Royalty OS v0.1 repository structure, validation flow, implementation stages, positioning documents, comparison matrix, and design philosophy.

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

* Defined the relationship between Epicenter Network, Trace Protocol, and Royalty OS:

```text
Epicenter Network
= humans as origins

Trace Protocol
= origins are recorded

Royalty OS
= recorded origins receive value circulation
```

* Defined the minimum viable implementation structure:

```text
docs/royalty-os-implementation.md
docs/positioning.md
docs/comparison-matrix.md
spec/royalty-os-v0.1.yaml
examples/value-circulation.example.yaml
schemas/royalty-os.schema.json
scripts/validate_examples.py
.github/workflows/validate-royalty-os.yml
README.md
CHANGELOG.md
CITATION.cff
```

### Positioning

* Clarified what Royalty OS is:

  * an origin-aware value circulation model,
  * a bridge between Trace Protocol and future compensation,
  * a machine-readable specification,
  * a human-originated thought infrastructure,
  * a minimum viable recognition layer.

* Clarified what Royalty OS is not:

  * not a legal royalty enforcement system,
  * not a copyright registry,
  * not a blockchain requirement,
  * not an automatic payment system,
  * not a universal AI training data tracker,
  * not a replacement for human judgment.

* Clarified Royalty OS relationships to adjacent fields:

  * copyright,
  * citation systems,
  * data provenance,
  * knowledge graphs,
  * creator economy platforms,
  * AI attribution research,
  * Trace Protocol,
  * Epicenter Network.

### Comparison Matrix

* Added structured comparison between Royalty OS and adjacent systems:

  * Copyright,
  * Citation Systems,
  * Data Provenance,
  * Knowledge Graphs,
  * DRM,
  * Creator Economy Platforms,
  * AI Attribution Research,
  * Blockchain / Web3,
  * Trace Protocol,
  * Epicenter Network.

* Added comparative feature matrix covering:

  * expression protection,
  * origin recording,
  * conceptual lineage,
  * AI-mediated reuse,
  * value signals,
  * allocation rules,
  * non-monetary return,
  * machine-readable records,
  * platform neutrality,
  * future compensation support.

### Validation

* Added schema-based validation for `examples/value-circulation.example.yaml`.

* Added support for validating Royalty OS records against `schemas/royalty-os.schema.json`.

* Added GitHub Actions validation on:

  * push,
  * pull request,
  * manual workflow dispatch.

### Documentation

* Updated `README.md` to include:

  * repository structure,
  * key documents,
  * positioning document,
  * comparison matrix,
  * minimal viable implementation,
  * validation instructions,
  * GitHub Actions workflow,
  * implementation stages,
  * relationship to adjacent fields,
  * recommended reading order,
  * citation guidance.

### Notes

This candidate release establishes the first minimum viable implementation of Royalty OS.

The current version focuses on non-monetary value circulation, including:

* citation,
* linkback,
* conceptual attribution,
* version lineage,
* repository reference,
* origin recognition.

Monetary compensation, licensing automation, tokenized rewards, AI usage-based compensation, and legal enforcement remain future extensions.

The added positioning and comparison documents are intended to prevent overclaiming and clarify the precise role of Royalty OS as a trace-to-value circulation architecture.

---

## [v0.1.0-draft] - 2026-06-04

### Added

* Drafted the initial Royalty OS concept.

* Established the third epicenter structure:

  * Epicenter Network,
  * Trace Protocol,
  * Royalty OS.

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

The draft focused on defining the conceptual relationship between origin, trace, and value circulation before moving into structured implementation.
