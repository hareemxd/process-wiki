---
title: Teamwork Cloud Administrator
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction
document_number: MBSE-WI-001  
metamodel_domain: not applicable
metamodel_pillar: not applicable 
domains:  
    - Systems Engineering  
outputs:
    - Naval Electronics Teamwork Cloud Category
    - Naval Electronics Teamwork Cloud User Roles and Permissions
---




# Purpose
This Model Based Systems Engineering (MBSE) Work Instruction describes Teamwork Cloud administrative roles and responsibilities.
# DRS Naval Electronics SysML Meta Model

This Work Instruction applies to all spaces of the DRS Naval Electronics Meta Model; see [Figure 1](#fig-drsne-meta-model).

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
  <ri:attachment ri:filename="peerreviewmetamodel.png"/>
</ac:image>

---

# Roles and Responsibilities

Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in [Table 1](#tab-raci-roles-definitions) and functional areas are assigned in [Table 2](#tab-twc-admin-raci-chart).

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-raci-roles-definitions</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="tip">
  <ac:rich-text-body>
    <p><strong>Table 1.</strong> RACI Roles and Definitions</p>
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
  <ac:parameter ac:name="">tab-twc-admin-raci-chart</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="tip">
  <ac:rich-text-body>
    <p><strong>Table 2.</strong> Teamwork Cloud Administrator RACI Chart</p>
  </ac:rich-text-body>
</ac:structured-macro>

| Function | Role |
|---|---|
| Systems Engineering | A |
| Project Engineering | C |
| Configuration Management | R |
| Electrical Engineering | I |
| Mechanical Engineering | I |
| Software Engineering | I |
| Test Engineering | I |
| Manufacturing | I |
| Specialty Engineering | I |
| Quality | C |
| Training | C |
| Business Development | I |


# Terms

| Term | Definition |
|---|---|
|Category| synonymous with *folder* in Teamwork Cloud|
| Resource| synonymous with *file* in Teamwork Cloud|
| Containment Tree| synonymous with *file directory* in Teamwork Cloud|
| Role| a set of permissions with a name (e.g. **Resource Contributor**)|
|Permission| a function in Teamwork Cloud|
| Scope| the resources and/or categories to which a user's permissions apply|


# Procedure

## Setup the Work Environment

<ac:Structured-macro ac:name="info">
<ac:rich-text-body>
<p>This section applies primarily to non-administrative users.</p>



### Access Cameo Systems Modeler

Submit an IT request for a Cameo Systems Modeler license.

### Access Teamwork Cloud

Contact a Teamwork Cloud Administrator (TCA) to gain access to Teamwork Cloud.

## Setup New Program Category in Teamwork Cloud

1. Open **Resources > Naval Electronics**.
2. To the bottom-right, select the **Create Category** plus ![plus icon](../assets/MBSE/Plus.png).  
3. Enter the `program name` **> Enter**.  
4. Open the new category and create two sub-categories called `Cameo Files` and `Collaborator Files`.  
5. Open **Collaborator Files** and create two sub-categories called `1. Peer Reviews`, `2. Archived Peer Reviews`, and `3. Other Collaborator Files`.  


## Manage Roles in Teamwork Cloud

In Teamwork Cloud, a *role* is a set of *permissions* which are added to users or user groups. Permissions, in turn, are user functions in Teamwork Cloud, such as opening, editing, or moving a *resource*, creating or moving categories, and creating users or user groups. Proper control of permissions in Teamwork Cloud allows users to complete assigned tasks and, critically, minimizes the risk of incidental data hazards. 

When a user is assigned a role, they must also be given a *scope* for the role: the resource/category in which their role's permissions are enabled. Scope may be applied at any level of the Teamwork Cloud server, from a single resource to the top-level category (which would apply the user's permissions to all server contents).

See the [Appendix](#appendix) for a complete list of permissions.

### Add Roles

1. In Teamwork Cloud, open **Users** and locate the user to be assigned a role, then select the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) to the right.  
2. Select **Change Roles > Add Roles**, then click the search field and select one of the options shown in [Figure 2](#fig-add-role-user-twc).  
3. Select **Assignments** to open the containment tree.
4. Expand the tree, then apply permissions to specific categories or resources using the checkboxes.
5. In the top left, click the back arrow, then click the arrow in the top right to confirm.

---

<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">fig-add-role-user-twc</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p><strong>Figure 2.</strong> Add Role to User in Teamwork Cloud</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:image ac:align="center">
  <ri:attachment ri:filename="twcaddrolesgeneral.png"/>
</ac:image>

---

#### Program Admin Roles

The DRS Naval Electronics Admin must grant permissions to staff designated as Program Admins to perform their assigned responsibilities, such as **Archive the Peer Review Artifact**; see [**Peer Review**](#references).

1. Add these roles to Program Admin users:  
    * Resource Manager  
    * Resource Synchronization Manager  
    * Locks Administrator  
2. Set the scope for these roles at the top-level project category.  

#### Modeler Roles

Modelers need read/write access to their project's original model.

1. Add **Resource Contributor** to Modeler users.  
2. Set the scope for this role to these categories under the user's project category:  
    *  **Cameo Files** 
    * **Peer Reviews** and **Other Collaborator Files** (under **Collaborator Files**).

#### Reviewer Roles

Reviewers need read/write access to their project's **Peer Reviews** category.

1. Add **Resource Contributor** to Reviewer users.  
2. Set the scope for this role to these categories under the user's project category:  
    * **Peer Reviews** and **Other Collaborator Files** (under **Collaborator Files**).

# References

| Document Number | Name|
| ---| ---|
|MBSE-WI-001| Peer Review|

# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|conf.1| - |03-02-2026| D. Ricart| Draft uploaded to General Engineering Practices Confluence space.|

# Appendix

## List of Permissions

| Permission | Description|
|---|---|
|Administer Resources|Read, edit, lock/unlock, move resources.|
|Configure Data Markings|View the data markings menu item in Settings|
|Configure Server|Configure secured connection, LDAP connection, and manage server licenses.|
|Create Resource|Create a resource and add resources to the server.|
|Create User|Create, edit, or delete users.|
|Edit Resource Properties|Edit a resource's properties.|
|Edit Resources|Edit a resource.|
|Edit User Properties|Edit user details.|
|List All Resources|View and access all resources.|
|List All Users|View all users.|
|Manage Categories|Create, edit, delete existing categories.|
|Manage Model Permissions|View all users.|
|Manage Owned Resource Access Right|Manage resource-specific access rights.|
|Manage Security Roles|Create, edit, or delete roles.|
|Manage User Groups|Create, edit, or delete user groups.|
|Manage User Permissions|Grant and revoke roles.|
|Mark Data|Mark users, groups, resources, categories with access levels.|
|Read Resources|Open and read a resource.|
|Release Resource Locks|Release all locks on a resource.|
|Remove Resource|Delete a resource.|
|Remove User|Delete a user.|

