# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight versioning model during the early draft and experimental phases.

---

## [v0.2.0-draft] - 2026-06-04

### Added

* Added initial Royalty OS v0.2 README.

  * `README.md`

* Added architecture documentation.

  * `docs/architecture.md`

* Added circulation model documentation.

  * `docs/circulation-model.md`

* Added layer diagram documentation.

  * `docs/layer-diagram.md`

* Added event model documentation.

  * `docs/event-model.md`

* Added review layer documentation.

  * `docs/review-layer.md`

* Added allocation layer documentation.

  * `docs/allocation-layer.md`

* Added relationship document between Royalty OS v0.1 and v0.2.

  * `docs/relationship-to-v0.1.md`

* Added core Royalty OS v0.2 specification.

  * `spec/royalty-os-v0.2.yaml`

* Added modular JSON Schema files.

  * `schemas/origin.schema.json`
  * `schemas/trace.schema.json`
  * `schemas/value-event.schema.json`
  * `schemas/review.schema.json`
  * `schemas/allocation.schema.json`
  * `schemas/return.schema.json`
  * `schemas/royalty-os-record.schema.json`

* Added example YAML records.

  * `examples/origin-record.example.yaml`
  * `examples/trace-record.example.yaml`
  * `examples/value-event-log.example.yaml`
  * `examples/review-record.example.yaml`
  * `examples/allocation-decision.example.yaml`
  * `examples/return-record.example.yaml`

* Added validation script.

  * `scripts/validate_examples.py`

* Added GitHub Actions workflow for automated validation.

  * `.github/workflows/validate-royalty-os-v0.2.yml`

* Added citation metadata.

  * `CITATION.cff`

---

## Updated

* Updated `README.md` to include:

  * `docs/circulation-model.md`
  * `docs/layer-diagram.md`
  * expanded repository structure
  * updated key documents
  * circulation model summary
  * layer diagram summary
  * updated recommended reading order
  * citation guidance

---

## Defined

### Event-Based Architecture

Royalty OS v0.2 extends the static Royalty OS v0.1 model into an event-based architecture.

Royalty OS v0.1:

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

Royalty OS v0.2:

```text
Origin
  ↓
Trace Record
  ↓
Value Event Log
  ↓
Review Layer
  ↓
Dynamic Value Signal
  ↓
Allocation Layer
  ↓
Return History
```

---

### Circulation Model

Defined Royalty OS v0.2 as a circulation model rather than a simple attribution log.

Core circulation flow:

```text
Human Origin
  ↓
Trace Record
  ↓
Value Event Log
  ↓
Review Layer
  ↓
Dynamic Value Signal
  ↓
Allocation Layer
  ↓
Return History
  ↓
Renewed Origin / New Trace
```

The circulation model clarifies that value should not move in only one direction.

It defines the return loop where returned value may become the seed of new creation.

Core principle:

```text
Value should return to the origin and become the seed of new creation.
```

---

### Layer Diagram

Defined the six-layer architecture of Royalty OS v0.2.

The six layers are:

```text
1. Origin Layer
2. Trace Layer
3. Value Event Log Layer
4. Review Layer
5. Allocation Layer
6. Return History Layer
```

Each layer has a distinct responsibility:

| Layer                 | Responsibility                                   | Main Object                      |
| --------------------- | ------------------------------------------------ | -------------------------------- |
| Origin Layer          | Record the human-originated source               | `origin_record`                  |
| Trace Layer           | Record origin lineage and conceptual ancestry    | `trace_record`                   |
| Value Event Log Layer | Record meaningful value-related events over time | `value_event_log`, `value_event` |
| Review Layer          | Separate AI detection from human judgment        | `review_record`                  |
| Allocation Layer      | Decide appropriate return methods                | `allocation_decision`            |
| Return History Layer  | Record completed return or recognition           | `return_record`                  |

This layer separation prevents confusion between:

* origin and output
* detection and judgment
* signal and allocation
* allocation and return
* correction and erasure

---

### Value Event Log

Defined the Value Event Log as an append-only record of value circulation events.

Initial event families include:

* origin events
* trace events
* reference events
* AI-related events
* review events
* value signal events
* allocation events
* return events
* correction events

Example flow:

```text
origin_registered
  ↓
trace_created
  ↓
reference_detected
  ↓
human_review_completed
  ↓
value_signal_updated
  ↓
allocation_decision_created
  ↓
return_recorded
```

---

### Review Layer

Defined the Review Layer as the judgment layer between detection and allocation.

Core principle:

```text
AI may detect.
Humans should judge.
The event log should preserve both.
```

The Review Layer includes:

* review statuses
* review requirement levels
* AI-assisted review
* human review
* evidence assessment
* confidence scoring
* dispute handling
* correction handling

---

### Allocation Layer

Defined the Allocation Layer as the decision layer that connects reviewed value signals to return methods.

Core chain:

```text
Reviewed Event
  ↓
Value Signal
  ↓
Allocation Decision
  ↓
Return Record
```

Allocation types include:

* non-monetary
* monetary
* hybrid
* experimental

v0.2 prioritizes non-monetary value return, including:

* citation
* linkback
* conceptual attribution
* repository reference
* acknowledgement
* version lineage

---

### Return History

Defined Return History as the record of completed value return.

Return History answers:

```text
What value actually returned?
When did it return?
To whom did it return?
What evidence confirms the return?
```

This separates allocation intent from completed return.

---

## Schema Architecture

### Added Modular Schemas

Royalty OS v0.2 introduces modular schema architecture.

Each layer has its own schema:

```text
schemas/origin.schema.json
schemas/trace.schema.json
schemas/value-event.schema.json
schemas/review.schema.json
schemas/allocation.schema.json
schemas/return.schema.json
schemas/royalty-os-record.schema.json
```

### Root Schema

Added `schemas/royalty-os-record.schema.json` as the root schema for complete Royalty OS v0.2 records.

It connects:

* origin
* trace
* value event log
* review records
* allocation decisions
* return records

---

## Examples

Added example files demonstrating the full v0.2 flow:

```text
Origin Record
  ↓
Trace Record
  ↓
Value Event Log
  ↓
Review Record
  ↓
Allocation Decision
  ↓
Return Record
```

The examples are centered on the lineage:

```text
Epicenter Network
  ↓
Trace Protocol
  ↓
Royalty OS v0.1
  ↓
Royalty OS v0.2
```

---

## Validation

Added validation support for:

* modular JSON Schema files
* example YAML files
* value event log events
* duplicate event IDs
* cross-file consistency checks

The validation script checks:

* all schema files are valid JSON Schemas
* each example matches its corresponding schema
* each event in the value event log matches `value-event.schema.json`
* core identifiers are consistent across examples

Run validation:

```bash
python scripts/validate_examples.py
```

Expected final output:

```text
All validations passed.
```

---

## GitHub Actions

Added automated validation workflow.

Workflow file:

```text
.github/workflows/validate-royalty-os-v0.2.yml
```

The workflow runs on:

* push to `main` or `master`
* pull request to `main` or `master`
* manual workflow dispatch

---

## Relationship to Royalty OS v0.1

Defined Royalty OS v0.1 as the stable minimum foundation.

Defined Royalty OS v0.2 as the experimental event-based extension.

```text
v0.1
= static trace-to-value record

v0.2
= event-based trace-to-value circulation
```

v0.1 preserves the origin.

v0.2 records the movement of value.

---

## Non-Goals

Royalty OS v0.2 does not provide:

* legal royalty enforcement
* automatic payment execution
* complete copyright protection
* universal AI training data tracking
* court-admissible ownership proof
* mandatory blockchain storage
* final ownership decisions
* full monetization infrastructure

v0.2 remains an experimental event architecture.

Its goal is to model the movement of value, not to enforce all consequences.

---

## Future Directions

Possible future extensions include:

* Q-Point Protocol integration
* signed value event logs
* cryptographic timestamping
* decentralized identifiers
* trace graph visualization
* AI-assisted lineage mapping
* human review workflow engine
* attribution scoring
* resonance scoring
* creator dashboard
* compensation mechanisms
* cross-platform trace registries

---

## Notes

This draft release begins the transition from static recognition records to event-based value circulation.

Royalty OS v0.1 established the first minimum structure.

Royalty OS v0.2 introduces:

* append-only value events
* modular schemas
* AI-assisted review
* human verification
* dynamic value signals
* allocation decisions
* return history
* circulation model
* layer diagram

Core principle:

```text
Value circulation should be recorded as an evolving event history.
```

Circulation principle:

```text
Value should return to the origin and become the seed of new creation.
```

Royalty OS v0.2 starts here.
