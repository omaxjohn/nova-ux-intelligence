# Nova UX Intelligence

Evidence-led design judgment, from premise to runtime.

Nova UX Intelligence is a modular Codex skill for designing, critiquing, redesigning and verifying digital interfaces and user flows. It applies a frozen reasoning kernel before visual treatment: understand the task, challenge the premise, classify evidence, preserve validated decisions, resolve conflicts and verify the delivered experience.

It is not a style generator or a project-specific design system. Liquid Glass is available as a preferred selectable direction and is evaluated for hierarchy, readability, accessibility and performance rather than applied by default.

## Install

Copy the repository folder into the Codex user skill directory:

```sh
mkdir -p "$HOME/.codex/skills"
cp -R nova-ux-intelligence "$HOME/.codex/skills/nova-ux-intelligence"
```

Start a new Codex task after installation. Invoke it explicitly with `$nova-ux-intelligence`, or let Codex select it for relevant UI/UX work.

## Example

```text
Use $nova-ux-intelligence to critique this checkout flow, preserve what works,
prioritize the smallest justified changes, and distinguish planned checks from
runtime verification.
```

## Architecture

```text
SKILL.md                 Compact reasoning kernel and router
operations/              Diagnose, design and verify workflows
references/              Routed domain, evidence and material knowledge
tests/                   Frozen contract and behavioral regression suite
agents/openai.yaml       Codex display metadata and invocation policy
```

`SKILL.md` contains how to think. References contain knowledge loaded only when relevant. Existing design systems contain prior decisions. Runtime behavior represents what users actually experience.

The kernel covers challenge, evidence, conflict, preservation, uncertainty, reasoning depth, quality trade-offs and runtime verification. Knowledge that changes over time—standards, platform guidance, frameworks and material techniques—remains outside the frozen semantics and should be refreshed from primary sources.

## Validate

Run the self-contained package checks:

```sh
python3 tests/check_structure.py
```

The checker validates identity, file routing, frozen-source integrity, regression coverage and GitHub package structure. Read [tests/protocol.md](tests/protocol.md) before changing reasoning behavior or test criteria.

The regression suite contains T1–T13, adversarial A1–A8 and five additional cases. Together they cover FM-01 through FM-18. Passing model scenarios is sampled reasoning evidence; it is not product usability research, accessibility certification or browser verification.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Changes to dynamic references and changes to the frozen kernel follow different review paths. A kernel change requires a newly observed failure, evidence, an explicit migration rationale and a complete regression rerun.

## License

[MIT](LICENSE)
