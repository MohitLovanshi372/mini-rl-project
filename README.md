# Mini RL Environment

## Description
This project simulates a simple Reinforcement Learning environment where an agent navigates a grid to reach a goal.

## Features
- Grid-based environment
- Reward system
- Random & Smart agent
- Grader (score calculation)

## Rewards
- Goal: +10
- Obstacle: -5
- Step: -1

## Run
python main.py
Demo explanation:
The agent navigates the grid using reward-based learning to reach the goal efficiently
# 🤖 Mini RL Environment

A lightweight, hackathon-ready Reinforcement Learning grid environment for the Meta AI Hackathon.

## 🎯 Overview

This project implements a simple grid-based navigation environment where an agent learns to move from a **Start (S)** position to a **Goal (G)** while avoiding obstacles.

**Real-World Use Case:** Delivery Robot Navigation  
Imagine a warehouse robot that needs to navigate from a pickup point to a delivery location while avoiding shelves and other obstacles. This environment simulates that scenario in a simplified 2D grid.

## 🚀 Quick Start

```bash
# Run the demo
python main.py
 ## OpenEnv Compatibility

This environment follows standard RL interface:

- reset(): returns initial state
- step(action): returns (state, reward, done, info)
- deterministic and reproducible
- suitable for agent evaluation

Compatible with OpenAI Gym / OpenEnv style environments.