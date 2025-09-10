# PyTorch Snake Game AI
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A deep reinforcement learning Snake game built with PyTorch and Pygame. The agent learns to play Snake using Q-learning and neural networks. Built by Krystian Filipek

<div align="center">
  <img src="https://raw.githubusercontent.com/kfilipekk/Pytorch_snake/master/docs/images/demo.gif" alt="Snake AI Training Demo" width="600"/>
</div>

## Features
- **Classic Snake Gameplay** with AI training
- **Deep Q-Network** with experience replay
- **Live training graphs** showing progress
- **Manual play mode** for testing

## Quick Start
```bash
git clone https://github.com/kfilipekk/Pytorch_snake.git
cd Pytorch_snake
pip install .
python main.py
```

## AI Details
- **State:** 11D vector (danger, direction, food location)
- **Actions:** [straight, right, left] 
- **Rewards:** +10 (food), -10 (collision)
- **Model:** 2-layer neural network with experience replay

Developed by [kfilipekk](https://github.com/kfilipekk)
