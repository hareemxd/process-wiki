---
title: "Scope Changes"
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

# Scope Changes
### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|MIL-HDBK-61B with Change 1| Configuration Management Guidance |
# Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner| Submits Change Request with initial scoping|
| Reviewer  | Reviews and approves, modifies, or rejects scoping|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) and best practices to scope engineering changes.

### Definition
Change Scoping is the second step of the **Control Changes** process. Scoping identifies the Configuration Items affected by the change (**Affected Items**), as well as verification activities (testing, analysis) to ensure complete change definition.  

### When to use Scope Changes
Owners of changes must use this procedure when submitting Engineering Change Requests (ECRs). 

Review Board members tasked with reviewing ECRs should use this procedure as reference.

### Best Practices

#### Review Parts Lists and Where Used References in PLM
If a change impacts a part or assembly's interface or integration with existing designs, those impacts must be identified and documented as part of the change request process. 
#### Review Product Baseline and Configuration Documentation
Review all supporting documentation in the affected baselines, including interface control documents, wiring diagrams, functional diagrams, and safety/reliability analyses, to determine which artifacts within the baseline are potentially impacted by the change.  
#### For Class I, Describe Required Testing  
FFF-impact updates usually require some level of testing to prove that the new part(s) meet existing requirements.
#### For Class II HW/SW, Describe Approach to Verify Interchangeability

The approach may include simulation/modeling or analysis by extension to similar products. The Owner should describe the plan in the ECR.

### Scope Changes Procedure

1. Identify the **Initiating Part Number** from the Problem Report. 
2. Identify all CIs that are potentially impacted by the change to the **Initiating Part Number**.
3. Document all identified CIs in the ECR.
4. Describe any required testing or activities to verify interchangeability in the ECR.


**Document Control**

* Document Number: CM01-001-02

