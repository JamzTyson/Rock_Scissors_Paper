# Modular Framework for Rock-Paper-Scissors Game.

![Rock Paper Scissors image](assets/rsp.png)

*A solo game of "Rock, Paper, Scissors" against the computer, implemented in
modern Python.*

## Purpose
This project provides a modular and extensible framework for creating and
experimenting with the Rock-Paper-Scissors game and its variants.

While the default game implements the classic three-choice version
(Rock, Paper, Scissors) with a simple Terminal interface, the architecture
supports:

- Adding more choices with cyclic rules
(e.g., Rock-Paper-Scissors-Lizard-Batman).
- Adding a more complex or graphical interface.
- Customizing input handling and game logic.
- Adding more players.
- Adding more advanced strategies for the computer player.
- Defining new rules and behaviors.

## Overview

A dynamic implementation of "Rock, Paper, Scissors" against the computer,
with support for additional choices. The game uses cyclic rules to determine
the winner, ensuring every option beats some choices and is beaten by an equal
number of other choices, thus there must be an odd number of choices.

## Features

- Play the classic version of "Rock, Paper, Scissors."
- Extend the game with custom rules, more choices.
- Unit tests (pytest) are provided to validate game logic.

## How It Works

Rather than hard coded "Scissor beats Paper" rules, the game generates rules
dynamically from a list of CHOICES, following the rules:

1. Each item beats `(n-1)//2` predecessors and is beaten by `(n-1)//2`
successors, where `n` is the total number of choices.
2. The total number of choices (`CHOICES`) must always be odd.
3. Choices cannot start with the letter 'Q' (reserved for "Quit").
4. All choices must start with a unique letter.

### Example Custom Configuration

An example configuration with five options:

```python
CHOICES = ('Rock', 'Batman', 'Paper', 'Lizard', 'Scissors')
```

The corresponding rules would be:

* Scissors decapitates Lizard.
* Scissors cuts Paper.
* Lizard eats Paper.
* Lizard poisons Batman.
* Paper disproves Batman.
* Paper covers Rock.
* Batman vaporizes Rock.
* Rock crushes Scissors.
* Batman smashes Scissors.
* Rock crushes Lizard.

If you make changes to CHOICES, ensure that you run
[test_default_choices.py](rock_scissors_paper_framework/tests/test_default_choices.py).

## Getting Started

### Prerequisites

- Python 3.10.11 or later.
- Pytest

See the [pyproject.toml](pyproject.toml) file for full details.

## Running the Game

1. Clone this repository:

```bash
git clone https://github.com/JamzTyson/Rock_Scissors_Paper.git
```

2. Navigate to the project directory:

```bash
cd Rock_Scissors_Paper
```

3. Run the game:

```bash
python rsp.py
```

## How to Play

* Choose an option by typing its initial letter (e.g., R for Rock, S for Scissors).
* The computer randomly selects its option.
* The winner is determined based on the predefined rules.
* Type `Q` to quit the game.

### Default Rules:

- Rock blunts Scissors: Rock wins
- Scissors cut Paper: Scissors wins
- Paper wraps Rock: Paper wins
- Game drawn when the player and the computer choose the same option.

## Contributing

Contributions are welcome! If you have ideas for new features, extended rules,
or bug fixes, feel free to submit a pull request. Please ensure your changes
are well-documented and accompanied by pytests if applicable.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

**Author:** JamzTyson

For inquiries, reach out through GitHub issues or discussions.
