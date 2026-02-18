# Deterministic Cellular Automaton for Action Potential Propagation

This repository contains a deterministic cellular automaton model that captures qualitative features of neuronal excitation waves.

## Model Description

- Grid size: 100×100
- States:
  - 0 → Resting
  - 1 → Excited
  - 2 → Refractory
- Neighborhood: Moore (8 neighbors)
- Boundary: Periodic (torus)

## Rules

1. Resting → Excited if exactly two neighbors are excited
2. Excited → Refractory
3. Refractory → Resting

## Run


