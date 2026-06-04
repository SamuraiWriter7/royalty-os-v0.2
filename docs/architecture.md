# Royalty OS v0.2 Architecture

## Version

`v0.2.0-draft`

## Status

Draft / Experimental Architecture

---

## Purpose

This document defines the architecture of **Royalty OS v0.2**.

Royalty OS v0.2 extends the static trace-to-value model of Royalty OS v0.1 into an event-based architecture.

The goal of v0.2 is to represent value circulation as a living, evolving process rather than a single static record.

Royalty OS v0.1 defined the minimum structure:

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

Royalty OS v0.2 extends this into:

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

## 1. Architectural Position

Royalty OS v0.2 is not a replacement for v0.1.

It is an experimental extension.

```text
Royalty OS v0.1
= static minimum recognition record

Royalty OS v0.2
= event-based value circulation architecture
```

v0.1 preserves the core chain.

v0.2 records how that chain evolves over time.

---

## 2. Core Architectural Idea

The central idea of Royalty OS v0.2 is:

```text
Value circulation should be recorded as an append-only event history.
```

In v0.1, a value circulation record describes a state.

In v0.2, value circulation is represented as a sequence of events.

For example:

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

This makes Royalty OS v0.2 closer to an evolving ledger of recognition, review, and return.

---

## 3. High-Level Architecture

Royalty OS v0.2 contains six major layers.

```text
┌─────────────────────────────────────┐
│  6. Return History Layer             │
├─────────────────────────────────────┤
│  5. Allocation Layer                 │
├─────────────────────────────────────┤
│  4. Review Layer                     │
├─────────────────────────────────────┤
│  3. Value Event Log                  │
├─────────────────────────────────────┤
│  2. Trace Layer                      │
├─────────────────────────────────────┤
│  1. Origin Layer                     │
└─────────────────────────────────────┘
```

Each layer has a clear responsibility.

---

## 4. Layer 1: Origin Layer

The Origin Layer records the human-originated source.

An origin may be:

* a question,
* a concept,
* an essay,
* a protocol,
* a specification,
* a philosophical model,
* a technical design,
* a creative work,
* a research note,
* an AI-assisted but human-originated structure.

The origin is the first anchor of value circulation.

Without an origin, there is no trace.

Without trace, there is no reliable value circulation.

Minimum fields:

```text
origin_id
origin_type
title
creator
first_published
primary_url
```

---

## 5. Layer 2: Trace Layer

The Trace Layer records the origin and its lineage.

It answers:

```text
Where did this thought begin?
What question created it?
What concepts are related to it?
What earlier or later structures are connected?
```

Minimum fields:

```text
trace_id
origin_id
core_question
related_concepts
lineage
version
```

The Trace Layer is inherited from Trace Protocol.

Royalty OS v0.2 does not replace Trace Protocol.

It uses Trace Protocol as its memory foundation.

---

## 6. Layer 3: Value Event Log

The Value Event Log is the central architectural addition in v0.2.

It records events over time.

Each event represents a meaningful action or change in the value circulation process.

Example event types:

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

The event log should be append-only.

Existing events should not be silently rewritten.

If a correction is required, a new correction event should be added.

This preserves historical integrity.

---

## 7. Layer 4: Review Layer

The Review Layer evaluates events.

Royalty OS v0.2 assumes that AI can help detect possible references, but human judgment remains important.

The Review Layer may include:

* AI-assisted detection,
* human review,
* confidence scoring,
* evidence review,
* dispute flags,
* review status,
* provenance notes.

Possible review statuses:

```text
pending
approved
rejected
needs_more_evidence
disputed
```

The Review Layer prevents automatic AI detection from becoming automatic truth.

AI may detect.

Humans may judge.

---

## 8. Layer 5: Allocation Layer

The Allocation Layer determines how value may return to the origin.

In v0.2, allocation is not necessarily final or monetary.

It may include:

* citation,
* linkback,
* conceptual attribution,
* repository reference,
* acknowledgement,
* collaboration offer,
* point allocation,
* future compensation request.

The Allocation Layer uses value events and review results to create allocation decisions.

Example allocation types:

```text
non_monetary
monetary
hybrid
experimental
```

In v0.2, allocation decisions should also be recorded as events.

---

## 9. Layer 6: Return History Layer

The Return History Layer records what was actually returned to the origin.

This may include:

* citation completed,
* linkback added,
* credit added,
* repository reference added,
* acknowledgement published,
* point allocation recorded,
* royalty payment recorded,
* collaboration initiated.

The Return History Layer answers:

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

## 10. Core Data Flow

The standard flow is:

```text
1. Register origin
2. Create trace record
3. Detect reference
4. Add value event
5. Review event
6. Update value signal
7. Create allocation decision
8. Record return
```

Expanded form:

```text
Origin
  ↓
Trace Record
  ↓
Reference Detected
  ↓
Value Event Created
  ↓
AI / Human Review
  ↓
Value Signal Updated
  ↓
Allocation Decision
  ↓
Return Recorded
  ↓
Return History Updated
```

---

## 11. Event Record Structure

A minimal event record may look like this:

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

This structure allows Royalty OS to represent not only static attribution, but the process of value circulation.

---

## 12. Modular Schema Architecture

Royalty OS v0.2 should use modular schemas.

Recommended schema modules:

```text
schemas/origin.schema.json
schemas/trace.schema.json
schemas/value-event.schema.json
schemas/review.schema.json
schemas/allocation.schema.json
schemas/return.schema.json
schemas/royalty-os-record.schema.json
```

Each schema should validate one architectural layer.

The root schema should combine them.

This modular approach improves maintainability and reduces schema complexity.

---

## 13. Append-Only Principle

The Value Event Log should follow the append-only principle.

This means:

* new events may be added,
* existing events should not be silently edited,
* corrections should be recorded as new events,
* review changes should be recorded as new review events,
* return updates should be recorded as new return events.

Example:

```text
reference_detected
human_review_completed
value_signal_updated
correction_added
value_signal_updated
return_recorded
```

The append-only principle protects the historical integrity of value circulation.

---

## 14. AI-Assisted Detection

Royalty OS v0.2 may allow AI-assisted detection of references or conceptual dependencies.

Possible AI-assisted tasks:

* detecting citations,
* detecting linkbacks,
* detecting conceptual similarity,
* detecting derivative works,
* detecting implementation dependency,
* suggesting value signal strength,
* suggesting review priority,
* summarizing evidence.

However, AI-assisted detection should not be treated as final authority.

AI output should be marked as:

```text
ai_assisted: true
human_review_required: true
```

This preserves the distinction between detection and judgment.

---

## 15. Human Review

Human review remains a critical layer.

Human reviewers may evaluate:

* whether a reference is meaningful,
* whether the dependency is shallow or deep,
* whether evidence is sufficient,
* whether attribution is appropriate,
* whether a value signal is overestimated,
* whether an allocation decision is justified.

Possible review outcomes:

```text
approved
rejected
needs_more_evidence
disputed
```

This prevents Royalty OS from becoming a fully automated attribution machine.

---

## 16. Value Signal Evolution

In v0.1, value signal is mostly static.

In v0.2, value signal can evolve.

For example:

```text
reference_detected → signal_strength: low
human_review_completed → signal_strength: medium
derivative_work_registered → signal_strength: high
implementation_dependency_detected → signal_strength: critical
```

This allows value to grow over time as influence becomes clearer.

---

## 17. Allocation Decision

An allocation decision determines how value should return.

Example allocation decision:

```yaml
allocation_decision:
  allocation_id: "allocation-001"
  based_on_events:
    - "event-001"
    - "event-002"
  allocation_type: "non_monetary"
  return_methods:
    - "citation"
    - "linkback"
    - "conceptual_attribution"
  status: "proposed"
```

Possible statuses:

```text
proposed
approved
rejected
completed
superseded
```

---

## 18. Return History

Return History records completed value returns.

Example return record:

```yaml
return_record:
  return_id: "return-001"
  allocation_id: "allocation-001"
  return_type: "linkback"
  recipient: "SamuraiWriter7"
  completed_at: "2026-06-04T00:00:00Z"
  evidence_url: "https://example.com/article-with-linkback"
  status: "completed"
```

Return History is important because it proves that recognition or return actually happened.

---

## 19. Relationship to Q-Point Protocol

Royalty OS v0.2 may integrate with Q-Point Protocol in future versions.

Possible connections:

* value signal scoring,
* question origin scoring,
* conceptual depth assessment,
* influence measurement,
* resonance score,
* review weighting,
* allocation priority.

However, v0.2 should not depend on Q-Point Protocol at the base layer.

Q-Point integration should remain optional.

---

## 20. Security and Integrity Considerations

Royalty OS v0.2 should consider the following risks:

### False Attribution

A reference event may incorrectly claim dependency.

### Overclaiming

An origin may claim influence without sufficient evidence.

### AI Misclassification

AI may detect similarity where no meaningful dependency exists.

### Event Tampering

Historical events may be altered if append-only integrity is not preserved.

### Value Inflation

Signal strength may be exaggerated.

### Reviewer Bias

Human reviewers may approve or reject events unfairly.

Mitigations may include:

* evidence fields,
* review status,
* confidence scores,
* human review,
* correction events,
* signed records,
* timestamping,
* public logs,
* dispute flags.

---

## 21. Non-Goals

Royalty OS v0.2 does not attempt to provide:

* legal enforcement,
* court-admissible ownership proof,
* automatic payments,
* universal AI training data tracking,
* complete copyright protection,
* full monetization infrastructure,
* mandatory blockchain storage.

v0.2 is an experimental event architecture.

Its goal is to model the movement of value, not to enforce all consequences.

---

## 22. Summary

Royalty OS v0.2 transforms Royalty OS from a static recognition model into an event-based value circulation architecture.

It introduces:

* value event logs,
* modular schema layers,
* AI-assisted detection,
* human review,
* dynamic value signals,
* allocation decisions,
* return history.

Its core principle is:

```text
Value circulation should be recorded as an evolving event history.
```

Royalty OS v0.1 preserved the origin.

Royalty OS v0.2 records the movement of value.

The wind has become a log.
