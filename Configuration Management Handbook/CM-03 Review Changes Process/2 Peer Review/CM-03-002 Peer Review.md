---
title: "Peer Review"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
---
### Procedure
# Peer Review
### References

| Document Number | Title                                |
| --------------- | ------------------------------------ |
| CM-01-001       | Version Control for Engineering Data |

### Purpose

This document defines the procedure(s) for conducting peer reviews of engineering data. 
### Definition
**Peer Review** is the practice of receiving and incorporating feedback from peers into your work. Peer Review is a formal change procedure that supports project management, product validation/verification, and quality assurance activities. Importantly, by bringing together key stakeholders, Peer Review verifies acceptance of the work across all engineering, administrative, and commercial perspectives.

### When to use Peer Review

*All changes* to engineering data and/or artifacts are subject to Peer Review before release or delivery. Peer Review is generally recommended for any deliverable effort regardless of technical nature, including proposal items (bids, BOEs, volumes) and vendor quotes.

## Best Practices  
### Owner  
#### Use a template  
#### Instruct reviewers on what to review  
#### Communicate with reviewers  
### Reviewer  
#### Be critical  
#### Communicate with owner  
## Procedure  
### Owner  
1.   
* Select a Peer Review Form (PRF) template suited to the target repository or artifact type.

  * Example: Use the SharePoint PRF template for documents in SharePoint.

#### Step 2: Identify the Modified Data Under Review

* In the PRF template, record the **part number** and **revision/increment number** for each data item under review.

**Note**: Identification fields must be data-validated from a reference list to reduce risk of typographical errors (see CM-02-002).

#### Step 3: Collect Data and Supporting Material

* Gather all relevant modified files, the PRF sheet, and any reference documentation required by reviewers.
* Upload all materials to a designated **shared folder**.

#### Step 4: Identify Reviewers

* Identify reviewers based on:

  * The **Authorized Signature List (ASL)** if available, or
  * **Manual assignment** by the data Owner or Engineering Lead.

**Reviewer assignment guidance:**

* Consider the **stage of the project lifecycle** (e.g., omit manufacturing review from early prototypes).
* Consider the **artifact type** (e.g., schematics need electrical review).
* Consider **system complexity** and **safety criticality** to determine needed domain participation.

Reviewer assignments and general approval structure for a project should be detailed in a project Configuration Management Plan. See CM-01-001 Approve Changes.

#### Step 5: Prepare Peer Review Record

* Populate the PRF with:

  * Configuration IDs (step 2)
  * Reviewers (step 4)
  * Change Description
* Notify reviewers and Configuration Management that the review has been initiated.

#### Step 6: CM Grants Reviewer Access

* CM grants reviewers **edit access** to the PRF.
* Access permissions must align with CM-02-001 Set Up Permissions for Data Repositories.

#### Step 7: Reviewer Commenting

* Reviewers analyze the data and enter comments directly into the PRF.
* **Reviewer guidance:**

  * Focus on the **modifications** made since the last version/revision.
  * Prioritize feedback on **domain-specific elements** relevant to their role.
  * Use clear, constructive language. Flag safety, performance, or compliance concerns.

#### Step 8: Owner Responds to Comments

* The data owner reviews each comment and records a **response**:

  * Accept and implement change
  * Reject with rationale
  * Defer or clarify as needed
* Data is modified as required to address valid feedback.

#### Step 9: Owner Closes Comments

* Once feedback is addressed, the owner **closes** each comment individually.
* Closed comments should reflect completion and traceability of action.

#### Step 10: Review Completion

* The PRF status changes from **Open** to **Closed** once:

  * All assigned reviewers have submitted at least one comment.
  * All comments are reviewed and responded to.
  * All comments are closed by the Owner.
  * All necessary data updates have been made.

---

### 6. Compliance

* All peer reviews must follow this procedure to ensure integrity, consistency, and approval traceability.
* CM must retain completed PRFs for audit and process verification.
* Incomplete or improperly executed reviews are not valid for release or revision.

---

**Document Control**

* Document Number: CM-01-003
* Effective Date: \[To be Assigned]
* Owner: \[Configuration Manager]
* Last Reviewed: \[To be Assigned]
