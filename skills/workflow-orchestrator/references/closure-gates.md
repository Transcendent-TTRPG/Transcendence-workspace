# Workflow Closure Gates

Every orchestrated run should leave explicit closure state.

## Ownership checks

- owner workflow explicit
- linked workflows explicit
- owning artifact skill explicit when relevant

## Checkpoint checks

- early-phase outputs captured before substantial edits
- blockers recorded instead of bypassed
- routing decisions recorded when boundaries are crossed

## Closure checks

- acceptance status explicit
- unresolved items explicit
- downstream follow-up explicit when required
- change impact explicit

## Failure patterns to avoid

- file edits before workflow ownership is chosen
- several workflows treated as co-owners with no closure authority
- "done enough" closure with no acceptance review
- artifact-skill usage with no work-card or checkpoint discipline
