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

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures for conducting peer reviews of MBSE artifacts. Adherence to this document ensures that peer reviews conform to DRS Naval Electronics process and quality standards. Review activities should be conducted regularly to:  

- keep pace with work updates, and
- limit each review activity to a reasonable scope.

# References

The Modeler should review [Table 1](#tab-work-instruction-inputs) to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-work-instruction-inputs</ac:parameter>
</ac:structured-macro>

| Description | Reference |
|---|---|
| The Modeler should have access to the required work elements in Teamwork Cloud. | MBSE-WI-001 Teamwork Cloud Administrator |
| The Modeler should be working in a Model using the DRS Naval Electronics MBSE package framework. | MBSE-WI-002 Project Templates |

# Roles and Responsibilities
Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in [Table 2](#tab-raci-definitions) and functional areas are assigned roles in [Table 3](#tab-raci--peer-review-chart).

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-raci-definitions</ac:parameter>
</ac:structured-macro>

| RACI Role | Definition |
|---|---|
| Responsible | Stakeholder is the owner of the document. |
| Accountable | Stakeholder depends on the document to effectively perform their job duties. |
| Consulted | Stakeholder provides input, which may or may not be optional, to the authoring of the document. |
| Informed | Stakeholder is made aware of the document. |
| Omitted | Not a stakeholder. |

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-raci-peer-review-chart</ac:parameter>
</ac:structured-macro>

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

# Terms

| Term | Definition |
|---|---|
|Smart Package| a special collection of model elements|
|Project Usage| a reference to a different project that provides access to that project's model elements|
|Category| synonymous with *folder* in Teamwork Cloud|
| Resource| synonymous with *file* in Teamwork Cloud|
| Containment Tree| synonymous with *file directory* in Teamwork Cloud|

# Procedure

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p>Before conducting a review, confirm that all changes to the system model(s) are complete and committed to the SysML server project.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="minLevel">2</ac:parameter>
  <ac:parameter ac:name="maxLevel">7</ac:parameter>
  <ac:parameter ac:name="type">list</ac:parameter>
  <ac:parameter ac:name="outline">true</ac:parameter>
</ac:structured-macro>



## Open the Peer Review Project

All peer reviews for a given program are contained in a separate project file so review comments do not clutter the system model.  

1. In Cameo, go to **Collaborate > Open Server Project**.
2. Locate the main project and select the ellipses ![ellipses](../assets/MBSE/Ellipses.png). Write down the *trunk number* displayed in the new window.
3. In the previous window, select the Peer Review Project under ![folder icon](../assets/MBSE/cameofolder.png)**Cameo Files > Open**.

---
<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-open-collab-project</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="opencollabproject.png"/>
</ac:image>
---

## Update Project Usages

Before creating the artifact, you must update the *project usages* of your Peer Review Project to reference the correct version of the original project.
 
1. In the Peer Review Project, go to **Options > Project Usages**.  
2. On the left, right-click the original project **> Lock**.  
3. Right-click the original project again, then **Change Version > OK > OK**.  
4. Go to **Collaborate > Commit Changes to Server**.  


## Create Peer Review Artifact

The Peer Review Artifact is the subject of the review: a *smart package* created by the author that contains all elements to be reviewed.
 

1. In the Peer Review Project, identify the **Reviews** package in the containment tree to contain the review artifact.
2. Right-click the package and **> Create Element > Smart Package**, and enter `YYYYMMDD - xxx` (the current date and a descriptive name for the review activity).
3. Above the containment tree, select the search icon, select **Any Element**, and search `peer review`. The top result is the Peer Review Content Diagram Template.
4. Copy the template into the new smart package, and rename the template `smart_package_name_CD`.
5. In the template, update the activity information fields and data markings.
6. Drag the model elements to be reviewed from the containment tree into the diagram (or select them in the smart package **Specification**).
7. Use **Align** ![align icon](../assets/MBSE/align.png) to organize the elements visually and use text headers to separate different element types; see [Figure 4](#fig-peer-review-content-diagram).

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>If you don't see the template in search results, check your project usages.</p>
  </ac:rich-text-body>
</ac:structured-macro>

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-peer-review-content-diagram</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="peerreviewcontentdiagram.png"/>
</ac:image>

---


## Publish Peer Review Artifact

The author publishes the smart package to Cameo Collaborator where teammates can review it and provide comments.

1. Go to **Tools > Cameo Collaborator > Publish**, and configure the publish fields/options per [Figure 5](#fig-publish-peer-review-package):  
   a.  **Document Name** matches the Smart Package name.  
   b.  **Category Name** is `Peer Reviews`.    
   c.  **Scope** is set to the package containing the Smart Package.  
   d. **Template** is set to `Diagrams`.  
   e. **Enable Commenting** and **Update Previously Published Document** are checked.  
2. Select **Publish**.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-publish-peer-review-package</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="publishpeerreviewpackage.png"/>
</ac:image>

---


## Perform Peer Review in Cameo Collaborator

### Review the Artifact

Reviewers are tasked with reviewing the Peer Review Artifact and identifying problems that are in-scope. 

1. Open the artifact in Teamwork Cloud. Review the content diagram notes.  
2. Open an element in the diagram from the main screen or containment tree.  


### Add Comments

Comments identify problems in the Peer Review Artifact and will be resolved by the author.

1. In the element, click the comment tool ![comment icon](../assets/MBSE/comment.png) to the bottom right.  
2. Click anywhere in the diagram to open **Graphical Comment** and the top-left toolbar.  
3. Select the rectangle tool ![rectangle tool icon](../assets/MBSE/rectangletool.png) from the main toolbar. Click and drag to create a comment shape.  
4. Locate it on or near whichever element(s) your comment is addressing.  
5. Select the shape, then select the comment tool ![comment icon](../assets/MBSE/comment.png) from the main toolbar.  
6. Enter `your name` in **Title** and `your comment` in **Comment > Done**.  

### Review Comments

1. Open Teamwork Cloud **> Resources**. Navigate to and open the Peer Review Artifact.  
2. Select the comment tool ![comment icon](../assets/MBSE/comment.png) in the top right. All comments on this artifact are displayed to the right.  
3. Select a comment to open the respective element.  

### Resolve Comments

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p>Do not resolve comments by making changes to the Peer Review Project or the original project in Cameo Collaborator.</p>
  </ac:rich-text-body>
</ac:structured-macro>

The author resolves a comment when the identified problem has been corrected, or if they deem the comment invalid or out-of-scope for the activity.  

1. For valid comments, update the model in the **original project** to correct the problem.  
2. In Cameo Collaborator, locate the comment and select the reply tool ![reply icon](../assets/MBSE/reply1.png).  
3. Enter `your reply` in **Comment** explaining the work you completed to address the problem, then **Enter**.  
4. Click the checkbox next to the original comment (*not* the comment you just made) to close the comment.  
5. For invalid comments, locate the comment and select the reply tool ![reply icon](../assets/MBSE/reply1.png).  
6. Enter `your reply` in **Comment** explaining why the comment should be closed with no action taken.  


## Close the Peer Review Activity

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p>Make sure all comment-driven changes are complete before closing the activity.</p>
  </ac:rich-text-body>
</ac:structured-macro>

The final step is to close the peer review activity.  

  1. In the Peer Review Project in Cameo, go to **Options > Project Usages**.  
  2. Right-click the original model **> Lock**, then right-click again and **Change Version**.  
  3. Select the correct version of the original model **> OK > OK**.  
  4. Go to **Collaborate > Commit Changes to Server**.  
  5. In the Peer Review Content Diagram, update the review start/close note with the review close version number.  


---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-peer-review-start-close-note</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="peerreviewnote.png"/>
</ac:image>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>The activity documented in [Figure 7](#fig-peer-review-start-close-note) began with Version 1 of the original model and ended with Version 4. The note provides traceability to all changes resulting from the review activity.</p>
  </ac:rich-text-body>
</ac:structured-macro>

---

## Publish the Peer Review Artifact

1. Go to **Tools > Cameo Collaborator > Publish**.  
2. Select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) by **Category Name**.  
3. Go to the original project **> Collaborator Files > 1 - Peer Reviews > OK**.  
4. Select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) by **Scope**.  
5. Select the peer review artifact, then select the plus ![plus icon](../assets/MBSE/Plus.png)**> OK**.  
6. Expand and configure your **Options** per [Figure 8](#fig-peer-review-publish-two) (uncheck **Enable Commenting**), then **Publish**.  

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-peer-review-publish-two</ac:parameter>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="peerreviewpublisher2.png"/>
</ac:image>

---

## Archive the Peer Review Artifact

1. In Teamwork Cloud, open your project category, then open **Collaborator Files > Peer Reviews**.  
2. To the right, select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) **> Move Resource**.  
3. Under the project containment tree, select **Archived Peer Reviews > Move**.  


# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|conf.1| - |03-02-2026| D. Ricart| Draft uploaded to General Engineering Practices Confluence space.|

# Appendix
