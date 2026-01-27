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
|CM01-002-01| Version Control |
|CM01-003-01| Internal Review|
|CM01-003| Review Changes|

### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Performs edits, participates in Peer Review, sends draft revision to Configuration Manager|
| Configuration Manager | Verifies the draft revision, submits and releases the resulting Engineering Change Order|
|Change Board | Verifies the ECO|
### Purpose
This document defines the procedure(s) and best practices to perform revision control and supports compliance to the company's QMS.  
### Definition
**Revision Control** is the practice of performing and recording changes to data with **revisions**. A new revision indiciates an update to a **Configuration Item** (CI) baseline released in a **Product Lifecycle Management** tool (PLM) for use by all company functions (Manufacturing, Supply).

 #### Objective
 Revision Control ensures quality and timely updates to baselined CIs to support project execution.

### When to use Revision Control

Revision Control is required when executing Class I and Class II changes to an approved CI baseline.

>[!NOTE]
>CI baselines are comprised of the CI itself (a uniquely identified collection of hardware and/or software) as well as all defining documentation (drawings, parts lists); see [blank].
### Best Practices

#### Highlight changes
When submitting your work for review and release, the draft of the new revision should contain redlines which highlight the changes from the previous revision.

### Procedure Map
![Revision Control Map](/revcontrolmap1.png)
### Procedure

#### Owner
Working in the **InWork** ECO:
1. Identify the CI and all comprising elements (prt, asm, dwg) to be revised.
2. Access the materials identified above in their respective workspaces.
3. Create a **Draft Revision**:  
   a. Locate and update all instances of the **FromRev** to the **ToRev**.  
   b. Make changes to the file in accordance with the ECO information and applicable work procedures.  
   c. For CIs comprised of multiple elements, make the above changes to the remaining elements.  
   d. Export and package together (ZIP) all elements of the CI. Name the package: [CI Part Number]-Rev[**ToRev**]_DRAFT

4. Perform **Internal Review** and create a **Review Record**; see **CM01-003-01 Internal Review**.
5. Submit the Draft Revision to the Configuration Manager.  


#### Configuration Manager

4. Verify the Draft Revision in accordance with **CM01-003 Review Changes**. 
5. Initiate the ECO in PLM.
### Revision Release States and Control Scheme

| State  | Scheme |Definition                                     |
| ----- | ---|--------------------------------------- |
|Preliminary Release| Revision A to Revision A.1|A draft revision stored in an Engineering workspace (Digital Engineering Tool, SharePoint). Access restricted to Owner and/or their team. |
|Internal Release| Revision A to Revision B_Draft|A revision reviewed per **CM01-003-01 Internal Review** and submitted on an ECO. Internal use only. |
| External Release | Revision A to Revision B|A revision released in PLM. |


