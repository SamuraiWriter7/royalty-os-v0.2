# Royalty OS v0.2 Review Layer

## Version

`v0.2.0-draft`

## Status

Draft / Review Layer Specification

---

## Purpose

This document defines the **Review Layer** of Royalty OS v0.2.

Royalty OS v0.2 introduces an event-based value circulation architecture.

In this architecture, references, citations, AI detections, derivatives, value signals, allocation decisions, and returns are recorded as events.

However, not all events should be automatically trusted.

The Review Layer exists to evaluate whether a value event is meaningful, valid, supported by evidence, and appropriate for value circulation.

Its core principle is:

```text
AI may detect.
Humans should judge.
The event log should preserve both.
```

---

## 1. Role of the Review Layer

The Review Layer evaluates value events before they influence allocation or return.

It is responsible for determining:

* whether a reference is meaningful,
* whether evidence is sufficient,
* whether an AI-detected relationship is valid,
* whether a value signal is too weak or too strong,
* whether a dependency is shallow or deep,
* whether attribution is appropriate,
* whether human review is required,
* whether an event should be approved, rejected, disputed, or corrected.

The Review Layer does not erase events.

It adds review events to the Value Event Log.

---

## 2. Why Review Is Necessary

Royalty OS v0.2 may include AI-assisted reference detection.

AI can help identify:

* citations,
* linkbacks,
* conceptual similarity,
* structural dependency,
* implementation dependency,
* derivative works,
* summaries,
* translations,
* AI-mediated reuse.

However, AI detection is not final judgment.

AI may:

* overestimate similarity,
* miss context,
* confuse common concepts with true dependency,
* mistake coincidence for influence,
* fail to understand conceptual lineage,
* generate false positives,
* generate false negatives.

Therefore, review is necessary.

The Review Layer prevents Royalty OS from becoming an automatic overclaiming machine.

---

## 3. Core Review Principle

The Review Layer follows three principles.

```text
Detection is not judgment.
Judgment should be recorded.
Disagreement should remain visible.
```

### 3.1 Detection Is Not Judgment

An event such as `ai_reference_detected` means only that AI detected a possible relationship.

It does not mean that the relationship is confirmed.

### 3.2 Judgment Should Be Recorded

When a human reviewer evaluates an event, the judgment should be added to the event log.

The original event should not be silently modified.

### 3.3 Disagreement Should Remain Visible

If a review is disputed, the dispute should be recorded as a new event.

The system should preserve disagreement rather than hide it.

---

## 4. Review Statuses

Royalty OS v0.2 defines the following review statuses.

```text
not_required
pending
approved
rejected
needs_more_evidence
disputed
superseded
archived
```

| Status                | Meaning                                                  |
| --------------------- | -------------------------------------------------------- |
| `not_required`        | The event does not require review.                       |
| `pending`             | Review has not yet been completed.                       |
| `approved`            | The event has been reviewed and accepted.                |
| `rejected`            | The event has been reviewed and rejected.                |
| `needs_more_evidence` | The event may be valid, but evidence is insufficient.    |
| `disputed`            | The event or review result is contested.                 |
| `superseded`          | The review has been replaced by a later review.          |
| `archived`            | The review is retained for history but no longer active. |

---

## 5. Review Requirement Levels

Not all events require the same level of review.

Royalty OS v0.2 defines four review requirement levels.

```text
none
optional
recommended
required
```

| Level         | Meaning                                               |
| ------------- | ----------------------------------------------------- |
| `none`        | Review is not required.                               |
| `optional`    | Review may be useful but is not necessary.            |
| `recommended` | Review is strongly recommended before allocation.     |
| `required`    | Review is required before value allocation or return. |

---

## 6. Events That Usually Require Review

The following event types should normally require human review:

```text
ai_reference_detected
ai_similarity_detected
ai_derivative_detected
conceptual_reference_detected
structural_dependency_detected
implementation_dependency_detected
derivative_work_registered
commercial_reference_detected
value_signal_upgraded
allocation_decision_created
compensation_recorded
```

These event types may influence value circulation significantly, so automatic approval should be avoided.

---

## 7. Events That May Not Require Review

The following event types may not require review if evidence is clear:

```text
citation_added
linkback_added
repository_reference_completed
acknowledgement_completed
origin_registered
trace_created
version_updated
```

However, review may still be requested if the event is disputed or evidence is unclear.

---

## 8. Review Record Structure

A review record should capture the result of evaluating a value event.

Minimum fields:

```text
review_id
reviewed_event_id
review_time
reviewer
review_status
review_decision
evidence_assessment
confidence
```

Recommended optional fields:

```text
review_notes
recommended_signal_strength
recommended_allocation
dispute_allowed
related_reviews
```

---

## 9. Minimal Review Example

```yaml
royalty_os_version: "0.2"

review:
  review_id: "review-001"
  reviewed_event_id: "event-003"
  review_time: "2026-06-04T01:00:00Z"

  reviewer:
    reviewer_type: "human"
    reviewer_id: "SamuraiWriter7"
    role: "originator"

  review_status: "approved"
  review_decision: "valid_conceptual_reference"

  evidence_assessment:
    evidence_sufficient: true
    evidence_quality: "high"
    evidence_notes: "The article explicitly references the Epicenter Network lineage."

  confidence: 0.9

  recommended_signal_strength: "high"
  recommended_allocation:
    allocation_type: "non_monetary"
    return_methods:
      - "citation"
      - "linkback"
      - "conceptual_attribution"

  review_notes: "The reference is conceptually direct and should be recorded as high value."
```

---

## 10. AI-Assisted Review

AI may assist in the review process.

AI-assisted review may be used for:

* summarizing evidence,
* detecting conceptual similarity,
* identifying missing attribution,
* classifying reference depth,
* suggesting signal strength,
* identifying related events,
* flagging possible disputes,
* recommending human review priority.

However, AI-assisted review should be marked clearly.

Example:

```yaml
review:
  review_id: "review-ai-001"
  reviewed_event_id: "event-003"
  review_time: "2026-06-04T01:00:00Z"

  reviewer:
    reviewer_type: "ai_system"
    reviewer_id: "ai-review-agent-v0.1"
    role: "assistant_reviewer"

  review_status: "pending"
  review_decision: "possible_conceptual_reference"

  ai_assisted: true
  human_review_required: true

  confidence: 0.72

  review_notes: "AI detected conceptual similarity. Human review is required before allocation."
```

---

## 11. Human Review

Human review is required when:

* AI confidence is low,
* conceptual dependency is ambiguous,
* allocation may be affected,
* compensation may be triggered,
* a dispute exists,
* evidence is incomplete,
* a high or critical value signal is proposed.

Human review should evaluate:

* context,
* evidence,
* reference depth,
* conceptual dependency,
* originality,
* fairness,
* risk of overclaiming,
* appropriate return methods.

Human review is not perfect, but it provides contextual judgment that AI detection alone cannot provide.

---

## 12. Review Decisions

Recommended review decisions include:

```text
valid_reference
valid_conceptual_reference
valid_structural_dependency
valid_implementation_dependency
valid_derivative_work
insufficient_evidence
not_meaningful_reference
false_positive
overclaimed_dependency
requires_correction
requires_dispute_resolution
```

These decisions help separate detection from evaluation.

---

## 13. Evidence Assessment

Review should include an evidence assessment.

Recommended evidence fields:

```text
evidence_sufficient
evidence_quality
evidence_type
evidence_url
evidence_notes
```

Recommended evidence quality values:

```text
low
medium
high
critical
```

Example:

```yaml
evidence_assessment:
  evidence_sufficient: true
  evidence_quality: "medium"
  evidence_type: "url"
  evidence_url: "https://example.com/reference"
  evidence_notes: "The reference is visible, but the dependency depth is moderate."
```

---

## 14. Confidence Score

Review records may include a confidence score.

The confidence score should be between `0` and `1`.

```text
0.0 = no confidence
1.0 = full confidence
```

Examples:

```yaml
confidence: 0.45
```

```yaml
confidence: 0.92
```

Confidence should not be treated as absolute truth.

It is a decision support signal.

---

## 15. Review and Value Signal

Review may update a value signal.

Example flow:

```text
reference_detected
  ↓
human_review_completed
  ↓
value_signal_updated
```

A review may recommend:

* lowering signal strength,
* raising signal strength,
* rejecting the signal,
* marking the signal as disputed,
* requiring more evidence.

Example:

```yaml
recommended_signal_strength: "medium"
```

If the value signal changes, a separate `value_signal_updated` event should be created.

The review itself should not silently overwrite the original event.

---

## 16. Review and Allocation

Review may affect allocation decisions.

For example:

```text
AI detects a possible reference.
Human review approves it as a deep conceptual dependency.
A high value signal is created.
A non-monetary allocation decision is proposed.
A linkback and conceptual attribution are recorded.
```

Allocation should normally depend on reviewed or approved events, especially when return is significant.

---

## 17. Dispute Handling

If a review is contested, a dispute event should be added.

Example:

```yaml
event:
  event_id: "event-dispute-001"
  event_type: "review_disputed"
  event_time: "2026-06-04T02:00:00Z"
  status: "disputed"

  dispute:
    disputed_review_id: "review-001"
    dispute_reason: "The dependency was classified as structural, but evidence only supports a shallow mention."
    raised_by: "reviewer-002"
```

Dispute events should not delete previous reviews.

They should preserve the disagreement as part of the event history.

---

## 18. Correction Handling

If a review is later found to be incorrect, a correction event should be added.

Example:

```yaml
event:
  event_id: "event-correction-001"
  event_type: "correction_added"
  event_time: "2026-06-04T03:00:00Z"
  status: "completed"

  correction:
    corrected_review_id: "review-001"
    correction_reason: "Evidence quality was overestimated."
    corrected_field: "evidence_assessment.evidence_quality"
    previous_value: "high"
    new_value: "medium"
```

The past is not erased.

It is corrected with visible trace.

---

## 19. Review Integrity Risks

The Review Layer should guard against the following risks:

### False Positives

AI or humans may detect a relationship that does not actually exist.

### False Negatives

A meaningful reference may be missed.

### Overclaiming

A weak relationship may be exaggerated into a strong dependency.

### Reviewer Bias

A reviewer may approve or reject events unfairly.

### Evidence Weakness

A claim may be made without sufficient evidence.

### Automation Bias

Humans may overtrust AI-generated review suggestions.

### Origin Bias

Originators may overestimate the influence of their own work.

---

## 20. Mitigation Strategies

Recommended mitigation strategies include:

* explicit evidence fields,
* confidence scores,
* human review requirements,
* dispute events,
* correction events,
* multiple reviewers for high-impact events,
* AI-assisted but not AI-final judgments,
* transparent review status,
* append-only logs,
* optional signed review records in future versions.

---

## 21. Review Layer and AI

Royalty OS v0.2 treats AI as an assistant, not a final authority.

AI may:

* detect,
* summarize,
* suggest,
* classify,
* flag,
* compare,
* recommend.

AI should not unilaterally:

* approve high-impact value events,
* assign final allocation,
* declare ownership,
* settle disputes,
* trigger compensation,
* erase or rewrite past events.

The boundary is simple:

```text
AI assists the review process.
Humans remain responsible for judgment.
The event log preserves the history.
```

---

## 22. Non-Goals

The Review Layer does not provide:

* legal dispute resolution,
* court-admissible proof,
* automatic truth detection,
* universal plagiarism detection,
* automatic royalty enforcement,
* final ownership decisions.

It only defines how value events can be reviewed, approved, rejected, disputed, or corrected.

---

## 23. Summary

The Review Layer is the judgment layer of Royalty OS v0.2.

It separates detection from decision.

It allows AI to assist without becoming the final authority.

It preserves review history through append-only events.

Its core principle is:

```text
Detect carefully.
Review transparently.
Correct visibly.
Do not erase the path.
```

Royalty OS v0.2 records value circulation as an evolving event history.

The Review Layer ensures that this history remains meaningful, accountable, and resistant to overclaiming.
