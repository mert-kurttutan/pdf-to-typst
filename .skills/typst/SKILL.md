# Typst Authoring Skill

## Purpose
Use this skill whenever creating or editing Typst documents in this repository.

## Primary Reference
Use local Typst documentation from:
- `/workspaces/pdf-to-typst/typst-docs`

Treat `typst-docs` as the canonical reference for syntax and examples during Typst generation.

## Typst Generation Workflow
1. Read the source content to convert (e.g., Markdown).
2. Map structure to Typst equivalents:
- headings (`=`, `==`, `===`)
- emphasis (`*text*`)
- math (`$ ... $`)
- matrices (`mat(...)`)
3. Prefer Typst-valid math identifiers:
- separate multiplied symbols (`A B`, `H v`)
- use quoted operator labels when needed (`"det"(A)`, `"sgn"(s)`, `"prod"_(...)`)
4. Validate by compiling:

```bash
typst compile <file>.typ
```

5. Fix compile errors and re-run until clean.

## Output Expectations
- Produce valid Typst that compiles.
- Preserve source meaning and section structure.
- Keep equations semantically equivalent to the source.
