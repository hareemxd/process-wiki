**Procedure**  
Classify Changes to Engineering Data
------------------------------------

**Applicable Domains:** Engineering, Configuration Management
-------------------------------------------------------------

### 1. Purpose

This document defines the procedure for classifying changes to controlled engineering data into one of three categories—**Major**, **Minor**, or **Non-Technical**—based on functional impact, criticality, and traceability. Accurate classification is essential for selecting the correct level of review, approval, and release control.

---

### 2. Revision History

---

### 3. References

| Document Number | Title                                    |
| --------------- | ---------------------------------------- |
| CM-03           | Approve Changes to Engineering Data      |
| CM-01-001       | Version Control for Engineering Data     |
| CM-01-002       | Peer Review Procedure                    |
| CM-01-003       | CCB and Baseline Control Process         |
| CM-04-002       | Maintain Configuration Integrity Process |
| CR-TEMPLATE     | Change Request Form Template             |

---

### 4. Scope

This procedure applies to all change requests affecting engineering documents, models, specifications, software, requirements, and related technical artifacts under configuration control.

---

### 5. Roles and Responsibilities

| Role                | Responsibility                                                   |
| ------------------- | ---------------------------------------------------------------- |
| Engineer/Requestor  | Initiates change request and proposes classification             |
| Engineering Lead    | Reviews and confirms classification decision                     |
| Configuration Owner | Ensures proper documentation, escalation, and process compliance |
| CCB                 | Required for final approval of major changes                     |

---

### 6. Change Categories

#### 6.1 Major Change (Class I)

* Affects form, fit, function, interface, performance, or safety.
* Impacts certification basis, compliance, or requires customer approval.
* Examples:

  * Structural redesign
  * Interface changes
  * New failure modes or test procedures

#### 6.2 Minor Change (Class II)

* Limited in scope and does not impact form, fit, function, or regulatory compliance.
* Requires internal review/approval, but not external escalation.
* Examples:

  * Schematic layout improvements
  * Software logic optimizations without external effect
  * BOM changes that maintain interchangeability

#### 6.3 Non-Technical Change

* Administrative or documentation-only edits.
* No effect on product design, function, or behavior.
* Examples:

  * Typographical corrections
  * Formatting or metadata updates
  * Internal part number or naming cleanup

---

### 7. Decision Tree for Classification

```
Start → Is the change functional, safety-critical, or externally visible?
          ↳ Yes → Major Change → Route through PRF and CCB → Revision + ECO
          ↳ No
            ↳ Is the change administrative or clerical only?
                  ↳ Yes → Non-Technical Change → Internal approval → Version only
                  ↳ No  → Minor Change → Peer or team approval → Version only
```

---

### 8. Process Steps

#### Step 1: Initiate Change Request

* Complete the **Change Request Form (CR-TEMPLATE)**.
* Summarize proposed change and affected configuration items.

#### Step 2: Apply Classification Criteria

* Use Section 6 definitions and Step 7 decision tree.
* Provide rationale for selected category in CR-TEMPLATE.

#### Step 3: Confirm Classification

* Engineering Lead or designated reviewer confirms classification.
* If **Major**, escalate to PRF (peer review), CCB, and ECO process (CM-03, CM-01-003).
* If **Minor or Non-Technical**, route via version control (CM-01-001).

#### Step 4: Process Change Based on Classification

| Category      | Required Review / Approval        | Control Mechanism          |
| ------------- | --------------------------------- | -------------------------- |
| Major         | Peer Review, ASL, CCB, ECO        | Revision + Baseline Update |
| Minor         | Peer or Functional Lead Approval  | Version + Internal Log     |
| Non-Technical | CM or Document Owner Confirmation | Version + Audit Comment    |

---

### 9. Compliance

* All engineering changes must be documented and classified using the CR-TEMPLATE.
* Improper classification bypassing peer or CCB review is a process violation.
* Configuration Management must audit a sample of change records for compliance.

---

**Document Control**

* Document Number: CM-01-004
* Effective Date: \[To be Assigned]
* Owner: \[Configuration Manager]
* Last Reviewed: \[To be Assigned]
