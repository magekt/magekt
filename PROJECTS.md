# Projects Documentation

This document provides a comprehensive overview of all projects in the magekt repository, including descriptions, file mappings, technologies, and instructions for running each project.

---

## Table of Contents

1. [Shooter Games](#shooter-games)
   - [Space Invaders Clone](#space-invaders-clone)
   - [Bullet Hell](#bullet-hell)
2. [MIDI Application](#midi-application)
   - [MIDI Sequencer](#midi-sequencer)

---

## Shooter Games

### Space Invaders Clone

**Description:**
A classic space invaders-inspired game where players control a spaceship at the bottom of the screen, moving left and right to avoid enemy projectiles while shooting down descending aliens.

**File Mappings:**
- `src/games/space_invaders/` - Main game directory
  - `main.py` - Entry point for the game
  - `game.py` - Core game logic and state management
  - `player.py` - Player spaceship class
  - `enemy.py` - Enemy alien class
  - `projectile.py` - Projectile/bullet class
  - `assets/` - Game sprites and sound effects
    - `sprites/` - Image files for players, enemies, and projectiles
    - `sounds/` - Audio files for shooting and explosions
  - `config.py` - Game configuration (window size, colors, speeds)

**Technologies Used:**
- Python 3.8+
- Pygame (Graphics and game loop)
- NumPy (Collision detection)

**How to Run:**
```bash
# Install dependencies
pip install pygame numpy

# Navigate to the project directory
cd src/games/space_invaders

# Run the game
python main.py
```

**Controls:**
- Arrow Keys (Left/Right) - Move spaceship
- Spacebar - Shoot
- ESC - Quit game
- P - Pause/Resume

**Features:**
- Progressive difficulty (enemies speed up over time)
- Score tracking
- Lives system
- Sound effects and music
- Collision detection

---

### Bullet Hell

**Description:**
An intense, fast-paced shooter where players must navigate through waves of incoming projectiles while fighting enemies. Features complex bullet patterns and challenging gameplay.

**File Mappings:**
- `src/games/bullet_hell/` - Main game directory
  - `main.py` - Entry point for the game
  - `game.py` - Core game logic and wave management
  - `player.py` - Player spaceship class with hitbox
  - `enemy.py` - Enemy types (basic, heavy, patterns)
  - `bullet.py` - Bullet and projectile patterns
  - `wave.py` - Wave manager and difficulty progression
  - `assets/` - Game sprites and sound effects
    - `sprites/` - Player, enemy, and bullet sprites
    - `sounds/` - Shooting, explosion, and background music
  - `config.py` - Game configuration and balance settings
  - `utils/` - Utility functions
    - `collision.py` - Collision detection algorithms
    - `particle.py` - Particle effects

**Technologies Used:**
- Python 3.8+
- Pygame (Graphics and game loop)
- NumPy (Mathematical calculations for bullet patterns)
- Math module (Trigonometry for bullet angles)

**How to Run:**
```bash
# Install dependencies
pip install pygame numpy

# Navigate to the project directory
cd src/games/bullet_hell

# Run the game
python main.py
```

**Controls:**
- WASD or Arrow Keys - Move player
- Left Mouse Button / Spacebar - Shoot
- ESC - Quit game
- P - Pause/Resume
- R - Restart after game over

**Features:**
- Multiple enemy types with different patterns
- Progressive wave system with increasing difficulty
- Score multiplier for dodging bullets
- Power-ups and special weapons
- Boss encounters
- Visual feedback for damage
- Sound effects and background music

---

## MIDI Application

### MIDI Sequencer

**Description:**
A versatile MIDI sequencer application that allows users to create, edit, and playback MIDI sequences. The application provides a user-friendly interface for composing music with support for multiple instruments, tempo control, and note editing.

**File Mappings:**
- `src/midi/` - Main MIDI application directory
  - `main.py` - Entry point for the application
  - `sequencer.py` - Core sequencer engine
  - `ui/` - User interface components
    - `main_window.py` - Main application window
    - `piano_roll.py` - Piano roll editor for note sequencing
    - `controls.py` - Playback and transport controls
    - `instrument_selector.py` - Instrument selection panel
    - `settings.py` - Settings and preferences dialog
  - `midi_handler.py` - MIDI I/O and playback functionality
  - `instruments.py` - Instrument definitions and configurations
  - `config.py` - Application configuration
  - `utils/` - Utility functions
    - `file_handler.py` - File save/load operations
    - `timing.py` - Timing and BPM calculations
  - `assets/` - Application resources
    - `sounds/` - Default instrument sounds
    - `icons/` - UI icons and images
  - `data/` - Sample MIDI files and presets

**Technologies Used:**
- Python 3.8+
- PyQt5 (GUI framework)
- python-midi / mido (MIDI handling)
- PyAudio (Audio playback)
- NumPy (Data handling)

**How to Run:**
```bash
# Install dependencies
pip install PyQt5 mido PyAudio numpy

# Navigate to the project directory
cd src/midi

# Run the application
python main.py
```

**Features:**
- **Piano Roll Editor**: Visual note input and editing on a piano roll interface
- **Instrument Selection**: Choose from various GM (General MIDI) instruments
- **Tempo Control**: Adjust BPM from 40 to 300 BPM
- **Track Management**: Create and manage multiple MIDI tracks
- **File Operations**: Save and load MIDI files (.mid format)
- **Playback Controls**: Play, pause, stop, and seek through sequences
- **Quantization**: Snap notes to grid for precise timing
- **Velocity Control**: Adjust note velocity for dynamics
- **Export**: Export compositions as standard MIDI files
- **Keyboard Shortcuts**: Quick access to common functions

**User Guide:**
1. Launch the application with `python main.py`
2. Select an instrument from the Instrument Selector panel
3. Click on the Piano Roll to add notes at desired positions
4. Adjust note duration by dragging the right edge of notes
5. Use the transport controls to play your composition
6. Set tempo using the BPM slider (default: 120 BPM)
7. Save your work using File > Save or Ctrl+S
8. Export as MIDI file for use in other DAWs

**Keyboard Shortcuts:**
- Ctrl+S - Save
- Ctrl+O - Open
- Ctrl+N - New Project
- Ctrl+E - Export
- Space - Play/Pause
- Delete - Remove selected note
- Ctrl+Z - Undo
- Ctrl+Y - Redo

---

## Common Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Virtual Environment Setup (Recommended)
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Install All Dependencies
```bash
# Install all project dependencies
pip install pygame numpy PyQt5 mido PyAudio
```

---

## Project Structure Overview

```
magekt/
├── src/
│   ├── games/
│   │   ├── space_invaders/
│   │   │   ├── main.py
│   │   │   ├── game.py
│   │   │   ├── player.py
│   │   │   ├── enemy.py
│   │   │   ├── projectile.py
│   │   │   ├── config.py
│   │   │   └── assets/
│   │   └── bullet_hell/
│   │       ├── main.py
│   │       ├── game.py
│   │       ├── player.py
│   │       ├── enemy.py
│   │       ├── bullet.py
│   │       ├── wave.py
│   │       ├── config.py
│   │       ├── utils/
│   │       └── assets/
│   └── midi/
│       ├── main.py
│       ├── sequencer.py
│       ├── midi_handler.py
│       ├── instruments.py
│       ├── config.py
│       ├── ui/
│       ├── utils/
│       ├── assets/
│       └── data/
├── PROJECTS.md
└── README.md
```

---

## Contributing

When adding new projects or features, please update this documentation to include:
- Clear project description
- Complete file mappings
- List of technologies used
- Step-by-step run instructions
- Key features and controls

---

## License

All projects in this repository are developed and maintained by magekt. Please refer to the LICENSE file for more information.

---

## Contact & Support

For issues, questions, or suggestions regarding any of these projects, please open an issue in the repository or contact the repository maintainer.

**Last Updated:** 2025-12-26
