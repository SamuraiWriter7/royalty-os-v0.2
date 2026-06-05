# Royalty OS v0.2

## Event-Based Trace-to-Value Circulation Architecture

Royalty OS v0.2 is an experimental event-based architecture for connecting traceable human-originated thought to dynamic value circulation.

Royalty OS v0.1 defined a static minimum recognition model:

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

Royalty OS v0.2 extends this model into an append-only event-based system:

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

v0.2 is designed to explore how human-originated thought can be traced, reviewed, evaluated, allocated, and connected to visible return over time.

---

## Status

```text
Version: v0.2.0-draft
Status: Draft / Experimental Architecture
Stage: Event-Based Extension
Base: Royalty OS v0.1
```

Royalty OS v0.2 is developed as a separate experimental repository.

Royalty OS v0.1 remains the stable minimum candidate specification.

---

## Why v0.2 Exists

Royalty OS v0.1 established the minimum structure for connecting Trace Protocol records to value circulation.

However, value circulation in the AI age is not static.

An idea may be referenced multiple times.

A concept may evolve.

An AI system may detect a possible dependency.

A human reviewer may approve or reject that detection.

A derivative work may appear later.

A value signal may become stronger over time.

Therefore, Royalty OS v0.2 introduces an event-based model.

Instead of treating value circulation as a single record, v0.2 treats it as an evolving append-only history of events.

---

## Core Concept

Royalty OS v0.2 is based on the following chain:

```text
Origin
  ↓
Trace Record
  ↓
Value Event Log
  ↓
Review Layer
  ↓
Allocation Layer
  ↓
Return History
```

### Origin

The human-originated source of a question, concept, structure, protocol, specification, essay, or creative work.

### Trace Record

A structured record of origin and lineage.

### Value Event Log

An append-only sequence of events related to references, citations, AI mentions, reviews, value signals, allocations, corrections, disputes, and returns.

### Review Layer

A layer where AI-assisted detection and human review can evaluate meaning, evidence, confidence, and validity.

### Allocation Layer

A rule-based or policy-based layer that determines possible forms of return.

### Return History

A record of completed value return, including attribution, linkback, citation, repository reference, acknowledgement, point allocation, or future compensation.

---

## Core Principles

### 1. Origin Remains Visible

Human-originated thought should remain connected to its origin even when referenced, summarized, transformed, or reused.

### 2. Append-Only History

Value circulation should be recorded as an append-only event history.

Existing events should not be silently rewritten.

### 3. Detection Is Not Judgment

AI may detect possible references or dependencies.

Human review remains important for judgment, especially for high-impact events.

### 4. Review Before High-Impact Allocation

High-impact allocation decisions should normally require approved review before return or compensation is recorded.

### 5. Return History Separates Intent From Completion

Allocation decisions define what should return.

Return records define what actually returned.

### 6. Non-Monetary First

v0.2 prioritizes citation, linkback, conceptual attribution, repository reference, acknowledgement, and visible recognition before monetary compensation.

---

## Repository Structure

```text
.
├── docs/
│   ├── architecture.md
│   ├── circulation-model.md
│   ├── layer-diagram.md
│   ├── event-model.md
│   ├── review-layer.md
│   ├── allocation-layer.md
│   └── relationship-to-v0.1.md
├── spec/
│   └── royalty-os-v0.2.yaml
├── schemas/
│   ├── origin.schema.json
│   ├── trace.schema.json
│   ├── value-event.schema.json
│   ├── review.schema.json
│   ├── allocation.schema.json
│   ├── return.schema.json
│   └── royalty-os-record.schema.json
├── examples/
│   ├── origin-record.example.yaml
│   ├── trace-record.example.yaml
│   ├── value-event-log.example.yaml
│   ├── review-record.example.yaml
│   ├── allocation-decision.example.yaml
│   └── return-record.example.yaml
├── scripts/
│   └── validate_examples.py
├── .github/
│   └── workflows/
│       └── validate-royalty-os-v0.2.yml
├── CHANGELOG.md
├── CITATION.cff
└── README.md
```

---

## Key Documents

### `docs/architecture.md`

Defines the overall Royalty OS v0.2 architecture.

It explains the transition from the v0.1 static record model to the v0.2 event-based value circulation architecture.

### `docs/circulation-model.md`

Defines Royalty OS v0.2 as a circulation model.

It shows how value moves through the system:

```text
Human Origin
  ↓
Trace Record
  ↓
Value Event Log
  ↓
Review Layer
  ↓
Allocation Layer
  ↓
Return History
  ↓
New Origin / New Trace
```

This document clarifies that Royalty OS v0.2 is not only an attribution log, but a circulation system where returned value may become the seed of new creation.

### `docs/layer-diagram.md`

Defines the six-layer structure of Royalty OS v0.2.

It explains the responsibilities of:

* Origin Layer
* Trace Layer
* Value Event Log Layer
* Review Layer
* Allocation Layer
* Return History Layer

This document helps readers understand the architecture as a layered OS rather than a loose collection of records.

### `docs/event-model.md`

Defines the Value Event Log and the `value_event` model.

It covers event types, event lifecycle, actor model, target model, evidence model, correction events, dispute events, and append-only principles.

### `docs/review-layer.md`

Defines the Review Layer.

It clarifies the boundary between AI-assisted detection and human judgment.

It also defines review statuses, review requirement levels, evidence assessment, confidence scoring, and dispute handling.

### `docs/allocation-layer.md`

Defines the Allocation Layer.

It explains how reviewed value signals may produce allocation decisions and how those decisions connect to return methods.

### `docs/relationship-to-v0.1.md`

Explains how Royalty OS v0.2 relates to Royalty OS v0.1.

It clarifies that v0.1 is the stable static foundation, while v0.2 is the experimental event-based extension.

### `spec/royalty-os-v0.2.yaml`

The core Royalty OS v0.2 specification.

It defines:

* purpose
* non-goals
* core principles
* conceptual flow
* architecture layers
* data model
* event model
* review layer
* allocation layer
* relationship to v0.1
* repository structure
* future extensions

---

## Schema Modules

Royalty OS v0.2 uses modular JSON Schemas.

### `schemas/origin.schema.json`

Validates Origin Layer records.

### `schemas/trace.schema.json`

Validates Trace Layer records.

### `schemas/value-event.schema.json`

Validates individual value events.

### `schemas/review.schema.json`

Validates review records.

### `schemas/allocation.schema.json`

Validates allocation decisions.

### `schemas/return.schema.json`

Validates return records.

### `schemas/royalty-os-record.schema.json`

Root schema for complete Royalty OS v0.2 records.

It connects origin, trace, value event log, review records, allocation decisions, and return records.

---

## Example Files

### `examples/origin-record.example.yaml`

Example origin record for the Epicenter Network.

### `examples/trace-record.example.yaml`

Example trace record connected to the Epicenter Network origin.

### `examples/value-event-log.example.yaml`

Example append-only value event log.

It demonstrates the event chain:

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

### `examples/review-record.example.yaml`

Example human review record for a detected conceptual reference.

### `examples/allocation-decision.example.yaml`

Example allocation decision based on reviewed value events.

### `examples/return-record.example.yaml`

Example return record confirming completed non-monetary value return.

---

## Validation

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Run validation:

```bash
python scripts/validate_examples.py
```

The validation script checks:

* all JSON Schema files are valid
* each example file matches its corresponding schema
* each value event in the event log matches `value-event.schema.json`
* event IDs are not duplicated
* core cross-file references are consistent

Expected final output:

```text
All validations passed.
```

---

## GitHub Actions

This repository includes automated validation through GitHub Actions.

Workflow file:

```text
.github/workflows/validate-royalty-os-v0.2.yml
```

The workflow runs on:

* push to `main` or `master`
* pull request to `main` or `master`
* manual workflow dispatch

---

## v0.1 vs v0.2

| Area            | Royalty OS v0.1           | Royalty OS v0.2             |
| --------------- | ------------------------- | --------------------------- |
| Model           | Static record             | Event-based log             |
| Core unit       | Royalty OS record         | Value event                 |
| Schema          | Single schema             | Modular schemas             |
| Value signal    | Mostly static             | Dynamic over time           |
| Review          | Simple flags              | Dedicated Review Layer      |
| Allocation      | Static allocation field   | Allocation decision records |
| Return          | Return methods            | Return history              |
| Best use        | Minimum recognition layer | Evolving value circulation  |
| Repository role | Stable candidate core     | Experimental extension      |

---

## Event Types

Royalty OS v0.2 introduces the following event families.

### Origin Events

```text
origin_registered
origin_updated
origin_deprecated
```

### Trace Events

```text
trace_created
trace_updated
trace_linked
trace_version_updated
```

### Reference Events

```text
reference_detected
citation_added
linkback_added
conceptual_reference_detected
structural_dependency_detected
implementation_dependency_detected
derivative_work_registered
translation_registered
summary_registered
```

### AI-Related Events

```text
ai_reference_detected
ai_similarity_detected
ai_summary_detected
ai_derivative_detected
ai_assisted_review_created
```

### Review Events

```text
human_review_requested
human_review_completed
review_rejected
review_disputed
review_reopened
```

### Value Signal Events

```text
value_signal_created
value_signal_updated
value_signal_downgraded
value_signal_upgraded
value_signal_disputed
```

### Allocation Events

```text
allocation_decision_created
allocation_decision_updated
allocation_decision_approved
allocation_decision_rejected
allocation_decision_superseded
allocation_decision_disputed
allocation_decision_completed
```

### Return Events

```text
return_recorded
citation_return_completed
linkback_return_completed
credit_return_completed
repository_reference_completed
acknowledgement_completed
point_allocation_recorded
compensation_recorded
```

### Correction Events

```text
correction_added
event_retracted
evidence_updated
status_updated
```

---

## Circulation Model Summary

Royalty OS v0.2 is not only a schema system.

It is a circulation model.

The core flow is:

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

The key idea is:

```text
Value should return to the origin and become the seed of new creation.
```

This is what separates Royalty OS v0.2 from a simple attribution log.

---

## Layer Diagram Summary

Royalty OS v0.2 has six core layers:

```text
1. Origin Layer
2. Trace Layer
3. Value Event Log Layer
4. Review Layer
5. Allocation Layer
6. Return History Layer
```

Each layer has a distinct responsibility.

This separation prevents the system from confusing:

* origin and output
* detection and judgment
* signal and allocation
* allocation and return
* correction and erasure

---

## Review Layer Summary

The Review Layer separates detection from judgment.

Core principle:

```text
AI may detect.
Humans should judge.
The event log should preserve both.
```

AI may assist with:

* reference detection
* conceptual similarity detection
* evidence summarization
* review priority suggestion
* value signal suggestion

AI should not unilaterally:

* approve high-impact value events
* assign final allocation
* declare ownership
* settle disputes
* trigger compensation
* erase or rewrite past events

---

## Allocation Layer Summary

The Allocation Layer connects reviewed value signals to return methods.

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

Core principle:

```text
Do not confuse detected value with completed return.
```

Allocation types include:

```text
non_monetary
monetary
hybrid
experimental
```

v0.2 prioritizes non-monetary return, including:

* citation
* linkback
* conceptual attribution
* repository reference
* acknowledgement
* version lineage

---

## Return History Summary

The Return History Layer records completed value return.

It answers:

```text
What value actually returned?
When did it return?
To whom did it return?
What evidence confirms the return?
```

This separates intention from completion.

An allocation decision says what should happen.

A return record says what actually happened.

---

## Relationship to Royalty OS v0.1

Royalty OS v0.1 should be treated as the stable minimum foundation.

Royalty OS v0.2 builds on v0.1, but does not overwrite it.

```text
v0.1
= static trace-to-value record

v0.2
= event-based trace-to-value circulation
```

v0.1 is the foundation stone.

v0.2 is the moving water.

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

v0.2 is an experimental event architecture.

Its goal is to model the movement of value, not to enforce all consequences.

---

## Future Extensions

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

## Recommended Reading Order

For first-time readers, the recommended order is:

```text
1. README.md
2. docs/relationship-to-v0.1.md
3. docs/architecture.md
4. docs/circulation-model.md
5. docs/layer-diagram.md
6. docs/event-model.md
7. docs/review-layer.md
8. docs/allocation-layer.md
9. spec/royalty-os-v0.2.yaml
10. examples/value-event-log.example.yaml
11. schemas/royalty-os-record.schema.json
```

This order moves from overview to version relationship, architecture, circulation, layer structure, event model, review, allocation, specification, examples, and validation.

---

## Design Philosophy

Royalty OS v0.2 follows the same core philosophy as v0.1:

```text
Do not block the flow of knowledge.
Do not erase the origin of knowledge.
Do not allow value to move in only one direction.
```

v0.2 adds one more principle:

```text
Value circulation should be recorded as an evolving event history.
```

The circulation model adds:

```text
Value should return to the origin and become the seed of new creation.
```

---

## License

MIT License

---

## Citation

If you use or reference this specification, please cite this repository using the metadata in:

```text
CITATION.cff
```

---

## Summary

Royalty OS v0.2 begins the transition from static recognition records to event-based value circulation.

It introduces:

* append-only value events
* modular schemas
* AI-assisted review
* human verification
* dynamic value signals
* allocation decisions
* return history
* circulation model
* layer diagram

Royalty OS v0.1 preserved the origin.

Royalty OS v0.2 records the movement of value.

The wind has become a cycle.
