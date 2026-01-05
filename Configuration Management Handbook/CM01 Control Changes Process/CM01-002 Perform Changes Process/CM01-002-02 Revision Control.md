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
| Number |  Title                                   |
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
**Revision Control** is the practice of performing and recording changes to data with **revisions**. A new revision indiciates a major update to a baselined **Configuration Item** (CI) in a Product Lifecycle Management tool (PLM) that is released for use by all company functions (Manufacturing, Supply).

> [!NOTE] 
> At a minimum, Class I revisions must undergo **Internal Review**, **Peer Review**, and **Configuration Management Review** prior to release.

 >[!NOTE] 
 >At a minimum, Class II revisions must undergo **Internal Review** and **Change Board Review** prior to release.
 
 Revision Control ensures quality and timely updates to baselined CIs to support project execution.

### When to use Revision Control

Revision Control is required when performing modifications to be released in a new revision. Any identified changes to an approved baseline of a **Configuration Item** are not usable by the company until released in a new revision. For example:

* Supply Chain needs a new revision of a parts list to procure a replacement for an **End of Life** (EOL) component.  
* Systems Engineering needs a new revision of a qualification test report to reference the test results in a Requirements Verification Matrix.

In general, the rules governing when and how to revise CIs are determined by contractual requirements.

### Best Practices


#### Highlight changes
When submitting your work for review and release, the draft of the new revision should contain redlines which highlight the changes from the previous revision.

### Procedure Map

### Procedure

#### Owner
   
1. Identify the CI to be revised and its current revision released in PLM.
2. Access the CI and/or its constituents (part files of an assembly). 
3. Create a draft revision:
   a. Locate and update all instances of the revision number to the number post-release.
   b. Perform modifications to the CI in accordance with the applicable processes. If modifying natives, batch the changes logically and trace them to a **Problem Report** in accordance with **CM01-002-01 Version Control**.
4. Conduct the applicable reviews in accordance with **CM01-003 Review Changes**.
5. Submit the draft revision to the Configuration Manager.  

#### Configuration Manager

4. Verify the draft revision in accordance with [**blank**].  
5. Configure and create a new ECO in PLM in accordance with [**blank**]. 
6. Once ready, release the ECO.

### Revision Release States and Control Scheme

| State  | Scheme |Definition                                     |
| ----- | ---|--------------------------------------- |
|Preliminary Release| Revision A to Revision A.1|A draft revision stored in an Engineering workspace (Digital Engineering Tool, SharePoint). Access restricted to Owner and/or their team. |
|Internal Release| Revision A to Revision B|A revision reviewed per **CM01-003-01 Internal Review** and released in a **Document Management System**. Internal use only. |
| External Release | Revision A to Revision B|A revision released in PLM. |


