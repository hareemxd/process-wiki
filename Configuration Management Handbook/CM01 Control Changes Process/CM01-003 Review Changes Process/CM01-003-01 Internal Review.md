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
This document defines the procedure(s) to perform internal reviews and supports compliance to the company's QMS. 
### Definition
**Internal Review** is the practice of engineers of the same discipline, function, or team reviewing each other's work.

Internal Review fits into multiple types of workflows and the specific review tasks will differ according to the nature of the data, the changes, and project-specific details. Internal Reviews can vary in their technical nature and level of formality. The table below lists examples of activities that can constitute Internal Review.

| Description                    | Reviewer|Function of Internal Review |
| ----------------------- | --- |------------------ |
| Class II EOL Component | Project Engineer |Verifies no FFF impact. Checks Assembly drawing updates for completeness (updates to Notes, Parts Lists, Callouts, Reference Designators). Checks that Configuration Control is intact.|
| Class I New Schematic | Electrical Engineer|Checks updated nets, connections, internal and external interfaces. Analyzes and critiques design decisions. Checks manufacturability and compliance to relevant specifications (derating)|
| Class I System Requirements Update | Systems Engineer |Verifies requirements are clear, concise, complete, correct, valid and verifiable. 
#### Objective  
 This procedure ensures work complies with internal standards, is free of objective errors, and is ready for delivery and/or use to a wider internal audience.

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


