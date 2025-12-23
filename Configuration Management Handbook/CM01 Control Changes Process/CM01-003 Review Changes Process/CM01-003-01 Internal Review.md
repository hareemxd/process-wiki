---
title: "Internal Review"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
---
 # Internal Review
 ### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|CM-01-001| Version Control
|CM-RC-001| Schematic Review Checklist
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner|Modifies engineering data and initiates review|
| Reviewer  | Reviews changes and provides feedback|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) to perform internal reviews. 
### Definition
**Internal Review** is the practice of engineers of the same discipline, function, or team reviewing each other's work. This procedure ensures work complies with internal standards. Internal Review focuses on objective errors that are simple to correct (e.g., typos, dangling connectors, noncompliances with style and design standards). Review of these items can be organized using an **Internal Review Checklist**; see **CM-RC-001 Schematic Review Checklist** for an example.  

Whether or not you use a checklist, each Internal Review activity should be recorded with the following information:
* Owner and Reviewer names
* Part Number and Revision
* Findings and resolutions (any errors discovered and the steps taken to address them)
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
1. Perform modifications to data. If using a Digital Engineering Tool, check in your changes; see **CM-01-001 Version Control**.
2. Send a link to the modified data to (at least) one reviewer, as well as any review instructions.
3. Resolve any review findings with the reviewer.
#### Reviewer
4. Review the data and record any findings.
5. If there are no findings, notify the Owner that the review is complete.
6. Send findings to the Owner.
---
### Document Control

* Document Number: CM-02-001

