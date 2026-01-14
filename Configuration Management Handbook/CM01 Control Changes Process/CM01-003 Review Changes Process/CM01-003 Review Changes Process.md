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

 Review is a cornerstone practice of the highly complex industries governed by ISO9001 that ensures work is complete and compliant prior to use (release, delivery). Reviews identify and fix mistakes, create critical knowledge which enhances the product (assumptions, risks, opportunities, design tradeoffs), and promote collaboration between company silos.  
 
To mandate their use, the company defines reviews as a Configuration Management process requirement to be conducted on all changes to engineering data.

### Review Activity Definition
Review activities vary in format, in the list of reviewers, and in the level of detail/formality. Differences are based on specific circumstances (product criticality, scope/depth of changes, resource constraints) to ensure the review activity is *purpose-built*.  

For each review activity, Project Engineering or Configuration Management shall determine the following attributes:  
* Objective Statement with scope and schedule defined (what, why, when)
* Review activity materials (checklists, review forms)
* List of Reviewers

### Approval  

The output of a review activity is **Approval**, in which the Reviewer tells the Owner if they **Accept** or **Reject** the work. The significance of an approval is based on the circumstances of the specific review activity. Generally, acceptance progresses the work toward its end state (release, delivery), and rejection regresses the work to a prior state. 

Approvals shall be documented in a **Review Record** comprised of the following elements:
* The reviewer's name
* The approval status (**Accepted** or **Rejected**)  
* The date of the approval  

Similar to reviews, the act of approval can take many forms. Formal approvals shall be managed in a controlled digital environment such as a **Product Lifecycle Management** tool (PLM). The table below lists common examples of approvals of increasing formality.


| Work Under Review  | Approval     | Review Record|
| ----------------------- | ------------------ | ---|
| Functional Baseline draft | Customer verbally accepts the proposed baseline.| Design Review Meeting Minutes
| Drawing Draft Revision| Reviewer emails Owner stating the work is ready to be submitted in an **Engineering Change Order** (ECO).|Email
| Drawing ECO Revision | Reviewer approves ECO in PLM| PLM Report
### Objective

This process, including its constituent documents in **CMH-01**, provides clear and compliant methods to review changes to engineering data across the complete product lifecycle. 

### When to use Review Changes

#### Change Board

Since customer approval is a common requirement to release ECOs, the company designates employees to communicate with customer **Points of Contact** (POCs) on a regular basis. All product/project development teams under contract must form a **Change Board** comprised of these individuals who are accountable for providing guidance to the customer throughout the change process. The table below lists common examples of functions in this role and their responsibilities.

| Function                    | Responsibility     |
| ----------------------- | ------------------ |
| Project Engineer|Ensure changes are estimated and implemented correctly|
| Supply Chain | Ensures complete flow of requirements to/from vendors/suppliers/manufacturers |  
| Program Manager| Ensures changes are implemented on plan (schedule/cost)|

 The Change Board is the primary customer interface in the Revision Control process and ensures the customer understands and agrees to all technical and programmatic aspects of changes.  


## Reviewer Guidelines

A review activity is only as valuable as the feedback provided by the reviewers.

### Mechanical Engineering

Mechanical Engineering  review checks the following items:
* drawing standard compliance; see [blank]
* material selection standard compliance; see [blank]
* physical configuration attributes (size, weight, volume, material)
* environmental qualification aspects:
  * Vibration, Shock, and Structural Deformation
  * Acoustic/Structural Noise
  * Material Ingress (Sand and Dust, Water, Humidity)

### Electrical Engineering
Electrical Engineering review checks the following items:
* schematic and layout standard compliance; see [blank]
* electrical component selection standard compliance; see [blank]
* electrical configuration attributes (power distribution, component derating)
* environmental qualification aspects:  
  * Electromagnetic Interference (Emissions, Susceptibility)
  * Thermal Management
  * Adverse Power Conditions (Inrush, Voltage Spike, Voltage Transients)
### Software Engineering

### Systems Engineering
Systems Engineering review checks the following items:
* requirements, system analysis, and system design standard compliance; see [blank]
* requirements definition and traceability
* system configuration attributes (interfaces, interchangeability, functional architecture, key characteristics)
* system analysis:
  * Behavioral and Performance Analysis
  * Functional Hazard Analysis
  * Validation (correct system) and Verification (system is correct)

### Project Engineering


### Speciality Engineering

### Configuration Management

### Program Management

### Quality

### Supply

