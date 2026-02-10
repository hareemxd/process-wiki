---
title: Project Templates
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction
document_number: MBSE-WI-002  
metamodel_domain: not applicable
metamodel_pillar: not applicable 
domains:  
    - Systems Engineering  
outputs:
    - Naval Electronics SysML Project
---

# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to create a new SysML project using the Naval Electronics project template and Naval Electronics MBSE styles.

# Company SysML Meta Model
This Work Instruction applies to all spaces of the company Meta Model; see [Figure 1](#figure1-mbsepr).

:::{figure} ../img/MBSE/peerreviewmetamodel.png
:align: center
:name: figure1-mbsepr

Company Meta Model

:::

The Modeler should review {numref}`table1-pr` to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

```{list-table} Work Instruction Inputs
:header-rows: 1
:name: table1-pr

* - Description
  - Reference
* - The Modeler has access to Cameo Systems Modeler and Teamwork Cloud.
  - Teamwork Cloud Administrator

```
# Roles and Responsibilities
Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in {numref}`table2-pr` and functional areas are assigned roles in {numref}`table3-pr`.

```{list-table} **RACI Roles and Definitions**
:header-rows: 1
:name: table2-pr

* - RACI Role
  - Definition
* - Responsible
  - Stakeholder is the owner of the document.
* - Accountable
  - Stakeholder depends on the document to effectively perform their job duties.
* - Consulted
  - Stakeholder provides input, which may or may not be optional, to the authoring of the document.
* - Informed
  - Stakeholder is made aware of the document.
* - Omitted
  - Not a stakeholder.

```
```{list-table} **Project Templates RACI Chart**
:header-rows: 1
:name: table3-pr

* - Function
  - Role
* - Systems Engineering
  - R
* - Project Engineering
  - C
* - Configuration Management
  - C
* - Electrical Engineering
  - I
* - Mechanical Engineering
  - I
* - Software Engineering
  - I
* - Test Engineering
  - I
* - Manufacturing
  - I
* - Specialty Engineering
  - I
* - Quality
  - A
* - Training
  - A
* - Business Development
  - I

```

# Terms

| Term | Definition |
|---|---|
|Project Usage| a reference to a different project that provides access to that project's model elements|
|Category| synonymous with *folder* in Teamwork Cloud|
|Containment Tree| synonymous with *file directory* in Teamwork Cloud|

# Procedure
## Setup SysML project
### Use the Naval Electronics Project Template

In Cameo Systems Modeler:

1. Go to **Collaborate > Login**. 
2. Select a server, then **OK**, and enter `your username` and `password` **> Sign In**.
3. Go to **Collaborate > Open Server Project**, then select **MBSE WG Style Guide Processes > Open**.

After the project opens: 

4. Go to **File > Save Project As**. Select a local destination, enter `your project name`, then **Save**.  
5. Open the local project, then go to **File > Project Properties**.  
6. Select **More** and go to **Advanced**.  
7. Select **Reset IDs > OK** and **Reset Project ID > OK > OK** to confirm the property updates.  

### Upload New Project to Teamwork Cloud
In the new project:

1. Select **Collaborate > Add Project to Server**.
2. Click the ellipses ![ellipses icon](../img/MBSE/Ellipses.png) to open the *containment tree* and select a *category*.
3. Select **More**, then uncheck **Maintain Mount Points**.
4. Add a comment to the text box (the first commit message of the server project), then select **Add** to upload the project.

### Add the Naval Electronics Styles Project Usage
In the new project:

1. Select **Options > Project Usages**.
2. Click the plus ![plus icon](../img/MBSE/Plus.png) **> Use Server Project**.
3. Inside the **Naval Electronics** category, select **Naval Electronics Profile**.
4. Select the highest version number, then **OK**.
5. Go to **Collaborate > Commit Changes to Server**. Add a comment to the text box (`updated project usages`), then **Commit**. 

# References
# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|ghp.1| - |02-10-2026| D. Ricart| First complete draft deployed to Github Pages using a MyST-powered site generator.|

# Appendix