---
title: MBSE Style Guide
subtitle: Model-Based Systems Engineering
---

## Why This Guide Exists

Modern engineering systems are no longer single products. They are **networks of hardware, software, people, processes, data, and constraints** that evolve over time. When those relationships are managed informally—or only in documents—projects become fragile, slow, and expensive to change.

This style guide exists to establish **clear, consistent, and scalable practices** for applying *Model-Based Systems Engineering (MBSE)* across the system lifecycle. It defines how systems are modeled, how information is structured, and how engineering intent is preserved as systems grow and change.

---

## Systems

### What Is a System

A **system** is a set of interacting elements organized to achieve a purpose (see **Systems definition** reference).

A useful way to think about this is with a familiar example:

A **desktop computer and a monitor together form a system**. Each works independently, but the *capability you care about*—being able to see and use your computer—only exists when they interact correctly.

If you’ve ever had to troubleshoot:
- a loose or damaged cable
- the wrong input selected on the monitor
- incompatible ports or adapters
- a display that powers on but shows nothing

—you were already dealing with a **systems problem**. The issue wasn’t “the monitor” or “the computer” alone. It was the **interaction between them**.

Now scale that idea up.

An aircraft is also a system—but instead of two elements, there are thousands. Instead of a single cable, there are countless interactions between physical components, software logic, human operators, maintenance actions, and operating environments. Failures rarely come from one part breaking in isolation; they emerge from **misunderstood, poorly controlled, or undocumented interactions**.

That difference in scale—not a difference in kind—is why systems need their own engineering discipline.

### Why Systems Require Their Own Engineering Discipline

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

**System modeling** is the practice of representing a system using structured, formal models rather than relying solely on narrative documents and disconnected diagrams (see **System modeling definition** reference).

In Model-Based Systems Engineering, the **model is the primary source of truth**. Documents, diagrams, and reports are derived from the model instead of being maintained separately.

A system model captures:
- What the system is made of
- What the system does
- How parts interact
- What constraints apply
- How requirements relate to design decisions

### Why Modeling Matters

Documents describe systems.  
Models **constrain and connect** them.

When information lives only in text:
- Relationships are implicit
- Inconsistencies hide easily
- Changes ripple unpredictably

Models make relationships explicit. When something changes, its effects are visible immediately—before they turn into downstream problems.

### Value Provided by System Modeling

**Visualization**  
Models provide a shared visual understanding of the system. Stakeholders can see structure and behavior without reading hundreds of pages.

**Requirements Management**  
Requirements are directly linked to system elements and behaviors, making traceability explicit and verifiable rather than inferred.

**Documentation Management**  
Instead of manually synchronizing specifications, diagrams, and interface descriptions, models generate consistent outputs from a single authoritative source.

**Change Impact Awareness**  
When requirements or design assumptions change, models reveal what is affected—early enough to manage the change intentionally.

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
