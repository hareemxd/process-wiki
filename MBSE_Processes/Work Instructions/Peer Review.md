---
title: Peer Review
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction
document_number: MBSE-WI-002  
metamodel_domain: not applicable
metamodel_pillar: not applicable 
domains:  
    - Systems Engineering  
---

# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures for conducting peer reviews of MBSE artifacts generated in Cameo Systems Modeler (CSM). Adherence to this document ensures that peer reviews conform to company process and quality standards.

# Company SysML Meta Model
This Work Instruction applies to all spaces of the company Meta Model; see [Figure 1](#figure1-mbsepr).

:::{figure} img/MBSE/peerreviewmetamodel.png
:align: center
:name: figure1-mbsepr

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

```{list-table} **RACI Roles and Definitions**
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
```{list-table} **Peer Review RACI Chart**
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

| Term | Definition |
|---|---|
|Smart Package| a special collection of model elements|
|Project Usage| a reference to a different project that provides access to that project's model elements|
|Category| synonymous with *folder* in Teamwork Cloud|
| Resource| synonymous with *file* in Teamwork Cloud|
| Containment Tree| synonymous with *file directory* in Teamwork Cloud|

# Procedure
## Create Peer Review Project

All peer reviews for a given program are contained in a separate project file so review comments do not clutter the system model.

In Cameo:
1. Go to **File > New Project**, then enter `Peer Reviews - Project Name`. Open the new project.
2. Go to **Options > Project Usages**.
3. Select the plus ![plus icon](img/MBSE/Plus.png) **> Use Server Project**.
4. Locate and select the original project **> Next**.
5. Select the most recent version **> Finish**.
6. Close the window, then go to **Collaborate > Commit Changes to Server**.

## Create Peer Review Artifact

This procedure describes the steps to create a peer review artifact that will be subject to the peer review activity. The author is responsible for choosing the artifact contents, including elements to be reviewed directly and elements which provide reviewers with useful background information.

### Update Project Usage Reference for Review Start

Before creating the artifact, you must update the *project usages* of your Peer Review Project to reference the correct version of the original project.

In the Peer Review Project:  
1. Go to **Options > Project Usages**.
2. On the left, right-click the original project **> Lock**.

:::{figure} img/MBSE/peerreviewlockcustomizations.png
:align: center
:name: figure2-mbsepr

Lock Project to Update Project Usage

:::

3. Right-click the original project again, then **Change Version > OK > OK**.
4. Go to **Collaborate > Commit Changes to Server**.

### Create Smart Package

The Peer Review artifact consists of a *smart package*, a set of project elements created by the author, in the peer reviews project.

1. Right-click the main model **> Create Element > Smart Package**, and enter `yyyy-mm-dd review-artifact-name`.

### Add Elements to Smart Package

Add review elements to the smart package by editing its **Specification**.

>[!NOTE]
You can drag and drop elements directly into the package, but this is not recommended for projects with extensive containment trees.

1. Right-click the smart package **> Specification**.
2. Under **Content**, select the cell next to **Additional Elements**, then click the ellipses ![ellipses icon](img/MBSE/Ellipses.png).
3. Expand **Project Usages** to view the original project containment tree.
4. Select the elements to include in the review activity, then click the plus ![plus icon](img/MBSE/Plus.png).
5. Select **OK > Close**.

### Create Peer Review Content Diagram

The Peer Review Content Diagram contains instructions for reviewers and model IDs to ensure traceability between the review activity and the main model.

In the Peer Review Project:
1. select the search-glass ![search icon](img/MBSE/Search.png), select **Any Element**, and search `peer review`.

The top result in [Figure 3](#figure3-mbsepr) is the Peer Review Content Diagram Template stored in the Naval Electronics Profile. If you don't see the template, check your project usages.

:::{figure} img/MBSE/peerreviewsearch.png
:align: center
:name: figure3-mbsepr

Search for Peer Review Content Diagram

:::

1. Select the template to locate it in the containment tree, then right-click the diagram and **Copy**, then right-click the smart package and **Paste**.
2. Rename the new copy `smart_package_name CD`.
3. Update the activity information fields.
4. Update the diagram's data markings as required.
5. Drag elements you want to visualize from the smart package into the diagram screen.
6. Use text headers and hierarchy to organize the content diagram; see [Figure 4](#figure4-mbsepr).

:::{figure} img/MBSE/peerreviewcontentdiagram.png
:align: center
:name: figure4-mbsepr

Peer Review Content Diagram

:::

## Initiate Peer Review Activity

This step includes publishing the artifact to Cameo Collaborator, granting permissions to reviewers, and notifying them the activity has started.

### Publish Artifact to Collaborator

In Cameo:

1. Go to **Tools > Cameo Collaborator > Publish**.
2. Click the ellipses ![ellipses icon](img/MBSE/Ellipses.png) next to **Category Name** to open the containment tree.
3. Open the project category **> Collaborator Files > Peer Reviews > OK**.
4. Click the ellipses ![ellipses icon](img/MBSE/Ellipses.png) next to **Scope** to open your project containment tree.
5. Select the smart package **>** select the plus ![plus icon](img/MBSE/Plus.png) **> OK**.
6. Check that your options are configured per [Figure 5](#figure5-mbsepr).
7. From **Scope**, copy the smart package name and paste to **Document name > Publish**.

:::{figure} img/MBSE/peerreviewpublisher.png
:align: center
:name: figure5-mbsepr

Publish the Peer Review Artifact

:::

### Grant Permissions to Reviewers in Teamwork Cloud

When initiating a review activity, you must confirm that all reviewers have the Review Contributor role for the correct category(s) enabled. Otherwise the reviewers will not be able to access the review artifact. See [Teamwork Cloud Administrator Work Instruction](#references) for more detail.

## Perform Peer Review in Cameo Collaborator

This procedure describes the review, comment, and resolve portion of the review activity.

### Review the Artifact in Cameo Collaborator

Reviewers are tasked with reviewing the artifact and identifying problems with comments.

1. Open the artifact in Teamwork Cloud. Review the content diagram notes.
2. Open an element in the diagram from the main screen or containment tree.

:::{figure} img/MBSE/peerreviewcollaboratormenu.png
:align: center
:name: figure6-mbsepr

Cameo Collaborator Containment Tree

:::

#### Add comment

1. In the element, click the comment tool ![comment icon](img/MBSE/comment.png) to the bottom right.
2. Click anywhere in the diagram to open **Graphical Comment** and the top-left toolbar.
3. Select the rectangle tool ![rectangle tool icon](img/MBSE/rectangle%20tool.png) from the main toolbar. Click and drag to create a comment shape.
4. Locate it on or near whichever element(s) your comment is addressing.
5. Select the shape, then select the comment tool ![comment icon](img/MBSE/comment.png) from the main toolbar.
6. Enter `your name` in **Title** and `your comment` in **Comment > Done**.

### Review Comments in Cameo Collaborator

1. Open Teamwork Cloud **> Resources**. Navigate to and open the peer review artifact.
2. Select the comment tool ![comment icon](img/MBSE/comment.png) in the top right. All comments on this artifact are displayed to the right.
3. Select a comment to open the respective element.

### Close Comments during the Peer Review Activity

The author closes a comment when the identified problem has been corrected, or if they deem the comment invalid or out-of-scope for the activity. The moderator closes a comment once they verify the author has corrected the problem as described in the review comments.

For valid comments:
1. Update the model in the original project to correct the problem.

>[!Warning]
Do not resolve comments by making changes to the peer review project or the original project in Cameo Collaborator.

#### Close Comments in Cameo Collaborator

1. Locate the comment in Cameo Collaborator and select the reply tool ![reply icon](img/MBSE/reply1.png) .
2. Enter `your reply` in **Comment** explaining the work you completed to address the problem, then **Enter**.
3. Click the checkbox next to the original comment (*not* the comment you just made) to close the comment.

For invalid and out-of-scope comments:
1. Locate the comment in Cameo Collaborator and select the reply tool ![reply icon](img/MBSE/reply1.png).
2. Enter `your reply` in **Comment** explaining why the comment should be closed with no action taken.

## Close Peer Review Activity
The final step is to close the peer review activity.

### Update Project Usage Reference for Review Close

In Cameo, in the Peer Reviews Project:
  1. Go to **Options > Project Usages**.
  2. Right-click the original model **> Lock**, then right-click again and **Change Version**.
  3. Select the correct version of the original model **> OK > OK**.
  4. Go to **Collaborate > Commit Changes to Server**.

### Publish Peer Review Artifact to Cameo Collaborator for Review Close

In the peer review content diagram:
1. Update the review start/close note with the review close version number.

>[!Note]
The activity documented in [Figure 7](#figure7-mbsepr) began with Version 1 of the original model and ended with Version 4. The note provides traceability to all changes resulting from the review activity.
  
:::{figure} img/MBSE/peerreviewnote.png
:align: center
:name: figure7-mbsepr

Peer Review Start/Close Note

:::

3. Go to **Tools > Cameo Collaborator > Publish**.
4. Select the ellipses ![ellipses icon](img/MBSE/Ellipses.png) by **Category Name** to open the containment tree.
5. Go to the original project **> Collaborator Files > 1 - Peer Reviews > OK**.
6. Select the ellipses ![ellipses icon](img/MBSE/Ellipses.png) by **Scope** to open your project containment tree.
7. Select the peer review artifact, then select the plus ![plus icon](img/MBSE/Plus.png)**> OK**.
8. Expand and configure your **Options** per [Figure 8](#figure8-mbsepr), then **Publish**.

:::{figure} img/MBSE/peerreviewpublisher2.png
:align: center
:name: figure8-mbsepr

Publish the Completed Peer Review Artifact

:::

### Archive the Peer Review Artifact

In Teamwork Cloud:
1. Open your project, then open **Collaborator Files > Peer Reviews**.
2. To the right, select the ellipses ![ellipses icon](img/MBSE/Ellipses.png) **> Move Resource**.
3. Under the project containment tree, select **Archived Peer Reviews > Move**. 
# References
# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|ghp.1| - |01-28-2026| D. Ricart| First complete draft deployed to Github Pages using a MyST-powered site generator.|

# Appendix