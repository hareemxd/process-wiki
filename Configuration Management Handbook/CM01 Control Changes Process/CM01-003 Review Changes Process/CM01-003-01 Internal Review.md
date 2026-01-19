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
|CM01-003| Review Changes|
|T-03| Checklists|
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Modifies work and initiates review activity|
| Reviewer  | Reviews work and provides feedback|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) to perform internal reviews and supports compliance to the company's Quality Management System. 
### Definition
**Internal Review** is the practice of teammates reviewing each other's work to ensure it is compliant with internal standards and free of mistakes. Internal Review focuses on *objective* aspects of work, such as basic design principles and significant figure usage.

Commonly, Internal Review takes place between two engineers of the same discipline because both individuals are familiar with each other's work and the applicable objective standards. This practice ensures work is consistent *within disciplines* and is ready for more critical reviews and wider use by an internal audience.

Internal Review activities range in formality from impromptu meetings to an assigned signoff in a **Product Lifecycle Management** tool (PLM) workflow. The appropriate level of formality depends entirely on the nature of the work. 

>[!NOTE]
>To utilize an Internal Review activity in a PLM workflow, the activity must be structured with a **Review Checklist**; see [T-03 Checklists]().  


The variety of activities that are considered Internal Review is broad. The table below lists some workplace examples of increasing formality.

| Term| Meaning|
|---|---|
|Huddle| An impromptu meeting between peers to discuss work.|
|Sanity check| A request for a peer to briefly review your work before it is presented, delivered, or otherwise used.|
|Design Assurance Independent Review| Updates to safety-critical software must be reviewed by the appropriate Subject Matter Expert using a safety checklist.|
|Configuration Management Verification| A PLM workflow stage. The review is structured using a checklist.|



### When to perform Internal Review

All changes must undergo Internal Review prior to the work's submittal on an ECO.

Review activities which are focused on *objective* aspects of work should use this procedure.
### Best Practices

#### Use Configuration Management to Control Review Artifacts
Work under review should be uniquely identified (version number, revision number, configuration number) and controlled. Providing teammates with uncontrolled changes to review could lead to misidentification of the review artifact (review the wrong item, incorporate findings into the wrong item).


#### Provide instructions to reviewers with Objective Statement

Specific instructions improve the value of the review activity; see [CM01-003 Review Changes]().

### Internal Review Procedure

#### Owner
After making changes:
1. Send a link or a copy of the modified data to (at least) one reviewer.
2. Resolve Comments with the reviewer(s).
#### Reviewer
1. Review the work and send Comments to the Owner.
2. If no Comments, notify the Owner that you **Accept** the work.



