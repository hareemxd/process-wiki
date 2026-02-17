---
title: Problem Domain Conceptual Subsystems Diagrams
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction  
document_number: MBSE-WI-004
metamodel_domain: Problem Domain White Box  
metamodel_pillar: Structure  
domains:  
    - Systems Engineering  
output: 
    - 
    - 
---


# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to create structural diagrams to represent the *conceptual subsystems* of the *system of interest* (SoI) in the Problem Domain. The SoI is the primary subject of the modeler's efforts, the system to be designed using the architectural definition realized in the system model.
# Company SysML Meta Model

This Work Instruction addresses the **Problem Domain White Box - Structure** space of the Company Meta Model; see [Figure 1](#figure1-pdcs).

The modeler defines the subsystems based on the elements defined at the next-higher structural level (system context). This definition removes one layer of abstraction to create a *white box* view of the SoI. Where the *black box* view defines the inputs and outputs of the SoI via external specifications, the white box view defines the top-level architecture of the SoI, each constituent subsystem itself treated as a black box. Over time, the white box and black box views evolve to meet new external specifications/constraints imposed by the Problem Domain.

:::{figure} ../img/MBSE/PDSCDiagramsMetaModel.png
:align: center
:name: figure1-pdcs

Company Meta Model

:::

The Modeler should review {numref}`table1-pdcs` to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

```{list-table} Work Instruction Inputs
:header-rows: 1
:name: table1-pdcs

* - Description
  - Reference
* - The Modeler should be working in a Model using the company MBSE package framework.
  - Template Work Instruction

```


# Roles and Responsibilities

Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in {numref}`table2-pdcs` and functional areas are assigned roles in {numref}`table3-pdcs`.

```{list-table} RACI Roles and Definitions
:header-rows: 1
:name: table2-pdcs

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

```{list-table} Problem Domain Conceptual Subsystems Diagrams RACI Chart
:header-rows: 1
:name: table3-pdcs

* - Function
  - Role
* - Systems Engineering
  - R
* - Project Engineering
  - C
* - Configuration Management
  - I
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
  - A

```


# Terms

| Term | Definition |
|---|---|
| Problem Domain System Context| the environment containing and surrounding the system of interest during key activities.|
| System of Interest| the primary subject of the modeler's efforts, the system to be designed using the architectural definition realized in the system model.|
|Project Usage| a reference to a different project that provides access to that project's model elements|
|Category| synonymous with *folder* in Teamwork Cloud|
| Resource| synonymous with *file* in Teamwork Cloud|
| Containment Tree| synonymous with *file directory* in Teamwork Cloud|

# Procedure


## Set up Subsystem Context Category
1. Expand **White Box**, then right-click **Subsystem Context (Structure) > Create Package**, and enter `Subsystems`.  
2. Expand **Black Box**, locate the SoI block and drag it into **Subsystem Context (Structure)**.  

## Create Block Definition Diagram

Add elements to diagrams by dragging them from the containment tree. Create relationships by drawing connections in the diagram.

1. Right-click **Subsystems > Create Diagram > SysML Block Definition Diagram**, and enter `[project/system name] Problem Domain Decomposition`.  

### Create Subsystems

1. Create a block in the diagram for each subsystem.
2. Create **Directed Composition** relationships from the SoI to the subsystem blocks.

### Layout the Diagram

In the diagram:  
1. Right-click **Subsystems > Create Diagram > SysML Block Definition Diagram**, and enter `[project/system name] Problem Domain Decomposition`.  
2. Drag the SoI block onto the diagram.  
3. Drag the subsystem blocks onto the diagram.  
4. Use the **Align** tool in the top toolbar to organize, resize, and reposition elements to give the diagram a uniform style.  

>[!NOTE]
All blocks should be the same size.

# References


# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|


# Appendix


