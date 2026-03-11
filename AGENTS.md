# AGENTS.md - ai-scaffolding

## Overview

<!-- Descreva o proposito do seu projeto aqui -->

## Setup

```bash
npm install
```


## Commands

```bash
# Test
npx vitest run

# Lint
npx eslint .
npx prettier --check .

# Type check
npx tsc --noEmit
```


## Development Rules

### TDD Enforcement

All changes MUST follow the RED-GREEN-REFACTOR cycle:

1. **RED**: Write a failing test first. Run tests to confirm failure.
2. **GREEN**: Write the minimum code to make the test pass.
3. **REFACTOR**: Clean up while keeping all tests green.

NEVER write production code without a failing test.
NEVER modify tests to make bad code pass.

### Minimal Changes

- Only change what was requested.
- No gold plating or speculative features.
- No opportunistic refactoring of unrelated code.

### Architecture Boundaries

- Separation of concerns: each module has one responsibility.
- No God Objects or circular dependencies.
- External I/O (filesystem, network, APIs) in dedicated modules only.

### Best Practices

- Follow ESLint and Prettier conventions.
- Use specific error types, never empty catch.
- Prefer node builtins over external dependencies.
- Use vitest with describe/it/expect pattern.

