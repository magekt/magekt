# FILE_MAPPING.md - Repository Structure Documentation

> **Last Updated**: 2025-12-26  
> **Repository**: magekt/magekt  
> **Documentation Version**: 1.0

## Table of Contents

1. [Overview](#overview)
2. [Directory Tree Structure](#directory-tree-structure)
3. [File Categories](#file-categories)
4. [Technology Stack](#technology-stack)
5. [Naming Conventions](#naming-conventions)
6. [Import Paths](#import-paths)
7. [Navigation Guide](#navigation-guide)
8. [Repository Statistics](#repository-statistics)

---

## Overview

This document provides a comprehensive guide to the magekt/magekt repository structure, helping developers navigate the codebase efficiently and understand the purpose of each directory and file.

### Quick Facts
- **Repository**: magekt/magekt
- **Purpose**: [Add repository purpose here]
- **Primary Language(s)**: [Add primary languages]
- **License**: [Add license information]
- **Maintainer**: magekt

---

## Directory Tree Structure

```
magekt/
├── docs/                          # Documentation files
│   ├── README.md                 # Repository documentation
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── API.md                    # API documentation
│   └── CHANGELOG.md              # Version history
├── src/                          # Source code directory
│   ├── components/               # Reusable components
│   │   └── [component-files]
│   ├── modules/                  # Feature modules
│   │   └── [module-files]
│   ├── utils/                    # Utility functions
│   │   ├── helpers.ts
│   │   ├── validators.ts
│   │   └── constants.ts
│   ├── services/                 # Business logic services
│   │   └── [service-files]
│   ├── types/                    # TypeScript type definitions
│   │   ├── index.ts
│   │   └── [type-files]
│   ├── config/                   # Configuration files
│   │   ├── environment.ts
│   │   └── settings.ts
│   └── index.ts                  # Main entry point
├── tests/                        # Test files
│   ├── unit/                     # Unit tests
│   │   └── [test-files]
│   ├── integration/              # Integration tests
│   │   └── [test-files]
│   └── fixtures/                 # Test data fixtures
├── .github/                      # GitHub configuration
│   ├── workflows/                # CI/CD workflows
│   │   ├── test.yml
│   │   ├── build.yml
│   │   └── deploy.yml
│   └── ISSUE_TEMPLATE/           # Issue templates
├── .husky/                       # Git hooks
│   ├── pre-commit
│   └── pre-push
├── .vscode/                      # VS Code configuration
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
├── node_modules/                 # Installed dependencies (git-ignored)
├── dist/                         # Compiled output (git-ignored)
├── coverage/                     # Test coverage reports (git-ignored)
├── .env.example                  # Environment variables template
├── .eslintrc.json               # ESLint configuration
├── .prettierrc                   # Prettier configuration
├── tsconfig.json                # TypeScript configuration
├── jest.config.js               # Jest testing configuration
├── package.json                 # Project dependencies and scripts
├── package-lock.json            # Locked dependency versions
├── .gitignore                   # Git ignore rules
├── .gitattributes               # Git attributes
├── README.md                    # Repository README
├── CHANGELOG.md                 # Version history
└── LICENSE                      # License file
```

---

## File Categories

### 📄 Configuration Files
These files configure tools and environments for the project.

| File | Purpose | Technology |
|------|---------|-----------|
| `package.json` | Project metadata, scripts, dependencies | NPM/Node.js |
| `tsconfig.json` | TypeScript compilation settings | TypeScript |
| `jest.config.js` | Unit testing configuration | Jest |
| `.eslintrc.json` | Code linting rules | ESLint |
| `.prettierrc` | Code formatting rules | Prettier |
| `.env.example` | Environment variables template | Node.js |
| `.gitignore` | Git ignore patterns | Git |

### 🔧 Build & Development Files
Files for building and developing the project.

| File | Purpose |
|------|---------|
| `dist/` | Compiled/bundled output |
| `node_modules/` | Installed npm packages |
| `coverage/` | Test coverage reports |

### 📚 Documentation Files
Project documentation files.

| File | Purpose |
|------|---------|
| `README.md` | Project overview and setup instructions |
| `CHANGELOG.md` | Version history and release notes |
| `docs/API.md` | API documentation |
| `docs/CONTRIBUTING.md` | Contribution guidelines |

### 🔨 Source Code Files

#### Components (`src/components/`)
Reusable UI/functional components with their own tests and documentation.

```
ComponentName/
├── ComponentName.tsx            # Main component
├── ComponentName.module.scss    # Component styles
├── ComponentName.test.tsx       # Component tests
├── index.ts                     # Public exports
└── README.md                    # Component documentation
```

#### Modules (`src/modules/`)
Feature-specific modules containing related functionality.

```
ModuleName/
├── components/                  # Module-specific components
├── services/                    # Module-specific services
├── types/                       # Module-specific types
├── index.ts                     # Module exports
└── README.md                    # Module documentation
```

#### Utils (`src/utils/`)
Utility functions and helpers.

- `helpers.ts` - General helper functions
- `validators.ts` - Input validation functions
- `constants.ts` - Application constants
- `formatters.ts` - Data formatting utilities

#### Services (`src/services/`)
Business logic and external API integration.

```
ServiceName.ts
├── Export class or functions
├── Connect to external APIs
└── Handle business logic
```

#### Types (`src/types/`)
TypeScript type and interface definitions.

```
index.ts                        # Main types export
├── User.types.ts
├── Component.types.ts
├── API.types.ts
└── Utility.types.ts
```

### 🧪 Test Files (`tests/`)

#### Unit Tests
Test individual functions and components in isolation.

```
tests/unit/
├── components/
├── services/
├── utils/
└── types/
```

#### Integration Tests
Test multiple components working together.

```
tests/integration/
├── api/
├── workflows/
└── scenarios/
```

### 🔄 GitHub Files (`.github/`)

#### Workflows (`.github/workflows/`)
CI/CD automation files.

- `test.yml` - Run tests on push/PR
- `build.yml` - Build distribution files
- `deploy.yml` - Deploy to production

#### Issue Templates (`.github/ISSUE_TEMPLATE/`)
Standardized issue creation templates.

- `bug_report.md` - Bug report template
- `feature_request.md` - Feature request template

### 🪝 Git Hooks (`.husky/`)
Pre-commit and pre-push hooks for code quality.

- `pre-commit` - Lint and format before commit
- `pre-push` - Run tests before push

---

## Technology Stack

### Runtime & Language
- **Node.js**: Runtime environment
- **TypeScript**: Static type checking
- **JavaScript (ES6+)**: Core language

### Frontend (if applicable)
- **React**: UI library/framework
- **SCSS/CSS**: Styling
- **HTML5**: Markup

### Build & Compilation
- **Webpack/Rollup**: Module bundler
- **Babel**: JavaScript transpiler
- **TypeScript Compiler**: Type checking and transpilation

### Testing
- **Jest**: Unit testing framework
- **React Testing Library**: Component testing
- **Supertest**: HTTP assertion library (if API testing)

### Code Quality
- **ESLint**: JavaScript linting
- **Prettier**: Code formatting
- **Husky**: Git hooks
- **lint-staged**: Run linters on staged files

### Development Tools
- **VS Code**: Recommended IDE
- **npm/yarn**: Package managers
- **Git**: Version control

---

## Naming Conventions

### Files & Directories

| Type | Convention | Example |
|------|-----------|---------|
| Component directory | PascalCase | `UserProfile/`, `LoginForm/` |
| Component file | PascalCase | `UserProfile.tsx` |
| Utility file | camelCase | `formatDate.ts`, `validateEmail.ts` |
| Type file | PascalCase with `.types` | `User.types.ts`, `Component.types.ts` |
| Service file | camelCase or Class name | `userService.ts`, `AuthService.ts` |
| Test file | `[name].test.ts(x)` | `User.test.ts`, `login.test.ts` |
| Config file | camelCase or dotfiles | `.eslintrc.json`, `environment.ts` |

### Code Identifiers

| Type | Convention | Example |
|------|-----------|---------|
| Classes | PascalCase | `UserService`, `AuthProvider` |
| Functions | camelCase | `formatDate()`, `validateEmail()` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_ENDPOINT` |
| Variables | camelCase | `userName`, `isLoading` |
| Interfaces | PascalCase, prefix I | `IUser`, `IComponent` |
| Types | PascalCase | `UserType`, `ComponentProps` |
| Enums | PascalCase | `UserRole`, `Status` |

### Git & Version Control

- **Branches**: `feature/feature-name`, `bugfix/issue-name`, `docs/doc-name`
- **Commits**: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `style:`, `chore:`
- **Tags**: `v1.0.0` (semantic versioning)

---

## Import Paths

### Absolute Imports (if configured)
```typescript
// Instead of relative imports:
import { User } from '../../../types/User.types';

// Use absolute imports:
import { User } from '@/types/User.types';
```

### Path Aliases (tsconfig.json)
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@services/*": ["src/services/*"],
      "@types/*": ["src/types/*"],
      "@utils/*": ["src/utils/*"]
    }
  }
}
```

### Import Organization
```typescript
// 1. External dependencies
import React from 'react';
import { useNavigate } from 'react-router-dom';

// 2. Absolute imports from project
import { User } from '@types/User.types';
import { UserService } from '@services/UserService';

// 3. Relative imports
import { UserProfile } from '../components/UserProfile';

// 4. Styles
import styles from './User.module.scss';
```

---

## Navigation Guide

### Quick Links to Common Directories

#### For UI Development
```
src/components/          # Reusable UI components
src/utils/              # Styling utilities, formatters
```

#### For Feature Development
```
src/modules/[FeatureName]/   # Feature-specific code
src/services/                # Business logic
src/types/                   # Type definitions
```

#### For Testing
```
tests/unit/              # Unit tests
tests/integration/       # Integration tests
tests/fixtures/          # Test data
```

#### For Configuration
```
.vscode/                 # Editor configuration
.github/                 # GitHub configuration
.husky/                  # Git hooks
```

### Finding Things

**Need to add a new feature?**
1. Create feature directory: `src/modules/FeatureName/`
2. Add components: `src/modules/FeatureName/components/`
3. Add services: `src/modules/FeatureName/services/`
4. Add tests: `tests/unit/modules/FeatureName/`
5. Update types: `src/types/` or module-specific types

**Need to fix a bug?**
1. Find the affected component/service
2. Create/update test in `tests/unit/` or `tests/integration/`
3. Implement the fix
4. Verify tests pass

**Need to add a reusable component?**
1. Create directory: `src/components/ComponentName/`
2. Add component file: `src/components/ComponentName/ComponentName.tsx`
3. Add styles: `src/components/ComponentName/ComponentName.module.scss`
4. Add tests: `src/components/ComponentName/ComponentName.test.tsx`
5. Export from: `src/components/ComponentName/index.ts`

---

## Repository Statistics

### Code Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Total Files | [To be calculated] | Includes all tracked files |
| Total Lines of Code | [To be calculated] | Excludes tests and node_modules |
| Total Test Files | [To be calculated] | Unit + Integration tests |
| Test Coverage | [To be calculated] | Run `npm run test:coverage` |
| Number of Components | [To be calculated] | Count of `src/components/*` |
| Number of Modules | [To be calculated] | Count of `src/modules/*` |
| Number of Services | [To be calculated] | Count of `src/services/*` |

### Dependencies

Run the following commands to get dependency statistics:

```bash
# Count total dependencies
npm ls --all | tail -1

# Get production dependencies
npm ls --prod | tail -1

# Get development dependencies
npm ls --dev | tail -1

# Check for outdated packages
npm outdated

# Check for vulnerabilities
npm audit
```

### Performance Benchmarks

| Metric | Target | Current |
|--------|--------|---------|
| Build Time | < 30s | [To be measured] |
| Test Suite Time | < 5s | [To be measured] |
| Bundle Size | < 500KB | [To be measured] |
| Code Coverage | > 80% | [To be measured] |

### Development Statistics

| Item | Count |
|------|-------|
| Active Branches | [To be counted] |
| Open Issues | [To be counted] |
| Open Pull Requests | [To be counted] |
| Total Commits | [To be counted] |
| Contributors | [To be counted] |

---

## Getting Started

### Setup Instructions
```bash
# Install dependencies
npm install

# Install git hooks
npx husky install

# Copy environment template
cp .env.example .env.local

# Start development
npm run dev
```

### Common Commands
```bash
# Development
npm run dev                 # Start development server
npm run build              # Build for production
npm run preview            # Preview production build

# Testing
npm test                   # Run all tests
npm run test:watch        # Run tests in watch mode
npm run test:coverage     # Generate coverage report

# Code Quality
npm run lint              # Run ESLint
npm run lint:fix          # Fix ESLint issues
npm run format            # Format code with Prettier
npm run format:check      # Check formatting

# Git
npm run prepare           # Setup git hooks
git push                  # Pre-push hooks run tests
```

---

## Contributing

Please see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed contribution guidelines.

### Summary
1. Create feature branch from `main`
2. Make changes following naming conventions
3. Write/update tests
4. Run `npm run lint:fix` and `npm run format`
5. Create pull request with clear description
6. Wait for CI/CD checks and code review

---

## Additional Resources

- [GitHub Issues](../../issues)
- [GitHub Discussions](../../discussions)
- [Project Board](../../projects)
- [Security Policy](.github/SECURITY.md)
- [Code of Conduct](.github/CODE_OF_CONDUCT.md)

---

**Last Updated by**: FILE_MAPPING generation script  
**Last Updated**: 2025-12-26
