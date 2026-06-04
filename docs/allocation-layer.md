# Royalty OS v0.2 Allocation Layer

## Version

`v0.2.0-draft`

## Status

Draft / Allocation Layer Specification

---

## Purpose

This document defines the **Allocation Layer** of Royalty OS v0.2.

Royalty OS v0.2 represents value circulation as an evolving event history.

The Allocation Layer determines how reviewed value events should be connected to return or recognition.

Its core purpose is to answer:

```text
What kind of value should return to the origin?
Why should it return?
How should it return?
When has it actually returned?
```

The Allocation Layer does not automatically execute payment.

It defines allocation decisions that may lead to non-monetary recognition, future compensation, or other forms of value return.

---

## 1. Role of the Allocation Layer

The Allocation Layer sits between the Review Layer and the Return History Layer.

```text
Value Event Log
  ↓
Review Layer
  ↓
Allocation Layer
  ↓
Return History Layer
```

The Review Layer decides whether an event is meaningful and valid.

The Allocation Layer decides what form of return is appropriate.

The Return History Layer records what actually happened.

---

## 2. Core Allocation Principle

The Allocation Layer follows this principle:

```text
Reviewed value signals may produce allocation decisions.
Allocation decisions may produce return records.
```

This separates three different concepts:

```text
Value Signal
= evidence of value or influence

Allocation Decision
= proposed or approved return method

Return Record
= completed return or recognition
```

This separation is important.

A value signal does not automatically mean return has occurred.

An allocation decision does not automatically mean return has been completed.

Only a return record confirms completion.

---

## 3. Why Allocation Is Necessary

In Royalty OS v0.1, value return was represented as a static list of return methods.

In v0.2, value may evolve over time.

For example:

```text
A citation is added.
A human review approves it.
The value signal becomes medium.
A derivative work is later registered.
The value signal becomes high.
An allocation decision proposes linkback and conceptual attribution.
A return record confirms that the linkback was added.
```

This requires a dedicated allocation structure.

Without the Allocation Layer, Royalty OS cannot distinguish between:

* detected value,
* reviewed value,
* proposed return,
* approved return,
* completed return.

---

## 4. Allocation Decision

An `allocation_decision` records how value should return to an origin.

Minimum fields:

```text
allocation_id
based_on_events
origin_id
trace_id
allocation_type
return_methods
allocation_status
created_at
```

Recommended optional fields:

```text
allocation_policy
recipient
allocation_reason
priority
review_reference
value_signal_reference
expected_return
notes
```

---

## 5. Minimal Allocation Example

```yaml
royalty_os_version: "0.2"

allocation_decision:
  allocation_id: "allocation-001"
  based_on_events:
    - "event-003"
    - "review-001"
    - "value-signal-001"

  origin_id: "epicenter-network-001"
  trace_id: "trace-protocol-001"

  allocation_type: "non_monetary"
  return_methods:
    - "citation"
    - "linkback"
    - "conceptual_attribution"

  allocation_status: "proposed"
  created_at: "2026-06-04T02:00:00Z"

  recipient:
    recipient_type: "human"
    recipient_id: "SamuraiWriter7"

  allocation_reason: >
    The reviewed event confirms a direct conceptual reference
    to the Epicenter Network and Trace Protocol lineage.

  priority: "medium"

  notes: "Initial non-monetary allocation decision for visible origin recognition."
```

---

## 6. Allocation Types

Royalty OS v0.2 defines the following allocation types:

```text
non_monetary
monetary
hybrid
experimental
```

### 6.1 Non-Monetary Allocation

Non-monetary allocation is the default in v0.2.

Examples:

* citation,
* linkback,
* credit,
* conceptual attribution,
* version lineage,
* repository reference,
* acknowledgement,
* collaboration offer.

### 6.2 Monetary Allocation

Monetary allocation may include:

* direct payment,
* royalty payment,
* licensing fee,
* revenue sharing,
* subscription revenue allocation.

This remains a future-oriented extension.

### 6.3 Hybrid Allocation

Hybrid allocation combines non-monetary and monetary return.

Example:

```text
citation + linkback + licensing request
```

### 6.4 Experimental Allocation

Experimental allocation may include:

* Q-Point allocation,
* token reward,
* reputation score,
* resonance score,
* community recognition point,
* future AI usage-based compensation.

---

## 7. Return Methods

Recommended return methods include:

```text
citation
linkback
credit
conceptual_attribution
version_lineage
repository_reference
acknowledgement
collaboration_offer
licensing_request
financial_compensation
royalty_payment
point_allocation
token_reward
q_point_allocation
resonance_score_update
```

In v0.2, non-monetary return methods should be prioritized.

This keeps the system practical and avoids premature legal or financial complexity.

---

## 8. Allocation Status

Allocation decisions should have a status.

Recommended statuses:

```text
draft
proposed
pending_review
approved
rejected
completed
superseded
disputed
archived
```

| Status           | Meaning                                                    |
| ---------------- | ---------------------------------------------------------- |
| `draft`          | The allocation is being prepared.                          |
| `proposed`       | The allocation has been proposed but not approved.         |
| `pending_review` | The allocation requires additional review.                 |
| `approved`       | The allocation has been approved.                          |
| `rejected`       | The allocation has been rejected.                          |
| `completed`      | The allocation has been fulfilled through a return record. |
| `superseded`     | The allocation has been replaced by a later decision.      |
| `disputed`       | The allocation is contested.                               |
| `archived`       | The allocation is retained for historical reference.       |

---

## 9. Allocation Policy

An allocation policy defines how allocation decisions should be made.

Example policies:

```text
origin_recognition_first
review_required_before_allocation
non_monetary_first
human_review_required_for_high_value
manual_approval_required
q_point_assisted
experimental_dynamic_allocation
```

### Example

```yaml
allocation_policy:
  policy_id: "origin-recognition-first"
  policy_type: "non_monetary_first"
  description: >
    Prioritize citation, linkback, conceptual attribution,
    and version lineage before monetary compensation.
```

---

## 10. Relationship to Value Signals

Allocation decisions should normally be based on reviewed value signals.

Example flow:

```text
reference_detected
  ↓
human_review_completed
  ↓
value_signal_updated
  ↓
allocation_decision_created
```

Possible value signal strengths:

```text
low
medium
high
critical
```

Suggested allocation behavior:

| Signal Strength | Suggested Allocation                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------- |
| `low`           | Optional citation or note                                                                          |
| `medium`        | Citation, linkback, attribution                                                                    |
| `high`          | Citation, linkback, conceptual attribution, repository reference                                   |
| `critical`      | Full attribution, repository reference, acknowledgement, possible licensing or compensation review |

This table is only a guideline.

It should not be treated as automatic enforcement.

---

## 11. Relationship to Review Layer

The Allocation Layer should respect the Review Layer.

High-impact allocation decisions should require approved reviews.

Examples of high-impact allocations:

* monetary allocation,
* licensing request,
* royalty payment,
* token reward,
* critical conceptual dependency,
* commercial use,
* implementation dependency.

Recommended rule:

```text
If allocation impact is high, human review should be required.
```

---

## 12. Relationship to Return History

The Allocation Layer proposes or approves return.

The Return History Layer records completion.

Example:

```text
allocation_decision_created
  ↓
allocation_decision_approved
  ↓
return_recorded
```

Allocation Decision:

```yaml
allocation_status: "approved"
return_methods:
  - "citation"
  - "linkback"
```

Return Record:

```yaml
return_record:
  return_id: "return-001"
  allocation_id: "allocation-001"
  return_type: "linkback"
  completed_at: "2026-06-04T03:00:00Z"
  evidence_url: "https://example.com/article-with-linkback"
  status: "completed"
```

The return record confirms that value actually returned.

---

## 13. Allocation Events

Allocation decisions should also be recorded as events.

Recommended allocation event types:

```text
allocation_decision_created
allocation_decision_updated
allocation_decision_approved
allocation_decision_rejected
allocation_decision_superseded
allocation_decision_disputed
allocation_decision_completed
```

Example:

```yaml
event:
  event_id: "event-allocation-001"
  event_type: "allocation_decision_created"
  event_time: "2026-06-04T02:00:00Z"
  origin_id: "epicenter-network-001"
  trace_id: "trace-protocol-001"
  status: "proposed"

  allocation_reference:
    allocation_id: "allocation-001"
```

---

## 14. Allocation Priority

Allocation decisions may include priority.

Recommended priority values:

```text
low
medium
high
critical
```

Priority may be based on:

* value signal strength,
* review confidence,
* reference depth,
* commercial impact,
* implementation dependency,
* community importance,
* time sensitivity,
* dispute risk.

Priority should guide attention.

It should not automatically determine compensation.

---

## 15. Allocation Recipient

Allocation should identify the recipient.

A recipient may be:

```text
human
organization
repository
project
protocol
collective
unknown
```

Example:

```yaml
recipient:
  recipient_type: "human"
  recipient_id: "SamuraiWriter7"
  recipient_role: "originator"
```

In future versions, recipients may include multiple parties.

---

## 16. Multi-Recipient Allocation

Some origins may involve multiple contributors.

Example:

```yaml
recipients:
  - recipient_type: "human"
    recipient_id: "originator-001"
    allocation_share: 0.7

  - recipient_type: "human"
    recipient_id: "contributor-001"
    allocation_share: 0.3
```

In v0.2, multi-recipient allocation is experimental.

It should be used carefully and should normally require human review.

---

## 17. Allocation Ratio

Allocation ratios may be used in future compensation systems.

Example:

```yaml
allocation_ratio: 0.25
```

However, in v0.2, allocation ratios should be optional.

For non-monetary returns, ratio may be set to `null`.

Example:

```yaml
allocation_ratio: null
```

---

## 18. Allocation and Q-Point Protocol

Royalty OS v0.2 may later integrate with Q-Point Protocol.

Possible use cases:

* scoring question depth,
* ranking conceptual influence,
* weighting allocation priority,
* identifying high-value origins,
* supporting non-monetary point allocation,
* informing future compensation models.

However, Q-Point integration should remain optional.

Royalty OS v0.2 should not depend on Q-Point Protocol at the base layer.

---

## 19. Allocation Integrity Risks

The Allocation Layer should guard against:

### Over-Allocation

Assigning too much value return to weak references.

### Under-Allocation

Failing to recognize meaningful references.

### Origin Bias

Originators may overestimate the value of their own work.

### Reviewer Bias

Reviewers may unfairly approve or reject allocation.

### AI Overconfidence

AI may suggest allocation based on weak or shallow similarity.

### Compensation Prematurity

Monetary return may be introduced before legal or institutional foundations are ready.

### Allocation Drift

Allocation criteria may change over time without clear records.

---

## 20. Mitigation Strategies

Recommended mitigation strategies include:

* reviewed value signals,
* explicit evidence fields,
* confidence scores,
* human review for high-impact allocation,
* allocation status tracking,
* dispute events,
* correction events,
* append-only allocation history,
* non-monetary-first policy,
* clear non-goals,
* optional rather than mandatory compensation logic.

---

## 21. Non-Goals

The Allocation Layer does not provide:

* automatic payment execution,
* legal royalty enforcement,
* final ownership decisions,
* court-admissible proof,
* universal licensing rules,
* mandatory monetary compensation,
* automatic AI-generated allocation approval.

The Allocation Layer defines how reviewed value signals may be connected to proposed or approved return methods.

---

## 22. Summary

The Allocation Layer is the decision layer of Royalty OS v0.2.

It connects reviewed value signals to return methods.

Its core chain is:

```text
Reviewed Event
  ↓
Value Signal
  ↓
Allocation Decision
  ↓
Return Record
```

Its core principle is:

```text
Do not confuse detected value with completed return.
```

Royalty OS v0.2 uses the Allocation Layer to transform traceable influence into visible, reviewable, and eventually returnable value.

The flow of knowledge should remain open.

The origin should remain visible.

The value should know where to return.
