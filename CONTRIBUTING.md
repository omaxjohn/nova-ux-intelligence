# Contributing

Contributions are welcome when they improve observable design decisions without turning the skill into a generic UX encyclopedia.

## Before changing files

1. Read `SKILL.md` and `tests/protocol.md`.
2. Classify the proposal as a dynamic knowledge update, operation clarification, packaging change or frozen-kernel semantic change.
3. Search existing runtime modules before adding guidance; keep one source of truth and route it from `SKILL.md` when agents need it.

## Frozen-kernel changes

The Nova Reasoning Kernel v1.0 is frozen. Do not weaken or remove an invariant because wording feels long or a single example prefers another answer. A semantic change requires:

1. A reproducible failing scenario observed before the change.
2. Evidence showing why the existing invariant is insufficient or harmful.
3. An explicit versioned migration rationale.
4. The smallest instruction change addressing that failure.
5. The affected case and the complete regression suite rerun with independent response and grading contexts.

Dynamic standards, platform guidance, framework knowledge and implementation techniques can be updated without changing kernel semantics. Record the primary source, applicable scope and checked date.

## Quality gates

Run:

```sh
python3 tests/check_structure.py
```

When skill-creator is available locally, also run its `quick_validate.py` against the repository root. For behavior changes, follow `tests/protocol.md`; do not treat regex checks or an AI self-review as behavioral proof.

Keep `SKILL.md` compact, keep project-specific rules outside this repository, and do not claim runtime checks that were only planned. Pull requests should state the observed problem, resulting behavior, validation evidence and remaining limits.
