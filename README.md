# Magekt Repository

Welcome to the **Magekt** repository! This is a comprehensive collection of web applications, interactive projects, and games built with modern web technologies.

## 📚 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Projects & Applications](#projects--applications)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [File Mapping](#file-mapping)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Magekt repository contains multiple interconnected projects including:

- **Web Applications**: Interactive web-based tools and utilities
- **Text-Based RPG Game**: A console-style adventure game
- **Utility Applications**: Various helper tools and utilities
- **Interactive Demos**: Showcase projects demonstrating web technologies

All projects are built with vanilla JavaScript, HTML, and CSS, ensuring broad compatibility and ease of deployment.

---

## Project Structure

```
magekt/
├── README.md                          # This file
├── index.html                         # Main landing page
├── games/
│   ├── text-rpg/
│   │   ├── index.html                # RPG game entry point
│   │   ├── game.js                   # Core game logic
│   │   ├── player.js                 # Player class and mechanics
│   │   ├── enemy.js                  # Enemy class and AI
│   │   ├── items.js                  # Item and inventory system
│   │   ├── styles.css                # RPG game styling
│   │   └── README.md                 # RPG documentation
│   └── [other games]/
├── apps/
│   ├── [web application 1]/
│   ├── [web application 2]/
│   └── [web application 3]/
├── utilities/
│   ├── [utility tools]/
│   └── [helper scripts]/
├── assets/
│   ├── images/                       # Images and graphics
│   ├── icons/                        # Icon assets
│   └── data/                         # JSON data files
└── docs/
    ├── INSTALLATION.md               # Installation instructions
    ├── API.md                        # API documentation
    └── CONTRIBUTING.md               # Contribution guidelines
```

---

## Projects & Applications

### 🎮 Text-Based RPG Game

**Location**: `games/text-rpg/`

A feature-rich text-based role-playing game with character progression, combat system, inventory management, and engaging gameplay mechanics.

#### Features:
- **Character Creation**: Customize your hero with different attributes
- **Combat System**: Turn-based battles with tactical options
- **Inventory Management**: Collect, use, and manage items
- **Enemy AI**: Dynamic enemy behavior and difficulty scaling
- **Progression System**: Level up, gain experience, and improve abilities
- **Status Effects**: Apply and manage various status conditions
- **Save/Load System**: Progress persistence between sessions

#### Files:
- `index.html` - Game interface and UI
- `game.js` - Main game loop and state management
- `player.js` - Player character class with abilities
- `enemy.js` - Enemy entities and combat logic
- `items.js` - Item database and inventory system
- `styles.css` - Game styling and animations

#### How to Play:
1. Navigate to `games/text-rpg/index.html`
2. Create your character
3. Choose your actions in battle
4. Defeat enemies and progress through levels
5. Upgrade equipment and abilities

---

### 💼 Web Applications

#### Application Categories:

**Productivity Tools**
- Tools designed to improve workflow and organization
- Real-time calculations and conversions
- Data visualization and management

**Educational Tools**
- Interactive learning experiences
- Tutorial systems
- Knowledge bases and references

**Utility Applications**
- Helper tools for daily tasks
- Quick access to frequently used functions
- Browser-based convenience apps

Each application includes:
- User-friendly interface
- Local storage for user data
- Responsive design for multiple devices
- Comprehensive help documentation

---

## Installation & Setup

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No backend server required
- No installation needed for most projects

### Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/magekt/magekt.git
   cd magekt
   ```

2. **Navigate to Project**
   ```bash
   # For the RPG game
   cd games/text-rpg/
   
   # For web applications
   cd apps/[application-name]/
   ```

3. **Run Locally**
   - Open `index.html` in your web browser
   - OR use a local server:
     ```bash
     python -m http.server 8000
     # Then visit http://localhost:8000
     ```

### Server Deployment

For deployment on a web server:

1. Upload repository contents to your web server
2. Ensure all file paths are correctly maintained
3. Verify assets are loading properly
4. Test all applications in production environment

---

## Usage Guide

### Text-Based RPG Game

**Starting the Game**
```
1. Open games/text-rpg/index.html
2. Click "New Game"
3. Enter your character name
4. Select your class
```

**Game Commands**
- **Attack**: Deal damage to enemy
- **Use Item**: Consume a healing or utility item
- **Special Ability**: Use class-specific power
- **Defend**: Reduce incoming damage
- **Flee**: Attempt to escape battle

**Inventory Management**
- Press "I" or click Inventory
- Use items directly from inventory
- Equip weapons and armor
- Sell unwanted items

### Web Applications

Each application has its own interface. General guidelines:

- **Input**: Provide required data in form fields
- **Process**: Click action buttons to execute functions
- **Output**: Results display in results section
- **Settings**: Adjust preferences in settings panel
- **Data**: Local storage persists your data

---

## File Mapping

### HTML Files

| File | Location | Purpose |
|------|----------|---------|
| index.html | `/` | Main landing page / Home |
| game.html | `/games/text-rpg/` | RPG game interface |
| app-*.html | `/apps/*/` | Individual application pages |

### JavaScript Files

| File | Module | Purpose |
|------|--------|---------|
| game.js | text-rpg | Game state and loop management |
| player.js | text-rpg | Player class and mechanics |
| enemy.js | text-rpg | Enemy entities and AI |
| items.js | text-rpg | Item and inventory system |

### CSS Files

| File | Scope | Purpose |
|------|-------|---------|
| styles.css | text-rpg | RPG game styling |
| responsive.css | global | Mobile responsiveness |
| theme.css | global | Color schemes and themes |

### Data Files

| File | Location | Content |
|------|----------|---------|
| enemies.json | `/assets/data/` | Enemy definitions |
| items.json | `/assets/data/` | Item database |
| skills.json | `/assets/data/` | Skill definitions |

---

## Core Components

### Player System
- **Classes**: Warrior, Mage, Ranger, Rogue
- **Attributes**: Strength, Dexterity, Intelligence, Endurance
- **Progression**: Level, Experience, Skill Points
- **Equipment**: Weapons, Armor, Accessories

### Combat System
- Turn-based mechanics
- Damage calculation with variance
- Critical hit system
- Status effects (poison, stun, burn, etc.)
- Special abilities per class

### Inventory System
- Item types: Weapons, Armor, Consumables, Quest Items
- Weight/capacity management
- Quick slots for frequent items
- Item combining and crafting

### Enemy System
- Difficulty scaling
- Loot drops (gold, items, experience)
- Boss encounters
- Special enemy types

---

## Development

### Architecture

The codebase follows a modular architecture:

```
┌─────────────────────────────────────┐
│       User Interface (HTML)          │
├─────────────────────────────────────┤
│    Game Logic & State (JavaScript)   │
├─────────────────────────────────────┤
│    Data & Assets (JSON/CSS)          │
└─────────────────────────────────────┘
```

### Code Standards

- **Naming**: camelCase for variables/functions, PascalCase for classes
- **Comments**: Clear documentation for complex logic
- **Functions**: Single responsibility principle
- **Structure**: Organized by feature/module

### Testing

For testing locally:

1. Open browser console (F12)
2. Check for any errors
3. Test all game features manually
4. Verify save/load functionality
5. Test across different browsers

---

## Browser Compatibility

✅ **Fully Supported**
- Chrome/Chromium (v90+)
- Firefox (v88+)
- Safari (v14+)
- Edge (v90+)

⚠️ **Partial Support**
- Internet Explorer 11 (basic functionality only)

---

## Performance Optimization

The repository uses several optimization techniques:

- **Lazy Loading**: Assets loaded on-demand
- **Caching**: Browser caching for static assets
- **Minification**: Production-ready compressed files
- **Event Delegation**: Efficient event handling
- **Asset Optimization**: Compressed images and fonts

---

## Data Persistence

### Local Storage

Applications use browser localStorage for:
- User preferences
- Game saves
- Progress tracking
- Settings and configuration

### Storage Limits

- Most browsers: 5-10MB per domain
- Check available space before saving large data
- Automatic cleanup of old data after 30 days (configurable)

---

## Security Considerations

- ✅ No sensitive data stored in localStorage
- ✅ Input validation on all user entries
- ✅ No external dependencies tracking users
- ✅ All processing done client-side
- ✅ No data sent to external servers

---

## Troubleshooting

### Game Won't Load
- Check browser console for errors (F12)
- Clear browser cache
- Try incognito/private mode
- Ensure JavaScript is enabled

### Save File Corrupted
- Clear browser localStorage:
  - Open DevTools (F12)
  - Go to Application → Local Storage
  - Delete entries for the domain
  - Restart application

### Performance Issues
- Close unnecessary browser tabs
- Clear browser cache
- Disable browser extensions
- Try a different browser

---

## Contributing

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Follow existing code style
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation as needed
- Be respectful and constructive

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🌐 Localization support

---

## Roadmap

### Planned Features

**Near Term** (Current Sprint)
- [ ] Additional RPG classes
- [ ] New game mechanics
- [ ] Enhanced UI/UX

**Mid Term** (Next Quarter)
- [ ] Mobile optimization
- [ ] New applications
- [ ] Multiplayer features

**Long Term** (Future)
- [ ] Backend API integration
- [ ] User authentication
- [ ] Cloud save system
- [ ] Community features

---

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.

**MIT License Summary**:
- ✅ Use for personal and commercial projects
- ✅ Modify and distribute
- ✅ Use privately
- ⚠️ Include license and copyright notice
- ❌ Hold liable for damages

---

## Support & Contact

### Getting Help

- 📖 Check the [Documentation](./docs/)
- 🎮 Read the [RPG Guide](./games/text-rpg/README.md)
- 💬 [Open an Issue](https://github.com/magekt/magekt/issues)
- 📧 Contact: via GitHub profile

### Community

- Report bugs and issues
- Suggest new features
- Share your experience
- Help other users

---

## Credits

### Built With
- **HTML5**: Structure and markup
- **CSS3**: Styling and animations
- **JavaScript (ES6+)**: Game logic and interactivity
- **localStorage**: Client-side data persistence

### Assets
- Custom-created game assets
- Open-source icons and fonts
- Community resources

---

## Changelog

### Version 1.0.0 (December 26, 2025)
- ✨ Initial release
- 🎮 Text-based RPG game
- 💼 Core web applications
- 📚 Complete documentation
- 🐛 Bug fixes and optimizations

---

## Frequently Asked Questions (FAQ)

**Q: Do I need to install anything to play?**
A: No! Just open the HTML files in your browser.

**Q: Where is my game saved?**
A: Game data is saved in your browser's localStorage automatically.

**Q: Can I use these projects for my own website?**
A: Yes! They're MIT licensed. See the LICENSE file for details.

**Q: Why isn't my save loading?**
A: Try clearing your browser cache or using an incognito window.

**Q: Can multiple users play on the same computer?**
A: Each browser profile has separate storage, so yes!

**Q: How do I report a bug?**
A: Open an issue on GitHub with details about what went wrong.

---

## Additional Resources

- [GitHub Repository](https://github.com/magekt/magekt)
- [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [HTML5 Guide](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS3 Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)

---

## Statistics

- 📁 Total Files: 50+
- 🎮 Games Included: 1 (RPG)
- 💼 Applications: Multiple productivity tools
- 📚 Documentation: Comprehensive
- 🧪 Test Coverage: Ongoing

---

**Last Updated**: December 26, 2025

**Repository**: [github.com/magekt/magekt](https://github.com/magekt/magekt)

**Author**: [magekt](https://github.com/magekt)

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/magekt/magekt.git

# Navigate to project
cd magekt

# Open in browser
# Option 1: Direct file
open index.html

# Option 2: Local server
python -m http.server 8000
# Visit http://localhost:8000
```

---

**Enjoy exploring the Magekt repository! Happy gaming and developing! 🚀**
