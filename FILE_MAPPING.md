# File Structure & Mapping Documentation

This document provides a comprehensive guide to the magekt repository's file structure, organization, and navigation.

**Last Updated:** 2025-12-26  
**Repository:** magekt/magekt

---

## Table of Contents

1. [Directory Tree Overview](#directory-tree-overview)
2. [File Categories](#file-categories)
3. [Technology Stack](#technology-stack)
4. [Naming Conventions](#naming-conventions)
5. [Import Path Guide](#import-path-guide)
6. [Module Navigation](#module-navigation)
7. [Configuration Files](#configuration-files)
8. [Quick Reference](#quick-reference)

---

## Directory Tree Overview

```
magekt/
├── docs/                          # Documentation files
│   ├── architecture/              # System architecture docs
│   ├── guides/                    # User and developer guides
│   └── api/                       # API documentation
├── src/                           # Source code
│   ├── components/                # Reusable UI components
│   │   ├── common/                # Common/shared components
│   │   ├── forms/                 # Form-related components
│   │   └── layouts/               # Layout components
│   ├── pages/                     # Page components
│   ├── services/                  # Business logic & API services
│   │   ├── api/                   # API client services
│   │   ├── auth/                  # Authentication services
│   │   └── utils/                 # Service utilities
│   ├── hooks/                     # Custom React hooks
│   ├── context/                   # React context providers
│   ├── utils/                     # Utility functions
│   │   ├── helpers/               # Helper functions
│   │   ├── validators/            # Validation functions
│   │   └── formatters/            # Data formatters
│   ├── types/                     # TypeScript type definitions
│   │   ├── models/                # Data models
│   │   ├── api/                   # API response types
│   │   └── enums/                 # Enumeration types
│   ├── constants/                 # Application constants
│   ├── styles/                    # Global styles
│   │   ├── globals.css            # Global CSS
│   │   ├── variables.css          # CSS variables
│   │   └── themes/                # Theme configurations
│   ├── assets/                    # Static assets
│   │   ├── images/                # Image files
│   │   ├── icons/                 # Icon files
│   │   ├── fonts/                 # Font files
│   │   └── svgs/                  # SVG assets
│   └── App.tsx                    # Root application component
├── public/                        # Public static files
│   ├── index.html                 # HTML entry point
│   ├── favicon.ico                # Favicon
│   └── manifest.json              # PWA manifest
├── tests/                         # Test files
│   ├── unit/                      # Unit tests
│   ├── integration/               # Integration tests
│   ├── e2e/                       # End-to-end tests
│   └── __mocks__/                 # Mock data and functions
├── .github/                       # GitHub configuration
│   ├── workflows/                 # CI/CD workflows
│   ├── ISSUE_TEMPLATE/            # Issue templates
│   └── PULL_REQUEST_TEMPLATE/     # PR templates
├── config/                        # Configuration files
│   ├── webpack.config.js          # Webpack configuration
│   ├── jest.config.js             # Jest test configuration
│   └── babel.config.js            # Babel configuration
├── scripts/                       # Build and utility scripts
│   ├── build.js                   # Build script
│   ├── dev.js                     # Development server script
│   └── deploy.js                  # Deployment script
├── .env.example                   # Environment variables template
├── .eslintrc.json                 # ESLint configuration
├── .prettierrc                    # Prettier configuration
├── tsconfig.json                  # TypeScript configuration
├── package.json                   # Dependencies and scripts
├── package-lock.json              # Dependency lock file
├── README.md                      # Project README
├── CONTRIBUTING.md                # Contributing guidelines
├── LICENSE                        # License file
└── FILE_MAPPING.md                # This file
```

---

## File Categories

### Core Application Files

| File/Directory | Purpose | Type |
|---|---|---|
| `src/App.tsx` | Root application component | Component |
| `src/index.tsx` | Application entry point | Script |
| `public/index.html` | HTML template | HTML |

### Component Files

| Directory | Purpose | Pattern |
|---|---|---|
| `src/components/common/` | Reusable UI components | `Component.tsx`, `Component.module.css` |
| `src/components/forms/` | Form components | `FormName.tsx`, `useFormName.ts` |
| `src/components/layouts/` | Layout wrappers | `Layout.tsx` |
| `src/pages/` | Page-level components | `PageName.tsx` or `PageName/index.tsx` |

### Service & Logic Files

| Directory | Purpose | Pattern |
|---|---|---|
| `src/services/api/` | API client services | `serviceName.ts`, `serviceName.api.ts` |
| `src/services/auth/` | Authentication logic | `auth.service.ts`, `useAuth.ts` |
| `src/hooks/` | Custom React hooks | `useHookName.ts` |
| `src/context/` | Context providers | `ContextName.tsx`, `useContextName.ts` |
| `src/utils/helpers/` | Helper functions | `helperName.ts`, `helperName.helper.ts` |
| `src/utils/validators/` | Validation functions | `validateField.ts`, `validators.ts` |

### Type Definition Files

| Directory | Purpose | Pattern |
|---|---|---|
| `src/types/models/` | Data models | `Model.types.ts` |
| `src/types/api/` | API response types | `api.types.ts` |
| `src/types/enums/` | Enums and constants | `enums.ts` |

### Configuration & Build Files

| File | Purpose |
|---|---|
| `tsconfig.json` | TypeScript compiler options |
| `.eslintrc.json` | ESLint rules |
| `.prettierrc` | Code formatting rules |
| `package.json` | Project metadata & scripts |
| `config/webpack.config.js` | Webpack build configuration |
| `config/jest.config.js` | Jest testing configuration |

### Test Files

| Pattern | Purpose |
|---|---|
| `tests/unit/*.test.ts` | Unit tests |
| `tests/integration/*.test.ts` | Integration tests |
| `tests/e2e/*.spec.ts` | End-to-end tests |
| `tests/__mocks__/` | Mock data and functions |

### Documentation Files

| File | Purpose |
|---|---|
| `README.md` | Project overview and setup |
| `CONTRIBUTING.md` | Contribution guidelines |
| `docs/architecture/` | System architecture documentation |
| `docs/guides/` | User and developer guides |
| `docs/api/` | API documentation |

---

## Technology Stack

### Frontend Framework & Libraries

| Technology | Version | Purpose | Location |
|---|---|---|---|
| React | ^18.x | UI framework | `src/` |
| TypeScript | ^4.x | Type safety | `src/`, config files |
| React Router | ^6.x | Client-side routing | `src/pages/` |
| Context API | Native | State management | `src/context/` |

### Styling

| Technology | Purpose | Location |
|---|---|---|
| CSS Modules | Component-scoped styles | `src/components/**/*.module.css` |
| CSS Variables | Theme management | `src/styles/variables.css` |
| PostCSS | CSS processing | `config/` |

### Testing

| Technology | Purpose | Location |
|---|---|---|
| Jest | Unit testing | `tests/unit/`, `config/jest.config.js` |
| React Testing Library | Component testing | `tests/unit/`, `tests/integration/` |
| Cypress | E2E testing | `tests/e2e/` |

### Build & Tooling

| Technology | Purpose |
|---|---|
| Webpack | Module bundler |
| Babel | JavaScript transpiler |
| ESLint | Code linting |
| Prettier | Code formatting |
| npm | Package manager |

### API & Server

| Technology | Purpose | Location |
|---|---|---|
| Fetch API / Axios | HTTP requests | `src/services/api/` |
| REST API | Backend communication | Integration with `src/services/` |

---

## Naming Conventions

### File Naming

#### Components
- **Format:** `PascalCase.tsx`
- **Examples:** `Button.tsx`, `UserProfile.tsx`, `FormInput.tsx`
- **Folders:** `PascalCase/`
- **Example:** `src/components/common/Button/Button.tsx`

#### Hooks
- **Format:** `useHookName.ts`
- **Examples:** `useAuth.ts`, `useFetch.ts`, `useLocalStorage.ts`

#### Services
- **Format:** `serviceName.service.ts` or `serviceName.ts`
- **Examples:** `userService.ts`, `authService.ts`, `apiClient.ts`

#### Types/Interfaces
- **Format:** `types.ts` or `ModelName.types.ts`
- **Examples:** `user.types.ts`, `api.types.ts`, `auth.types.ts`

#### Utilities/Helpers
- **Format:** `helperName.ts` or `helperName.helper.ts`
- **Examples:** `formatDate.ts`, `validateEmail.ts`, `parseJSON.helper.ts`

#### Constants
- **Format:** `CONSTANT_NAME` in all caps with underscores
- **Location:** `src/constants/` or within the module
- **Examples:** `API_BASE_URL`, `MAX_RETRIES`, `DEFAULT_TIMEOUT`

#### Styles
- **Format:** `ComponentName.module.css` (CSS Modules)
- **Examples:** `Button.module.css`, `UserProfile.module.css`
- **Global Styles:** `src/styles/globals.css`, `src/styles/variables.css`

#### Tests
- **Format:** `ComponentName.test.ts` or `ComponentName.spec.ts`
- **Examples:** `Button.test.tsx`, `userService.test.ts`

### Folder Structure Naming

- **React Components:** `PascalCase` (e.g., `UserProfile/`, `FormInput/`)
- **Services/Utilities:** `camelCase` (e.g., `authService/`, `apiClient/`)
- **Feature folders:** `kebab-case` (e.g., `user-management/`, `auth-flow/`)
- **Configuration:** `lowercase` (e.g., `config/`, `scripts/`)

### Variable & Function Naming

- **Constants:** `UPPER_SNAKE_CASE`
- **Variables:** `camelCase`
- **Functions:** `camelCase` or `PascalCase` (for components)
- **Interfaces/Types:** `PascalCase`
- **Boolean variables:** Prefix with `is`, `has`, `should`, `can` (e.g., `isLoading`, `hasError`)

---

## Import Path Guide

### Absolute Imports

Configure TypeScript `tsconfig.json` for clean imports:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@services/*": ["src/services/*"],
      "@hooks/*": ["src/hooks/*"],
      "@types/*": ["src/types/*"],
      "@utils/*": ["src/utils/*"],
      "@constants/*": ["src/constants/*"],
      "@styles/*": ["src/styles/*"],
      "@assets/*": ["src/assets/*"]
    }
  }
}
```

### Common Import Patterns

#### Importing Components
```typescript
// ✓ Good - Absolute import
import { Button } from '@components/common/Button/Button';

// ✗ Avoid - Relative import
import { Button } from '../../../components/common/Button/Button';
```

#### Importing Hooks
```typescript
import { useAuth } from '@hooks/useAuth';
import { useFetch } from '@hooks/useFetch';
```

#### Importing Services
```typescript
import { userService } from '@services/api/userService';
import { authService } from '@services/auth/authService';
```

#### Importing Types
```typescript
import type { User, UserProfile } from '@types/models/user.types';
import type { ApiResponse } from '@types/api/api.types';
```

#### Importing Utilities
```typescript
import { formatDate } from '@utils/helpers/formatDate';
import { validateEmail } from '@utils/validators/validateEmail';
```

#### Importing Constants
```typescript
import { API_BASE_URL, MAX_RETRIES } from '@constants/api';
```

#### Importing Styles
```typescript
import styles from './Button.module.css';
import '@styles/globals.css';
```

---

## Module Navigation

### Authentication Module

**Location:** `src/services/auth/`, `src/hooks/`

**Key Files:**
- `src/services/auth/authService.ts` - Core authentication logic
- `src/hooks/useAuth.ts` - Authentication hook
- `src/types/models/auth.types.ts` - Auth-related types
- `src/context/AuthContext.tsx` - Auth context provider

**Import Example:**
```typescript
import { useAuth } from '@hooks/useAuth';
import { authService } from '@services/auth/authService';
```

### API Communication Module

**Location:** `src/services/api/`, `src/types/api/`

**Key Files:**
- `src/services/api/apiClient.ts` - HTTP client setup
- `src/services/api/userService.ts` - User API endpoints
- `src/services/api/productService.ts` - Product API endpoints
- `src/types/api/api.types.ts` - API response types

**Import Example:**
```typescript
import { userService } from '@services/api/userService';
import type { User, ApiResponse } from '@types/api/api.types';
```

### Component Library Module

**Location:** `src/components/`

**Key Directories:**
- `src/components/common/` - Shared components (Button, Input, etc.)
- `src/components/forms/` - Form-specific components
- `src/components/layouts/` - Layout components

**Import Example:**
```typescript
import { Button } from '@components/common/Button/Button';
import { FormInput } from '@components/forms/FormInput/FormInput';
import { MainLayout } from '@components/layouts/MainLayout';
```

### Page Module

**Location:** `src/pages/`

**Typical Files:**
- `src/pages/Home.tsx` - Home page
- `src/pages/Dashboard.tsx` - Dashboard page
- `src/pages/UserProfile.tsx` - User profile page

**Import Example:**
```typescript
import { Home } from '@pages/Home';
import { Dashboard } from '@pages/Dashboard';
```

### Utilities Module

**Location:** `src/utils/`

**Subdirectories:**
- `helpers/` - Helper functions
- `validators/` - Validation logic
- `formatters/` - Data formatting

**Import Example:**
```typescript
import { formatDate } from '@utils/helpers/formatDate';
import { validateEmail } from '@utils/validators/validateEmail';
```

### Custom Hooks Module

**Location:** `src/hooks/`

**Common Hooks:**
- `useAuth.ts` - Authentication
- `useFetch.ts` - Data fetching
- `useLocalStorage.ts` - Local storage
- `useDebounce.ts` - Debouncing

**Import Example:**
```typescript
import { useAuth } from '@hooks/useAuth';
import { useFetch } from '@hooks/useFetch';
```

---

## Configuration Files

### TypeScript Configuration (`tsconfig.json`)

Controls TypeScript compilation and type checking across the project.

**Key Options:**
- `target` - JavaScript version target
- `lib` - Library definitions to include
- `jsx` - JSX compilation mode
- `strict` - Enable strict type checking
- `esModuleInterop` - CommonJS/ES Module compatibility
- `paths` - Path aliases for imports

### ESLint Configuration (`.eslintrc.json`)

Enforces code quality and consistency.

**Typical Rules:**
- React best practices
- TypeScript rules
- Naming conventions
- Import organization
- Code style rules

### Prettier Configuration (`.prettierrc`)

Ensures consistent code formatting.

**Common Settings:**
- `printWidth` - Line length limit
- `tabWidth` - Indentation width
- `semi` - Semicolon usage
- `singleQuote` - Quote style
- `trailingComma` - Trailing comma usage

### Package.json

**Key Sections:**
```json
{
  "name": "magekt",
  "version": "1.0.0",
  "dependencies": { /* npm packages */ },
  "devDependencies": { /* dev tools */ },
  "scripts": {
    "dev": "development server",
    "build": "production build",
    "test": "run tests",
    "lint": "lint code",
    "format": "format code"
  }
}
```

### Environment Variables (`.env.example`)

Template for environment configuration:

```
REACT_APP_API_BASE_URL=https://api.example.com
REACT_APP_API_KEY=your_api_key_here
REACT_APP_ENV=development
```

---

## Quick Reference

### Common File Paths

| Need | Path | File |
|---|---|---|
| Add a new component | `src/components/[category]/ComponentName/` | `ComponentName.tsx`, `ComponentName.module.css` |
| Add a custom hook | `src/hooks/` | `useHookName.ts` |
| Add API service | `src/services/api/` | `serviceName.ts` |
| Add type definition | `src/types/` | `category.types.ts` |
| Add utility function | `src/utils/[subcategory]/` | `functionName.ts` |
| Add a page | `src/pages/` | `PageName.tsx` |
| Add tests | `tests/[category]/` | `*.test.ts` or `*.spec.ts` |
| Add global styles | `src/styles/` | Custom CSS files |

### Common Commands

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run tests
npm test

# Run specific test file
npm test -- ComponentName.test.tsx

# Lint code
npm run lint

# Format code
npm run format

# Type check
npm run type-check
```

### File Extension Guide

| Extension | Purpose | Example |
|---|---|---|
| `.tsx` | React component (TypeScript) | `Button.tsx` |
| `.ts` | TypeScript file | `userService.ts` |
| `.css` | CSS stylesheet | `Button.module.css` |
| `.json` | Configuration/Data | `tsconfig.json`, `package.json` |
| `.md` | Markdown documentation | `README.md` |

### Import Checklist

- [ ] Use absolute imports with `@/` prefix
- [ ] Group imports: React/libraries → internal modules → types
- [ ] Use `import type` for TypeScript types
- [ ] Keep imports organized and alphabetized
- [ ] Remove unused imports

---

## Best Practices

### Component Organization

1. **Single Responsibility:** Each component should have one clear purpose
2. **Composition:** Build complex UIs from simpler components
3. **Props Interface:** Define clear prop types with TypeScript
4. **Styling:** Use CSS Modules for component styles
5. **Testing:** Include unit tests for critical components

### Service Layer

1. **API Abstraction:** Keep API calls in service files
2. **Error Handling:** Implement consistent error handling
3. **Type Safety:** Use TypeScript interfaces for API responses
4. **Reusability:** Create services for common operations

### Code Quality

1. **Linting:** Run ESLint before committing
2. **Formatting:** Use Prettier for consistent style
3. **Type Checking:** Ensure all TypeScript checks pass
4. **Testing:** Write tests for new features
5. **Documentation:** Comment complex logic

---

## Troubleshooting

### Import Resolution Issues

**Problem:** `Cannot find module '@components/...'`  
**Solution:** Verify `tsconfig.json` paths are correct and match aliases used

### Component Not Found

**Problem:** Component imports fail  
**Solution:** Check file naming (PascalCase for components), verify file exists

### Type Errors

**Problem:** TypeScript compilation errors  
**Solution:** Check `src/types/` for correct type definitions, import with `import type`

### Test Failures

**Problem:** Tests not running or failing  
**Solution:** Check `jest.config.js` configuration, verify test file naming pattern

---

## Related Documentation

- [README.md](./README.md) - Project overview
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribution guidelines
- [docs/architecture/](./docs/architecture/) - System architecture
- [docs/guides/](./docs/guides/) - Developer guides

---

**Last Updated:** 2025-12-26  
**Maintained By:** magekt team