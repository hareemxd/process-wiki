## **Applicable Domains:** Engineering, Configuration Management

### 1. Purpose

This document defines the procedure for setting up engineering data repositories with the correct baseline structure for a project. This includes organizing baseline content, folder structure, and subfolders across designated repositories in alignment with the approved project baseline.

---

### 2. Revision History

---

### 3. References

| Document Number | Title                                             |
| --------------- | ------------------------------------------------- |
| CM-04-001       | Initial Project Baseline Creation Process         |
| CM-04-002       | Maintain Configuration Integrity Process          |
| CM-02-001       | Permission Scheme for Controlled Engineering Data |

---

### 4. Scope

This process applies to all engineering data repositories used to manage baseline artifacts across:

- SharePoint (Microsoft documents)
- PTC Creo/Windchill (CAD models and engineering drawings)
- Xpedition/Cadence (electrical design data)
- DOORS (requirements)
- Git/Bitbucket (source code)
- Cameo (system models)

This SOP is executed **after** the completion of CM-04-001: Initial Project Baseline Creation.

---

### 5. Roles and Responsibilities

| Role                | Responsibility                                                        |
| ------------------- | --------------------------------------------------------------------- |
| Configuration Owner | Leads repository setup and ensures compliance with baseline structure |
| Engineering Lead    | Validates completeness and correctness of the repository setup        |
| Project Engineer    | Confirms coverage of configuration items and relationships            |

---

### 6. Repository Setup Requirements

Each repository must contain the complete and approved baseline data relevant to its domain. The following must be established:

- **Baseline artifacts**: All engineering data from the project baseline (e.g., CAD, documents, ECAD files, requirements) must be uploaded.
- **Repository-specific structure**: Follow tool conventions while ensuring alignment with DRS configuration principles.

#### SharePoint Repository Structure

Each SharePoint repository will follow this structure:

```
/Project Repository Root
   /[Document Number or Assembly Number]
       /Archive
       /[Current Version and Revision Folder, e.g., Rev A.0]
```

- Each document or assembly has its **own top-level folder**.
- **Archive** subfolder contains all superseded versions.
- **Current revision folder** contains the most up-to-date files for working and review.

#### Windchill / Xpedition / DOORS / Git / Cameo

- Use project-level containers, workspaces, or branches to segment baseline artifacts.
- Cross-reference item metadata (part number, document number, revision) to match PLM entries.
- Follow tool-specific implementation guides, ensuring traceability to project baseline.

---

### 7. Process Steps

#### Step 1: Prerequisite Completion

- Ensure CM-04-001 (Initial Project Baseline Creation) is complete.
- Confirm receipt of technical data package and import into DRS PLM.

#### Step 2: Create Repository Structure

- For each configuration item:
  - Create a **top-level folder** in the appropriate repository.
  - Label folder by **document or assembly number**.
  - Create the following subfolders:
    - `/Archive`
    - `/Rev A.0` (or first official revision per version control SOP)

#### Step 3: Load Baseline Artifacts

- Upload the baseline version of each artifact into its respective folder (e.g., Rev A.0).
- Validate filenames match the document/part number and revision level.

#### Step 4: Align With Configuration Items

- Cross-check loaded items with baseline list from CM-04-001.
- Ensure every configuration item is represented by:
  - Folder location
  - Revision folder
  - Supporting metadata (e.g., description, owner, traceability ID)

#### Step 5: Set Permissions

- Execute SOP CM-02-001 to apply the proper permission scheme to each folder.
- Default all archive folders to read-only.

#### Step 6: Repository Sign-Off

- Engineering Lead validates folder structure and artifact coverage.
- Configuration Owner audits naming, permissions, and structure consistency.
- Repository is marked ready for team-wide access.

---

### 8. Integration With Other Processes

This repository setup process must be coordinated with:

- **CM-04-001: Initial Project Baseline Creation** – source of baseline content
- **CM-04-002: Maintain Configuration Integrity** – defines rules for ongoing alignment and part number issuance
- **CM-02-001: Permission Scheme** – enforces controlled access
- **CM-01-001: Version Control** – governs update and check-in workflows

---

### 9. Compliance

- Repository structure must match the approved baseline before access is granted to project teams.
- Misaligned, incomplete, or unstructured repositories are considered out of configuration control.
- CM is responsible for performing audits before each major configuration event (e.g., revision release, baseline update).

---

**Document Control**

- Document Number: CM-04-003
- Effective Date: [To be Assigned]
- Owner: [Configuration Manager]
- Last Reviewed: [To be Assigned]

