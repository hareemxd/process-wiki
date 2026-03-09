---
title: MBSE Style Guide Home Page
subtitle: Model-Based Systems Engineering
---

## Why This Guide Exists

Modern engineering efforts focus on *systems*, not individual or disconnected products. When the relationships within/without a system are defined or controlled informally, projects become difficult to manage and prone to cost/schedule overrun.

This style guide exists to establish **clear, consistent, and scalable practices** for applying *Model-Based Systems Engineering (MBSE)* across the system lifecycle. It defines how systems are modeled, how information is structured, and how engineering intent is preserved as systems grow and change across the complete life cycle.

---

## Systems

### What Is a System

A **system** is a set of interacting elements (subsystems, products, services, processes, and people) organized to achieve a purpose.

A useful way to think about this is with a familiar example.

A **desktop computer and a monitor together form a system**. Each works independently, but only when connected and functioning do they create the user's need: a computer displayed on a monitor.

If you’ve ever had to troubleshoot:
- a loose or damaged cable
- the wrong input selected on the monitor
- incompatible ports or adapters
- a display that powers on but shows nothing

—you already understand what a **systems problem** is. Some characteristic of the **interactions** between parts is the root of the issue.

The importance of the systems problem concept becomes clear when thinking about a common mode of transportation: aircraft.

A single aircraft is a system, which itself is comprised of *hundreds* of subsystems. Instead of a single cable between computer and monitor, aircraft rely on countless interactions between physical components, software logic, human operators, maintenance actions, and operating environments. Failures rarely come from one part breaking in isolation; they emerge from **misunderstood, poorly controlled, or undocumented interactions**. 


---
![Aircraft Systems](../assets/aircraftsystems.png)


<div style="text=align: center;">
<i>Aircraft Systems</i>
</div>
---



### Systems Engineering

Traditional engineering disciplines focus on optimizing individual parts. Systems engineering exists because successful systems depend on how parts interact with each other, their environments, the operators, and over time.

Systems engineering addresses:
- Interfaces and interactions
- Trade-offs across competing constraints
- End-to-end behavior, not just component performance
- The full lifecycle, from concept through operation and change

---

## System Modeling

### What Is System Modeling

**System modeling** is the practice of representing a system using structured, formal models rather than relying solely on textual documents that describe a system using language and static diagrams.

In Model-Based Systems Engineering, the **model is the primary source of truth**. Documents, diagrams, and reports are derived from the model instead of being created and maintained separately.

A system model captures:
- What the system is made of (subsystems)
- What the system does (functions)
- How parts interact (interfaces)
- Requirements (structure, performance, behavior)

---
![Block Definition Diagram of a Vehicle](..assets/MBSE/car_bdd.png)

<div style="text=align: center;">
<i>Block Defition Diagrams define the system composition. A vehicle is composed of the Enginge, Wheel, and Transmission. The wheel can also be decomposed into smaller parts.</i>

---

![Internal Block Diagram of a System](..assets/MBSE/acpower_ibd.png)

<div style="text-align: center;">
<i>Internal Block Diagrams define the relationships between elements within a system. Models can impose design requirements through <b>specifications</b>. The diagram will throw an error if the modeler attempts to connect the blocks with a DC power cord.</i></div>

---

### Value Provided by System Modeling

**Visualization**  
Models provide a shared visual understanding of the system. Stakeholders can see structure and behavior without reading hundreds of pages.

**Requirements Management**  
Requirements are directly linked to system elements, structures, and behaviors, establishing clear traceability and verification methods.

**Documentation Management**  
Instead of manually synchronizing specifications, diagrams, and interface descriptions, models generate consistent outputs from a single authoritative source with built-in validation features.

---

## How This Style Guide Helps

This guide defines:
- Modeling conventions and structural rules
- Expectations for clarity, consistency, and traceability
- How models interface with documentation and change control
- How engineering intent is preserved over time

The goal is not modeling for its own sake. The goal is **engineering systems that can be understood, changed, and sustained**.

---

## Who This Is For

This guide is intended for:
- Systems engineers and system architects
- Engineers contributing to system-level models
- Technical leads responsible for interfaces and requirements
- Configuration and change management practitioners supporting MBSE

If your work depends on understanding or changing the system, this guide defines how that work is structured.

---

## From Concepts to Practice

This page explains **what systems are** and **why modeling matters**. The rest of this style guide explains **how those ideas are applied in practice**.

The MBSE process defined here translates system thinking into concrete, repeatable work. It describes:
- How system models are structured and decomposed
- How requirements are introduced, linked, and maintained
- How behavior, interfaces, and architecture are represented
- How models evolve as the system changes

Rather than treating modeling as a one-time design activity, the process treats the system model as a **living engineering artifact**—maintained, reviewed, and controlled throughout the lifecycle.

### What to Read Next

Work in progress.