---
title: Problem Domain Black Box Behavior Diagrams
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction  
document_number: MBSE-WI-004
metamodel_domain: Problem Domain Black Box  
metamodel_pillar: Behavior
domains:  
    - Systems Engineering  
output: 
    - Use Case Diagram
    - Activity Diagram
---

# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to create behavioral diagrams in the problem domain.  

# DRS Naval Electronics SysML Meta Model

This Work Instruction addresses the **Problem Domain Black Box - Behavior** space of the DRS Naval Electronics Meta Model; see [Figure 1](#fig-drsne-meta-model).

In the Problem Domain, the SoI is modeled as a *black box*; only the external boundaries and connections are defined. The black box perspective helps the modeler identify the most fundamental SoI specifications: external interfaces, and the states, behaviors, and functions inferred from its inputs and outputs. Allocating these specifications to discrete objects within the SoI gives rise to structure in the system model.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-drsne-meta-model</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p><strong>Figure 1.</strong> DRS Naval Electronics Meta Model</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="PDBBBDiagramsMetaModel.png"/>
</ac:image>

---

The Modeler should review [Table 1](#tab-work-instruction-inputs) to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.


<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-work-instruction-inputs</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="tip">
  <ac:rich-text-body>
    <p><strong>Table 1.</strong> Work Instruction Inputs</p>
  </ac:rich-text-body>
</ac:structured-macro>

| Description | Reference |
|---|---|
| The Modeler should have access to the required work elements in Teamwork Cloud. | MBSE-WI-001 Teamwork Cloud Administrator |
| The Modeler should be working in a Model using the DRS Naval Electronics MBSE package framework. | MBSE-WI-002 Project Templates |
| The Modeler should be working in a Model with a defined System Context (Structure) in the Problem Domain. | MBSE-WI-004 Problem Domain System Context Diagrams |


# Roles and Responsibilities

Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in [Table 2](#tab-raci-roles-definitions) and functional areas are assigned roles in [Table 3](#tab-raci-chart).


<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-raci-roles-definitions</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="tip">
  <ac:rich-text-body>
    <p><strong>Table 2.</strong> RACI Roles and Definitions</p>
  </ac:rich-text-body>
</ac:structured-macro>

| RACI Role | Definition |
|---|---|
| Responsible | Stakeholder is the owner of the document. |
| Accountable | Stakeholder depends on the document to effectively perform their job duties. |
| Consulted | Stakeholder provides input, which may or may not be optional, to the authoring of the document. |
| Informed | Stakeholder is made aware of the document. |
| Omitted | Not a stakeholder. |


<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-raci-chart</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="tip">
  <ac:rich-text-body>
    <p><strong>Table 3.</strong> Problem Domain Black Box Behavior Diagrams RACI Chart</p>
  </ac:rich-text-body>
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
| Business Development | A |


# Terms

# Procedure

## Identify and Define Use Cases

A *use case* is a description of a system's operation in context that meets a user need. This description creates a clear basis for identifying system functions considered essential/critical by the end-user. 

The Use Case Diagram (UCD) is the highest level behavior diagram. Accordingly, behavioral system modeling starts with the UCD before proceeding to the Activity Diagram (AD), which is based on the UCD and further specifies the identified functions in an *activity*. Each UCD is associated with (at least) one Activity Diagram (AD).

For more information on identifying and defining use cases, see [blank].  

## Import Behavioral Diagram Template

Use this procedure for each identified use case.
 
1. Navigate to the **DRS Naval Electronics Profile > Templates**, then expand **Use Case, UCD, AD**.  
2. Right-click **Template UC > Copy**, right-click the **1 Use Cases** package in your model and **Paste**.  
3. Rename the Use Case `Use Case Name UC`, the nested diagram `Use Case Name UCD`, the nested activity `Use Case Name AD`, and the lower nested diagram `Use Case Name AD`.  

## Create Use Case Diagram

1. Open the Use Case Diagram, delete all placeholder content, and enter `Use Case Name UCD` into the title text box.  
2. Write the pre-conditions that are required for the use case to begin.  
3. Write the Use Case Description.  
   a. Architecture Level: the domain of the diagram (Problem Domain Black Box)  
   b. Main Operational Concept: a brief description of the use case  
   c. Primary Actor(s) 
   d. Participating Actor(s)
   e. Trigger: a brief description of the context, state, or set of conditions which immediately precedes or initiates the use case  
   f. Main Success Behavioral Flow: a detailed description of the successful use case 
   g. Alternate Flow: a description of the failed use case  
   h. Exceptional Flow  
4. From the **System Context (Structure)** package, drag the SoI (top center) and the appropriate actors (left) and the external systems (right) onto the diagram.  
5. Create **Associations** between the UC and the SoI, actors, and external systems.  
6. Use the **Align** tool in the top toolbar to resize and reposition the diagram elements to look organized and uniform.  

<ac:Structured-macro ac:name="info">
<ac:rich-text-body>
<p>The description fields must be valid as they will be re-used in the Activity Diagram.</p>
</ac:rich-text-body>
</ac:structured-macro>

## Create Activity Diagram

1. Open `Use Case Name AD`, delete all placeholder content, and enter `Use Case Name AD` into the title text box.  
2. Confirm the UCD's pre-conditions are displayed in the Pre-Conditions Comment.

### Create Swimlanes

A swimlane is a vertical frame (column) within the activity diagram that is allocated to a specific entity (SoI, actor, external system). All activities within a swimlane must be owned by the same entity.  

Create swimlanes first to aid with the general structuring and layout of the activity diagram.  

Swimlanes should be ordered so the general flow of the activity diagram proceeds from left to right and top to bottom.  

Each entity included in the UCD should have an allocated swimlane in the associated AD.  

1. Right-click a placeholder swimlane, then **Insert Swimlane** and choose the position (left or right) for the new swimlane.
2. Drag entities from **1 System Context (Structure)** into the swimlane headers to allocate swimlanes to entities.

### Create Successful Flow

The successful flow defined in the UCD describes the system's operation to execute the **Main Operational Concept** from start to finish.

1. Create the **Initial Node**. Name the element to match the **Trigger** of the Use Case Description.  
2. Create the **Call Behavior Actions** which outline the successful flow and place them into the appropriate swimlanes.
3. Create the **Control Flows** to connect actions occurring in sequence. 
4. Create the **Final Node**. Name the element `Success` and connect the final action to it with a **Control Flow**.

These steps produce a basic outline of an Activity Diagram. Most Activity Diagrams will require additional types of elements to be considered complete. Refer to [Decision and Merge Nodes](#decision-and-merge-nodes), [Fork and Join Horizontals](#fork-and-join-horizontals), and [Activity Diagram Objects](#activity-diagram-objects), and integrate the described elements into the outline to complete the Activity Diagram.

### Decision and Merge Nodes

Decision Nodes determine the *route* of the Activity using if/else logic.

A Decision Node receives and outputs a single flow into one of two distinct paths. The paths are defined by a **Guard**, a true/false statement, and the Activity Diagram chooses the true-value path to route the flow.  

A Merge Node is the counterpart to a Decision Node. The Merge Node ensures that the dual pathing routes to the same location. Merge Nodes may also be used in isolation to resolve alternate/exceptional flow paths.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-decision-merge</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p><strong>Figure 2.</strong> Decision and Merge Nodes</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="decision_merge.png"/>
</ac:image>

---

#### Create Decision and Merge Node

1. Create a **Decision Node**.
2. Create two **Control Flows** emerging from the node.
3. Open the flow **Specification** and edit the **Guard** to be a true/false statement. 

### Fork and Join Horizontals

Fork Horizontals create multiple concurrent flows within an Activity, used when the actions of multiple entities are required to progress the activity.  

The Fork Horizontal receives a single flow as input and outputs multiple flows. Each flow proceeds through its own set of actions. In this sense, the input flow into a Fork Horizontal may be considered a "trigger" for the multiple outputted flows.

The Join Horizontal receives multiple flows (created by its counterpart Fork) as input and outputs a single flow. The activity does not progress beyond the Join Horizontal until all inputs are received.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-join-fork</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p><strong>Figure 3.</strong> Join and Fork Horizontals</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="decision_merge.png"/>
</ac:image>

---

#### Create Fork and Join Horizontal

1. Create a **Fork Horizontal** and lengthen it to output multiple flows.  
2. Create a **Control Flow** from the previous action/node to the Fork Horizontal.  
3. Create multiple **Control Flows** from the Fork Horizontal to the subsequent actions/nodes.  
4. Create a **Join Horizontal** and lengthen it to receive multiple flows.  
5. Create multiple **Control Flow** from the previous actions/nodes to the Join Horizontal.  
6. Create a **Control Flow** from the Join Horizontal to the subsequent action/node.  

### Activity Diagram Objects

#### Object Flow