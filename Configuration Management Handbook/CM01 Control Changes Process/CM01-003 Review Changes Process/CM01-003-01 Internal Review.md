<!--
---
title: "Internal Review"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
tags:  
    -Traceability  
    -Collaboration  
    -Verification  
---
-->
 # Internal Review
 ### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|CM-01-001| Version Control
|T-03| Checklists|
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Modifies engineering data and initiates review|
| Reviewer  | Reviews changes and provides feedback|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) to perform internal reviews and supports compliance to the company's Quality Management System. 
### Definition
**Internal Review** is the practice of teammates reviewing each other's work to ensure it is compliant with internal standards and free of mistakes.

Internal Review focuses on *objective* aspects of work, such as schematic net label nomenclature, dimension sig-fig usage, and basic design principles. 

>[!NOTE]
>For formal process compliance, Internal Reviews must be structured with **Review Checklists**; see **T-03 Checklists**.  
>If the review activity is too complex or open-ended to be formatted as a checklist, you should use **CM01-003-02 Peer Review** instead of this procedure.

Commonly, Internal Review takes place between two engineers of the same discipline because both individuals are familiar with each other's work and the applicable objective standards, hence the term *internal*. This practice ensures work is consistent *within disciplines* and does not contain any obvious flaws before progressing to the next stage.  

Internal Review activities range in formality from spontaneous meetings to an assigned signoff in a **Product Lifecycle Management** tool (PLM) workflow. The appropriate level of formality depends entirely on the nature of the work.

Some example references to Internal Review include:

| Term| Meaning|
|---|---|
|Huddle| An impromptu meeting between peers to discuss work|
|Sanity check| A request for a peer to review your work

#### Objective  
 This procedure ensures work complies with internal standards, is free of mistakes, and is ready for delivery to and/or use by a wider internal audience.

### When to perform Internal Review

Any changes to data must be internally reviewed prior to the data's submittal for **Peer Review**.

### Best Practices

#### Use Configuration Management to Control Review Artifacts
Data to be reviewed should be uniquely identified with a baseline identifier (version number, revision number, configuration number). Providing teammates with uncontrolled changes to review could lead to misidentification of the review artifact (review the wrong item, or incorporate findings into the wrong item).

#### Submit work that is ready for review

You should only submit work for review if you believe it is ready to be reviewed by a non-internal audience (e.g., during **Peer Review**). Do not submit artifacts with incomplete or inconsistent changes for review unless explicitly directed.

#### Provide instructions to reviewers

Reviews are more effective when the reviewer knows what to look for. You should ask reviewers to double-check specific items, tables, or sheets. Provide helpful context like, *these changes were driven by* [X].

### Internal Review Procedure

#### Owner
1. Perform modifications to data. If using a Digital Engineering Tool, check in your changes; see **CM01-002-01 Version Control**.
2. Send a link to the modified data to (at least) one reviewer, as well as any review instructions.
3. Resolve any review findings with the reviewer.
#### Reviewer
4. Review the data and record any findings.
5. If there are no findings, notify the Owner that the review is complete.
6. Send findings to the Owner.

### Document Control


