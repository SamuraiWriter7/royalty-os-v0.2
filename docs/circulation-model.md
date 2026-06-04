# Royalty OS v0.2 Circulation Model

## Version

`v0.2.0-draft`

## Status

Draft / Circulation Model Document

---

## Purpose

This document defines the **circulation model** of Royalty OS v0.2.

Royalty OS v0.2 extends the static recognition model of v0.1 into an event-based circulation architecture.

The purpose of this document is to show how value moves through the system:

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

This final return loop is important.

Royalty OS v0.2 is not only a record system.

It is a circulation system.

---

## 1. Core Circulation Principle

The core principle of the circulation model is:

```text
Value should not move in only one direction.
```

In a one-way extraction model, value flows like this:

```text
Human Origin
  ↓
AI / Platform
  ↓
Generated Output
  ↓
Platform Value
```

The origin may disappear.

The trace may weaken.

The value may not return.

Royalty OS v0.2 proposes a different model:

```text
Human Origin
  ↓
Trace
  ↓
Reference
  ↓
Review
  ↓
Allocation
  ↓
Return
  ↓
Renewed Origin
```

This changes value movement from extraction into circulation.

---

## 2. High-Level Circulation Diagram

```text
┌───────────────────────────────────────────────┐
│  1. Human Origin                               │
│  Question / Concept / Protocol / Work          │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  2. Trace Record                               │
│  Origin, lineage, core question, related ideas │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  3. Value Event Log                            │
│  References, citations, AI mentions, changes   │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  4. Review Layer                               │
│  AI may detect. Humans judge.                  │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  5. Dynamic Value Signal                       │
│  Influence, dependency, recognition strength   │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  6. Allocation Layer                           │
│  Decide appropriate return methods             │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  7. Return History                             │
│  Citation, linkback, attribution, recognition  │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│  8. Renewed Origin / New Trace                 │
│  Returned value supports future creation       │
└───────────────────────────────────────────────┘
```

The final stage is not the end.

It becomes the beginning of another cycle.

---

## 3. Linear Flow vs Circulation Flow

### Linear Flow

A linear model ends with output.

```text
Origin → Reference → Output
```

This is not enough for AI-era value circulation.

It records that something happened, but not whether value returned.

### Circulation Flow

A circulation model continues until return is recorded.

```text
Origin
  ↓
Trace
  ↓
Reference
  ↓
Review
  ↓
Allocation
  ↓
Return
  ↓
Renewal
```

This makes Royalty OS v0.2 an origin-aware circulation model rather than a simple attribution log.

---

## 4. Stage 1: Human Origin

The circulation begins with a human-originated source.

An origin may be:

* a question,
* a concept,
* an essay,
* a protocol,
* a specification,
* a technical design,
* a philosophical model,
* a creative work,
* an AI-assisted but human-originated structure.

The origin is the first vibration.

Without origin, there is nothing to trace.

Without trace, value return becomes ambiguous.

---

## 5. Stage 2: Trace Record

The Trace Record preserves the origin and lineage.

It records:

* origin ID,
* core question,
* related concepts,
* lineage,
* version,
* previous versions,
* derived concepts.

The Trace Record answers:

```text
Where did this thought begin?
What question generated it?
What lineage does it belong to?
```

This prevents the origin from being flattened into anonymous output.

---

## 6. Stage 3: Value Event Log

The Value Event Log records movement.

It may include:

* origin registration,
* trace creation,
* reference detection,
* citation events,
* linkback events,
* AI-assisted detections,
* human reviews,
* value signal updates,
* allocation decisions,
* return records,
* corrections,
* disputes.

The event log follows the append-only principle.

Existing events should not be silently rewritten.

Corrections and disputes should be added as new events.

---

## 7. Stage 4: Review Layer

The Review Layer evaluates events.

It separates detection from judgment.

Core principle:

```text
AI may detect.
Humans should judge.
The event log should preserve both.
```

AI may help detect:

* references,
* conceptual similarity,
* structural dependency,
* implementation dependency,
* derivatives,
* summaries,
* translations.

Human review evaluates:

* evidence,
* context,
* dependency depth,
* fairness,
* risk of overclaiming,
* appropriate value signal strength.

This prevents AI detection from becoming automatic truth.

---

## 8. Stage 5: Dynamic Value Signal

A value signal represents the strength or type of value created by a reference or dependency.

In v0.1, the value signal was mostly static.

In v0.2, it can evolve.

Example:

```text
reference_detected → signal_strength: low
human_review_completed → signal_strength: medium
derivative_work_registered → signal_strength: high
implementation_dependency_detected → signal_strength: critical
```

This allows influence to grow or weaken over time as new events appear.

---

## 9. Stage 6: Allocation Layer

The Allocation Layer determines what kind of return is appropriate.

It connects reviewed value signals to return methods.

Possible return methods include:

* citation,
* linkback,
* conceptual attribution,
* version lineage,
* repository reference,
* acknowledgement,
* collaboration offer,
* Q-Point allocation,
* future licensing request,
* future compensation.

In v0.2, non-monetary return is prioritized.

This keeps the system practical and avoids premature legal or financial complexity.

---

## 10. Stage 7: Return History

Return History records what actually returned.

This is important because intention and completion are different.

```text
Allocation Decision
= what should return

Return Record
= what actually returned
```

Examples of completed return:

* citation completed,
* linkback added,
* repository reference added,
* acknowledgement published,
* point allocation recorded,
* compensation recorded.

Return History makes value return visible.

---

## 11. Stage 8: Renewed Origin / New Trace

Returned value can support future creation.

Recognition may lead to:

* new readers,
* new collaborators,
* new citations,
* new questions,
* new specifications,
* new protocols,
* new origins.

This creates the circulation loop:

```text
Return
  ↓
Renewed Origin
  ↓
New Trace
  ↓
New Value Event Log
```

This is where Royalty OS becomes more than attribution.

It becomes a generative value circulation system.

---

## 12. Extraction Model vs Royalty OS Model

| Dimension      | Extraction Model     | Royalty OS v0.2               |
| -------------- | -------------------- | ----------------------------- |
| Origin         | Often hidden         | Explicitly recorded           |
| Trace          | Weak or missing      | Structured                    |
| AI role        | Absorbs and outputs  | Detects and assists           |
| Human role     | Source material      | Origin and reviewer           |
| Value movement | One-way              | Circular                      |
| Review         | Often absent         | Explicit layer                |
| Return         | Unclear              | Recorded                      |
| History        | Output-focused       | Event-based                   |
| Correction     | Often invisible      | Append-only correction events |
| Goal           | Efficient extraction | Origin-aware circulation      |

---

## 13. Circulation Event Example

A minimal circulation cycle may look like this:

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
  ↓
new_origin_registered
```

This final `new_origin_registered` event represents the next cycle.

Value return may become the seed of another origin.

---

## 14. Circulation and AI

Royalty OS v0.2 does not reject AI.

It assigns AI a specific role.

AI may:

* detect references,
* summarize evidence,
* identify possible lineage,
* suggest value signal strength,
* flag missing attribution,
* recommend review priority.

AI should not:

* erase the origin,
* silently absorb value,
* approve high-impact events alone,
* assign final allocation alone,
* settle disputes alone,
* rewrite event history.

AI is a carrier of circulation, not the owner of origin.

---

## 15. Circulation and Human Review

Human review is the stabilizing layer.

It ensures that value circulation does not become automatic overclaiming.

Human review is especially important for:

* conceptual dependency,
* structural dependency,
* implementation dependency,
* commercial use,
* high-value allocation,
* disputes,
* corrections.

The circulation model depends on judgment.

Without judgment, event logs become noise.

Without event logs, judgment has no memory.

Both are required.

---

## 16. Circulation and Non-Monetary Return

Royalty OS v0.2 begins with non-monetary return.

This includes:

* citation,
* linkback,
* conceptual attribution,
* repository reference,
* acknowledgement,
* version lineage.

This is intentional.

Non-monetary return is easier to implement immediately.

It creates visible origin recognition.

It prepares the foundation for future compensation.

In other words:

```text
Recognition comes first.
Evaluation comes next.
Compensation may come later.
```

---

## 17. Circulation and Future Compensation

Future versions may connect the circulation model to compensation mechanisms.

Possible extensions:

* Q-Point Protocol,
* creator dashboards,
* AI reference frequency tracking,
* signed event logs,
* licensing requests,
* revenue sharing,
* royalty payment records,
* token or point allocation.

However, v0.2 does not attempt to execute payments.

It records the architecture needed before payment can become meaningful.

---

## 18. Circulation Integrity

The circulation model should protect against:

* false attribution,
* overclaiming,
* AI misclassification,
* missing evidence,
* reviewer bias,
* allocation inflation,
* silent deletion,
* unrecorded corrections,
* value extraction without return.

Recommended safeguards:

* append-only logs,
* evidence fields,
* review statuses,
* confidence scores,
* correction events,
* dispute events,
* return records,
* human review for high-impact events.

---

## 19. Minimal Circulation Record

A minimal circulation record includes:

```text
origin
trace
value_event_log
review
allocation_decision
return_record
```

This corresponds to the current v0.2 example set:

```text
examples/origin-record.example.yaml
examples/trace-record.example.yaml
examples/value-event-log.example.yaml
examples/review-record.example.yaml
examples/allocation-decision.example.yaml
examples/return-record.example.yaml
```

Together, these files demonstrate one full circulation cycle.

---

## 20. Summary

Royalty OS v0.2 is not only a schema system.

It is a circulation model.

Its core flow is:

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

The key idea is simple:

```text
Value should return to the origin and become the seed of new creation.
```

Royalty OS v0.1 preserved the origin.

Royalty OS v0.2 records the movement of value.

The circulation model shows how the movement becomes a loop.

The wind has become a cycle.
