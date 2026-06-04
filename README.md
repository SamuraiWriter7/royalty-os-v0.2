# Royalty OS v0.2

## Event-Based Trace-to-Value Circulation Architecture

Royalty OS v0.2 is an experimental event-based architecture for connecting traceable human-originated thought to dynamic value circulation.

Royalty OS v0.1 defined the minimum static structure:

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

Royalty OS v0.2 extends this model into an event-based system:

```text
Origin
  ↓
Trace Record
  ↓
Value Event Log
  ↓
AI / Human Review
  ↓
Dynamic Value Signal
  ↓
Allocation Decision
  ↓
Return History
```

v0.2 is designed to explore how human-originated thought can be traced, reviewed, evaluated, and connected to non-monetary or future monetary value return over time.

---

## Status

```text
Version: v0.2.0-draft
Status: Draft / Experimental Architecture
Stage: Event-Based Extension
Base: Royalty OS v0.1
```

Royalty OS v0.2 is a separate experimental repository.

Royalty OS v0.1 remains the stable minimum candidate specification.

---

## Why v0.2 Exists

Royalty OS v0.1 established a static record model.

It defined:

* origin,
* trace,
* reference event,
* value signal,
* allocation,
* return method.

However, value circulation in the AI age is not static.

An idea may be referenced many times.

A concept may evolve.

An AI system may summarize it.

A human reviewer may confirm or reject a value signal.

A derivative work may appear months later.

A reference may change from shallow mention to deep structural dependency.

Therefore, v0.2 introduces an event-based model.

Instead of treating value circulation as a single record, v0.2 treats it as an append-only history of events.

---

## Core Concept

Royalty OS v0.2 is based on the following model:

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

The structured record of origin and lineage.

### Value Event Log

An append-only sequence of events related to references, citations, AI mentions, derivative works, value signals, reviews, allocations, and returns.

### Review Layer

A layer where AI-assisted detection and human review can evaluate the meaning, depth, and reliability of value events.

### Allocation Layer

A rule-based or policy-based layer that determines possible forms of return.

### Return History

A record of visible value returned to the origin, including attribution, linkback, citation, repository reference, acknowledgement, point allocation, or future compensation.

---

## v0.1 vs v0.2

| Area            | Royalty OS v0.1           | Royalty OS v0.2                     |
| --------------- | ------------------------- | ----------------------------------- |
| Model           | Static record             | Event-based log                     |
| Schema          | Single schema             | Modular schemas                     |
| Value signal    | Single signal             | Dynamic signals over time           |
| Review          | Human-reviewed flag       | AI / human review layer             |
| Allocation      | Static allocation field   | Allocation decision events          |
| Return          | Return methods            | Return history                      |
| Use case        | Minimum recognition layer | Evolving trace-to-value circulation |
| Repository role | Stable candidate core     | Experimental extension              |

---

## Design Goals

Royalty OS v0.2 aims to:

* introduce append-only value event logs,
* modularize JSON Schemas,
* separate origin, trace, event, review, allocation, and return structures,
* support AI-assisted reference detection,
* preserve human review as a critical layer,
* allow value signals to evolve over time,
* support future Q-Point Protocol integration,
* prepare for attribution scoring and value circulation dashboards.

---

## Non-Goals

Royalty OS v0.2 does not attempt to provide:

* legally binding royalty enforcement,
* automatic payment execution,
* universal AI training data tracking,
* copyright dispute resolution,
* blockchain token issuance,
* court-admissible ownership proof,
* complete platform monetization.

v0.2 remains an experimental architecture.

Its purpose is to define a structured event model for trace-to-value circulation.

---

## Proposed Repository Structure

```text
.
├── docs/
│   ├── architecture.md
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
│   └── allocation-decision.example.yaml
├── scripts/
│   └── validate_examples.py
├── .github/
│   └── workflows/
│       └── validate-royalty-os-v0.2.yml
├── README.md
├── CHANGELOG.md
├── CITATION.cff
└── LICENSE
```

---

## Core Event Types

Royalty OS v0.2 introduces value events.

Initial event types include:

```text
origin_registered
trace_created
reference_detected
citation_added
linkback_added
ai_reference_detected
human_review_requested
human_review_completed
value_signal_updated
allocation_decision_created
return_recorded
derivative_work_registered
version_updated
```

---

## Example Event Flow

```text
origin_registered
  ↓
trace_created
  ↓
reference_detected
  ↓
ai_reference_detected
  ↓
human_review_requested
  ↓
human_review_completed
  ↓
value_signal_updated
  ↓
allocation_decision_created
  ↓
return_recorded
```

This allows Royalty OS to represent value circulation as a living process rather than a single static record.

---

## Minimal Event Example

```yaml
royalty_os_version: "0.2"

event:
  event_id: "event-001"
  event_type: "reference_detected"
  event_time: "2026-06-04T00:00:00Z"
  origin_id: "epicenter-network-001"
  trace_id: "trace-protocol-001"
  actor:
    actor_type: "human"
    actor_id: "SamuraiWriter7"
  target:
    target_type: "article"
    title: "Royalty OS v0.2"
    url: "https://example.com/royalty-os-v0.2"
  evidence:
    evidence_type: "link"
    url: "https://example.com/reference"
  value_signal:
    signal_type: "conceptual_reference"
    signal_strength: "high"
    confidence: 0.85
  review:
    human_review_required: true
    ai_assisted: true
    status: "pending"
```

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

This separation preserves the clarity of v0.1 while allowing v0.2 to explore more dynamic and experimental structures.

---

## Implementation Phases

### Phase 1: Event Model

Define the basic value event structure.

### Phase 2: Modular Schemas

Split the schema into modules:

* origin,
* trace,
* value event,
* review,
* allocation,
* return.

### Phase 3: Validation

Create examples and validation scripts.

### Phase 4: AI / Human Review Layer

Define how AI-assisted detection and human review interact.

### Phase 5: Dynamic Allocation

Define how value signals can influence allocation decisions.

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

---

## Summary

Royalty OS v0.2 begins the transition from static recognition records to event-based value circulation.

It introduces:

* append-only value events,
* modular schemas,
* AI-assisted review,
* human verification,
* dynamic value signals,
* allocation decisions,
* return history.

Royalty OS v0.1 preserved the origin.

Royalty OS v0.2 begins to record the movement of value.

The wind has become a log.

