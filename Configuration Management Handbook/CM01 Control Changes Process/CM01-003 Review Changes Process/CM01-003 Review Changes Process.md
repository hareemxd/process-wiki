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
|CM-RC-001| Schematic Review Checklist|
|CM-RC-002| Mechanical Drawing Review Checklist|
|CM-RC-003| Requirements Review Checklist|
|CM-RC-004| Configuration Management Review Checklist|
|CM-RC-005| Component Selection Review Checklist
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

The following subsections describe the components and conduct of review activities.

### Objective Statement
A review activity should be purpose-built with an **Objective Statement** that sets expectations for reviewers and explains the significance of the activity. A clearly defined objective keeps everyone aligned and focused on the appropriate scope of work.

The Objective Statement includes the following details:  
* Primary elements to review
* **End Use** of the work (development activity, production unit)
* Review activity closure date

Formal review activities should be guided with an Objective Statement. The Statement may be omitted if all participants understand the expectations and significance of the activity.
### Activity Roles
Each review activity includes (minimally) two participants: the **Owner** and the **Reviewer**. A third role, **Quality Reviewer**, is included as required by product, program, or contractual requirements. The table below provides the  definition of each role.

| Role                    | Definition     |
| ----------------------- | ------------------ |
| Owner| Responsible for the work under review. The Owner completes the work, initiates the review activity, and resolves **Comments** with reviewers.|
| Reviewer | Assigned to review the work. The Reviewer applies their domain expertise and/or familiarity with the work to make comments, resolve them with the Owner, and provide **Approval** of the work. |
| Quality Reviewer| Responsible for verifying comment resolutions. The Quality Reviewer ensures the Owner incorporated feedback from reviewers as described in the **Review Record**.|

### Comments


### Approval  

The goal of all review activities is to gain reviewer acceptance through their **Approval**, in which the Reviewer tells the Owner if they **Accept** or **Reject** the work. Acceptance progresses the work toward its End Use and rejection regresses the work to a prior state. 


Review activities shall conclude only once all reviewers have provided  **Approval**.
### Review Record

The Review Record is the artifact documenting the review activity. Artifacts range in formality from an email between participants to a **Peer Review Form** (PRF) structured with a template.

All review activities shall be documented with a Review Record containing the following data:
* Participants (name and domain)
* Activity closure date
* **Approval** status of each reviewer


### When to use Review Changes
This process must be followed whenever performing changes to engineering data from Contract Award to product obsolescence, and it is applicable to all programs and contracts. 

## Review Domains

The following sections describe the role of each domain in a review activity. The lists are illustrative and not exhaustive.

### Change Board

The Change Board is a unique domain that must review every PLM-released change within their project scope.


Since **Customer Approval** is a common requirement to release ECOs, the company designates employees to communicate with **Points of Contact** (POCs) on a regular basis. All project teams under contract must form a **Change Board** comprised of these individuals who guide the customer through the change process. 

Change Boards for certain programs, such as **Build-to-Prints** (BTPs) executing mostly minor changes, may consist of only one member with the required technical skill, project knowledge, and customer relationship. At the other extreme, Change Boards for safety-critical products may require participation from Speciality Engineering and Quality to provide technical support and process assurance. Any domain with expertise (Supply, Manufacturing) can play a critical role in a Change Board.

>[!NOTE]
At least one member of a Change Board shall be responsible for the financial aspects of changes. For 1-member boards, this role is typically performed by Project Engineering.

The table below lists common examples of functions in this role and their responsibilities.

| Function                    | Responsibility     |
| ----------------------- | ------------------ |
| Project Engineer|Ensure changes are estimated, scheduled, and implemented correctly|
| Program Manager| Ensures changes are implemented on plan (schedule/cost) and per customer expectations|

 The Change Board is the primary customer interface in the Configuration Management process and ensures the customer understands and agrees to all technical and programmatic aspects of changes.  

### Mechanical Engineering


#### Internal Review
* Drawing and material selection standard compliance; see **CM-RC-002 Mechanical Drawing Review Checklist**

#### Peer Review
* Physical configuration attributes:
  * Size
  * Weight
  * Materials
  * Physical interchangeability and modularity

* Capability to meet environmental requirements:
  * Vibration, shock, and structural deformation
  * Acoustic/structural noise
  * Material ingress (sand and dust, water, humidity)

### Electrical Engineering
#### Internal Review
* Schematic and layout standard compliance; see **CM-RC-001 Schematic Review Checklist**
* Electrical component selection standard compliance; see **CM-RC-005 Component Selection Checklist**

#### Peer Review
* Electrical configuration attributes:
  * Power distribution
  * Component derating
  * Electrical/Electronic interchangeability and modularity 

* Capability to meet environmental requirements:  
  * Electromagnetic Interference (EMI) (Emissions, Susceptibility)
  * Thermal management
  * Adverse power conditions (Inrush, Voltage Spike, Voltage Transients)

### Systems Engineering
#### Internal Review
* Requirements writing and management standard compliance; see **CM-RC-003 Requirements Review Checklist**
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
* Change Verification; see **CM-RC-004 Configuration Management Review Checklist**
 <!-- * Revision block and signatures on front page
  * Revision on subsequent pages
  * Page-level revisions
  * ECO description matches the actual changes
  * Documentation revisions match the ECO configuration
  * Review Record is valid
  * -->

#### Peer Review
* Change attributes:
  * Change Classification
  * Change Board composition
  * ECO workflow
  
* Traceability across **CM01** activities 
### Program Management

#### Internal Review
* Work alignment to customer preferences and expectations
* Work alignment to program plan

### Quality

### Supply

