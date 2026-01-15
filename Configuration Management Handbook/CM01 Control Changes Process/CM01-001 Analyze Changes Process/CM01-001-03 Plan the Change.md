---
title: "Plan the Change"
author: "David Ricart"
project: "ProcessWiki"
genre: "procedure"
domains:
    - Engineering
    - Configuration Management
tags:
    - Traceability
    - Identification
---

# Plan Changes
### References
Number |  Title                                   |
| ----- | --------------------------------------- |
|MIL-HDBK-61B with Change 1| Configuration Management Guidance |
# Roles and Responsibilities
| Role                    | Responsibility     |
| ----------------------- | ------------------ |
| Owner| Submits Change Request with initial scoping|
| Change Board  | Reviews and approves, modifies, or rejects scoping|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) and best practices to scope engineering changes.

### Definition
Planning is the second step of the **Analyze the Change** process. The scoping activity starting point is the **Initiating Part Number** (IPN), documented in the **Engineering Change Request**. By reviewing the IPN in the **Product Lifecycle Management** tool (PLM), the Owner identifies the **Configuration Items** (CIs) affected by the change (**Affected Items**), as well as expected **Verification Activities** (testing, analysis, documentation) to ensure the change is fully defined. The Owner documents the scoping activity in the **Engineering Change Request** (ECR). The **Change Board** reviews and approves the ECR, automatically converting it to an ECO which will trigger the next set of procedures in the **Control Changes** process. 

### When to use Scope Changes
The Owner of the change must use this procedure when submitting Engineering Change Requests (ECRs). 

Review Board members tasked with reviewing ECRs should use this procedure as reference.

### Best Practices

#### Review the IPN Parts Lists and Where Used References in PLM
You should determine the impacts of changes to the IPN, especially to controlled interfaces and integrations, when scoping changes. This practice helps identify potentially affected baselines (system, assembly).
#### Review Product Baseline and Configuration Documentation
You should review the **Configuration Documentation** of the affected baseline(s), including interface control documents (ICDs), wiring diagrams, functional diagrams, and system safety analyses (SSAs), to determine which items within the baseline(s) are potentially impacted.  
#### Identify test items to verify acceptability of Class I changes
You should identify any required updates to test items (schedules, plans, procedures, test configurations) to be included in the **Affected Items**.  

#### Prioritize Schedule Drivers
You should prioritize the changes that significantly influence scheduled activities (production, procurement, testing).

#### Prioritize Higher Level Changes

Changes to complex systems may include multiple **Affected Items** with parent-child relationships (interface control diagram provides the required definition for a wiring diagram). You should prioritize the higher level changes so the items that require their inputs are not subject to regression/re-work.
#### Review Applicable Control Procedures
You should reference **CM01-002 Perform Changes**, **CM01-003 Review Changes**, and their subordinate procedures, to support change planning estimates.
### Plan the Change Procedure

#### Owner

Working in the **Class Approved** ECR:  
1. Identify the **Initiating Part Number**.
2. In PLM, identify and document all CIs impacted by the IPN (**Affected Items**) in the ECR.
3. For each item, identify and document the current (**FromRev**) and future (**ToRev**) version, revision, and/or configuration numbers.
4. Analyze and document potential **Verification Activities** required to fully define and implement the work.
5. Confirm all the ECR details and press OK to convert to an **Engineering Change Proposal** (ECP) with status **Pending Approval**.
6. Submit the ECP to the **Change Board**.

#### Change Board

Working in the ECP:
1. Review the ECP contents.
2. Suggest and make changes if the Owner approves; see **CM01-003-01 Internal Review**.
3. Devise and document an **Implementation Plan** including change sequence/priority, funding work packages, and material/manufacturing/supply instructions.
4. Set a **Preliminary Schedule**: the start date is the date when **Customer Approval** is expected, and the end date is an estimate of when the ECP will be fully implemented.
5. Submit the ECP to the Customer.
   
#### Configuration Management

1. Receive the **Customer Approval** of the ECP.
2. Convert the ECP to an **Engineering Change Order** (status **InWork**) with the **Customer Approval** attached and submit to the Owner.