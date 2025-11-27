**Standard Operating Procedure (SOP)**
Master Data List
----------------

**Document Number:** CM-02-003
**Applicable Domains:** Configuration Management, Engineering
-------------------------------------------------------------

### 1. Purpose

This document defines the procedure for creating and maintaining the **Master Data List (MDL)**—a formal index of all configuration items (CIs) in the approved baseline. The MDL provides traceability between configuration items, their revision states, and their storage locations across repositories.

---

### 2. Revision History

---

### 3. References

| Document Number | Title                                    |
| --------------- | ---------------------------------------- |
| CM-04-001       | Create Functional Baseline               |
| CM-04-002       | Maintain Configuration Integrity Process |
| CM-04-003       | Repository Baseline Setup                |
| CM-01-004       | Classify Changes Procedure               |
| CR-TEMPLATE     | Change Request Form Template             |

---

### 4. Scope

This procedure applies to all configuration items under formal configuration control in DRS-managed data repositories. The MDL includes:

* Documents, drawings, models, and code files
* Specifications, analysis records, and system artifacts
* Any item formally tracked and released as part of the product baseline

---

### 5. Roles and Responsibilities

| Role                | Responsibility                                                    |
| ------------------- | ----------------------------------------------------------------- |
| Configuration Owner | Creates and maintains the MDL; performs periodic data audits      |
| Engineering Lead    | Supports CI definition during baseline creation or change reviews |
| Change Requestor    | Identifies new configuration items as part of change proposal     |

---

### 6. MDL Structure

The MDL is a table with the following columns:

| Field                     | Description                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| Part Number / Document ID | Unique identifier for the configuration item                     |
| Formal Baseline Revision  | Revision level at the time of last formal baseline release       |
| Current Revision          | Most recent approved version, based on repository audit          |
| Repository                | System where the CI resides (e.g., SharePoint, Windchill, DOORS) |

* The MDL may be maintained in Excel or SharePoint list format.
* Optional additional fields (Owner, Description, CI Type) may be added based on program needs.

---

### 7. Process Steps

#### Step 1: MDL Initialization

* CM creates the initial MDL during execution of CM-04-001 (Create Functional Baseline).
* All configuration items released at that time are logged with their part number, baseline revision, and repository.

#### Step 2: Ongoing Maintenance

* CM updates the MDL as configuration items change or new items are added.
* Inputs include:

  * Approved change requests that introduce new CIs (see CR-TEMPLATE)
  * Baseline updates triggered by peer review or CCB events
  * Repository audits conducted periodically by CM

#### Step 3: Audit and Reconciliation

* CM performs a routine audit (recommended monthly or per major release) to:

  * Verify repository revision matches MDL entries
  * Identify discrepancies, such as unlogged revisions or unregistered new items
  * Update current revision fields and flag anomalies

---

### 8. Integration With Other Processes

* **CM-01-004: Classify Changes** – identifies major changes that may introduce new CIs
* **CR-TEMPLATE** – includes a branch for proposing new configuration items
* **CM-04-002: Maintain Configuration Integrity** – depends on the MDL to ensure consistency and control
* **CM-04-003: Repository Baseline Setup** – repository structure is cross-checked against the MDL

---

### 9. Compliance

* All configuration items must be logged in the MDL upon release into formal configuration control.
* CM must ensure the MDL is current and aligned with repository contents.
* Change Requests that propose new configuration items must include all necessary metadata for MDL entry.

---

**Document Control**

* Document Number: CM-02-003
* Effective Date: \[To be Assigned]
* Owner: \[Configuration Manager]
* Last Reviewed: \[To be Assigned]
