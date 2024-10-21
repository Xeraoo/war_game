# Game Simulation

## Description
This repository contains a simple game simulation implemented in Python. The game features different entities such as soldiers, tanks, and jets, each with their own characteristics and methods for attacking and taking damage. The simulation runs through a predefined sequence of actions, demonstrating interactions between various entities.

## Features
- **Game Entities:** Supports multiple types of entities: Soldiers, Tanks, and Jets, each with unique properties and behaviors.
- **Combat Mechanics:** Entities can attack one another, take damage, and be defeated based on their health.
- **Simulation Phases:** The game is structured into phases, allowing for organized combat sequences.

## Classes
### `GameEntity`
- Base class representing a general entity in the game.
- Attributes: `name`, `health`
- Methods: 
  - `take_damage(amount)`: Reduces health based on the damage taken.

### `Soldier`
- Inherits from `GameEntity`.
- Attributes: `strength`
- Methods:
  - `attack(enemy)`: Attacks the specified enemy and deals random damage based on strength.

### `Tank`
- Inherits from `GameEntity`.
- Attributes: `armor`
- Methods:
  - `take_damage(amount)`: Modifies damage taken based on armor value.
  - `fire_main_gun(enemy)`: Deals significant damage to the specified enemy.

### `Jet`
- Inherits from `GameEntity`.
- Attributes: `speed`
- Methods:
  - `attack(enemy)`: Performs an airstrike on the specified enemy.
  - `retreat()`: Retreats to a safe distance.

## How to Run the Simulation
1. Clone the repository or download the script.
2. Run the program in a Python environment.

