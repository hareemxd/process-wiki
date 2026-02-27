---
title: Version Control
author: David Ricart
project: ProcessWiki
genre: procedure
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
|CM01-003-01| Internal Review |
|MIL-HDBK-61B with Change 1| Configuration Management Guidance |  
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner |Unlocks and locks files, performs edits, writes commit messages|
| Approver  | Reviews and approves commits as required|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) to perform version control and supports compliance to the company's Quality Management System.
### Definition
**Version Control** is the practice of performing and recording changes to data with **versions**. This procedure presents an iterative activity set that can be used to make changes to data in a controlled fashion.

A version is a baseline that is stored in a **Digital Engineering Tool** (DET): storage and editing platforms for engineering data files. Files must be unlocked from the DET repository before changes can be made. After locking the file back into the repository, the Owner creates a unique version identified by these metadata:
* Who created the version
* When they created it
* Commit Message

### When to use Version Control

Version control is required when performing modifications to files in DETs. Files stored in DETs are commonly referred to as "design files" or "natives". These files are digital representations of physical product: drawings, models, schematics, and layouts. More abstract representations, such as system models, source code, or object-based requirements, shall be considered natives as well.


 The table below lists common examples and their associated file types.  

| Tool                    | Data Description| Native File Types     |
| ----------------------- | --- |------------------ |
| Mechanical Design DET | 2D drawings and 3D models|dwg, prt, asm, stp |
| Electrical Design DET| Electronic Design |sch, pcb |
| System Model DET | SysML Diagrams | mdzip|


>[!NOTE]  
>Version control is optional when using SharePoint or SharePoint-supported platforms (Word, Excel, etc.). However, in cases where SharePoint hosts documents with natively modifiable data (e.g. Excel-based analytical data), Version Control is still mandatory.

### Best Practices

#### Write clear commit messages

The **Version History** is only as valuable as the individual **Commit Messages**. Messages should be suitable for a wide audience (including non-engineers).

#### Batch your changes logically

The scope of changes should be logically defined for each version. For example, Instead of modifying a part's dimensions and fixing cover page typos in the same version, separate these tasks into two versions.

#### Limit unlock time

Do not keep files unlocked for long periods of time. Revert changes and lock in the file if you don't have time to finish the version.
### Procedure Map 
![Flowchart showing the Version Control Procedure with five sequential steps: Step 1 - Open file in DET and check out/lock for edits; Step 2 - Perform modifications to data per applicable processes; Step 3 - Write commit message in 1-2 sentences including change summary, location reference, and Problem/Trouble Report if applicable; Step 4 - Check in the file; Step 5 - Submit for approval if required per CM-02-001. Arrows connect each step flowing left to right, depicting the linear workflow for version control in digital engineering tools.](/vcmap.png)
### Procedure

#### Identify the elements under change

*Applicable to*: Owner

1. Review the change record (Problem Report, Engineering Change Order) to locate the **Initiating Part Number**.  
2. Review the change record description and identify which version-controlled elements of the IPN require changes to implement the change record.  

If an assembly drawing file displays the assembly Parts List (PL) on any page, any change to a listed part number or revision requires a new version. For assembly drawing files without PLs, only the changes affecting reference designators, notes, dimensions, or callouts require a new version.

#### Implement changes

*Applicable to*: Owner  

1. Access the identified element in its DET.
2. Create a new version:  
   a. Make changes to the file according to the change record and the applicable engineering processes.  
   b. Write a **Commit Message** in 1-2 sentences indicating:  
    * what changed
    * where the changes occurred in the file
    * the associated change record number.  
3. Lock in the file.  

#### Review changes



### Version Release States

| Term  | Definition                                     |
| ----- | --------------------------------------- |
|Preliminary Release| A version checked in to a DET repository. Access restricted to Owner and/or their team |
|Internal Release| A version reviewed following **CM01-003-01 Internal Review**, exported from the DET and attached to an ECO in a **Draft Revision**|
|External Release | not applicable; all updates within versions must be processed in an ECO prior to external release.|
