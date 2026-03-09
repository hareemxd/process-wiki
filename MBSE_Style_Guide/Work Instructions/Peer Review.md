---
title: Peer Review
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction
document_number: MBSE-WI-003  
metamodel_domain: not applicable
metamodel_pillar: not applicable 
domains:  
    - Systems Engineering  
outputs:
    - Peer Review Activity
    - SysML Peer Review Artifact
---



# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures for conducting peer reviews of MBSE artifacts. Adherence to this document ensures that peer reviews conform to DRS Naval Electronics process and quality standards.

# DRS Naval Electronics SysML Meta Model
This Work Instruction applies to all spaces of the DRS Naval Electronics Meta Model; see [Figure 1](#fig1-peer-review-metamodel).  

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-peer-review-metamodel</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p><strong>Figure 3.</strong> Peer Review Meta Model</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="peerreviewmetamodel.png"/>
</ac:image>

---

The Modeler should review [Table 1](#tab-work-instruction-inputs) to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-work-instruction-inputs</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p><strong>Table 1.</strong> Work Instruction Inputs</p>
  </ac:rich-text-body>
</ac:structured-macro>

| Description | Reference |
|---|---|
| The Modeler should have access to the required work elements in Teamwork Cloud. | MBSE-WI-001 Teamwork Cloud Administrator |
| The Modeler should be working in a Model using the DRS Naval Electronics MBSE package framework. | MBSE-WI-002 Project Templates |

# Roles and Responsibilities
Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in **Table 2** and functional areas are assigned roles in **Table 3**.

| RACI Role | Definition |
|---|---|
| Responsible | Stakeholder is the owner of the document. |
| Accountable | Stakeholder depends on the document to effectively perform their job duties. |
| Consulted | Stakeholder provides input, which may or may not be optional, to the authoring of the document. |
| Informed | Stakeholder is made aware of the document. |
| Omitted | Not a stakeholder. |

<div style="text-align: left;">
<i>Table 2 RACI Roles and Definitions</i>
</div>

| Function | Role |
|---|---|
| Systems Engineering | R |
| Project Engineering | C |
| Configuration Management | C |
| Electrical Engineering | I |
| Mechanical Engineering | I |
| Software Engineering | I |
| Test Engineering | I |
| Manufacturing | I |
| Specialty Engineering | I |
| Quality | A |
| Training | A |
| Business Development | I |

<div style="text-align: left;">
<i>Table 3 Peer Review RACI Chart</i>
</div>

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
3. Select the plus ![plus icon](../assets/MBSE/Plus.png) **> Use Server Project**.  
4. Locate and select the original project **> Next**.  
5. Select the most recent version **> Finish**.  
6. Close the window, then go to **Collaborate > Commit Changes to Server**.  

## Create Peer Review Artifact

This procedure describes the steps to create a peer review artifact that will be subject to the peer review activity. The author is responsible for choosing the artifact contents, including elements to be reviewed directly and elements which provide reviewers with useful background information.

### Update Project Usage Reference for Review Start

Before creating the artifact, you must update the *project usages* of your Peer Review Project to reference the correct version of the original project.
 
1. In the Peer Review Project, go to **Options > Project Usages**.  
2. On the left, right-click the original project **> Lock**.  
3. Right-click the original project again, then **Change Version > OK > OK**.  
4. Go to **Collaborate > Commit Changes to Server**.  

---
![Lock Project to Update Project Usage](../assets/MBSE/peerreviewlockcustomizations.png)

<div style="text-align: center;">
<i>Figure 2 Lock Project to Update Project Usage</i>
</div>
---

### Create Smart Package

The Peer Review artifact consists of a *smart package*, a set of project elements created by the author, in the Peer Review Project.  

Right-click the main model **> Create Element > Smart Package**, and enter `yyyy-mm-dd review-artifact-name`.  

### Add Elements to Smart Package

Add review elements to the smart package by editing its **Specification**.  

| Note |
|---|
| You can drag and drop elements directly into the package, but this is not recommended for projects with extensive containment trees. |

1. Right-click the smart package **> Specification**.  
2. Under **Content**, select the cell next to **Additional Elements**, then click the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png).  
3. Expand **Project Usages** to view the original project containment tree.  
4. Select the elements to include in the review activity, then click the plus ![plus icon](../assets/MBSE/Plus.png).  
5. Select **OK > Close**.  

### Create Peer Review Content Diagram

The Peer Review Content Diagram contains instructions for reviewers and model IDs to ensure traceability between the review activity and the main model.  

In the Peer Review Project, select the search-glass ![search icon](../assets/MBSE/Search.png), select **Any Element**, and search `peer review`.  

The top result in **Figure 3** is the Peer Review Content Diagram Template stored in the DRS Naval Electronics Profile. If you don't see the template, check your project usages.  

---
![Search for Peer Review Content Diagram](../assets/MBSE/peerreviewfind.png)

<div style="text-align: center;">
<i>Figure 3 Search for Peer Review Content Diagram</i>
</div>
---

1. Select the template to locate it in the containment tree, then right-click the diagram and **Copy**, then right-click the smart package and **Paste**.  
2. Rename the new copy `smart_package_name CD`.  
3. Update the activity information fields.  
4. Update the diagram's data markings as required.  
5. Drag elements you want to visualize from the smart package into the diagram screen.  
6. Use text headers and hierarchy to organize the content diagram; see **Figure 4**.  

---
![Peer Review Content Diagram](../assets/MBSE/peerreviewcontentdiagram.png)

<div style="text-align: center;">
<i>Figure 4 Peer Review Content Diagram</i>
</div>
---

## Initiate Peer Review Activity

This step includes publishing the artifact to Cameo Collaborator, granting permissions to reviewers, and notifying them the activity has started.  

### Publish Artifact to Collaborator

1. In Cameo Systems Modeler, go to **Tools > Cameo Collaborator > Publish**.  
2. Click the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) next to **Category Name** to open the containment tree.  
3. Open the project category **> Collaborator Files > Peer Reviews > OK**.  
4. Click the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) next to **Scope**.  
5. Select the smart package **>** select the plus ![plus icon](../assets/MBSE/Plus.png) **> OK**.  
6. Check that your options are identical to **Figure 5**.  
7. From **Scope**, copy the smart package name and paste to **Document name > Publish**.  

---
![Publish the Peer Review Artifact](../assets/MBSE/peerreviewpublisher.png)

<div style="text-align: center;">
<i>Figure 5 Publish the Peer Review Artifact</i>
</div>
---

### Grant Permissions to Reviewers in Teamwork Cloud

When initiating a review activity, you must confirm that all reviewers have the Review Contributor role for the correct category(s) enabled. Otherwise, the reviewers will not be able to access the review artifact. See [MBSE-WI-001 Teamwork Cloud Administrator Work Instruction](#references) for more detail.  

## Perform Peer Review in Cameo Collaborator

This procedure describes the review, comment, and resolve portion of the review activity.  

### Review the Artifact in Cameo Collaborator

Reviewers are tasked with reviewing the artifact and identifying problems with comments.  

1. Open the artifact in Teamwork Cloud. Review the content diagram notes.  
2. Open an element in the diagram from the main screen or containment tree.  

---
![Cameo Collaborator Containment Tree](../assets/MBSE/peerreviewcollaboratormenu.png)  

<div style="text-align: center;">
<i>Figure 6 Cameo Collaborator Containment Tree</i>
</div>
---

#### Add comment

1. In the element, click the comment tool ![comment icon](../assets/MBSE/comment.png) to the bottom right.  
2. Click anywhere in the diagram to open **Graphical Comment** and the top-left toolbar.  
3. Select the rectangle tool ![rectangle tool icon](../assets/MBSE/rectangletool.png) from the main toolbar. Click and drag to create a comment shape.  
4. Locate it on or near whichever element(s) your comment is addressing.  
5. Select the shape, then select the comment tool ![comment icon](../assets/MBSE/comment.png) from the main toolbar.  
6. Enter `your name` in **Title** and `your comment` in **Comment > Done**.  

### Review Comments in Cameo Collaborator

1. Open Teamwork Cloud **> Resources**. Navigate to and open the peer review artifact.  
2. Select the comment tool ![comment icon](../assets/MBSE/comment.png) in the top right. All comments on this artifact are displayed to the right.  
3. Select a comment to open the respective element.  

### Close Comments during the Peer Review Activity

The author closes a comment when the identified problem has been corrected, or if they deem the comment invalid or out-of-scope for the activity. The moderator closes a comment once they verify the author has corrected the problem as described in the review comments.  

1. For valid comments, update the model in the **original project** to correct the problem.  
2. In Cameo Collaborator, locate the comment and select the reply tool ![reply icon](../assets/MBSE/reply1.png).  
3. Enter `your reply` in **Comment** explaining the work you completed to address the problem, then **Enter**.  
4. Click the checkbox next to the original comment (*not* the comment you just made) to close the comment.  
5. For invalid comments, locate the comment and select the reply tool ![reply icon](../assets/MBSE/reply1.png).  
6. Enter `your reply` in **Comment** explaining why the comment should be closed with no action taken.  

| Note |
|---|
| Do not resolve comments by making changes to the peer review project or the original project in Cameo Collaborator. |

## Close Peer Review Activity
The final step is to close the peer review activity.  

### Update Project Usage Reference for Review Close

  1. In the Peer Review Project in Cameo, go to **Options > Project Usages**.  
  2. Right-click the original model **> Lock**, then right-click again and **Change Version**.  
  3. Select the correct version of the original model **> OK > OK**.  
  4. Go to **Collaborate > Commit Changes to Server**.  

### Publish Peer Review Artifact to Cameo Collaborator for Review Close

1. In the Peer Review Content Diagram, update the review start/close note with the review close version number.  

| Note |
|---|
| The activity documented in **Figure 7** began with Version 1 of the original model and ended with Version 4. The note provides traceability to all changes resulting from the review activity. |

---
![Peer Review Start/Close Note](../assets/MBSE/peerreviewnote.png)

<div style="text-align: center;">
<i>Figure 7 Peer Review Start/Close Note</i>
</div>
---

1. Go to **Tools > Cameo Collaborator > Publish**.  
2. Select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) by **Category Name**.  
3. Go to the original project **> Collaborator Files > 1 - Peer Reviews > OK**.  
4. Select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) by **Scope**.  
5. Select the peer review artifact, then select the plus ![plus icon](../assets/MBSE/Plus.png)**> OK**.  
6. Expand and configure your **Options** per **Figure 8**, then **Publish**.  

---
![Publish the Completed Peer Review Artifact](../assets/MBSE/peerreviewpublisher2.png)  

<div style="text-align: center;">
<i>Figure 8 Publish the Completed Peer Review Artifact</i>
</div>
---

### Archive the Peer Review Artifact

1. In Teamwork Cloud, open your project category, then open **Collaborator Files > Peer Reviews**.  
2. To the right, select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) **> Move Resource**.  
3. Under the project containment tree, select **Archived Peer Reviews > Move**.  

# References

| Document Number | Name|
| ---| ---|
|MBSE-WI-001| Teamwork Cloud Administrator|
|MBSE-WI-002| Project Templates|

# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|conf.1| - |03-02-2026| D. Ricart| Draft uploaded to General Engineering Practices Confluence space.|

# Appendix

