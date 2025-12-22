---
title: "Control Changes"
author: "David Ricart"
project: "ProcessWiki"
genre: "process"
domains:
    - Engineering
    - Configuration Management
---
### Process
# Control Changes
 ### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|CM-01-001| Version Control |
|CM-01-002| Revision Control |
|CM-01-003| Baseline Control |
|CM-01-004| Project Control |
### Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Engineering|Perform and review changes|
| Configuration Management | Control changes|
### Purpose
This document defines the Change Control process for Engineering data.
### Definition
Change Control is the process of managing changes to Engineering data. Change Control encompasses the required activities to perform, record, review, approve, and implement Engineering changes across all levels of the product and/or program.  
### When to use Change Control
This process must be followed whenever performing changes to Engineering data.

## Process
###  Change Hierarchy

Engineering changes can vary from an updated torque value on a part drawing, to a new revision of a Requirements Specification that affects the entire product structure. Understanding this hierarchy is critical when deciding how to prioritize, sequence,combine, and implement changes.

#### Analyze Parts Lists, Where Used Lists, and Interfaces to fully scope change

While a change such as a swapped cable may consist of a single redline on a Bill of Materials (BOM), the change itself (converting from RS232 to RS485) may drive updates to other parts or assemblies. Particularly when scoping changes to assemblies, review any sub-assembly drawings on the Parts List, and all **Where Used** references of the assembly. These details provide full context for analyzing the change.

#### High level changes take priority

The further up a change occurs in a product structure, the higher priority it should be given due to downstream effects that interfere or obsolete lower level changes. The high-level definition of change should be settled on before attempting to resolve Class II or III changes beneath it.

#### Lower level changes can be combined

Low level changes that do not conflict may be combined with higher level changes. If an assembly is being revised and its DWG file updated for the new revision, any Class III changes raised against the DWG file can be incorporated into the Engineering Change Order (ECO) with a Problem Report number.

### Control Documents by Release State



#### Identify release status of changes

Some changes may require Customer approval before they can be implemented. Customer approval is achieved using **CM01-003-02 Peer Review**. Any changes approved by the customer and implemented are considered **External Release**

Some changes may not require Customer approval before implementation. These changes can remain in a state of **Internal Release** until delivered as part of a formal deliverable or milestone item, at which time they progress to **External Release** status.

**Document Control**

* Document Number: CM01
