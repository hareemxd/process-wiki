---
title: Problem Domain System Context Diagrams
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction  
document_number: MBSE-WI-003
metamodel_domain: Problem Domain Black Box  
metamodel_pillar: Structure  
domains:  
    - Systems Engineering  
output: 
    - Block Definition Diagram
    - Internal Block Diagram
---


# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to create structural diagrams in the *problem domain system context* (PDSC), the environment containing and surrounding the *system of interest* (SoI) during key activities. The SoI is the primary subject of the modeler's efforts, the system to be designed using the architectural definition realized in the system model.
# Company SysML Meta Model

This Work Instruction addresses the **Problem Domain Black Box - Structure** space of the Company Meta Model; see [Figure 1](#figure1-pdsc).

In the Problem Domain, the SoI is modeled as a *black box*; only the external boundaries and connections are defined. The black box perspective helps the modeler identify the most fundamental SoI specifications: external interfaces, and the states, behaviors, and functions inferred from its inputs and outputs. Allocating these specifications to discrete objects within the SoI gives rise to structure in the system model.



:::{figure} img/MBSE/PDSCDiagramsMetaModel.png
:align: center
:name: figure1-pdsc

Company Meta Model

:::

The Modeler should review {numref}`Table1` to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

```{list-table} Work Instruction Inputs
:header-rows: 1
:name: Table1

* - Description
  - Reference
* - The Modeler should be working in a Model using the company MBSE package framework.
  - Template Work Instruction

```


# Roles and Responsibilities

Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in {numref}`Table2` and functional areas are assigned roles in {numref}`Table3`.

```{list-table} RACI Roles and Definitions
:header-rows: 1
:name: Table2

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

```{list-table} Problem Domain System Context Diagrams RACI Chart
:header-rows: 1
:name: Table3

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
## Create Elements of Definition

Create elements by right-clicking in the containment tree.


>[!NOTE]
Customizations are located under **Other Blocks**; see [Figure 2](#figure2-pdsc).

:::{figure} img/MBSE/PDSCcustomizations.png
:align: center
:name: figure2-pdsc

Element Customizations
:::

---

### Create Problem Domain System Context Block
1. Right-click **System Context (Structure) > Create Element**.
2. Open the element **Specification** and edit the **Documentation**. Write a brief description of the PDSC.

### Create System of Interest

1. Right-click **System Context (Structure) > Create Element > System of Interest**.
2. Open the element **Specification** and edit the **Documentation**. Write a brief description of the SoI.

### Create Actors


1. Right-click **Actors > Create Element > Actor**.
2. Open the actor **Specification** and edit the **Documentation**. Write a brief description of each element.
3. Open the **Actor Descriptions** table and drag all actors into the table.
4. In the top toolbar, select **Columns > Documentation**. A new column displaying the **Documentation** field is added to the table.

### Create External Systems
 

1. Under **Structure**, right-click **External Systems > Create Element > External System**.
2.   Open the External System **Specification** and edit the **Documentation**. Write a brief description of each element.
3.  Open the **External System Descriptions** table and drag all external systems into the table.
4.  In the top toolbar, select **Columns > Documentation**. A new column displaying the **Documentation** field is added to the table.


## Create Block Definition Diagram

Add elements to diagrams by dragging them from the containment tree. Create relationships by drawing connections in the diagram.


### Layout the Diagram


 1. Right-click the **PDSC block** **> Create Diagram > SysML Block Definition Diagram**. Open the diagram.

1. Drag the PDSC block into the middle of the diagram and lengthen it to extend to the bottom of the screen.
2. Update the title to match the element name.

3. Drag the SoI block onto the diagram above the PDSC block, all actors to the left, and all external systems to the right.
4. Drag the **Actor Descriptions** table into the top-left region and  the **External System Descriptions** table into the top-right region.
5. Use the **Align** tool in the top toolbar to organize, resize, and reposition elements to give the diagram a uniform style.

>[!NOTE]
All external system and actor blocks should be the same size.


### Create Design Comments


1. Select the element to attach a comment to, then select the anchor ![anchor](img/MBSE/Anchor.png). Move the mouse to nearby whitespace and click to create a note.
2. Right-click the note, then **Refactor > Convert To > Comment**.
3. Right-click again, and under **Stereotype**, select a comment stereotype.
4. Enter the comment in the text field.

>[!NOTE]
All design comments should have an applied stereotype.

### Create System of Interest Documentation Comment


1. Right-click the SoI **> Specification**. Expand the **Documentation/Comments** category in the left navigation menu.

:::{figure} img/MBSE/PDSCSOIContainmentTree.png
:align: center
:name: figure3-pdsc

Display System of Interest Documentation
:::


1. Click and drag the comment nested under **Documentation/Comments** into the top-left region to create a **Comment**.
2. Mouse over the comment and select the anchor ![anchor](img/MBSE/Anchor.png), then select the PDSC block and connect the elements.

### Create Relationships

1. Create **Directed Aggregation** relationships from the PDSC block to each of the actors and external systems.
2. Create a **Directed Composition** relationship from the PDSC block to the SoI block.

3. Right-click each new connector **> Specification > Multiplicity**, and set the correct value.

>[!NOTE]
The primary user should be assigned a multiplicity of **[1..*]**.

### Output

[Figure 4](#figure4-pdsc) provides an example of a properly styled PDSC BDD. The red labels indicate the location of style elements captured as Review Checklist items; see {numref}`Table4`.

:::{figure} img/MBSE/PDSCBDD.png
:align: center
:name: figure4-pdsc

Problem Domain System Context Block Definition Diagram
:::

```{list-table} Block Definition Diagram Review Checklist Items
:header-rows: 1
:name: Table4

* - Review Checklist Item
  - Description
* - Item 1 Comments
  - All design comments have a company custom stereotype applied.
* - Item 2 Structure
  - PDSC block is in the middle, actors are on the left, systems are on the right, and blocks are organized and uniform.
* - Item 3 Documentation
  - Actor and external system description tables are located above their blocks and the SoI documentation is displayed in the top-left region.
* - Item 4 Relationships
  - The PDSC block has a directed composition relationship to the SoI block and directed aggregation relationships to all actor and external system blocks.


```

## Create Internal Block Diagram

Add elements to diagrams by dragging them from the containment tree. Create relationships by drawing connections in the diagram.

### Layout the Diagram

1. In the containment tree, right-click the PDSC block **> Create Diagram > SysML Internal Block Diagram > OK**. Cameo automatically adds all elements of definition to the new diagram.
2. Drag the SoI block into the middle of the diagram and lengthen it to extend to the bottom of the screen.
3. Update the title in the text box so it matches the file name.
4. Drag all actors to the left and all external systems to the right.
5. Drag the **Actor Descriptions** table into the top-left region and the **External System Descriptions** table into the top-right region.
6. Use the **Align** tool in the top toolbar to organize, resize, and reposition elements to give the diagram a uniform style.

7. Drag the **Interface Types** legend into the top-left region.

### Create Connections and Ports

1. Select a property (element) in the diagram, then select the **Proxy Port**. Create a new port on the inner side (close to the SoI).
2. Select the SoI and create another port that will connect the SoI with the property port.
3.  Select each port on the SoI, select the **Connector**, then create a connection between the SoI and property ports.

>[!NOTE]
Connected ports should be horizontally aligned to the greatest possible extent. Use the **Align** tool.

4. Right-click each port **> Legend Item**, then assign the appropriate **Legend Item**.
5. Position all port labels next to their ports and inside the owning block.

:::{figure} img/MBSE/PDSCPortStyle.png
:align: center
:name: figure5-pdsc

Figure 5 Port Style
:::

### Create Flows and Interfaces
1. Identify and create elements to represent all types of information flowing between the SoI and external systems.
2. Right-click **Logical Information Flows > Create Element > Flow Specification**.
3. Drag the Flow Specification block onto the appropriate connector in the diagram.
4. Check the flow's direction to confirm it is correct, then select **Finish**.

>[!NOTE]
All connected ports must be typed by the same Interface Block.

5. Identify all types of interfaces through which information is transferred between all PDSC elements of definition.
6. Right-click **Logical Interface Types > Create Element > Interface Block**.
7. Drag the Interface Block onto the appropriate port in the diagram.

### Output

[Figure 6](#figure6-pdsc) provides an example of a properly styled PDSC IBD. 

:::{figure} img/MBSE/PDSCIBD.png
:align: center
:name: figure6-pdsc

Problem Domain System Context Internal Block Diagram
:::


# References


# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|ghp.1| - |01-28-2026| D. Ricart| First complete draft deployed to Github Pages using a MyST-powered site generator.|

# Appendix


## Actors Supplement
Actors represent humans or human groups who interact with the SoI in the Problem Domain System Context. A common approach to designating actors is to consider them in terms of their *behaviors* and *needs* and how these characteristics may influence and/or interact with the SoI.



## External Systems Supplement

External Systems are the systems that interact with the SoI in the Problem Domain. Common examples include power, networking, and thermal control systems, and structural systems such as mounts and cable harnesses. Identifying all external systems is critical to the definition of the SoI from a black box perspective.
