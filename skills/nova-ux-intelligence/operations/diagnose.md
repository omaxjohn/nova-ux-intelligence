# Diagnose operations

Read for ANALYZE (understand a task/system), CRITIQUE (judge an artifact), AUDIT (systematically assess requested scope).

Inspect the supplied artifact and relevant implementation before conclusions. Record artifact type/version and coverage. A screenshot supports visible observations; a design file supports intended relationships; code supports implementation; rendered interaction supports experienced behavior. Business truth (goals/data), UX truth (task evidence), design-system truth (decisions) and runtime truth (behavior) answer different questions.

Use an issue record: observation/location → task consequence → evidence/status → problem type → severity/confidence → smallest response → verification needed. Missing artifacts mean missing observations, not permission to invent critique. Use [quality](../references/quality.md) to prioritize.

For conflicting sources, use the required response contract in [evidence](../references/evidence.md).

For AUDIT, cover the requested scope and retain a complete findings artifact when needed; present a bounded implementation queue. CRITIQUE may conclude KEEP or no redesign. ANALYZE may conclude that information architecture or content, rather than styling, causes the issue.

Default handoff groups: Fix Now (critical blockers), Fix Next (material improvements), Polish Later (craft). Explain dependencies rather than inventing numerical priority scores. Do not drop a critical issue to satisfy a cosmetic change budget. Route implementation to [design](design.md) only when authorized and runtime assessment to [verify](verify.md).
