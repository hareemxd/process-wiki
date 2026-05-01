---
title: Stakeholder Needs
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction  
document_number: MBSE-WI-007
metamodel_domain: Problem Domain Black Box  
metamodel_pillar: Requirements  
domains:  
    - Systems Engineering  
outputs:
    - PSPEC Project Usage
    - Stakeholder Requirements Table
---

# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to import and configure Stakeholder requirements, also known as Performance Specification (PSPEC) requirements, using the MBSE methodology. This process is used when establishing the MBSE baseline of a pre-existing system where a PSPEC has been provided in Cameo Systems Modeler `.mdzip` format.


# DRS Naval Electronics SysML Meta Model

This Work Instruction addresses the **Problem Domain Black Box - Requirements** space of the DRS Naval Electronics Meta Model; see [Figure 1](#fig-drsne-meta-model).

In the Problem Domain, Stakeholder requirements (PSPEC) define the external performance expectations and constraints placed on the System of Interest. Making these requirements accessible within the program model is the prerequisite for all downstream requirements derivation in the Solution Domain.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-drsne-meta-model</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-component-level-landing</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---


# Procedure

<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="minLevel">2</ac:parameter>
  <ac:parameter ac:name="maxLevel">7</ac:parameter>
  <ac:parameter ac:name="type">list</ac:parameter>
  <ac:parameter ac:name="outline">true</ac:parameter>
</ac:structured-macro>

The Modeler's path through this procedure depends on whether the PSPEC model already resides in the same *[Teamwork Cloud](#terms)* environment as the program model. Follow **either** [Import PSPEC Model](#import-pspec-model) **or** [Establish Project Usage](#establish-project-usage), then proceed to [Create Stakeholder Requirements Table](#create-stakeholder-requirements-table).

| Condition | Procedure to follow |
|---|---|
| PSPEC model is **not** yet in TWC | [§ Import PSPEC Model](#import-pspec-model) |
| PSPEC model is already in TWC | [§ Establish Project Usage](#establish-project-usage) |


## Import PSPEC Model

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p>Perform this section only if the PSPEC model is not housed within the same Teamwork Cloud environment as the program model. This section requires the PSPEC <code>.mdzip</code> file to be present on the Modeler's local workstation before beginning.</p>
  </ac:rich-text-body>
</ac:structured-macro>

This section uploads the PSPEC model to Teamwork Cloud so that it can be referenced as a *[project usage](#terms)* by the program model.

1. Open Cameo Systems Modeler and go to **Collaborate >> Login**. Select the server, enter `{your username}` and `{password}`, then **>> Sign In**.
2. Go to **File >> Open Project**. Navigate to the PSPEC `.mdzip` file on the local workstation and open it.
3. Confirm that all supporting models referenced by the PSPEC load without errors.
4. Go to **Collaborate >> Add Project to Server**.
5. Click the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) to open the *[containment tree](#terms)* and select the appropriate *[category](#terms)* for the PSPEC.
6. Add a comment to the text box (the first commit message), then select **Add** to upload the project to TWC.

After completing this section, proceed to [Establish Project Usage](#establish-project-usage).


## Establish Project Usage

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p>This section requires the program model to already exist in Teamwork Cloud. If it has not been created, complete MBSE-WI-002 SysML Project Templates before proceeding.</p>
  </ac:rich-text-body>
</ac:structured-macro>

This section links the PSPEC model to the program model so that PSPEC requirements are accessible within the program's *[containment tree](#terms)* under ***Used Projects***.

1. In Cameo Systems Modeler, go to **Collaborate >> Login** and open the program model via **Collaborate >> Open Server Project**.
2. Go to **Options >> Project Usages**.
3. Click the plus ![plus icon](../assets/MBSE/Plus.png) **>> Use Server Project**.
4. Locate and select the PSPEC model in the TWC server, configure the settings as required, then **OK**.
5. Confirm the PSPEC model appears at the bottom of the containment tree under ***Used Projects***.
6. Go to **Collaborate >> Commit Changes to Server**. Add a comment to the text box (`updated project usages - added PSPEC`), then **Commit**.


## Create Stakeholder Requirements Table

Because PSPEC requirements are contained in a read-only package, a *[requirements table](#terms)* must be created in the program model to produce customized views of the requirements and expose underlying data.

1. In the program model's containment tree, navigate to the package designated to contain stakeholder requirements artifacts.
2. Right-click the package **>> Create Diagram >> Requirements Table**.
3. Set the ***Scope*** of the requirements table to the highest-order package containing all PSPEC requirements.
4. At the top of the requirements diagram pane, select the **Columns** tool to expose additional requirement element data and meta chains as needed.

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>The resulting table displays requirement ID, Name, and textual description by default. Use the **Columns** tool to add further attributes such as Verification Method, State, or Derived From.</p>
  </ac:rich-text-body>
</ac:structured-macro>


# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|conf.1| - |04-30-2026| D. Ricart| Initial draft converted from Standard Operating Practice source (Revision: DRAFT, 19 March 2024).|


# References

The Modeler should review [Table 1](#tab-work-instruction-inputs) to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-work-instruction-inputs</ac:parameter>
</ac:structured-macro>

| Document | Description |
|---|---|
| MBSE-WI-001 Teamwork Cloud Administrator| The Modeler should have access to the required work elements in Teamwork Cloud. |
| MBSE-WI-002 SysML Project Templates| The Modeler should be working in a program model using the DRS Naval Electronics MBSE package framework. |


# Roles and Responsibilities

Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in [Table 2](#tab-raci-roles-definitions) and functional areas are assigned roles in [Table 3](#tab-stakeholder-needs-raci-chart).

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-raci-roles-definitions</ac:parameter>
</ac:structured-macro>

| RACI Role | Definition |
|---|---|
| Responsible | Stakeholder is the owner of the document. |
| Accountable | Stakeholder depends on the document to effectively perform their job duties. |
| Consulted | Stakeholder provides input, which may or may not be optional, to the authoring of the document. |
| Informed | Stakeholder is made aware of the document. |
| Omitted | Not a stakeholder. |

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-stakeholder-needs-raci-chart</ac:parameter>
</ac:structured-macro>

| Function | Role |
|---|---|
| Systems Engineering | R |
| Project Engineering | C |
| Configuration Management | I |
| Electrical Engineering | I |
| Mechanical Engineering | I |
| Software Engineering | I |
| Test Engineering | I |
| Manufacturing | I |
| Specialty Engineering | I |
| Quality | A |
| Training | A |
| Business Development | I |


# Terms

| Term | Definition |
|---|---|
| PSPEC | Performance Specification; the stakeholder requirements document provided as input to the MBSE baseline process |
| Teamwork Cloud (TWC) | the server-based repository where SysML project models are stored and version-controlled |
| Project Usage | a reference to a different project that provides access to that project's model elements |
| Used Projects | the section of the containment tree listing all projects referenced via project usages |
| Requirements Table | a Cameo diagram type that allows the user to view and interact with requirements within a scoped package |
| Category | synonymous with *folder* in Teamwork Cloud |
| Containment Tree | synonymous with *file directory* in Teamwork Cloud |

# Appendix
