---
title: "Review Changes"
author: "David Ricart"
project: "ProcessWiki"
genre: "process"
domains:
    - Engineering
    - Configuration Management
---
# Review Changes
 ## References  
 ### Configuration Management Handbook
| Number |  Title                                   |
| ----- | --------------------------------------- |
|CMH-01| Configuration Management Handbook |  
|CM01| Control Changes |
|CM01-003-01| Internal Review |
|CM01-003-02| Peer Review |

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

This document defines the Level 3 **Review Changes** process for company employees who manage, modify, or otherwise work with engineering data. The process facilitates alignment with the **Configuration Change Management** (CCM) function of the **Configuration Management Standard EIA-649C**.

This document provides a guide for company employees and a roadmap to compliance with enterprise-level Configuration Management objectives. Employees should first read this process before reading the lower level procedures, to become familiar with the process inputs/outputs, involved stakeholders, handoffs, and objectives. This familiarity will improve your understanding of how the process integrates with our business activities, and will help you comprehend and tailor the constituent procedures to the specifics of your job.

## Definition

 Review is a cornerstone practice of the highly complex industries governed by ISO9001 that ensures work is correct, complete, compliant, and feasible prior to use (release, delivery). Reviews identify and fix mistakes, create valuable insights that enhance the product (assumptions, risks, opportunities, design tradeoffs), verify feasibility, and promote collaboration between company silos.  
 
To mandate their use, the company defines reviews as a Configuration Management process requirement to be conducted on all changes to engineering data.

### Review Activity Definition
The ideal review activity is *purpose-built* with an **Objective Statement** that sets expectations for reviewers and explains the significance of the activity. A clearly defined objective keeps the team aligned and focused on the appropriate scope of work.

For each review activity, Project Engineering or Configuration Management shall determine the following attributes and document them in a **Review Record**:  
* Objective statement including:
  * What is the next stage for the artifact after review 
  * What are the primary elements to review
  * When should the review be completed
* Links to Review Templates (checklists, review forms)
* Supporting technical materials (drawings, data, planning documents)

>[!NOTE]
The Objective Statement should largely be copied or paraphrased from the initiating **Change Vehicle** (Problem Report, Engineering Change Request, Engineering Change Order).
### Approval  

The output of a review activity is **Approval**, in which the Reviewer tells the Owner if they **Accept** or **Reject** the work. The significance of an approval is based on the review activity circumstances. Generally, acceptance progresses the work toward its end state (release, delivery), and rejection regresses the work to a prior state. Reviewers are the *gatekeepers* of work releases, and for this reason, they need to be aware of what it means to accept work during a review.

Approvals shall be documented in the Review Record by the following elements:
* The reviewer's name
* The approval status (**Accepted** or **Rejected**)  
* The date of the approval  

Similar to reviews activities, the act of approval can take many forms and is called by many different names (approve, sign off, verify). Formal approvals shall be managed in a controlled digital environment such as a **Product Lifecycle Management** tool (PLM). The table below lists common examples of approvals of increasing formality and corresponding review levels.


| Work Under Review  | Approval     | Review Record| Review Level|
| ----------------------- | ------------------ | ---| ---|
| Functional Baseline draft | Customer verbally agrees with the proposed baseline.| Design Review Meeting Form| Peer Review
| Drawing Draft Revision| Reviewer emails Owner stating the work is ready to be submitted in an **Engineering Change Order** (ECO).|Email| Internal Review
| Drawing ECO Revision | Reviewer approves an ECO in PLM.| PLM Report| Internal or Peer Review
| Production Unit Delivery| Inspector verifies the delivered unit.| Contract Letter| Internal Review
### Objective

This process, including its constituent documents in **CMH-01**, provides clear and compliant methods to review changes to engineering data across the complete product lifecycle. 

### When to use Review Changes
This process must be followed whenever performing changes to engineering data from Contract Award to product obsolescence, and it is applicable to all programs and contracts. 

## Review Guidelines

The following sections describe the role of each domain in a review activity.

### Change Board

The Change Board is the only domain that must review every change within their project scope.


Since **Customer Approval** is a common requirement to release ECOs, the company designates employees to communicate with customer **Points of Contact** (POCs) on a regular basis. All project teams under contract must form a **Change Board** comprised of these individuals who guide the customer through the change process. 

Change Boards for certain programs, such as **Build-to-Prints** (BTPs) executing mostly minor changes, may consist of only one member with the required technical skill, project knowledge, and customer relationship. At the other extreme, Change Boards for safety-critical products may require participation from Speciality Engineering and Quality to provide technical support and process assurance.

>[!NOTE]
At least one member of a Change Board must be responsible for the financial aspects of changes. For 1-member boards, this role is typically performed by Project Engineering.

The table below lists common examples of functions in this role and their responsibilities.

| Function                    | Responsibility     |
| ----------------------- | ------------------ |
| Project Engineer|Ensure changes are estimated, scheduled, and implemented correctly|
| Program Manager| Ensures changes are implemented on plan (schedule/cost)|

 The Change Board is the primary customer interface in the Configuration Management process and ensures the customer understands and agrees to all technical and programmatic aspects of changes.  

### Mechanical Engineering


#### Internal Review
* Drawing standard compliance; see [blank]
* Material selection standard compliance; see [blank]

#### Peer Review
* Physical configuration attributes:
  * Size
  * Weight
  * Volume
  * Materials

* Capability to meet environmental requirements:
  * Vibration, shock, and structural deformation
  * Acoustic/structural noise
  * Material ingress (sand and dust, water, humidity)

### Electrical Engineering
#### Internal Review
* Schematic and layout standard compliance; see [blank]
* Electrical component selection standard compliance; see [blank]

#### Peer Review
* Electrical configuration attributes:
  * Power distribution
  * Component derating

* Capability to meet environmental requirements:  
  * Electromagnetic Interference (EMI) (Emissions, Susceptibility)
  * Thermal management
  * Adverse power conditions (Inrush, Voltage Spike, Voltage Transients)

### Systems Engineering
#### Internal Review
* Requirements writing and management standard compliance; see [blank]
* Requirements definition and traceability

#### Peer Review
* System configuration attributes:
  * Interfaces
  * Interchangeability
  * Functional architecture
  * Key characteristics

* System analysis:
  * Behavioral and Performance Analysis
  * Functional Hazard Analysis
  * Validation (correct system) and Verification (system is correct)

### Project Engineering


### Speciality Engineering

### Configuration Management

#### Internal Review
* Change Verification:
  * Revision block and signatures on front page
  * Revision on subsequent pages
  * Page-level revisions
  * ECO description matches the actual changes
  * Documentation revisions match the ECO configuration
  * Review Record is valid

#### Peer Review
* Change attributes:
  * Change Classification
  * Change Board composition
  * ECO workflow
  
* Traceability across **CM01** activities 
### Program Management

### Quality

### Supply

