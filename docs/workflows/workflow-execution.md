# Workflow Execution

This document defines how workflows should be executed by agents so that they
do not become optional reference material that is easy to ignore.

The goal is to create a small execution discipline:
- choose the right workflow
- create a work card
- advance through checkpoints in order
- refuse ambiguous closure

## Purpose

Use this document when:
- starting a new task that should follow one of the project workflows
- deciding which workflow owns a task
- deciding whether a task needs multiple workflows
- ensuring closure criteria are actually enforced

## Core principle

Workflows do not execute themselves.

To become operational, every workflow needs:
1. a selected owning workflow
2. a work card
3. phase checkpoints
4. acceptance closure
5. change impact recording

If those pieces are absent, the workflow is only advisory.

## Execution model

The execution model is:

- `workflow` defines the required phase order
- `skill` defines how a repeated artifact task is performed
- `work card` stores the current run state
- `agent` performs the work and updates the card
- `acceptance closure` prevents silent “close enough” endings

## Step 1. Choose the owning workflow

Before editing files, identify the primary workflow.

Examples:
- new or revised Technique -> `technique-workflow`
- full Technique backfill (sim + corebook entry + technique card) -> `technique-workflow` with `simulation-port-workflow` linked
- sim-only backfill (no publication artifacts needed) -> `simulation-port-workflow`
- publication divergence -> `core-sync-workflow`
- taxonomy contradiction -> `authority-revision-workflow`
- broad retroactive cleanup -> `batch-refactor-workflow`

Important: use `simulation-port-workflow` as owner only when publication
artifacts (corebook entry, technique card) are explicitly out of scope. If the
run must also produce a corebook entry or technique card, `technique-workflow`
is the correct owner.

If the task seems to need more than one workflow:
- choose one owner
- record the others as linked workflows

The owner controls closure.

## Step 2. Create a work card

Before substantial work begins, create or fill a work card from the matching
template.

The work card must record:
- owner workflow
- linked workflows if any
- scope
- sources
- current phase
- outputs by phase
- blockers
- acceptance checklist
- change impact note

The work card is not a diary. It is the control surface for the run.

## Step 3. Advance by checkpoints, not intuition

Each workflow phase should produce a visible checkpoint.

Examples:
- intake complete
- dependency map recorded
- runtime gap classified
- runtime gate resolved
- publication scope mapped
- evidence inventory recorded

The agent should not skip from “I understand the problem” to “I edited files”
without recording the required intermediate checkpoint outputs.

## Step 4. Route when a workflow boundary is crossed

If a task begins under one workflow but discovers that another workflow really
owns the hard part:
- do not force the wrong workflow to absorb the problem
- record the dependency or blocker in the current card
- route the next task to the correct workflow

Examples:
- a Technique pass that discovers unstable doctrine -> route to `authority-revision`
- a sim port blocked by treatment logic -> route to `dependency-review` or `authority-revision`
- a local cleanup that grows into a migration -> route to `batch-refactor`

## Step 5. Use skills only after workflow ownership is clear

Skills should be invoked only after:
- the owning workflow is known
- the work card exists
- the phase currently being executed is clear

This prevents skills from becoming an alternate informal process.

## Step 6. Closure must be explicit

A task is not considered closed just because files were edited.

To close a run:
- acceptance checklist must be reviewed
- unresolved items must be explicit
- downstream routing must be explicit if needed
- change impact must be recorded

## Single-workflow runs

Many tasks should still be simple.

Examples:
- a local wording cleanup
- a small sim port using existing runtime
- a bounded core sync

These runs still need:
- owner workflow
- work card
- closure

They just use fewer linked workflows.

## Multi-workflow runs

Some work naturally crosses layers.

Example:
- revise Technique doctrine
- port it to sim
- sync core

In these cases:
- one owner workflow should still be chosen
- the others should be linked
- the work card should show the handoff points

## When to spawn subagents

Subagents are useful when:
- the task is long
- the lenses are separable
- the work can proceed in parallel without stepping on one write scope

They are not required for every workflow run.

If subagents are used:
- the main agent still owns the work card
- the main agent still owns closure

## Mandatory run artifacts

Every workflow execution should leave behind at least:
- a work card
- updated target artifacts
- acceptance status
- change impact note

If any of these are missing, the workflow execution was incomplete.

## Recommended directory usage

- workflow definitions:
  - `docs/workflows/`
- work card templates:
  - `docs/workcards/`
- actual filled work cards:
  - project may later choose a home such as `docs/work-runs/` or another tracked location

This document only standardizes the execution model and templates, not the final
archival location for filled runs.

## Good execution

Good workflow execution leaves behind:
- clear ownership
- explicit checkpoints
- explicit blockers
- explicit closure
- fewer forgotten downstream updates

## Bad execution

Bad workflow execution leaves behind:
- “we mostly followed the workflow”
- skipped phases with no recorded reason
- edited artifacts with no owning workflow
- closure with no acceptance review
