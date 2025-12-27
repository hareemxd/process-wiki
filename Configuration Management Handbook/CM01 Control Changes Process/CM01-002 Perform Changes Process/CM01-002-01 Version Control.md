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
|MIL-HDBK-61B with Change 1| Configuration Management Guidance |  
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner |Unlocks and locks files, performs edits, writes commit messages|
| Approver  | Reviews and approves commits as required|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) and best practices to perform version control.  
### Definition
**Version Control** is the practice of performing and recording changes to data with **versions**.

Version Control is a common feature of **Digital Engineering Tools**, as well as SharePoint. To perform edits, the engineer unlocks a file from a secure repository. After performing edits and locking the file back into the repository, the engineer creates a unique version with the following metadata:
* Who created the version (**Owner**)
* When they created it (**Timestamp**)
* Change Summary (**Commit Message**)

The **Commit Messages** form a **Version History**, which records complete traceability of changes, to achieve and maintain compliance with the *Configuration Control* requirements of **MIL-HDBK-61B**.

### When to use Version Control

Version control is required when using DETs, including, but not limited to:
* PTC Creo/Windchill
* SVN
* Cameo Systems Modeler
* IBM DOORS
* ANSYS
* Software development repos (Github, Bitbucket)

The types of files/data that are controlled with Version Control include, but are not limited to:
* 3D Models
* Schematic, Layout, and Gerber files
* Software
* Requirements
* System Models

Version control is optional when using SharePoint or SharePoint-supported platforms (Word, Excel, etc.) to modify non-technical documents.

>[!NOTE]  
>In cases where SharePoint documents contain data that can be natively modified, Version Control is still mandatory. Engineering and Configuration Management are responsible for identifying these documents so they can be stored in a separate version-controlled site.

### Best Practices

#### Write clear summaries

The **Version History** is only as valuable as the individual **Commit Messages**. Messages should be clear and understandable to a wide audience (including non-engineers).

#### Batch changes logically

Traceability is harder to establish if a version contains changes spanning multiple pages or types of fixes (technical and administrative fixes in one version). You should work on one batch of changes at a time and document each batch with its own version. 

#### Limit unlock time

Since your teammates cannot access files that you have unlocked, you should do so only when you have enough time to finish a new version.  

Do not keep files unlocked for long periods of time. Revert changes and lock in the file if you don't have time to finish the version.
### Version Control Procedure Map 
![Flowchart showing the Version Control Procedure with five sequential steps: Step 1 - Open file in DET and check out/lock for edits; Step 2 - Perform modifications to data per applicable processes; Step 3 - Write commit message in 1-2 sentences including change summary, location reference, and Problem/Trouble Report if applicable; Step 4 - Check in the file; Step 5 - Submit for approval if required per CM-02-001. Arrows connect each step flowing left to right, depicting the linear workflow for version control in digital engineering tools.](/vcmap.png)
### Version Control Procedure

1. Unlock the file in the DET for edits.  
   
2. Create a new version by performing modifications to the file in accordance with the applicable processes. 
   
3. Write a **Commit Message** in 1-2 sentences that indicates:   
   a. What changed with a location reference (page number, block number)  
   c. Associated **Problem Report**, if applicable

4. Check in the file.

### Version Release

A checked in version is considered a **Preliminary Release**, which means that only the supervising individual, team, function, or department can access the version and reference it in other locations. The version transitions to an **Internal Release** once it is reviewed and released in a **Document Management System**; see **CM01-003-01 Internal Review**. At this point, the version gains a level of authority, is accessible to all team members, and is considered acceptable for activities outside of Design Engineering, including but not limited to:
* Procurement for Development
* Production for Development
* Test and Analysis
* Customer Review  

Versions  transition to an **External Release** once they undergo **Peer Review**, incorporation into a **Revision**, and are released in a **Product Lifecycle Management** tool (PLM); see **CM01-003-02 Peer Review** and **CM01-002-02 Revision Control**.

