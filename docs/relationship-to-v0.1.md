# Relationship to Royalty OS v0.1

## Version

`v0.2.0-draft`

## Status

Draft / Version Relationship Document

---

## Purpose

This document defines the relationship between **Royalty OS v0.1** and **Royalty OS v0.2**.

Royalty OS v0.1 and v0.2 are closely related, but they serve different roles.

```text
Royalty OS v0.1
= static minimum recognition model

Royalty OS v0.2
= event-based value circulation architecture
```

The purpose of this document is to clarify:

* what v0.1 established,
* what v0.2 extends,
* what should remain stable,
* what may be experimental,
* and why v0.2 is developed as a separate repository.

---

## 1. Summary

Royalty OS v0.1 defines the minimum viable structure for connecting Trace Protocol to value circulation.

Royalty OS v0.2 extends this structure into an event-based model.

The relationship can be summarized as follows:

```text
v0.1 preserves the origin.
v0.2 records the movement of value.
```

v0.1 is the foundation.

v0.2 is the dynamic extension.

---

## 2. What v0.1 Established

Royalty OS v0.1 established the first static model of trace-to-value circulation.

Its core chain is:

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

v0.1 defined:

* origin records,
* trace records,
* reference events,
* value signals,
* allocation rules,
* return methods,
* non-monetary value circulation,
* YAML examples,
* JSON Schema validation,
* GitHub Actions validation,
* positioning documentation,
* comparison with adjacent fields.

v0.1 is intentionally minimal.

It is designed to be readable, understandable, and stable.

---

## 3. What v0.2 Adds

Royalty OS v0.2 extends v0.1 by introducing event-based value circulation.

Its core chain is:

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

v0.2 adds:

* append-only value event logs,
* modular schema architecture,
* AI-assisted reference detection,
* human review workflows,
* dynamic value signal updates,
* allocation decision records,
* return history records,
* correction events,
* dispute events,
* optional Q-Point integration,
* future preparation for dashboards and compensation systems.

v0.2 is more experimental than v0.1.

---

## 4. Why v0.2 Is Separate

Royalty OS v0.2 is developed separately to preserve the clarity of v0.1.

The reason is simple:

```text
v0.1 is a stable minimum core.
v0.2 is an experimental dynamic extension.
```

If v0.2 were developed inside the same repository without separation, the v0.1 structure could become harder to understand.

A separate repository allows:

* cleaner version boundaries,
* simpler file structure,
* safer experimentation,
* less schema complexity,
* clearer documentation,
* easier AI-assisted development,
* easier rollback,
* better conceptual separation.

This is especially important because v0.2 introduces significantly more moving parts.

---

## 5. Conceptual Difference

| Area            | Royalty OS v0.1                       | Royalty OS v0.2                  |
| --------------- | ------------------------------------- | -------------------------------- |
| Model           | Static record                         | Event-based log                  |
| Main purpose    | Minimum recognition structure         | Dynamic value circulation        |
| Core unit       | Royalty OS record                     | Value event                      |
| Value signal    | Mostly static                         | Evolves over time                |
| Review          | Simple flags                          | Dedicated Review Layer           |
| Allocation      | Static allocation rule                | Allocation decision events       |
| Return          | Return methods                        | Return history                   |
| Schema          | Single schema                         | Modular schemas                  |
| Repository role | Stable candidate foundation           | Experimental extension           |
| Complexity      | Low                                   | Medium to high                   |
| Best use        | Establishing origin-aware recognition | Tracking evolving value movement |

---

## 6. Data Model Difference

### v0.1 Static Record

Royalty OS v0.1 represents one value circulation record.

```yaml
royalty_os_version: "0.1"

origin:
  origin_id: "epicenter-network-001"

trace:
  trace_id: "trace-protocol-001"

reference_event:
  event_id: "ref-001"

value_signal:
  signal_type: "attribution"
  signal_strength: "high"

allocation:
  allocation_type: "non_monetary"
  return_methods:
    - "citation"
    - "linkback"

status: "draft"
```

This is simple and stable.

---

### v0.2 Event-Based Log

Royalty OS v0.2 represents value circulation as an evolving event history.

```yaml
royalty_os_version: "0.2"

value_event_log:
  log_id: "log-001"
  origin_id: "epicenter-network-001"
  trace_id: "trace-protocol-001"

  events:
    - event_id: "event-001"
      event_type: "origin_registered"
      event_time: "2026-06-04T00:00:00Z"
      status: "completed"

    - event_id: "event-002"
      event_type: "reference_detected"
      event_time: "2026-06-04T00:10:00Z"
      status: "pending_review"

    - event_id: "event-003"
      event_type: "human_review_completed"
      event_time: "2026-06-04T00:20:00Z"
      status: "approved"

    - event_id: "event-004"
      event_type: "return_recorded"
      event_time: "2026-06-04T00:30:00Z"
      status: "completed"
```

This is more flexible, but also more complex.

---

## 7. Stability Boundary

Royalty OS v0.1 should remain stable.

v0.1 should avoid adding:

* event logs,
* modular schemas,
* AI review logic,
* dynamic allocation,
* dispute handling,
* return history,
* scoring systems,
* compensation logic.

These belong to v0.2 or later.

Royalty OS v0.1 should remain focused on:

```text
Origin
Trace
Reference
Value Signal
Allocation
Return
```

This keeps v0.1 understandable and reusable.

---

## 8. Experimental Boundary

Royalty OS v0.2 may explore:

* event sourcing,
* review workflows,
* AI-assisted detection,
* modular schema composition,
* allocation decisions,
* return history,
* correction events,
* dispute events,
* scoring,
* Q-Point integration,
* future compensation logic.

However, v0.2 should avoid claiming full legal, financial, or institutional completeness.

v0.2 is an experimental architecture, not a finished royalty infrastructure.

---

## 9. Backward Compatibility

Royalty OS v0.2 should be conceptually compatible with v0.1.

A v0.1 record may be interpreted as a snapshot.

A v0.2 event log may be interpreted as a history.

Possible mapping:

| v0.1 Field        | v0.2 Equivalent                                        |
| ----------------- | ------------------------------------------------------ |
| `origin`          | `origin_registered` event or Origin Layer record       |
| `trace`           | `trace_created` event or Trace Layer record            |
| `reference_event` | `reference_detected` event                             |
| `value_signal`    | `value_signal_created` or `value_signal_updated` event |
| `allocation`      | `allocation_decision_created` event                    |
| `status`          | event-level and log-level status                       |
| `return_methods`  | allocation decision + return history                   |

v0.2 should preserve the conceptual logic of v0.1 while expanding its temporal structure.

---

## 10. Migration Concept

A v0.1 record can be converted into a v0.2 event log.

Example v0.1 record:

```text
Origin + Trace + Reference + Value Signal + Allocation
```

Possible v0.2 migration:

```text
origin_registered
  ↓
trace_created
  ↓
reference_detected
  ↓
value_signal_created
  ↓
allocation_decision_created
```

If a return has already been completed, add:

```text
return_recorded
```

This allows v0.1 records to become initial event histories in v0.2.

---

## 11. Governance Difference

Royalty OS v0.1 governance is simple.

It mainly requires:

* documentation consistency,
* schema validation,
* example validation,
* changelog updates,
* citation metadata.

Royalty OS v0.2 governance is more complex.

It may require:

* event type control,
* schema module consistency,
* event ordering rules,
* review status definitions,
* correction policies,
* dispute policies,
* allocation policy boundaries,
* return history validation.

Therefore, v0.2 should be developed carefully.

The event model is powerful, but it can become chaotic if event types and review rules are not disciplined.

---

## 12. Why v0.1 Should Not Be Overloaded

Royalty OS v0.1 is valuable because it is simple.

Its strength is that it defines a minimum structure:

```text
Who created the origin?
Where was it recorded?
Who referenced it?
What value signal was created?
How should recognition or return occur?
```

If too many experimental concepts are added to v0.1, this clarity may be lost.

Therefore:

```text
Do not overload v0.1.
Use v0.2 for dynamic experimentation.
```

This preserves both stability and innovation.

---

## 13. Why v0.2 Should Not Forget v0.1

Royalty OS v0.2 is more dynamic, but it should not lose the simplicity of v0.1.

Every v0.2 event should still serve the same core purpose:

```text
Make origin visible.
Preserve trace.
Record reference.
Evaluate value.
Support return.
```

If v0.2 becomes too complex to explain, it should return to the v0.1 chain.

The v0.1 chain is the compass.

The v0.2 event log is the map.

Both are necessary.

---

## 14. Recommended Development Policy

Royalty OS v0.2 should follow this policy:

```text
Keep v0.1 stable.
Use v0.2 for event-based experimentation.
Do not break the origin-trace-value chain.
Prefer append-only history over silent mutation.
Prefer human review for high-impact value decisions.
Avoid premature monetary automation.
Document every major conceptual expansion.
```

---

## 15. Repository Relationship

Recommended repository relationship:

```text
royalty-os-v0.1
= stable minimum candidate specification

royalty-os-v0.2
= experimental event-based extension
```

The v0.2 README should link back to v0.1 as its foundation.

The v0.1 README may include a note such as:

```text
Royalty OS v0.2 development is explored in a separate repository to preserve the stability and clarity of the v0.1 candidate specification.
```

---

## 16. Summary

Royalty OS v0.1 and v0.2 are not competing versions.

They are layered versions.

```text
v0.1 = core structure
v0.2 = event dynamics
```

v0.1 answers:

```text
What is the minimum structure for connecting trace to value circulation?
```

v0.2 answers:

```text
How does value circulation evolve over time as events, reviews, allocations, and returns?
```

Royalty OS v0.1 is the foundation stone.

Royalty OS v0.2 is the moving water.

The foundation should remain stable.

The water may flow.
