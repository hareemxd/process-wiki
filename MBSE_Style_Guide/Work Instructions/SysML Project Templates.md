---
title: SysML Project Templates
subtitle: MBSE Work Instruction
project: MBSE Style Guide  
genre: Work Instruction
document_number: MBSE-WI-002  
metamodel_domain: not applicable
metamodel_pillar: not applicable 
domains:  
    - Systems Engineering  
outputs:
    - Naval Electronics SysML Project
---



# Purpose

This Model Based Systems Engineering (MBSE) Work Instruction demonstrates the procedures to create a new SysML project using the Naval Electronics project template and Naval Electronics MBSE styles.


# Procedure

<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="minLevel">2</ac:parameter>
  <ac:parameter ac:name="maxLevel">7</ac:parameter>
  <ac:parameter ac:name="type">list</ac:parameter>
  <ac:parameter ac:name="outline">true</ac:parameter>
</ac:structured-macro>

## Setup SysML project
### Use the Naval Electronics Project Template

1. In Cameo Systems Modeler, go to **Collaborate > Login**. 
2. Select a server, then **OK**, and enter `your username` and `password` **> Sign In**.
3. Go to **Collaborate > Open Server Project**, then select **MBSE WG Style Guide Processes > Open**.
4. In the project, go to **File > Save Project As**. Select a local destination, enter `your project name`, then **Save**.  
5. Open the local project, then go to **File > Project Properties**.  
6. Select **More** and go to **Advanced**.  
7. Select **Reset IDs > OK** and **Reset Project ID > OK > OK** to confirm the property updates.  

### Upload New Project to Teamwork Cloud

1. In the new project, go to **Collaborate > Add Project to Server**.
2. Click the ellipses ![ellipses icon](../assets/MBSE/Ellipses.png) to open the *containment tree* and select a *category*.
3. Select **More**, then uncheck **Maintain Mount Points**.
4. Add a comment to the text box (the first commit message of the server project), then select **Add** to upload the project.

### Add the Naval Electronics Styles Project Usage

1. Go to **Options > Project Usages**.
2. Click the plus ![plus icon](../assets/MBSE/Plus.png) **> Use Server Project**.
3. Inside the **Naval Electronics** category, select **Naval Electronics Profile**.
4. Select the highest version number, then **OK**.
5. Go to **Collaborate > Commit Changes to Server**. Add a comment to the text box (`updated project usages`), then **Commit**. 



# Revision History

| Version|Revision|Date|Author|Change History|
| ---|---|---|---|---|
|conf.1| - |03-02-2026| D. Ricart| Draft uploaded to General Engineering Practices Confluence space.|

# References

The Modeler should review [Table 1](#tab-work-instruction-inputs) to ensure they have the required process inputs for the work activities described in this MBSE Work Instruction.


<ac:structured-macro ac:name="anchor">
  <ac:parameter ac:name="">tab-work-instruction-inputs</ac:parameter>
</ac:structured-macro>


| Document | Description |
|---|---|
| MBSE-WI-001 Teamwork Cloud Administrator|The Modeler should have access to the required work elements in Teamwork Cloud. |

# Roles and Responsibilities
Roles and responsibilities for the MBSE Style Guide are assigned with a RACI chart. Roles are defined in [Table 2](#tab-raci-roles-definitions) and functional areas are assigned roles in [Table 3](#tab-project-templates-raci-chart).


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
  <ac:parameter ac:name="">tab-project-templates-raci-chart</ac:parameter>
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
|Project Usage| a reference to a different project that provides access to that project's model elements|
|Category| synonymous with *folder* in Teamwork Cloud|
|Containment Tree| synonymous with *file directory* in Teamwork Cloud|

# Appendix
