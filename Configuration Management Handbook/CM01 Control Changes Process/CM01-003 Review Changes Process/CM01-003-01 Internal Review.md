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
>To utilize an Internal Review activity in a workflow, the activity must be structured with a **Review Checklist**; see **T-03 Checklists**.  
>If the review activity is too complex or open-ended to be formatted as a checklist, you should use **CM01-003-02 Peer Review** instead of this procedure.

Commonly, Internal Review takes place between two engineers of the same discipline because both individuals are familiar with each other's work and the applicable objective standards, hence the term *internal*. This practice ensures work is consistent *within disciplines* and does not contain any obvious flaws before progressing to the next stage. This first-pass review ensures that simple mistakes like typos or improper formats do not distract from more important review findings in later stages.

Internal Review activities range in formality from spontaneous meetings to an assigned signoff in a **Product Lifecycle Management** tool (PLM) workflow. The appropriate level of formality depends entirely on the nature of the work. So long as the review is scoped to _objective_ findings (and ideally structured with a checklist), Internal Review can be used in multiple workflows, or multiple times in the same workflow, to support compliance to the requirements of **Control Changes**.

The variety of activities that are considered Internal Review is broad. The table below lists some workplace examples of increasing formality.

| Term| Meaning|
|---|---|
|Huddle| An impromptu meeting between peers to discuss work.|
|Sanity check| A request for a peer to briefly review your work before it is presented, delivered, or otherwise used.|
|Configuration Management Verification| A PLM workflow stage. The review is structured using a checklist.|
|Independent Review| Updates to safety-critical software must be reviewed using a safety checklist for process assurance.|

#### Objective  
 This procedure ensures work complies with internal standards, is free of mistakes, and is ready for delivery to and/or use by a wider internal audience.

### When to perform Internal Review

Any changes to data must be internally reviewed prior to the data's submittal on an ECO.

>[!WARNING]
All employees conducting or participating in Internal Review must create a written record of the activity. The record may be as simple as a few words in an email.

### Best Practices

#### Use Configuration Management to Control Review Artifacts
Data to be reviewed should be uniquely identified with a baseline identifier (version number, revision number, configuration number). Providing teammates with uncontrolled changes to review could lead to misidentification of the review artifact (review the wrong item, incorporate findings into the wrong item).

#### Create a Review Record

The **Review Record** is the proof that Internal Review occurred. 

#### Provide instructions to reviewers

Reviews are more effective when the reviewer knows what to look for. You should ask reviewers to double-check specific items, tables, or sheets. Provide helpful context like, *these changes were driven by* [X].

### Internal Review Procedure

#### Owner
After making changes:
1. Send a link or a copy of the modified data to (at least) one reviewer, as well as any review instructions.
2. Resolve any review findings with the reviewer.
#### Reviewer
1. Review the data and record any findings.
2. Send findings to the Owner.
3. If there are no findings, notify the Owner that you **Accept** the work.



