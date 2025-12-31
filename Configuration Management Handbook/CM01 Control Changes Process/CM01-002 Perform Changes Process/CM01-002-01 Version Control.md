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
This document defines a set of procedures to perform version control and supports compliance to the company's QMS.
### Definition
**Version Control** is the practice of performing and recording changes to data with **versions**. This procedure presents an iterative activity set that can be used to make changes to data in a controlled fashion.

A version is a baseline that is stored in a **Digital Engineering Tool** (DET): storage and editing platforms for engineering data files. Files must be unlocked from the DET repository before changes can be made. After locking the file back into the repository, the engineer creates a unique version with the following metadata:
* Who created the version (**Owner**)
* When they created it (**Timestamp**)
* Change Summary (**Commit Message**)

### When to use Version Control

Version control is required when using DETs. The table below lists common examples and their associated file types.  

| Tool                    | Data Description| Native File Types     |
| ----------------------- | --- |------------------ |
| Windchill | 2D drawings and 3D models|dwg, prt, asm, stp |
| Xpedition| Electronic Design |sch, pcb |
| Cameo Systems Modeler | SysML Diagrams | mdzip|
| DOORS | Object-level Requirements | dma |


>[!NOTE]  
>Version control is optional when using SharePoint or SharePoint-supported platforms (Word, Excel, etc.). However, in cases where SharePoint hosts documents with natively modifiable data, Version Control is still mandatory.

### Best Practices

#### Write clear summaries

The **Version History** is only as valuable as the individual **Commit Messages**. Messages should be suitable for a wide audience (including non-engineers).

#### Batch your changes logically

Traceability is harder to establish if a version contains multiple changes or types of changes (technical and administrative fixes in one version). You should work on one batch of changes at a time and document each batch with its own version. 

#### Limit unlock time

Since your teammates cannot access files that you have unlocked, you should do so only when you have enough time to finish a new version.  

Do not keep files unlocked for long periods of time. Revert changes and lock in the file if you don't have time to finish the version.
### Procedure Map 
![Flowchart showing the Version Control Procedure with five sequential steps: Step 1 - Open file in DET and check out/lock for edits; Step 2 - Perform modifications to data per applicable processes; Step 3 - Write commit message in 1-2 sentences including change summary, location reference, and Problem/Trouble Report if applicable; Step 4 - Check in the file; Step 5 - Submit for approval if required per CM-02-001. Arrows connect each step flowing left to right, depicting the linear workflow for version control in digital engineering tools.](/vcmap.png)
### Procedure

1. Unlock the file in the DET for edits.  
   
2. Create a new version by performing modifications to the file in accordance with the applicable processes. 
   
3. Write a **Commit Message** in 1-2 sentences that indicates:   
   a. What changed with a location reference (page number, block number)  
   c. Associated **Problem Report**, if applicable

4. Check in the file.

### Version Release States

| Term  | Definition                                     |
| ----- | --------------------------------------- |
|Preliminary Release| A version checked in to a DET repository. Access restricted to Owner and/or their team |
|Internal Release| A version reviewed per **CM01-003-01 Internal Review** and released in a **Document Management System**. Read access granted to entire organization |
| External Release | N/A |
