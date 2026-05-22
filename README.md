# FIBONACCI-SPECTRAL-DYNAMICS-
Fibonacci-Spectral Dynamics: computational framework for discrete dynamical systems using Fibonacci operators, spectral analysis, orbit structure, entropy flow, and invariant discovery. Includes Kaprekar comparison systems, CLI tools, dataset export, and visualization for eigen-spectra, phase-space evolution, and dynamical classification.

~~~

A computational framework for studying discrete dynamical systems through Fibonacci operators, spectral analysis, orbit structure, and invariant detection.

This project treats simple iterative rules as mathematical objects and explores their behavior using linear algebra, numerical simulation, and structural comparison with other dynamical systems (including Kaprekar-type maps).

---

## Overview

Fibonacci-Spectral-Dynamics is built around the idea that discrete update rules can be analyzed using:

- state-space evolution
- spectral decomposition (eigenvalues / eigenvectors)
- orbit structure and recurrence behavior
- entropy trends over time
- numerical invariant detection

The Fibonacci system is treated as a linear recurrence operator, while comparison systems (such as Kaprekar-style digit maps) provide nonlinear contrast.

---

## Core Systems

### Fibonacci Operator
A linear recurrence system expressed in state-space form:

- captures growth dynamics
- supports matrix representation
- enables spectral analysis

### Kaprekar-Type Operator
A nonlinear digit-based transformation:

- finite state space
- convergence behavior
- cycle and attractor formation

---

## Key Features

- discrete dynamical system simulation
- orbit generation and cycle detection
- eigenvalue / spectral analysis of operators
- entropy tracking over trajectories
- dataset export for repeated experiments
- comparative system analysis (linear vs nonlinear dynamics)

---

## CLI Interface

The framework includes a basic CLI for running experiments:

```bash
dynop run --system fibonacci --seed 1 --steps 50
dynop run --system kaprekar --seed 3524 --steps 50
dynop compare --steps 50
dynop export --system fibonacci --size 100




Research Direction (informal)


This project explores how different classes of discrete update rules behave under:




spectral structure


long-term orbit behavior


entropy evolution


state-space constraints




It is not a complete theory, but a structured way to experiment with these properties.



Requirements




Python 3.9+


numpy


scipy


matplotlib





Install


pip install -e .




Notes




This project is exploratory in nature.


Results depend heavily on system definition and state encoding.


Some tools are experimental and may evolve as the framework develops.





License

MIT


