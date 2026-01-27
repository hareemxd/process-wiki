<!--
---
title: "Problem Domain System Context Diagrams"
author: "David Ricart"
project: "ProcessWiki"
genre: "work instruction"
domains:
    - Systems Engineering
tags: 
---
-->

# Problem Domain System Context Diagrams
## Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to create a **Problem Domain System Context Block Definition Diagram** (BDD) and **Internal Block Diagram** (IBD) that conform to company standards of style and quality. These diagrams represent the **Problem Domain System Context** (PDSC), the environment containing and surrounding the **System of Interest** (SoI) during key activities. The SoI is the primary subject of the modeler's efforts, the system to be designed using the architectural definition provided by the system model.
### Company SysML Meta Model

This Work Instruction addresses the **Problem Domain Black Box - Structure** space of the Company Meta Model. In the Problem Domain, the SoI is modeled as a **black box**; only the external boundaries and connections are defined in the model. The black box perspective helps the modeler identify the most fundamental SoI specifications: external interfaces, and the states, behaviors, and functions inferred from its inputs and outputs. Allocating these specifications to discrete objects within the SoI gives rise to structure.

**Figure 1 Company Meta Model**

The Modeler should review Table 1 to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

**Table 1 Problem Domain System Context Diagrams Inputs**

| Description| Reference|
|---|---|
|The Modeler should be working in a Model using the company MBSE package framework.| Template Work Instruction|

## Roles and Responsibilities

Roles and responsibilities for the Model Based Systems Engineering (MBSE) Style Guide are assigned using a Resonsible, Accountable, Consulted, Informed (RACI) chart.

**Table 2 RACI Roles and Definitions**

| RACI Roles| Definitions|
|---|---|
| Responsible| Stakeholder is the owner of the document.|
|Accountable| Stakeholder depends on the document to effectively perform their job duties.|
|Consulted| Stakeholder provides input, which may or may not be optional, to the authoring of the document.|
|Informed| Stakeholder is made aware of the document.|
|Omitted| Not a stakeholder.|

**Table 3 Problem Domain System Context Diagrams RACI Chart**

## Terms
### Definitions

**Table 4 Problem Domain System Context Diagrams Terms and Definitions**

### Acronyms, Abbreviations, and Special Units

## Problem Domain System Context Diagrams Procedure
### Create Elements of Definition

Create elements by right-clicking in the containment tree.


To access company customizations when creating an element, collapse the **General** and **Requirements** sections. The customizations are listed under **Other Blocks**.

**Figure 2 Problem Domain System Context Diagrams Customizations**

---

#### Create Problem Domain System Context Block
1. Right-click **System Context (Structure) > Create Element**.
2. Open the element **Specification** and edit the **Documentation**. Write a 2-3 sentence description of the PDSC in terms of the SoI and its purpose and primary user.

#### Create System of Interest

3. Right-click **System Context (Structure) > Create Element > System of Interest**.
4. Open the element **Specification** and edit the **Documentation**. Write a 2-3 sentence description of the SoI in terms of its purpose and primary user.

#### Create Actors


5. Right-click **Actors > Create Element > Actor**.
6. Open the actor **Specification** and edit the **Documentation**. Write a 2-3 sentence description of each actor in terms of their relationship with the PDSC and the SoI.
7. Open the **Actor Descriptions** table and add all the actors.
8. In the top toolbar, select **Columns > Documentation**. A new column displaying the **Documentation** field is added to the table.

#### Create External Systems
 

9. Under **Structure**, right-click **External Systems > Create Element > External System**.
10.   Open the External System **Specification** and edit the **Documentation**. Write a 2-3 sentence description in terms of its interactions with the SoI in the Problem Domain System Context.
11.  Open the External System Descriptions table and drag all systems into the table.
12.  In the top toolbar, select **Columns > Documentation**. A new column displaying the **Documentation** field is added to the table.

---

### Create Block Definition Diagram

Add elements to diagrams by dragging them from the containment tree. Create relationships by drawing connections in the diagram.


#### Layout the diagram


 1. Right-click the **PDSC block** **> Create Diagram > SysML Block Definition Diagram**. Open the diagram.

1. Drag the PDSC block into the middle of the diagram. Lengthen it vertically so it extends to the bottom.
2. Update the title in the text box so it matches the file name.


3. Drag the SoI block onto the diagram above the PDSC block, all Actors to the left, and all External Systems to the right.
4. From the containment tree, drag **Actor Descriptions** into the top-left region and drag **External System Descriptions** into the top-right region.
5. Use the **Align** tool in the top toolbar to resize and reposition the diagram elements to look organized and uniform.

>[!NOTE]
All external system and actor blocks should be the same size.


#### Create Design Comments


7. Select the element for the comment **> Anchor**. Drag it to a white space near the block and click to create a **Note**.
8. Right-click the **Note > Refactor > Convert To > Comment**.
9. Right-click again, and from the **Stereotype** menu, choose the appropriate **Stereotype**.
10. Enter the comment in the text field.

#### Create System of Interest Documentation Comment


11. Right-click the SoI **> Specification**. Expand the **Documentation/Comments** category in the left navigation menu.

**Figure 4 Display System of Interest Documentation**

12. Click and drag the comment nested under **Documentation/Comments** into the top-left region to create a **Comment**.
13. Mouse over the comment and select the **Anchor**, then select the PDSC block and connect the elements.

#### Create Relationships

14. Create **Directed Aggregation** relationships from the PDSC block to each of the actors and external systems.
15. Create a **Directed Composition** relationship from the PDSC block to the SoI block.

16. Right-click the connector **> Specification > Multiplicity**, and set the correct value.

>[!NOTE]
the primary user should be assigned a multiplicity of **1..***

#### Output

Figure 5 provides an example of a properly styled PDSC BDD. THe red labels indicate the location of style elements captured as Review Checklist items; see Table 5.

**Figure 5 Problem Domain System Context Diagrams Block Definition Diagram**

**Table 5 Problem Domain System Context Diagrams Block Definition Diagram Review Checklist Items**

| Review Checklist Item| Description|
|---|---|
| RCI-1 Comments| All comments have a company custom stereotype applied.|
| RCI-2 Structure| PDSC block is in the middle, actors are on the left, systems are on the right, and blocks are organized and uniform.|
| RCI-3 Extra Elements| Actor and external system description tables are located above their blocks and the SoI documentation is displayed in the top-left region.|
| RCI-4 Relationships| The PDSC block has a directed composition relationship to the SoI block and directed aggregation relationships to all actor and external system blocks.|

### Create Internal Block Diagram

Add elements to diagrams by dragging them from the containment tree. Create relationships by drawing connections in the diagram.

1. In the containment tree, right-click the PDSC block **> Create Diagram > SysML Internal Block Diagram > OK**. The diagram screen displays all System Context elements of definition.

#### Create Diagram Layout
2. Move the SoI block into the middle of the diagram. Lengthen it vertically so it extends to the bottom.
3. Update the title in the text box so it matches the file name.
4. Move all Actors to the left and all External Systems to the right.
5. From the containment tree, drag **Actor Descriptions** into the top-left region, and drag **External System Descriptions** into the top-right region.
6. Use the **Align** tool in the top toolbar to organizem, resize, and reposition elements to give the diagram a uniform style.

#### Add Interface Type Legend
7. Drag the **Interface Types** legend into the top-left region.

### Create Ports, Connections, Interface Types, Information Types
#### Create Ports and Connections
8. Select a property (element) in the diagram, then select the **Proxy Port**. Create a new port on the inner side (close to the SoI).
9. Select the SoI and create another port that will connect the SoI with the property port
10. Select each port on the SoI, select the **Connector**, then create a connection between the SoI and property ports.

>[!NOTE]
Connected ports should be horizontally aligned. Use the **Align** tool.
##### Port Styles
11. Right-click each port **> Legend Item**, then assign the appropriate **Legend Item**.
12. Position all port labels next to their ports and inside the owning block.

##### Create Flow Specifications
13. Identify and create elements to represent all types of information flowing between the SoI and external systems.
14. Right-click **Logical Information Flows > Create Element > Flow Specification**.
15. Drag the Flow Specification block onto the appropriate connector in the diagram.
16. Check the flow's direction is correct, then select **Finish**.

##### Create Interface Blocks
All connected ports must be typed by the same Interface Block.

16. Identify all types of interfaces through which information is transferred between all PDSC elements of definition.
17. Right-click **Logical Interface Types > Create Element > Interface Block**.
18. Drag the Interface Block onto the appropriate port in the diagram.

#### Output

Figure 7 provides an example of a properly styled PDSC IBD. 

**Figure 7 Problem Domain System Context Diagrams Internal Block Diagram**



## References

## Opportunities and Risks

## Revision History

## Appendix


### Actors Supplement
Actors represent humans or human groups who interact with the SoI in the Problem Domain System Context. A common approach to designating actors is to consider them in terms of their *behaviors* and *needs* and how these characteristics may influence and/or interact with the SoI.

The figure below provides common examples of actors:


**Figure 3 Actor Examples**

### External Systems Supplement

External Systems are the systems that interact with the SoI in the Problem Domain. Common examples include power, networking, and thermal control systems, and structural systems such as mounts and cable harnesses.