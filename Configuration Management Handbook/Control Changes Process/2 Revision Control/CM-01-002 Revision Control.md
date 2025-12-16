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
| CM-01-001 | Internal Review |
|CM-02-002| Peer Review |

### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner| Identifies need for update, performs updates, initiates and oversees **Peer Review**|
| Configuration Manager | Monitors compliance with procedure|
### Purpose
This document defines the procedure(s) to perform revision control of engineering data.  
### Definition
**Revision Control** is the practice of documenting and releasing changes to data with **revisions**.

A revision is a unique instance of any item referenced by a part number that is controlled in a Product Lifecycle Management (PLM) tool. Revisions are reviewed by internal and external stakeholders prior to release.

### When to use Revision Control


>[!NOTE]  
>Revision Control applies only to changes executed within an established Program of Record (PoR) and Technical Data Package (TDP).


Any changes to a drawing (DWG) file must be implemented in a new revision, including:  
* Technical Specifications
* Notes
* Parts List
* Reference Designators
* Callouts
* Title block (contract number, proprietary or export markings, cage code)

Form Fit Function (FFF) changes of parts or assemblies result in new **baselines**, not revisions, and are thus out of scope of this procedure.
***
### Best Practices

#### Associate Revisions with Problem/Trouble Reports
Revisions should result from official notice or documentation of a required update. This notice may originate externally (e.g., customer observes a defect) or internally (e.g., supply chain identifies obsolescence issue). From the onset of the Revision Control procedure, the Owner of the change should reference a Problem/Trouble Report that clearly establishes the reason for the change.
#### Conduct Peer Review
Draft revisions must be reviewed by at least one teammate prior to release. Peer Review can be implemented in PLM workflows or conducted informally. See **CM-02-002 Peer Review**.
#### Assess Where Used References for Impacts
If a change impacts a part or assembly's interface or integration with existing designs, those impacts must be identified and documented as part of the change request process. Potential "suspect links" should be reported using Problem/Trouble Reports.
#### Highlight changes
Draft revisions should contain *redlines* (visual indicators of change) to speed the review process.
***
### Procedure

1. Identify the reason for change and its supporting documentation.
   
2. Create the draft revision by performing modifications to the data in accordance with the applicable processes.
   
3. Conduct **Internal Review**; see **CM-02-001**.

4. Conduct **Peer Review**; see **CM-02-002**

5. Implement the new revision into the appropriate baselines; see **CM-01-003**.

6. Submit the draft revision to Configuration Management for PLM release.

---
**Document Control**

* Document Number: CM-01-002

