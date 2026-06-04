# Royalty OS v0.2 Event Model

## Version

`v0.2.0-draft`

## Status

Draft / Event Model Specification

---

## Purpose

This document defines the event model of **Royalty OS v0.2**.

Royalty OS v0.2 extends the static record model of v0.1 into an event-based architecture.

In v0.1, value circulation is represented as a single structured record:

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

In v0.2, value circulation is represented as an evolving sequence of events:

```text
origin_registered
  ↓
trace_created
  ↓
reference_detected
  ↓
review_completed
  ↓
value_signal_updated
  ↓
allocation_decision_created
  ↓
return_recorded
```

The purpose of the event model is to make value circulation traceable over time.

---

## 1. Core Idea

The core idea of the event model is:

```text
Every meaningful change in value circulation should be recorded as an event.
```

A value event is a structured record that describes:

* what happened,
* when it happened,
* who or what caused it,
* which origin or trace it relates to,
* what evidence supports it,
* whether AI was involved,
* whether human review is required,
* and how it affects value circulation.

This makes Royalty OS v0.2 suitable for evolving intellectual lineages, AI-mediated references, human review workflows, and dynamic return histories.

---

## 2. Event Log Principle

Royalty OS v0.2 uses an append-only event log.

This means:

* new events may be added,
* existing events should not be silently modified,
* corrections should be added as correction events,
* review changes should be recorded as new events,
* allocation updates should be recorded as new events,
* return completion should be recorded separately from allocation decisions.

This protects the historical integrity of value circulation.

---

## 3. Value Event Definition

A `value_event` is the smallest event unit in Royalty OS v0.2.

A value event records one meaningful occurrence in the trace-to-value circulation process.

Minimum event fields:

```text
event_id
event_type
event_time
origin_id
trace_id
actor
target
evidence
status
```

Recommended optional fields:

```text
value_signal
review
allocation_reference
return_reference
related_events
notes
```

---

## 4. Event Lifecycle

A typical event lifecycle may look like this:

```text
created
  ↓
pending_review
  ↓
reviewed
  ↓
approved / rejected / disputed
  ↓
value_signal_updated
  ↓
allocation_decision_created
  ↓
return_recorded
```

Not all events require every step.

For example, a simple `linkback_added` event may not require a deep review.

However, an `ai_reference_detected` or `structural_dependency_detected` event should normally require human review.

---

## 5. Event Types

Royalty OS v0.2 defines the following initial event types.

### Origin Events

```text
origin_registered
origin_updated
origin_deprecated
```

These events relate to the registration or update of an origin.

### Trace Events

```text
trace_created
trace_updated
trace_linked
trace_version_updated
```

These events relate to origin lineage and trace records.

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

These events relate to references, dependencies, derivatives, and transformations.

### AI-Related Events

```text
ai_reference_detected
ai_similarity_detected
ai_summary_detected
ai_derivative_detected
ai_assisted_review_created
```

These events involve AI-assisted detection or AI-mediated reuse.

### Review Events

```text
human_review_requested
human_review_completed
review_rejected
review_disputed
review_reopened
```

These events relate to human evaluation.

### Value Signal Events

```text
value_signal_created
value_signal_updated
value_signal_downgraded
value_signal_upgraded
value_signal_disputed
```

These events record changes in the perceived value or influence of a reference.

### Allocation Events

```text
allocation_decision_created
allocation_decision_updated
allocation_decision_approved
allocation_decision_rejected
allocation_decision_superseded
```

These events relate to how value should return to the origin.

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

These events record completed return or recognition.

### Correction Events

```text
correction_added
event_retracted
evidence_updated
status_updated
```

These events preserve integrity without silently rewriting history.

---

## 6. Event Status

Each event should have a status.

Recommended statuses:

```text
draft
pending
pending_review
approved
rejected
disputed
completed
superseded
retracted
archived
```

### Status Meaning

| Status           | Meaning                                                  |
| ---------------- | -------------------------------------------------------- |
| `draft`          | The event is being prepared.                             |
| `pending`        | The event exists but has not been reviewed or completed. |
| `pending_review` | The event requires human or AI-assisted review.          |
| `approved`       | The event has been approved.                             |
| `rejected`       | The event has been rejected.                             |
| `disputed`       | The event is contested.                                  |
| `completed`      | The event has been completed.                            |
| `superseded`     | The event has been replaced by a later event.            |
| `retracted`      | The event has been withdrawn.                            |
| `archived`       | The event is retained for history but no longer active.  |

---

## 7. Actor Model

Each event should identify an actor.

An actor may be:

```text
human
ai_system
repository
platform
organization
protocol
unknown
```

Example:

```yaml
actor:
  actor_type: "human"
  actor_id: "SamuraiWriter7"
  role: "originator"
```

AI-assisted events should explicitly identify AI involvement:

```yaml
actor:
  actor_type: "ai_system"
  actor_id: "ai-reference-detector-v0.1"
  role: "detector"
```

---

## 8. Target Model

The target describes the object or location affected by the event.

A target may be:

```text
article
repository
specification
protocol
essay
book
ai_output
dataset
web_page
social_post
unknown
```

Example:

```yaml
target:
  target_type: "article"
  title: "Royalty OS v0.2"
  url: "https://example.com/royalty-os-v0.2"
```

---

## 9. Evidence Model

Evidence supports the event.

Evidence may include:

```text
url
quote
repository_commit
citation
screenshot_reference
hash
doi
manual_note
ai_detection_report
unknown
```

Example:

```yaml
evidence:
  evidence_type: "url"
  url: "https://example.com/reference"
  description: "The article links to the original Trace Protocol document."
```

Evidence is important because Royalty OS should avoid unsupported attribution claims.

---

## 10. Value Signal Model

A value signal describes the type and strength of value created by an event.

Example:

```yaml
value_signal:
  signal_type: "conceptual_reference"
  signal_strength: "high"
  confidence: 0.85
```

Recommended signal types:

```text
citation
linkback
conceptual_reference
structural_dependency
implementation_dependency
translation
summary
derivative_work
commercial_use
educational_use
research_use
ai_reference
community_recognition
```

Recommended signal strengths:

```text
low
medium
high
critical
```

Confidence should use a number between `0` and `1`.

---

## 11. Review Model

The review model records whether an event has been evaluated.

Example:

```yaml
review:
  human_review_required: true
  ai_assisted: true
  status: "pending"
  reviewer: null
  notes: "AI detected a possible conceptual dependency. Human review is required."
```

Recommended review statuses:

```text
not_required
pending
approved
rejected
needs_more_evidence
disputed
```

AI detection should not be treated as final judgment.

A typical AI-assisted event should include:

```yaml
review:
  human_review_required: true
  ai_assisted: true
  status: "pending"
```

---

## 12. Allocation Linkage

A value event may later connect to an allocation decision.

Example:

```yaml
allocation_reference:
  allocation_id: "allocation-001"
  status: "proposed"
```

The allocation decision itself should be recorded separately.

This separation keeps the event log clean:

```text
reference_detected
  ↓
value_signal_updated
  ↓
allocation_decision_created
```

---

## 13. Return Linkage

A value event may also connect to a return record.

Example:

```yaml
return_reference:
  return_id: "return-001"
  return_type: "linkback"
  status: "completed"
```

Allocation defines what should return.

Return records what actually returned.

---

## 14. Related Events

Events may reference other events.

Example:

```yaml
related_events:
  - "event-001"
  - "event-002"
```

This allows Royalty OS to represent chains such as:

```text
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

## 15. Minimal Event Example

```yaml
royalty_os_version: "0.2"

event:
  event_id: "event-001"
  event_type: "reference_detected"
  event_time: "2026-06-04T00:00:00Z"
  origin_id: "epicenter-network-001"
  trace_id: "trace-protocol-001"
  status: "pending_review"

  actor:
    actor_type: "human"
    actor_id: "SamuraiWriter7"
    role: "originator"

  target:
    target_type: "article"
    title: "Royalty OS v0.2"
    url: "https://example.com/royalty-os-v0.2"

  evidence:
    evidence_type: "url"
    url: "https://example.com/reference"
    description: "The article references the Epicenter Network lineage."

  value_signal:
    signal_type: "conceptual_reference"
    signal_strength: "high"
    confidence: 0.85

  review:
    human_review_required: true
    ai_assisted: false
    status: "pending"

  related_events: []

  notes: "Initial reference event for the Royalty OS v0.2 lineage."
```

---

## 16. Event Log Example

A value event log may contain multiple events.

```yaml
royalty_os_version: "0.2"

value_event_log:
  log_id: "log-royalty-os-v0.2-001"
  origin_id: "epicenter-network-001"
  trace_id: "trace-protocol-001"

  events:
    - event_id: "event-001"
      event_type: "origin_registered"
      event_time: "2026-06-04T00:00:00Z"
      status: "completed"

    - event_id: "event-002"
      event_type: "trace_created"
      event_time: "2026-06-04T00:10:00Z"
      status: "completed"

    - event_id: "event-003"
      event_type: "reference_detected"
      event_time: "2026-06-04T00:20:00Z"
      status: "pending_review"

    - event_id: "event-004"
      event_type: "human_review_completed"
      event_time: "2026-06-04T00:30:00Z"
      status: "approved"

    - event_id: "event-005"
      event_type: "value_signal_updated"
      event_time: "2026-06-04T00:40:00Z"
      status: "completed"

    - event_id: "event-006"
      event_type: "allocation_decision_created"
      event_time: "2026-06-04T00:50:00Z"
      status: "proposed"

    - event_id: "event-007"
      event_type: "return_recorded"
      event_time: "2026-06-04T01:00:00Z"
      status: "completed"
```

---

## 17. Event Ordering

Events should be ordered by `event_time`.

If two events occur at the same time, ordering may be determined by:

```text
event_index
event_id
created_at
log_order
```

Future schemas may include an explicit `event_index`.

---

## 18. Correction Model

Events should not be silently edited.

If an event is incorrect, add a correction event.

Example:

```yaml
event:
  event_id: "event-008"
  event_type: "correction_added"
  event_time: "2026-06-04T02:00:00Z"
  status: "completed"

  correction:
    corrected_event_id: "event-003"
    correction_reason: "The reference depth was initially overestimated."
    corrected_field: "value_signal.signal_strength"
    previous_value: "high"
    new_value: "medium"
```

This preserves transparency.

The past is not erased.

It is corrected with a visible trace.

---

## 19. Dispute Model

An event may be disputed.

Example:

```yaml
event:
  event_id: "event-009"
  event_type: "review_disputed"
  event_time: "2026-06-04T03:00:00Z"
  status: "disputed"

  dispute:
    disputed_event_id: "event-003"
    dispute_reason: "Insufficient evidence for structural dependency."
    raised_by: "reviewer-001"
```

Disputes should not delete events.

They should create new events in the log.

---

## 20. Integrity Considerations

The event model should protect against:

* false attribution,
* overclaiming,
* AI misclassification,
* unsupported value signals,
* silent event editing,
* reviewer bias,
* inflated signal strength,
* missing evidence.

Recommended mitigations:

* evidence fields,
* human review,
* confidence scores,
* correction events,
* dispute events,
* append-only logs,
* signed records in future versions,
* timestamping in future versions.

---

## 21. Non-Goals

The v0.2 event model does not provide:

* legal enforcement,
* automatic royalty payment,
* full AI training data tracking,
* court-admissible ownership proof,
* guaranteed attribution detection,
* universal compensation rules.

It only defines a structured event model for value circulation.

---

## 22. Summary

The Royalty OS v0.2 event model turns value circulation into an evolving record.

Its core unit is the `value_event`.

Its core structure is the `value_event_log`.

Its core rule is:

```text
Do not silently overwrite value history.
Record events.
Review events.
Correct events with new events.
Return value visibly.
```

Royalty OS v0.1 defined the first static recognition structure.

Royalty OS v0.2 records the movement of value through time.
