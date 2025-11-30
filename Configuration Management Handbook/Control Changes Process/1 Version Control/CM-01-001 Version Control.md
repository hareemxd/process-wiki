---
title: "Version Control"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
---
### Procedure
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
This document defines the procedure(s) and presents the common use cases and best practices to perform version control of engineering data.  
### Definition
**Version Control** is the practice of performing and recording changes to data with **versions**. When a user modifies data in a version-controlled file repository, they create a new, uniquely identified version. Version control establishes a complete and legible **change history**. Versions contain the following metadata:
* Who created the version (**Owner**)
* When they created it (**Commit Timestamp**)
* Why and/or how they created it (**Commit Message**)

Version Control is a common built-in feature of **Digital Engineering Tools** (DETs), which engineers use to modify data. DETs require the user to *check out* the file before making changes. This feature ensures only one person can make changes at a time. The file becomes avaiable for another check-out once the new version is committed. 
### When to use Version Control

Version control is required when using DETs, including, but not limited to:
* PTC Creo
* Altium (or a separate configuration tool like SVN)
* Cameo Systems Modeler
* IBM DOORS
* ANSYS
* Software development environments (Git, Github, Bitbucket)

Version control is optional when using SharePoint to modify non-technical documents, such as Word, PDF, Excel, PPT, and Visio files.
***
NOTE  
In cases where SharePoint documents contain data that can be natively modified in a non-DET, Version Control is **still mandatory**. Engineering and Configuration Management are responsible for identifying these documents in a given program and/or work environment so they can be stored in a separate version-controlled site.
***
Version Control is also useful for:

* Managing collaboration. Version Control helps multiple engineers maintain awareness of changes as they work on the same files concurrently. Versioning keeps everyone on the same page as work progresses, and speeds up the onboarding process.
- Simplifying re-work. When data must be reverted to a previous state, the commit messages in the version history help pinpoint the right version to restore.


### Best Practices
***
#### Limit the number of changes in a version
Versions are considered smaller increments of change than other control methods like **revisions** or **baselines**. Since the goal of version control is to produce a comprehensible change history, you should limit the changes in a single version to only a few significant changes or a handful of minor changes. This approach allows an independent reviewer to quickly grasp the evolution of the data.

If you can't summarize the changes in 1-2 sentences in the commit message, the changes may be too complex or dense to be understood in the change history. Revert some of the changes, create a first new version, and then create a second new version with the remaining changes.

#### Limit the amount of time a file is checked out

You should not check out files unless your immediate attention will be devoted to completing the new version. Leaving a file in check-out status for many hours leaves teammates in the dark on your progress, and you may forget what work was left incomplete when you pick it up again. Lengthy check-outs slow down collaboration and degrade the quality of the change history (e.g., a version with only a few typo fixes was checked out for 7 hours). 

#### For major changes, add traceability to an external change record

At certain pivot points in development, (e.g. scope of work change, requirements change), it may be necessary to create a new version with a substantial amount of change from the previous version. This is acceptable so long as the change history is still comprehensible and legibile, **and** the Commit Message for the major version includes an external record ID, such as a **Problem Report** or **Trouble Report**.


### Version Control Procedure

1. Open the file in the DET and check it out/lock for edits.  
   
2. Perform modifications to the data in accordance with the applicable processes. 
   
3. Write a Commit Message in 1-2 sentences that includes:   
   a. Brief summary of the change  
   b. Reference to location of changes (page/sheet/block/module/partNumber)  
   c. Reference to Problem/Trouble Report (if applicable)

4. Commit the changes to the DET server. 

##### Version Control Approval

Certain files may require a **commit approval step**.  

1. Locate the file to be approved, in a notifications menu or inbox, or by manually searching the DET.
2. Review the change history and the changes in the new version.
3. Approve the changes or notify the Owner of issues to be resolved before approval.


---
**Document Control**

* Document Number: CM-01-001

