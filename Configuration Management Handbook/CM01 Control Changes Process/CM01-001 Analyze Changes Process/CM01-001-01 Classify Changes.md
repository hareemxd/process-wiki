---
title: "Classify Changes"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
tags:
    - Traceability
    - Collaboration
---

# Classify Changes (Form Fit Function Analysis)
### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|MIL-HDBK-61B with Change 1| Configuration Management Guidance |
# Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner| Submits Change Request with initial classification|
| Reviewer  | Reviews and approves, modifies, or rejects classification|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) and best practices to classify engineering changes.

### Definition
Change Classification is the first step of the **Control Changes** process. Classification routes the change to the appropriate resources for review and implementation. Classes are based on the **Form, Fit, Function** (FFF) impacts of the change.


| Class                    | Description     |
| ----------------------- | ------------------ |
| Class I "Major" |Form Fit Function design change|
| Class II "Minor" | No FFF impact, Documentation only|
| Class III "Admin" | No technical impact

The definitions below are provided in **MIL-HDBK-61B**:

| Term                    | Definition     |
| ----------------------- | ------------------ |
| Form |The shape, size, dimensions, mass, weight, and other physical parameters that uniquely characterize an item. For software, form denotes the language and media|
| Fit | The ability of an item to physically interface or interconnect with or become an integral part of another item|
| Function | The action or actions that an item is designed to perform
| Interchangeable Item | A product which possesses such functional and physical attributes as to be equivalent in performance to another product of similar or identical purposes; and is capable of being exchanged for the other product without selection for fit or performance, and without alteration of the products themselves or of adjoining products, except for adjustment.

### When to use Classify Changes
Owners of changes must use this procedure when submitting Engineering Change Requests (ECRs). 

Review Board members tasked with reviewing ECRs should use this procedure as reference.

### Best Practices

#### Assign Class I to edge or ambiguous cases

Sometimes, changes must be assessed with incomplete information (unknown external interface specification). Assigning Class I to these changes ensures that all potential FFF impacts are routed correctly. The Review Board can re-classify changes at a later stage.

#### Analyze all functional characteristics

The engineer must consider all product characteristics that may impact performance, operation, or verification to design requirements. Interchangeable parts should be zero-impact on the part or larger system's compliance with all specifications.


### Classify Changes Procedure Map
![Classify Change decision tree. Each branch leads to Yes or No decisions determining classification as Class I Major, Class II Minor, or Class III Admin. The flowchart guides users through systematic evaluation of engineering changes based on physical characteristics, interface compatibility, and operational performance impacts.](/classify_change_decision_tree.png)

### Classify Changes Procedure

The Owner should use the decision tree above to guide the classification activity.

1. Determine if the change includes any updates to hardware or software.  
   a. If yes, determine if the change has any FFF impacts.  
**YES = CLASS I**  
**NO  = CLASS II**  
b. If no, determine if the change has any technical impacts.    
**YES = CLASS II**  
**NO  = CLASS III**

2. Record the classification in the ECR.


**Document Control**

* Document Number: CM01-001-01
