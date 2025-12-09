---
title: "Revision Control"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
---
### Procedure
# Revision Control
 ### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|CM-02-001| Set Up Permissions for Data Repositories |

### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Checks out files, commits files, writes commit messages|
| Approver  | Reviews and approves commits as required|
| Configuration Manager | Monitors compliance with procedure|
### Purpose
This document defines the procedure(s) to perform revision control of engineering data.  
### Definition
**Revision Control** is the practice of documenting and releasing changes to data with **revisions**.

A revision is a unique instance of any item referenced by a part number that is controlled and released in a Product Lifecycle Management (PLM) tool. Because of their significance, revisions are reviewed by internal and external stakeholders prior to release.

### When to use Revision Control

***
**NOTE**  
Revision Control applies only to changes executed within an established Program of Record (PoR) and Technical Data Package (TDP).
***

Any changes to a drawing (DWG) file may initiate a new revision, including:  
* Technical Specifications
* Notes
* Parts List
* Reference Designators
* Callouts
* Title block (contract number, proprietary or export markings, cage code)




### Best Practices
***

#### Conduct Peer Review
Revisions must always be reviewed by at least one teammate prior to release. Peer Review can be implemented in PLM workflows or conducted informally. See **CM-02-002 Peer Review**.
#### Assess Where Used References for Impacts
If a change impacts a part or assembly's interface or integration with existing designs, those impacts must be identified and documented as part of the change request process. Potential "suspect links" should be reported using Problem Reports. See **CM-02-002**

#### Highlight changes
When submitting your work for review and release, the draft of the new revision should contain *redlines* which highlight the changes from the previous revision.

### Procedure

1. Open the file in the DET and check it out/lock for edits.  
   
2. Perform modifications to the data in accordance with the applicable processes. 
   
3. Write a Commit Message in 1-2 sentences that includes:   
   a. Brief summary of the change  
   b. Reference to location of changes (page/sheet/block/module/partNumber)  
   c. Reference to Problem/Trouble Report (if applicable)

4. Commit the changes to the DET server. 

---
**Document Control**

* Document Number: CM-01-002

