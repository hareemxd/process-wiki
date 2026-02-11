---
title: MBSE Style Guide
subtitle: Model-Based Systems Engineering
---

## Why This Guide Exists

Modern engineering efforts focus on *systems*, not individual or disconnected products. A system is an **interactive web of hardware, software, people, processes, and data** that evolves over time. When the relationships within a system are managed informally—or only in documents—projects become error-prone and difficult to manage.

This style guide exists to establish **clear, consistent, and scalable practices** for applying *Model-Based Systems Engineering (MBSE)* across the system lifecycle. It defines how systems are modeled, how information is structured, and how engineering intent is preserved as systems grow and change.

---

## Systems

### What Is a System

A **system** is a set of interacting elements organized to achieve a purpose.

A useful way to think about this is with a familiar example.

A **desktop computer and a monitor together form a system**. Each works independently, but only when connected and functioning do they create a functioning computer display.

If you’ve ever had to troubleshoot:
- a loose or damaged cable
- the wrong input selected on the monitor
- incompatible ports or adapters
- a display that powers on but shows nothing

—you already understand what a **systems problem** is. Some characteristic of the parts' **interactions** is the root of the issue.

The importance of the systems problem concept becomes clear when thinking about a common mode of transportation: aircraft.

A single aircraft is a system, which itself is comprised of *thousands* of systems. Instead of a single cable between computer and monitor, aircraft rely on countless interactions between physical components, software logic, human operators, maintenance actions, and operating environments. Failures rarely come from one part breaking in isolation; they emerge from **misunderstood, poorly controlled, or undocumented interactions**. 

:::{figure} ../img/MBSE/aircraftsystems.png
:align: center
:name: figure1-mbsesghp

Aircraft Systems

:::

That difference in scale—not a difference in kind—is why systems need their own engineering discipline.

### Systems Engineering

Traditional engineering disciplines focus on optimizing individual parts. Systems engineering exists because **successful systems depend on how parts work together**, not just how well they work individually.

Systems engineering addresses:
- Interfaces and interactions
- Trade-offs across competing constraints
- End-to-end behavior, not just component performance
- The full lifecycle, from concept through operation and change

Without this discipline, complexity accumulates silently—until it surfaces as cost overruns, delays, or failures that are difficult to diagnose after the fact.

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

:::{figure} ../img/MBSE/car_bdd.png
:align: center
:name: figure2-mbsesghp

Block Definition Diagrams define the *composition* of a system. A vehicle is composed of the blocks Transmission, Engine, and Wheel (itself composed of Brake and Tire).

:::

:::{figure} ../img/MBSE/acpower_ibd.png
:align: center
:name: figure3-mbsesghp

Internal Block Diagrams define the *relationships* between elements within a system. Models can impose design requirements through *specifications*. The diagram will throw an error if the modeler attempts to connect the blocks with a DC power cord.

:::

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

Start with **Work Instructions** in the left sidebar. If you prefer a jump list, use the cards below.

:::{grid} 2
:gutter: 2

:::{card} Problem Domain System Context Diagrams
:link: ./Work Instructions/Problem Domain System Context Diagrams
:link-type: doc

Procedures to create structural diagrams representing a system's problem domain.
:::

:::{card} Peer Review
:link: ./Work Instructions/Peer Review
:link-type: doc

Procedure to conduct peer review activities in Cameo Collaborator.
:::

:::{card} Teamwork Cloud Administrator
:link: ./Work Instructions/Teamwork Cloud Administrator
:link-type: doc

Administration procedures for Teamwork Cloud.
:::

:::{card} Project Templates
:link: ./Work Instructions/Project Templates
:link-type: doc

Templates for setting up and configuring SysML projects.
:::

:::
