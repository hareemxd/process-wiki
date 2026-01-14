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
**Revision Control** is the practice of performing and recording changes to data with **revisions**. A new revision indiciates a major update to a baselined **Configuration Item** (CI) in a **Product Lifecycle Management** tool (PLM) that is released for use by all company functions (Manufacturing, Supply).

 #### Objective
 Revision Control ensures quality and timely updates to baselined CIs to support project execution.

### When to use Revision Control

Revision Control is required when performing modifications to be released in a new revision. Any identified changes to an approved baseline of a **Configuration Item** are not usable by the company until released in a new revision. For example:

* Supply Chain needs a new revision of a parts list to procure a replacement for an **End of Life** (EOL) component.  
* Systems Engineering needs a new revision of a qualification test report to reference the test results in a Requirements Verification Matrix.

In general, the rules governing when and how to revise CIs are determined by contractual requirements.
### Best Practices

#### Define all attributes required by the Engineering Change Order process

You should review [blank] to determine which attributes to define for your changes. ECOs must include all information required to implement the changes, including material dispositions, work packages, and effectivity dates. Defining these attributes early in the change process allows other stakeholders to fully verify the changes.
#### Highlight changes
When submitting your work for review and release, the draft of the new revision should contain redlines which highlight the changes from the previous revision.

### Procedure Map
![Revision Control Map](/revcontrolmap1.png)
### Procedure

#### Owner
   
1. Identify the CI to be revised and its current revision released in PLM.
2. Access the CI and/or its documentation (a drawing file, part files of an assembly). 
3. Create a draft revision:  
   a. Locate and update all instances of the revision number to the number post-release.  
   b. Perform modifications to the CI and/or its documentation in accordance with the applicable processes. If modifying natives, batch the changes logically and trace them to a **Problem Report**; see **CM01-002-01 Version Control**.
4. Conduct the applicable reviews in accordance with **CM01-003 Review Changes**.
5. Submit the draft revision to the Configuration Manager.  

#### Configuration Manager

4. Configure and create a new ECO in PLM in accordance with [**blank**]. 
5. Verify the draft revision in accordance with [**blank**].  

#### Change Board
6. Verify the ECO.

### Revision Release States and Control Scheme

| State  | Scheme |Definition                                     |
| ----- | ---|--------------------------------------- |
|Preliminary Release| Revision A to Revision A.1|A draft revision stored in an Engineering workspace (Digital Engineering Tool, SharePoint). Access restricted to Owner and/or their team. |
|Internal Release| Revision A to Revision B|A revision reviewed per **CM01-003-01 Internal Review** and released in a **Document Management System**. Internal use only. |
| External Release | Revision A to Revision B|A revision released in PLM. |


