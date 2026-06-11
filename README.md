# VRP OSM Optimization System

## Overview

This project implements the Vehicle Routing Problem (VRP) using OR-Tools with real-world geospatial data from OpenStreetMap (OSM).

The system optimizes vehicle routes under capacity constraints using a distance matrix based on Haversine distance.

---

## Features

- Vehicle Routing Problem (VRP) solver using OR-Tools
- OpenStreetMap (OSMnx) data integration
- Haversine distance matrix computation
- Capacity-constrained routing
- FastAPI inference endpoint
- Route visualization using Matplotlib
- Evaluation & benchmarking script

---

## Mathematical Formulation

### Objective

Minimize total travel distance:

Minimize:
Σ d(i, j) \* x(i, j)

### Constraints:

- Each node is visited exactly once
- Each vehicle respects capacity limit
- Routes start and end at depot

---

## System Architecture

OSM Data → Preprocessing → Distance Matrix → OR-Tools Solver → Routes → Visualization

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```
