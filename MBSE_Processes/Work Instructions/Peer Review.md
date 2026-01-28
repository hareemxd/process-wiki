---
title: Peer Review
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction  
metamodel_domain: not applicable
metamodel_pillar: not applicable 
domains:  
    - Systems Engineering  
---

# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures for conducting peer reviews of MBSE artifacts generated in Cameo Systems Modeler (CSM). Adherence to this document ensures that peer reviews conform to company process and quality standards.

# Company SysML Meta Model
This Work Instruction applies to all spaces of the company Meta Model; see [Figure 1](#figure1).

:::{figure} /img/MBSE/peer review meta model.png
:align: center
:name: figure1

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
```{list-table} Peer Review RACI Chart
:header-rows: 1
:name: Table3

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
# Procedure
## Create Peer Review Project

All peer reviews for a given program are contained in a separate project file so review comments do not clutter the system model.

In Cameo:
1. Go to **File > New Project**: Peer Reviews - <project name>. Open the new project.
2. Go to **Options > Project Usages**.
3. Select the plus ![plus icon](/img/MBSE/Plus.png) **> Use Server Project**.
4. Locate and select the original project **> Next**.
5. Select the most recent version **> Finish**.
6. Close the window, then go to **Collaborate > Commit Changes to Server**.

## Create Peer Review Artifact

This procedure describes the steps to create a peer review artifact that will be subject to the peer review activity. THe author is responsible for choosing the artifact contents, including elements to be reviewed directly and elements which provide reviewers with useful background information.

### Update Project Usage Reference for Review Start

Before creating the artifact, you must update the Project Usages of your Peer Review Project to reference the correct version of the original project.

In the Peer Review Project:  
1. Go to **Options > Project Usages**.
2. On the left, right-click the original project **> Lock**.

:::{figure} /img/MBSE/peer review lock customizations.png
:align: center
:name: figure2

Lock Project to Update Project Usage

:::

3. Right-click the original project again, then **Change Version > OK > OK**.
4. Go to **Collaborate > Commit Changes to Server**.

### Create Smart Package

The Peer Review artifact consists of a *smart package*, a set of project elements created by the author, in the peer reviews project.

1. Right-click the main model **> Create ELement > Smart Package**:

### Add Elements to Smart Package

Add elements from the original project to the smart package by editing its **Specification**.

>[!NOTE]
You can drag and drop elements directly into the package, but this is not recommended for large projects whose containment trees are difficult to navigate.

1. Right-click the smart package **> Specification**.
2. Under **Content**, select the cell next to **Additional Elements**, then click the ellipses ![ellipses icon](/img/MBSE/Ellipses.png) to open a new window.
3. Expand **Project Usages** to view the original project's containment tree.
4. Select the elements to include in the peer review, then click the plus ![plus icon](/img/MBSE/Plus.png).
5. Select **OK > Close** to confirm.

### Create Peer Review Content Diagram

The Peer Review Content Diagram contains instructions for reviewers and model IDs to ensure traceability between the review activity and the main model.

1. In the Peer Review Project, select the search ![search icon](/img/MBSE/Search.png).
2. Select **Any Element** and search for peer review.

The top result shown in [Figure 3](#figure3) is the Peer Review Content Diagram Template stored in the Naval Electronics Profile model. If you don't see the template, check your **Project Usages**.

:::{figure} /img/MBSE/peer review search.png
:align: center
:name: figure3

Search for Peer Review Content Diagram

:::

3. Select the template to locate it in the containment tree, then right-click and **Copy**, then right-click the smart package **> Paste**.
4. Rename the new copy to match the smart package file name, plus CD.
5. Update the activity information fields.
6. Update the diagram's data markings as required.
7. Select elements from the smart package to display as blocks in the diagram, and drag them into the screen.
8. Organize the content diagram to generally match [Figure 4](#figure4).

:::{figure} /img/MBSE/peer review content diagram.png
:align: center
:name: figure4

Peer Review Content Diagram

:::

## Initiate Peer Review Activity

This step includes publishing the artifact to Cameo Collaborator, granting permissions to reviewers, and notifying them the activity has started.

### Publish Artifact to Collaborator

In Cameo:

1. Go to **Tools > Cameo Collaborator > Publish**.
2. Click the ellipses ![ellipses icon](/img/MBSE/Ellipses.png) next to **Category Name** to open the containment tree.
3. Open the project category **> Collaborator Files > Peer Reviews OK**.
4. Click the ellipses ![ellipses icon](/img/MBSE/Ellipses.png) next to **Scope** to open your project containment tree.
5. Select the smart package **>** ![plus icon](/img/MBSE/Plus.png) **> OK**.
6. Check that your options are configured per [Figure 5](#figure5).
7. From **Scope**, copy the smart package name and paste to **Document name > Publish**.

:::{figure} /img/MBSE/peer review publisher.png
:align: center
:name: figure5

Peer Review Content Diagram

:::

### Grant Permissions to Reviewers in Teamwork Cloud

When initiating a review activity, you must confirm that all reviewers have the **Review Contributor** role for the correct category(s). See [Teamwork Cloud Administrator Work Instruction](#references) for more detail.

## Perform Peer Review in Cameo Collaborator

This procedure describes the review, comment, and resolve portion of peer review activities.

### Review the Artifact in Cameo Collaborator

Reviewers are tasked with reviewiewing the peer review artifact and identifying problems with comments.

1. Open the artifact in Teamwork Cloud. Review the content diagram notes.
2. Open an element in the diagram from the main screen or containment tree.

:::{figure} /img/MBSE/peer review collaborator menu.png
:align: center
:name: figure6

Cameo Collaborator Containment Tree

:::

#### Add comment

1. In the element, click ![comment icon](/img/MBSE/comment.png) to the bottom right.
2. Click anywhere in the diagram to open the **Graphical Comment** window and the top-left toolbar.
3. Select the rectangle tool from the main toolbar. Click and drag to create a comment shape.
4. Locate it on or near whichever element(s) your comment is addressing.
5. Select the shape, then select ![comment icon](/img/MBSE/comment.png) from the main toolbar
6. Enter your name for the **Title**, then enter your comment in the **Comment** field **> Done**.

### Review Comments in Cameo Collaborator




# References
# Revision History
# Appendix