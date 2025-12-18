---
title: "Version Control"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
tags:
    - Traceability
    - Collaboration
---

# Version Control
 ### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|CM-02-001| Set Up Permissions for Data Repositories |
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Checks out files, commits files, writes commit messages|
| Approver  | Reviews and approves commits as required|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) and best practices to perform version control.  
### Definition
**Version Control** is the practice of performing and recording changes to data with **versions**.

Version Control is a common feature of **Digital Engineering Tools**, as well as SharePoint. To perform edits, the engineer must "unlock" or "check out" the design files from a secure repository. After performing edits and sending or "committing" them back to the repository, the engineer creates a unique version with the following metadata:
* Who created the version (**Owner**)
* When they created it (**Timestamp**)
* Why they created it (**Summary**)

### When to use Version Control

Version control is required when using DETs, including, but not limited to:
* PTC Creo
* Altium (or a separate configuration tool like SVN)
* Cameo Systems Modeler
* IBM DOORS
* ANSYS
* Software development environments (Git, Github, Bitbucket)

Version control is optional when using SharePoint or SharePoint-supported apps (Word, Excel, etc.) to modify non-technical documents.
***
**NOTE**  
In cases where SharePoint documents contain data that can be natively modified, Version Control is **still mandatory**. Engineering and Configuration Management are responsible for identifying these documents so they can be stored in a separate version-controlled site.
***
Version Control is also useful for:

* Collaboration. Versioning keeps everyone on the same page as work progresses, and a clean version history accelerates the onboarding process.
- Re-work. When data must be reverted to a previous state, the commit messages in the version history help pinpoint the right version to restore.
* Traceability. Version history documents why changes were made, making it easier to understand design decisions and facilitate audits.

### Version Control Procedure Map 
![Flowchart showing the Version Control Procedure with five sequential steps: Step 1 - Open file in DET and check out/lock for edits; Step 2 - Perform modifications to data per applicable processes; Step 3 - Write commit message in 1-2 sentences including change summary, location reference, and Problem/Trouble Report if applicable; Step 4 - Check in the file; Step 5 - Submit for approval if required per CM-02-001. Arrows connect each step flowing left to right, depicting the linear workflow for version control in digital engineering tools.](/vcmap.png)
### Version Control Procedure

1. Open the file in the DET and check it out/lock for edits.  
   
2. Perform modifications to the data in accordance with the applicable processes. 
   
3. Write a Commit Message in 1-2 sentences that includes:   
   a. Brief summary of the change  
   b. Reference to location of changes (page/sheet/block/module/partNumber)  
   c. Reference to Problem/Trouble Report (if applicable)

4. Check in the file.

##### Version Control Approval

Certain files may require a **commit approval step**. See **CM-02-001 Engineering Internal Review** for the appropriate procedures.

---
**Document Control**

* Document Number: CM-01-001

