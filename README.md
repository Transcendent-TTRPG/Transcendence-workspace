# Transcendence Workspace

This workspace contains the main repositories for the Transcendence ecosystem.

## Purpose

The project is divided into separate repositories to keep concerns clean while preserving a shared creative and production workflow.

This workspace exists to unify:

- design and canon
- Foundry VTT implementation
- editorial and narrative publications

It is the recommended root folder for working with AI coding/writing assistants that benefit from visibility across multiple repositories.

## Repositories

### `transcendence-design`
Source of truth for:

- worldbuilding
- lore
- species
- cultures
- mechanics
- frameworks
- design QA
- canon decisions

### `transcendence-foundry`
Technical implementation for Foundry VTT:

- system code
- data models
- sheets
- item/actor definitions
- automation
- tests
- packaging

### `transcendence-publications`
Editorial output and publication pipeline:

- core book manuscript
- light novels
- supplements
- export-ready publication assets

## Shared AI Context

The folder `shared-ai-context/` contains compact cross-project context intended for AI tools and contributors.

These files should remain short, curated, and updated regularly.

Recommended files:

- `canon-summary.md`
- `terminology.md`
- `design-principles.md`
- `project-status.md`
- `current-priorities.md`

## Recommended Workflow

1. Define or update canon/system truth in `transcendence-design`
2. Implement playable behavior in `transcendence-foundry`
3. Produce readable/public material in `transcendence-publications`
4. Sync shared context when major decisions are made

## Dependency Direction

The intended dependency direction is:

`design -> foundry`
`design -> publications`

Foundry and publications may interpret or implement design, but should not silently redefine canon.

## AI Usage Notes

For tools like Claude Code or Codex:

- open this workspace as the main working directory when cross-repo visibility is needed
- keep repo-level instructions inside each repository
- use short context summaries rather than massive lore dumps
- update shared context after major structural decisions

## Status Model

This workspace supports three parallel lanes:

- **canon/design**
- **implementation**
- **publication**

Each lane can progress independently, but major canon changes should be decided in `transcendence-design` first.