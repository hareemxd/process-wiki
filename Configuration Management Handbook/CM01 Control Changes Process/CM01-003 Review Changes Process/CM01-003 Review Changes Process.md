**Process**  
Preserve Integrity of Engineering Data  
---
## **Applicable Domains:** Engineering, Configuration Management

### 1. Purpose

This document defines the process for preserving the integrity of controlled engineering data. Integrity in this context refers to protection against both unauthorized and accidental changes. This process is fundamental to ensuring data traceability, quality, consistency, and regulatory compliance.

---

### 2. Revision History

---

### 3. References

| Document Number | Title                                             |
| --------------- | ------------------------------------------------- |
| CM-01-001       | Version Control for Engineering Data              |
| CM-02-001       | Permission Scheme for Controlled Engineering Data |

---

### 4. Scope

This process applies to all engineering data controlled by DRS.

---

### 5. Roles and Responsibilities

| Domain                   | Responsibility                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Engineering              | Follows process safeguards when accessing or modifying data; identifies and communicates risks to Configuration Management |
| Configuration Management | Implements proper controls and preventative mechanisms                                                                     |
|                          |                                                                                                                            |

### 6. Definition of Integrity

**Integrity** refers to maintaining the trustworthiness and correctness of engineering data by protecting it from:

* **Unauthorized changes** (e.g., access by unapproved personnel)
* **Accidental changes** (e.g., unintentional edits, incorrect updates)

This includes:

* Enforcing permission controls
* Enforcing check-in/check-out protocols
* Preventing clerical errors, particularly in identifying information (e.g., part numbers, revision levels)

---

### 7. Integrity Controls

#### 7.1 Permissions Enforcement

* Permissions must be implemented as outlined in SOP CM-002.
* Access is limited to authorized users only, based on a documented RACI model.
* Unauthorized privilege escalation or ad-hoc access must be blocked or flagged.

#### 7.2 Version Control and Check-Out Protocols

* All repositories must support and enforce a check-out/check-in workflow (see SOP CM-001).
* Files not checked out are **read-only**, preventing inadvertent changes.
* File status indicators (e.g., "checked out by...") must be visible to all users.

#### 7.3 Prevention of Accidental Edits

* Default permission for general users should be **read-only** unless editing is required.
* In document systems (e.g., SharePoint), file locking and version protection must be configured.
* Templates used for controlled forms (e.g., change requests) must include protected fields for part numbers, document IDs, etc., with validation rules to reduce clerical errors.

#### 7.4 Identification Consistency

* Part numbers, version numbers, and document IDs must be copy/paste traceable from a controlled source of truth (e.g., metadata lists, PLM export).
* Any manual edits to identifiers must be verified in peer review or automated validation, where feasible.

---

### 8. Integration With Other Processes

The preserve integrity process is a **parent control** to several subordinate SOPs, including:

* CM-001: Version Control for Engineering Data
* CM-002: Permission Scheme for Controlled Engineering Data
* CM-XXX: \[Change Request and Review Workflow – future template]

---

### 9. Compliance

* All engineering personnel are responsible for preserving data integrity by adhering to the procedures and safeguards defined here.
* Configuration Management is responsible for defining and auditing the technical implementations.
* Any identified breach of integrity controls must be reported to CM and remediated within 5 business days.

---

**Document Control**

* Document Number: CM-02
* Effective Date: \[To be Assigned]
* Owner: \[Configuration Manager]
* Last Reviewed: \[To be Assigned]
