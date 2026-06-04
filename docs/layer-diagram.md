# Royalty OS v0.2 Layer Diagram

## Version

`v0.2.0-draft`

## Status

Draft / Layer Diagram Document

---

## Purpose

This document defines the **layer diagram** of Royalty OS v0.2.

Royalty OS v0.2 is an event-based trace-to-value circulation architecture.

Its purpose is to preserve the visibility of human-originated thought and record how value moves through references, reviews, allocations, and returns.

The architecture can be understood as six core layers:

```text
1. Origin Layer
2. Trace Layer
3. Value Event Log Layer
4. Review Layer
5. Allocation Layer
6. Return History Layer
```

These layers work together to transform a human-originated thought into a traceable, reviewable, and returnable value flow.

---

## 1. Full Layer Diagram

```text
┌─────────────────────────────────────────────────────────────┐
│  6. Return History Layer                                    │
│  Completed recognition, attribution, linkback, return        │
└───────────────────────────────▲─────────────────────────────┘
                                │
                                │ Return record
                                │
┌───────────────────────────────┴─────────────────────────────┐
│  5. Allocation Layer                                         │
│  Allocation decisions, return methods, value routing         │
└───────────────────────────────▲─────────────────────────────┘
                                │
                                │ Reviewed value signal
                                │
┌───────────────────────────────┴─────────────────────────────┐
│  4. Review Layer                                             │
│  AI-assisted detection + human judgment                      │
└───────────────────────────────▲─────────────────────────────┘
                                │
                                │ Events requiring review
                                │
┌───────────────────────────────┴─────────────────────────────┐
│  3. Value Event Log Layer                                    │
│  Append-only events: reference, citation, AI detection        │
└───────────────────────────────▲─────────────────────────────┘
                                │
                                │ Traceable movement
                                │
┌───────────────────────────────┴─────────────────────────────┐
│  2. Trace Layer                                              │
│  Origin lineage, core question, related concepts             │
└───────────────────────────────▲─────────────────────────────┘
                                │
                                │ Origin anchor
                                │
┌───────────────────────────────┴─────────────────────────────┐
│  1. Origin Layer                                             │
│  Human-originated thought, question, concept, protocol        │
└─────────────────────────────────────────────────────────────┘
```

The diagram flows upward from human origin to return history.

In circulation form, the return may support a renewed origin or a new trace.

---

## 2. Layer Responsibilities

| Layer                 | Responsibility                                   | Main Object                      |
| --------------------- | ------------------------------------------------ | -------------------------------- |
| Origin Layer          | Record the human-originated source               | `origin_record`                  |
| Trace Layer           | Record origin lineage and conceptual ancestry    | `trace_record`                   |
| Value Event Log Layer | Record meaningful value-related events over time | `value_event_log`, `value_event` |
| Review Layer          | Separate AI detection from human judgment        | `review_record`                  |
| Allocation Layer      | Decide appropriate return methods                | `allocation_decision`            |
| Return History Layer  | Record completed return or recognition           | `return_record`                  |

Each layer should remain conceptually separate.

This separation prevents the system from confusing detection, judgment, allocation, and completed return.

---

## 3. Layer 1: Origin Layer

### Purpose

The Origin Layer records the first human-originated source.

This may be:

* a question,
* a concept,
* an essay,
* a protocol,
* a specification,
* a technical design,
* a philosophical model,
* a creative work,
* an AI-assisted but human-originated structure.

### Main object

```text
origin_record
```

### Example schema

```text
schemas/origin.schema.json
```

### Example file

```text
examples/origin-record.example.yaml
```

### Core idea

```text
No origin, no trace.
No trace, no reliable value circulation.
```

---

## 4. Layer 2: Trace Layer

### Purpose

The Trace Layer records the origin and its lineage.

It answers:

```text
Where did this thought begin?
What question generated it?
What concepts are related?
What lineage does it belong to?
```

### Main object

```text
trace_record
```

### Example schema

```text
schemas/trace.schema.json
```

### Example file

```text
examples/trace-record.example.yaml
```

### Core idea

The Trace Layer prevents human-originated thought from being flattened into anonymous content.

---

## 5. Layer 3: Value Event Log Layer

### Purpose

The Value Event Log Layer records meaningful events over time.

This is the central innovation of v0.2.

Instead of treating value circulation as a single static record, v0.2 records it as an append-only event history.

### Main objects

```text
value_event_log
value_event
```

### Example schema

```text
schemas/value-event.schema.json
```

### Example file

```text
examples/value-event-log.example.yaml
```

### Event examples

```text
origin_registered
trace_created
reference_detected
ai_reference_detected
human_review_completed
value_signal_updated
allocation_decision_created
return_recorded
correction_added
review_disputed
```

### Core idea

```text
Do not silently overwrite value history.
Record changes as events.
```

---

## 6. Layer 4: Review Layer

### Purpose

The Review Layer evaluates events before they influence allocation or return.

It separates AI detection from human judgment.

### Main object

```text
review_record
```

### Example schema

```text
schemas/review.schema.json
```

### Example file

```text
examples/review-record.example.yaml
```

### Core principle

```text
AI may detect.
Humans should judge.
The event log should preserve both.
```

### Why it matters

Without review, AI-assisted detection may become automatic overclaiming.

The Review Layer prevents detection from becoming truth without evaluation.

---

## 7. Layer 5: Allocation Layer

### Purpose

The Allocation Layer determines how value should return to the origin.

It connects reviewed value signals to return methods.

### Main object

```text
allocation_decision
```

### Example schema

```text
schemas/allocation.schema.json
```

### Example file

```text
examples/allocation-decision.example.yaml
```

### Return methods

Examples include:

```text
citation
linkback
credit
conceptual_attribution
repository_reference
acknowledgement
point_allocation
future compensation
```

### Core principle

```text
Do not confuse detected value with completed return.
```

Allocation defines what should happen.

Return History records what actually happened.

---

## 8. Layer 6: Return History Layer

### Purpose

The Return History Layer records completed return or recognition.

It confirms that value actually returned to the origin.

### Main object

```text
return_record
```

### Example schema

```text
schemas/return.schema.json
```

### Example file

```text
examples/return-record.example.yaml
```

### It answers

```text
What value returned?
When did it return?
To whom did it return?
What evidence confirms the return?
```

### Core idea

Return History separates intention from completion.

---

## 9. Data Flow Across Layers

A typical value circulation flow looks like this:

```text
Origin Layer
  ↓
Trace Layer
  ↓
Value Event Log Layer
  ↓
Review Layer
  ↓
Allocation Layer
  ↓
Return History Layer
```

Expanded as events:

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

This is the minimum complete v0.2 circulation path.

---

## 10. Separation of Concerns

Royalty OS v0.2 separates the following concepts:

| Concept          | Layer                 |
| ---------------- | --------------------- |
| Human source     | Origin Layer          |
| Lineage          | Trace Layer           |
| Movement         | Value Event Log Layer |
| Judgment         | Review Layer          |
| Return decision  | Allocation Layer      |
| Completed return | Return History Layer  |

This separation is important.

Without separation:

* AI detection may be mistaken for truth,
* value signals may be mistaken for return,
* allocation decisions may be mistaken for completion,
* origin may be lost inside later outputs.

---

## 11. Event Flow With Review

```text
reference_detected
  ↓
review_required
  ↓
human_review_completed
  ↓
value_signal_updated
  ↓
allocation_decision_created
```

The Review Layer acts as a gate between detection and allocation.

AI can help create the initial signal.

Human review stabilizes it.

---

## 12. Allocation and Return Flow

```text
allocation_decision_created
  ↓
allocation_decision_approved
  ↓
return_recorded
```

Allocation is not the same as return.

Allocation means:

```text
This value should return in this form.
```

Return means:

```text
This value actually returned.
```

---

## 13. Correction and Dispute Flow

Royalty OS v0.2 uses append-only correction and dispute events.

```text
event_created
  ↓
review_completed
  ↓
dispute_added
  ↓
correction_added
  ↓
value_signal_updated
```

The past is not silently erased.

It is corrected visibly.

This preserves integrity.

---

## 14. Layer-to-Schema Mapping

| Layer                 | Schema                                  |
| --------------------- | --------------------------------------- |
| Origin Layer          | `schemas/origin.schema.json`            |
| Trace Layer           | `schemas/trace.schema.json`             |
| Value Event Log Layer | `schemas/value-event.schema.json`       |
| Review Layer          | `schemas/review.schema.json`            |
| Allocation Layer      | `schemas/allocation.schema.json`        |
| Return History Layer  | `schemas/return.schema.json`            |
| Root Record           | `schemas/royalty-os-record.schema.json` |

---

## 15. Layer-to-Example Mapping

| Layer                 | Example                                     |
| --------------------- | ------------------------------------------- |
| Origin Layer          | `examples/origin-record.example.yaml`       |
| Trace Layer           | `examples/trace-record.example.yaml`        |
| Value Event Log Layer | `examples/value-event-log.example.yaml`     |
| Review Layer          | `examples/review-record.example.yaml`       |
| Allocation Layer      | `examples/allocation-decision.example.yaml` |
| Return History Layer  | `examples/return-record.example.yaml`       |

---

## 16. Visual Summary

```text
Human Origin
    │
    ▼
Trace Record
    │
    ▼
Value Event Log
    │
    ▼
Review Layer
    │
    ▼
Allocation Decision
    │
    ▼
Return Record
    │
    ▼
Return History
    │
    └───► Renewed Origin / New Trace
```

This final loop is what makes Royalty OS v0.2 a circulation model rather than a simple log system.

---

## 17. Design Philosophy

Royalty OS v0.2 follows this architectural philosophy:

```text
Preserve the origin.
Record the movement.
Review the signal.
Allocate the return.
Confirm the return.
Preserve the history.
```

The layers are not decorative.

They exist to prevent confusion between:

* origin and output,
* detection and judgment,
* signal and allocation,
* allocation and return,
* correction and erasure.

---

## 18. Summary

Royalty OS v0.2 is built as a layered architecture.

Its six layers are:

```text
Origin
Trace
Value Event Log
Review
Allocation
Return History
```

Each layer has a distinct responsibility.

Together, they create an event-based trace-to-value circulation system.

Royalty OS v0.1 preserved the origin.

Royalty OS v0.2 shows how value moves through layers and returns.

The wind has become an architecture.
