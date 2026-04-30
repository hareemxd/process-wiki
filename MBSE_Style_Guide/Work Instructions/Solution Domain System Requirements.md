---
title: Solution Domain System Requirements
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction  
document_number: MBSE-WI-006
metamodel_domain: Solution Domain  
metamodel_pillar: Requirements  
domains:  
    - Systems Engineering  
outputs:
    - Requirements Table
    - Requirements Derivation Table
    - Relationship Map Diagram
    - Dependency Matrix
---

# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to develop system level requirements using the MBSE methodology. This process is used when establishing the MBSE baseline of a pre-existing system, and ensures that new requirements artifacts conform to DRS Naval Electronics process and quality standards.


# DRS Naval Electronics SysML Meta Model

This Work Instruction addresses the **Solution Domain - Requirements** space of the DRS Naval Electronics Meta Model at the System Level; see [Figure 1](#fig-drsne-meta-model).

The Requirements Pillar of the Solution Domain captures the system-level requirements and their relationships. Within this work scope, MBSE Engineers develop specific configurations of Requirements Tables, Requirements Derivation Tables, Relationship Map Diagrams, and Dependency Matrices that together provide full traceability from customer documentation through verification.

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
  <ac:parameter ac:name="">fig-system-level-solution-landing</ac:parameter>
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

The following sections describe how each requirements artifact is developed and the information required to consider it complete.

## Package Setup

Requirements in Cameo Systems Modeler are heavily affected by the containment relationship, so the package structure that contains the model's requirements is highly prescriptive. Follow the package structure shown in [Figure 3](#fig-requirements-package-structure), which separates Functional, Non-Functional, and Verification Requirements.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-package-structure</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

Each requirement type package can be refined further by adding categories as shown in [Figure 4](#fig-requirements-categories).

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-categories</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---


## Create Requirements Tables

Requirements are developed via interaction with the *[requirements table](#terms)* diagram, which allows the user to create, manage, and change requirements. A requirements table is created for each of the three requirement types under their package as shown in [Figure 5](#fig-requirements-table-location).

1. Right-click the requirement type package **>> Create Diagram >> Requirements Table**.
2. Set the table scope to the requirement type package under which it was created; see [Figure 6](#fig-requirements-table-context).

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-table-location</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-table-context</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

### Configure Attribute Columns

Set up attribute columns to display the standard attributes of a DRS Naval Electronics Requirement. See [Appendix A](#appendix) for required and optional attributes.

1. At the top of the requirements diagram pane, select the **Columns** tool; see [Figure 7](#fig-requirements-table-attributes).
2. Add the columns required for the applicable requirement type per [Figure 8](#fig-functional-requirements-table), [Figure 9](#fig-non-functional-requirements-table), or [Figure 10](#fig-verification-requirements-table).

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-table-attributes</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-functional-requirements-table</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-non-functional-requirements-table</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-verification-requirements-table</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

### Create New Requirements

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p>Only the custom requirement stereotypes used in the Naval Electronics Profile shall be used. Other stereotypes will break the velocity script that exports requirements to MS Word.</p>
  </ac:rich-text-body>
</ac:structured-macro>

The DRS Naval Electronics division uses a customized requirements profile, so ensure the correct ***ne_*** requirement type is used for the package (e.g. a ***Non-Functional_Rqmt*** type in a non-functional requirement package).

1. Select the **Add New** tool at the top of the requirements table; see [Figure 11](#fig-create-new-requirement).
2. Select the appropriate ***ne_*** requirement stereotype for the containing package.
3. Populate the requirement attributes per the *DRS Naval Electronics Requirements Writing Guide*.
4. Update the requirement's ***State*** in accordance with [Appendix B](#appendix).

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-create-new-requirement</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---


## Create Requirements Derivation Tables

Requirements Derivation Tables are a review tool that ensures total traceability between the parent specifications/documentation and the system requirements model. Create a derivation table for each requirement type under the corresponding package; see [Figure 12](#fig-requirements-derivation-location).

1. Right-click the requirement type package **>> Create Diagram >> Requirements Derivation Table**.
2. Configure the diagram criteria per [Figure 13](#fig-requirements-derivation-setup):
   a. ***Row Element Type*** is set to ***AbstractRequirement***.
   b. ***Column Element Type*** is set to ***AbstractRequirement***.
   c. ***Dependency Criteria*** is set to ***DeriveReqt***.
   d. ***Row Scope*** is set to the system level requirement type package.
   e. ***Column Scope*** is set to the customer requirements/documentation being traced to.
3. Inspect the resulting traceability and create relationships where required to achieve full traceability; see [Figure 14](#fig-requirements-derivation-example) for a properly configured example.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-derivation-location</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-derivation-setup</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-requirements-derivation-example</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---


## Create Relationship Map Diagrams

The *[Relationship Map Diagram](#terms)* is a requirements review tool that visually shows the relationships between requirements. It is used in the requirements review to understand the full traceability of a requirement. One Relationship Map Diagram is created per Functional Requirement under the requirement type package; see [Figure 15](#fig-relationship-map-location).

1. Right-click the functional requirements package **>> Create Diagram >> Relationship Map Diagram**.
2. Set the relationship criteria to the values shown in [Figure 16](#fig-relationship-map-criteria).
3. Drag and drop the requirement for which this diagram is being made onto the ***Context*** input.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-relationship-map-location</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-relationship-map-criteria</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

### Create Generic Table for Relationship Maps

Because a large number of relationship maps are created, a *[generic table](#terms)* is used to list all of them.

1. Under the functional requirements package, create a generic table; see [Figure 17](#fig-relationship-map-generic-location).
2. Configure the table per [Figure 18](#fig-relationship-map-generic-setup):
   a. ***Element Type*** is set to ***Diagram***.
   b. ***Scope*** is set to the functional requirements package under which the diagrams were created.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-relationship-map-generic-location</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-relationship-map-generic-setup</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---


## Create Dependency Matrices

*[Dependency Matrices](#terms)* are used to review the traceability of non-functional and verification requirements to functional requirements. Create one Dependency Matrix in each of the non-functional and verification requirement type packages; see [Figure 19](#fig-dependency-matrices-location).

1. Right-click the requirement type package **>> Create Diagram >> Dependency Matrix**.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-dependency-matrices-location</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

### Configure Non-Functional Dependency Matrix

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>***Row Scope*** is the non-functional requirements package and ***Column Scope*** is the functional requirements package.</p>
  </ac:rich-text-body>
</ac:structured-macro>

1. Set up the criteria for the non-functional Dependency Matrix as shown in [Figure 20](#fig-non-functional-criteria).

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-non-functional-criteria</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

### Configure Verification Dependency Matrix

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>***Row Scope*** is the verification requirements package and ***Column Scope*** is the functional requirements package.</p>
  </ac:rich-text-body>
</ac:structured-macro>

1. Set up the criteria for the verification Dependency Matrix as shown in [Figure 21](#fig-verification-criteria).

The resulting diagram should look similar to [Figure 22](#fig-dependency-matrix-example).

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-verification-criteria</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-dependency-matrix-example</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename=""/>
</ac:image>

---


# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|conf.1| - |04-30-2026| D. Ricart| Initial draft converted from Standard Operating Practice source.|


# References

The Modeler should review [Table 1](#tab-work-instruction-inputs) to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.


<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-work-instruction-inputs</ac:parameter>
</ac:structured-macro>

| Document | Description |
|---|---|
| MBSE-WI-001 Teamwork Cloud Administrator| The Modeler should have access to the required work elements in Teamwork Cloud. |
| MBSE-WI-002 SysML Project Templates| The Modeler should be working in a Model using the DRS Naval Electronics MBSE package framework. |
| DRS Naval Electronics Requirements Writing Guide| Provides specific instructions on how to write requirements and the information that goes in each field of the requirements table. |


# Roles and Responsibilities

Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in [Table 2](#tab-raci-roles-definitions) and functional areas are assigned roles in [Table 3](#tab-system-requirements-raci-chart).


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
  <ac:parameter ac:name="">tab-system-requirements-raci-chart</ac:parameter>
</ac:structured-macro>

| Function | Role |
|---|---|
| Systems Engineering | R |
| Project Engineering | C |
| Configuration Management | C |
| Electrical Engineering | I |
| Mechanical Engineering | I |
| Software Engineering | I |
| Test Engineering | C |
| Manufacturing | I |
| Specialty Engineering | I |
| Quality | A |
| Training | A |
| Business Development | I |


# Terms

| Term | Definition |
|---|---|
| Requirements Table| a Cameo diagram type that allows the user to create, manage, and change requirements within a containing package |
| Requirements Derivation Table| a review tool that traces system requirements to their parent specifications/documentation |
| Relationship Map Diagram| a review tool that visually shows the relationships between a requirement and the elements it traces to |
| Generic Table| a Cameo diagram type that lists model elements matching a configured element type and scope |
| Dependency Matrix| a review tool that traces non-functional and verification requirements to functional requirements |
| AbstractRequirement| the SysML metaclass shared by all requirement stereotypes; used as the row/column element type in derivation tables |
| DeriveReqt| the SysML dependency stereotype used to trace a derived requirement to its source |


# Appendix

## Appendix A: Requirement Completion Instructions

Each line entry in a Requirements Table represents a requirement object and its associated data of interest.

### Functional Requirements

| Attribute | Required / Optional | Description |
|---|---|---|
| # | NA | A dynamic line number generated by the tool to keep track of your place in a requirements table. Not directly linked to a requirement object; changes based on filtering and sorting. |
| ID | Required | The unique ID of the requirement. This string shall be used to reference the requirement in all cases. The string is specifically coded to inform the reader of its requirement type, where `CON` refers to "Console". |
| Name | Required | The unique descriptive name of the requirement. |
| Text | Required | The formal requirement sentence body. |
| Rationale | Optional | Describes the originating systems engineer's intent with the creation of the requirement and its text. It should be a statement as to WHY the requirement is needed. |
| Supporting Text | Optional | Describes concepts introduced in the Text field which require further elaboration to substantiate or understand the requirement. |
| Verification Method | Required | Describes the intended method by which the requirement will be verified. Available in a drop-down list of 4 options. |
| Derived From | Required (before Approval State) | Lists the higher order PSPEC, standard, or doctrinal source from which this requirement is derived. |
| Refined By | Optional | Lists the non-functional requirements which constrain the functional requirement. |
| Verified By | Required (before Approval State) | Lists the verification requirements which constrain the verification method of the functional requirement. |
| State | Required | Describes the current state of the requirement. Available in a drop-down list of multiple options. |
| Documentation | Optional | Contains links or embedded documents referenced in the Text, Rationale, or Supporting Text fields. May also contain issues/comments to be resolved while the requirement is in NewDraft/InChange state. |

### Non-Functional Requirements

| Attribute | Required / Optional | Description |
|---|---|---|
| # | NA | A dynamic line number generated by the tool to keep track of your place in a requirements table. Not directly linked to a requirement object; changes based on filtering and sorting. |
| ID | Required | The unique ID of the requirement. This string shall be used to reference the requirement in all cases. The string is specifically coded to inform the reader of its requirement type, where `CON` refers to "Console". |
| Name | Required | The unique descriptive name of the requirement. |
| Text | Required | The formal requirement sentence body. |
| Rationale | Optional | Describes the originating systems engineer's intent with the creation of the requirement and its text. It should be a statement as to WHY the requirement is needed. |
| Supporting Text | Optional | Describes concepts introduced in the Text field which require further elaboration to substantiate or understand the requirement. |
| Verification Method | Required | Describes the intended method by which the requirement will be verified. Available in a drop-down list of 4 options. |
| Derived From | Required (before Approval State) | Lists the higher order PSPEC, standard, or doctrinal source from which this requirement is derived. |
| Refines | Optional | Lists the functional requirements which this non-functional requirement constrains. |
| Verified By | Required (before Approval State) | Lists the verification requirements which constrain the verification method of the functional requirement. |
| State | Required | Describes the current state of the requirement. Available in a drop-down list of multiple options. |
| Documentation | Optional | Contains links or embedded documents referenced in the Text, Rationale, or Supporting Text fields. May also contain issues/comments to be resolved while the requirement is in NewDraft/InChange state. |

### Verification Requirements

| Attribute | Required / Optional | Description |
|---|---|---|
| # | NA | A dynamic line number generated by the tool to keep track of your place in a requirements table. Not directly linked to a requirement object; changes based on filtering and sorting. |
| ID | Required | The unique ID of the requirement. This string shall be used to reference the requirement in all cases. The string is specifically coded to inform the reader of its requirement type, where `CON` refers to "Console". |
| Stereotype | Required | One of `Non-Functional_Reqt`, `Functional_Req't`, or `Verification_Req't`. |
| Name | Required | The unique descriptive name of the requirement and ID. |
| Text | Required | The formal requirement sentence body. |
| Rationale | Optional | Describes the originating systems engineer's intent with the creation of the requirement and its text. It should be a statement as to WHY the requirement is needed. |
| Supporting Text | Optional | Describes concepts introduced in the Text field which require further elaboration to substantiate or understand the requirement. |
| Verification Method | Required | Describes the intended method by which the requirement will be verified. Available in a drop-down list of 4 options. |
| Derived From | Required (before Approval State) | Lists the higher order PSPEC, standard, or doctrinal source from which this requirement is derived. |
| Verifies | Required (before Approval State) | Lists the functional requirements which this verification requirement constrains the Verification Method of. |
| State | Required | Describes the current state of the requirement. Available in a drop-down list of multiple options. |
| Documentation | Optional | Contains links or embedded documents referenced in the Text, Rationale, or Supporting Text fields. May also contain issues/comments to be resolved while the requirement is in NewDraft/InChange state. |

## Appendix B: Requirement States

| State | Description |
|---|---|
| NewDraft | The requirement is a newly authored, draft requirement. |
| InChange | A previously Approved requirement is in the process of being changed, either being reworded or deleted. |
| InReview | The requirement is in the requirements peer review process. |
| Rejected | A NewDraft requirement has been rejected in the requirements peer review process for implementation in the program baseline. |
| Deleted | A previously Approved requirement has been deleted from the program baseline through a requirements peer review or change control board. |
| Approved | A requirements peer review has approved a NewDraft or InChange requirement for implementation in the program baseline. |
| Allocated | An Approved requirement has been allocated in the program baseline and is awaiting implementation in a specified future release. |
| Deferred | Implementation of an Approved requirement has been deferred to a to be determined (TBD) future program release. |
| Implemented | An Approved requirement has been implemented in a specified program release. |
