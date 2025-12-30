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
| Reviewer  | Reviews and approves, modifies, or rejects scoping|
| Configuration Manager | Monitors compliance with procedures
### Purpose
This document defines the procedure(s) and best practices to scope engineering changes.

### Definition
Planning is the second step of the **Analyze the Change** process. The scoping activity starting point is the **Initiating Part Number** (IPN), documented in the originating **Problem Report**. By reviewing the IPN in the **Product Lifecycle Management** tool (PLM), the Owner identifies the **Configuration Items** (CIs) affected by the change (**Affected Items**), as well as expected verification activities (testing, analysis, documentation) to ensure the change is fully defined. The Owner documents the scoping activity in an **Engineering Change Request** (ECR).  

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

1. Identify the **Initiating Part Number** from the **Problem Report**. 
2. Identify all CIs that are potentially impacted by the change to the **Initiating Part Number**.
3. Document all identified CIs in the ECR.
4. Describe any required testing or activities to verify interchangeability in the ECR.
5. Identify the **Affected Items** of the change.
6. For each item, identify the current ("from") and future ("to") version, revision, or configuration numbers.
