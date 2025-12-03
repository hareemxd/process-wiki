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
**Revision Control** is the practice of performing and recording changes to data with **revisions**.

A revision is a specific configuration of a part, sub-assembly, or assembly. Revisions exist to record changes 

### When to use Revision Control

***
**NOTE**  
The following sections apply mostly to programs managing changes to an established Technical Data Package (TDP). Change control procedures and best practices may vary widely for early development and prototype efforts, and thus should be tailored and documented in a project Configuration Management Plan (CMP).
***

Any changes to a drawing (DWG) file require a new revision, including:  
* Notes
* Bill of Materials
* Reference Designators
* Specifications
* Callouts
* Title block (contract number, proprietary or export markings, cage code)

All design changes resulting in a new physical product definition (e.g., geometry, dimensions) require a new revision.

One-for-one parts list updates (e.g., replacing an obsolete component with an FFF equivalent) require a new revision.


### Best Practices
***

#### Assess Where Used References for Impacts
If a change impacts a part or assembly's interface or integration with existing designs, those impacts must be identified and documented as part of the change request process.

#### Highlight changes
When submitting for review and/or release, new revisions should contain *redlines* or some other visual feature that highlights the changes from the previous revision.

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

* Document Number: CM-01-001
* Effective Date: \[To be Assigned]
* Owner: \[Configuration Manager]
* Last Reviewed: \[To be Assigned]
