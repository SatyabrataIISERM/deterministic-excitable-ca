# Deterministic Excitable Cellular Automaton
![Simulation](examples/simulation.gif)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)]()

Overview

This repository implements a **deterministic excitable cellular automaton** that models wave-like excitation patterns, qualitatively analogous to action potential propagation in excitable media.

The model was developed as part of coursework in computational biology.

---

Model Summary

Each cell can be in one of three states:

| State       | Meaning        |
|-------------|----------------|
| `0`         | Resting (OFF)  |
| `1`         | Excited (ON)   |
| `2`         | Refractory     |

The update rules:

1. Resting → Excited if **exactly two neighbors are excited**  
2. Excited → Refractory  
3. Refractory → Resting (recover)

Periodic (toroidal) boundary conditions are used.

---
## Visual Simulation

<p align="center">
  <img src="examples/simulation.gif" width="600px">
</p>


