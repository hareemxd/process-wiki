---
title: Schematic Review Checklist
author: David Ricart
project: ProcessWiki
genre: checklist
domains:
    - Engineering
    - Configuration Management
tags:
    - Form
---
 
 # CM-RC-001 Schematic Review Checklist  

Owner:              ___________________

Part Description:   ___________________

Part Number:        ___________________

Revision:           ___________________
| ID        | Review Question                                                                                     | Y| N|
| --------- | --------------------------------------------------------------------------------------------------- | -|-|
| **CI-1**  | Does the schematic pass the Xpedition Design Rules Check?                                           | ☐|☐|

### Style  
| ID        | Review Question                                                                                     | Y|N|
| --------- | --------------------------------------------------------------------------------------------------- | -|-|
| **CI-2**  | Are pull-ups positioned above their nets and pull-downs below their nets?                           | ☐|☐|
| **CI-3**  | Are all ground symbols pointing down?                                                               | ☐|☐|
| **CI-4**  | Is all text unobstructed?                                                                           | ☐|☐|
| **CI-5**  | Is all text oriented horizontally?                                                                  | ☐|☐|
| **CI-6** | Are notes, comments, and special instructions clearly written and free of ambiguity?                | ☐|☐|

### Configuration  
| ID        | Review Question                                                                                     | Y|N|
| --------- | --------------------------------------------------------------------------------------------------- | -|-|
| **CI-7**  | Do all external configurations include a specification note?                                        | ☐|☐|
| **CI-8**  | Are all component reference designators unique, correct, and consistently labeled?                  | ☐|☐|
| **CI-9**  | Are all component values, tolerances, and ratings clearly defined and appropriate for the design?   | ☐|☐|
| **CI-10**  | Are power pins properly connected, with correct net names and expected voltage rails?               | ☐|☐|
| **CI-11**  | Are all nets clearly named, with no conflicting or ambiguous net labels?                            | ☐|☐|
| **CI-12** | Are component symbols correct and aligned with manufacturer datasheets?                             | ☐|☐|
| **CI-13** | Are all connectors fully defined, including pin numbers, functions, and directions?                 | ☐|☐|
| **CI-14** | Has the bill of materials been cross-checked against the schematic?                                 | ☐|☐|

### Design Quality
| ID        | Review Question                                                                                     | Y|N|
| --------- | --------------------------------------------------------------------------------------------------- | -|-|
| **CI-15**  | Are decoupling/bypass capacitors placed according to best practices for each IC?                    | ☐|☐|
| **CI-16**  | Are differential pairs clearly labeled and correctly routed from a logical standpoint?              | ☐|☐|
| **CI-17**  | Are analog and digital domains properly isolated or partitioned where necessary?                    | ☐|☐|
| **CI-18** | Have all no-connect pins been intentionally verified and documented as NC?                          | ☐|☐|
| **CI-19** | Are all protection devices (TVS, fuses, OCP, ESD diodes) included where appropriate?                | ☐|☐|
| **CI-20** | Are test points provided for critical nets (power rails, clocks, communication lines)?              | ☐|☐|
| **CI-21** | Are timing-critical nets (clocks, resets) properly identified and validated?                        | ☐|☐|
| **CI-22** | Are all signal directions clear, and are buffer/level-translation needs properly addressed?         | ☐|☐|
| **CI-23** | Are all interfaces consistent with related documents (datasheets, ICDs, PCB footprint definitions)? | ☐|☐|


### Requirements
| ID        | Review Question                                                                                     | Y|N|
| --------- | --------------------------------------------------------------------------------------------------- | -|-|
| **CI-24** | Are power-up and power-down sequencing requirements satisfied?                                      | ☐|☐|
| **CI-25** | Does the schematic align with system-level requirements and architecture documentation?             | ☐|☐|


## Review Summary  
Notes:  ___________________



Date Review Completed: ___________________


Reviewer Signature: ___________________
