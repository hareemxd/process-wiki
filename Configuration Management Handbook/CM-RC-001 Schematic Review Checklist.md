---
title: "Schematic Review Checklist"
author: "David Ricart"
project: "ProcessWiki"
genre: "checklist"
domains:
    - Engineering
    - Configuration Management
---
 
 # Schematic Review Checklist  

Owner:              ___________________

Part Description:   ___________________

Part Number:        ___________________

Revision:           ___________________
| ID        | Review Question                                                                                     | Y| N|
| --------- | --------------------------------------------------------------------------------------------------- | -|-|
| **CI-1**  | Are all component reference designators unique, correct, and consistently labeled?                  | ☐|☐|
| **CI-2**  | Are all component values, tolerances, and ratings clearly defined and appropriate for the design?   | ☐|☐|
| **CI-3**  | Are power pins properly connected, with correct net names and expected voltage rails?               | ☐|☐|
| **CI-4**  | Are ground references and ground symbol usage consistent across the schematic?                      | ☐|☐|
| **CI-5**  | Are decoupling/bypass capacitors placed according to best practices for each IC?                    | ☐|☐|
| **CI-6**  | Are all nets clearly named, with no conflicting or ambiguous net labels?                            | ☐|☐|
| **CI-7**  | Are differential pairs clearly labeled and correctly routed from a logical standpoint?              | ☐|☐|
| **CI-8**  | Are pull-up/pull-down resistors present where required (reset lines, configuration pins, etc.)?     | ☐|☐|
| **CI-9**  | Are analog and digital domains properly isolated or partitioned where necessary?                    | ☐|☐|
| **CI-10** | Are high-current nets and critical power paths clearly identified and validated?                    | ☐|☐|
| **CI-11** | Are component symbols correct and aligned with manufacturer datasheets?                             | ☐|☐|
| **CI-12** | Are all connectors fully defined, including pin numbers, functions, and directions?                 | ☐|☐|
| **CI-13** | Are all interfaces consistent with related documents (datasheets, ICDs, PCB footprint definitions)? | ☐|☐|
| **CI-14** | Have all no-connect pins been intentionally verified and documented as NC?                          | ☐|☐|
| **CI-15** | Are all protection devices (TVS, fuses, OCP, ESD diodes) included where appropriate?                | ☐|☐|
| **CI-16** | Are test points provided for critical nets (power rails, clocks, communication lines)?              | ☐|☐|
| **CI-17** | Are timing-critical nets (clocks, resets) properly identified and validated?                        | ☐|☐|
| **CI-18** | Are all signal directions clear, and are buffer/level-translation needs properly addressed?         | ☐|☐|
| **CI-19** | Are power-up and power-down sequencing requirements satisfied?                                      | ☐|☐|
| **CI-20** | Does the schematic align with system-level requirements and architecture documentation?             | ☐|☐|
| **CI-21** | Are all design rule or corporate standard compliance requirements satisfied?                        | ☐|☐|
| **CI-22** | Are notes, comments, and special instructions clearly written and free of ambiguity?                | ☐|☐|
| **CI-23** | Has the bill of materials been cross-checked against the schematic?                                 | ☐|☐|
| **CI-24** | Have all known risks, open items, and mitigations been identified and documented?                   | ☐|☐|

## Review Summary  
Notes:  ___________________



Date Review Completed: ___________________


Reviewer Signature: ___________________
