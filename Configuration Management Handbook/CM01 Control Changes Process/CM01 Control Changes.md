---
title: "Change Control"
author: "David Ricart"
project: "ProcessWiki"
genre: "process"
domains:
    - Engineering
    - Configuration Management
---
# Control Changes
 ## References  
 ### Configuration Management Handbook
| Number |  Title                                   |
| ----- | --------------------------------------- |
|CMH-01| Configuration Management Handbook |  
|CM01-001| Analyze the Change |
|CM01-002| Perform the Change |
|CM01-003| Review the Change |
|CM01-004| Baseline the Change |  

### External Documents  
Number |  Title                                   |
| ----- | --------------------------------------- |
|EIA-649C| Configuration Management Standard |

## Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Engineering| Analyze, perform, review, and baseline changes|
| Configuration Management | Control changes|
## Purpose
This document defines the Level 2 **Control Changes** process for company employees who manage, modify, or otherwise work with engineering data. The process facilitates alignment with the **Configuration Change Management** (CCM) function of the **Configuration Management Standard EIA-649C**. The Appendix includes a table of the CCM principles with reference to the applicable document(s) in the **Configuration Management Handbook CMH-01**.  

This document functions as a high-level guide for company employees and a roadmap to compliance with Corporate objectives. Employees should first read this process before reading the lower level procedures, to become familiar with the process inputs/outputs, involved stakeholders, handoffs, and objectives. This familiarity will improve your understanding of how the process integrates with our business activities, and will help you comprehend and tailor the constituent procedures to the specifics of your job.
## Definition
The process encompasses the activities to analyze, perform, review, and implement changes to all company products. This process is critical to establishing and maintaining **Traceability** and **Product Integrity** (the product is developed, tested, manufactured, delivered, and serviced as described in the approved configuration baseline). 

This process, including its constituent documents in **CMH-01**, provides clear methods to control engineering data across the complete product lifecycle. 
### When to use Change Control
This process must be followed whenever performing changes to engineering data from Contract Award to product obsolescence, and it is applicable to all programs and contracts.  



## Best Practices  

### Establish clear baselines  



### Define internal and external visibility of changes

### Use Templates

## Process
### Analyze the Change

The Level 3 Process **CM01-001 Analyze the Change** is comprised of Level 4 Procedures, which are summarized in the following subsections. Refer to the procedures for more detailed information.
#### Detect the Change
This procedure is initiated with a **Problem Report** (PR), the mechanism to detect and track potential changes and the first uniquely identified artifact in the process. [This table](#problem-report-examples) provides simple examples of PRs and the required attributes.

##### Activity Flow

1. Configuration Management (CM):   
   a. receives or creates the PR (status: **Open**),  
   b. verifies the required attributes, and  
   c. transfers the PR to Engineering.


2. Engineering: 
   a. reviews the PR,  
   b. writes a **Change Justification**, and  
   c. submits the PR to the **Level 1 Review Board**.

3. Upon approval, the Level 1 Review Board:   
   a. reviews and approves the PR (state: **Closed**),    
   b. generates an **Engineering Change Request** (ECR) (status: **Open**) directly from the PR, and  
   c. transfers the ECR back to Engineering for further analysis.

#### Responsibilities
CM shall review the operation of the Problem Reporting system and regularly communicate with other functional areas (Engineering, Quality, Supply) to ensure PRs are flowing into and across company systems as expected.

#### Classify the Change
This procedure is initiated when Engineering receives the ECR with **Open** status. The first step to completing the ECR is to Classify the Change.

Change Classification is based on the **Form, Fit, Function** (FFF) impacts of the change. Changes with interchangeable items have zero FFF impact. [This table](#change-classifications) lists the definition of each class.  

##### Activity Flow  

1. Engineering:  
   a. reviews the ECR,  
   b. performs a Form Fit Function (FFF) analysis, and  
   c. records the classification on the ECR (status: **InProgress**).
2. Configuration Management:  
   a. verifies the FFF analysis and classification,  
   b. submits the ECR to the **Approval Authority**,  
   c. receives the Notice of Approval, and  
   d. updates the ECR to status **Class Approved**.

#### Responsibilities

CM shall retain the original record of the Notice of Approval from the Approval Authority.
#### Plan the Change
This procedure is initiated when the ECR status transitions to **Class Approved**. The scope of analysis broadens to fully investigate the technical aspects of the change as well as project and schedule considerations.  

##### Activity Flow
1. Engineering:  
    a. performs analysis to identify:
   * **Affected Items**: all items that will change within the scope of the ECR  
   * **Verification Activities**: test and analysis required to verify the change  
   * **Implementation Plan**: the logical sequence and prioritization of the change
   * **Schedule**: start and finish dates
  
    b. updates the ECR.

#### Responsibilities

### Perform the Change
#### Version Control
#### Revision Control
#### Configuration Control



### Baseline the Change

## Appendix

### Problem Report Examples
| Reason to Change                   | Description     | Source | Initiating Part Number|
| ----------------------- | -------------- |------------------ | ---|
| Corrective Action| Product failed a test event| Internal (Engineering)| System
| Corrective Action| Part declared obsolete| External (Vendor)| Electronic Component
| Corrective Action| Part does not conform to standard/specification/drawing | Internal (Quality)| Mechanical Part
| Opportunity| Product can be modified for new customer demand | Internal (Sales)|  System
| Opportunity| BOM consolidation can reduce manufacturing cost | Internal (Engineering) |  Documentation

### Change Classifications

| Class                    | Description     |
| ----------------------- | ------------------ |
| Class I "Major" |Form Fit Function design change (hardware or software)|
| Class II "Minor" | No FFF impact, Documentation only|
| Class III "Admin" | No technical impact

### EIA-649 Configuration Change Management Principles  
|Number | Text |
| ----- | ---- |
|CCM-1	| Changes to an approved configuration are accomplished using a systematic, measurable change process. |
|CCM-2	| Justifying the need for a change provides the rationale to commit resources required to document, process, and if approved, implement the change. |
|CCM-3	| A unique change identifier enables tracking of the request for change and the status of implementation and verification of the approved change. |
|CCM-4	| Classification of a requested change determines the appropriate level of review and the applicable change approval authority. |
|CCM-5	| As the primary vehicle for referencing and managing a change, the request for change document must be clear and comprehensive from technical, cost and scheduling perspectives. |
|CCM-6	| Prior to approval, a requested change is evaluated for all impacts and risk considerations including technical, operational, support, schedule, and cost, as well as the consequences of not approving the request. |
|CCM-7	| After considering all impacts and risk factors, change approval decisions are made by an appropriate authority who can commit resources to implement the change. |
|CCM-8	| An approved change is implemented in accordance with documented direction approved by the appropriate level of authority. |
|CCM-9	| If it is necessary to temporarily depart from approved product configuration information, a request for variance is identified, classified, documented, coordinated, evaluated and dispositioned. |