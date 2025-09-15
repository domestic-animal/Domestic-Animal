# Domestic-Animal
## 🛠 Tech Stack

![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-0E8C3A?style=for-the-badge&logo=pygame&logoColor=white)
![Pygame Menu](https://img.shields.io/badge/Pygame_Menu-512BD4?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-FF0000?style=for-the-badge&logo=security&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=checkmarx&logoColor=white)


## Overview

Domestic-Animal is a feature-rich desktop game built with PyQt5 and pygame. It offers multiple game modes, a launcher UI, profile management, and a variety of assets including music, backgrounds, and sprites. The project demonstrates advanced Python OOP, game engine design, and UI integration.

## Features

- PyQt5-based launcher and UI
- Multiple game modes: Story, Endless, VS
- Customizable player profiles
- Asset management for music, sprites, backgrounds
- Save/load game states
- Leaderboard and achievements
- Modular engine architecture
- Extensive use of OOP and design patterns

## Folder Structure

```
Assets/           # Images, music, sounds, backgrounds
assets_handler/   # Asset management modules
Engines/          # Game engine controllers and logic
Entities/         # Game entities: player, enemy, bullet, powerup
file/             # File management, profiles, save/load
launcher/         # Launcher UI, customization, leaderboard
menue_components/ # UI components for menus
profiles/         # Profile data and saves
pyqt_tests/       # PyQt test scripts
tests/            # Unit tests for core modules
main.py           # Main entry point (PyQt5 launcher)
requirements.txt  # Python dependencies
README.md         # Project documentation
```

## Installation

1. Clone the repository:
	```powershell
	git clone <repo-url>
	```
2. Install dependencies:
	```powershell
	pip install -r requirements.txt
	```
3. Run the game:
	```powershell
	python main.py
	```

## Usage

- Launch the game using `main.py`.
- Use the launcher UI to select game modes, customize profiles, and view leaderboards.
- Play through story or endless modes, or challenge friends in VS mode.

## Credits

- Assets: Custom and open-source resources
- Libraries: PyQt5, pygame, pygame_menu, cryptography, pytest

## License

This project is for educational and entertainment purposes. See LICENSE for details.