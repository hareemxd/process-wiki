---
title: "Revision Control"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
---

# Revision Control
 ### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|CM-02-001| Set Up Permissions for Data Repositories |

### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Performs edits, participates in Peer Review, sends draft revision to Configuration Manager|
| Configuration Manager | Verifies the draft revision and submits the resulting Engineering Change Order|
### Purpose
This document defines the procedure(s) and best practices to perform revision control and supports compliance to the company's QMS.  
### Definition
**Revision Control** is the practice of performing and recording changes to data with **revisions**. This procedure presents an iterative activity set that can be used to make changes to data in a controlled fashion.

A revision is a baseline of a **Configuration Item** (CI) in a Product Lifecycle Management tool (PLM) that is released for use by all company functions (Manufacturing, Supply) . Revisions are executed with **Engineering Change Orders** and always require internal and external review before release.

### When to use Revision Control

Revision Control is required when performing modifications to be released in a new revision. Changes to a baselined **Configuration Item** are not usable by the company until released in a new revision. For example:

* Supply Chain needs a new revision of a parts list to order a replacement for an **End of Life** (EOL) component.  
* Systems Engineering needs a new revision of a qualification test report to reference the test results in a Requirements Verification Matrix.

In general, the rules governing when and how to revise CIs are determined by contractual requirements.


### Best Practices


####

#### Track progress of draft revisions with Version Control  

When modifying CIs which are stored in a version-controlled repository, you should use **CM01-002-01 Version Control** as reference for establishing traceability of all changes.

#### Track progress of draft revisions with Problem Reports  

Revision-level changes will always be tied to a **Problem Report** (PR). You should leave comments on the PR to document your progress, as well as any related activities, such as **Peer Review** of the changes.

#### Highlight changes
When submitting your work for review and release, the draft of the new revision should contain *redlines* which highlight the changes from the previous revision.

### Procedure Map

### Procedure

#### Owner
   
1. Create a new draft revision by performing modifications to the data/document in accordance with the applicable processes. 
   
2. Conduct **Peer Review** in accordance with **CM01-003-02 Peer Review**.
3. Submit the draft revision and **Peer Review Record** (PRR) to the Configuration Manager.  

#### Configuration Manager

4. Verify the draft revision in accordance with [**blank**].  
5. Configure and create a new ECO in PLM in accordance with [**blank**]. 
6. Once ready, release the ECO.

### Revision Release

A draft revision is considered a **Preliminary Release**, which means that only the supervising individual, team, function, or department can access the draft revision and reference it in other locations. The revision transitions to an **Internal Release** once it is reviewed and released in a **Document Management System**; see **CM01-003-01 Internal Review**. At this point, the revision gains a level of authority, is accessible to all team members, and is considered acceptable for activities outside of Design Engineering, including but not limited to:  
* Procurement for Development
* Production for Development
* Test and Analysis
* Customer Review

Revisions transition to an **External Release** once they undergo **Peer Review** and are released in PLM.



