# Regression protocol

This directory is maintainer-only. Normal skill use does not load it. The immutable source is [frozen-kernel.md](source/frozen-kernel.md); its SHA-256 and change policy are in [kernel-contract.json](kernel-contract.json). [traceability.json](traceability.json) maps frozen invariants to runtime locations. Historic PASS claims in source are conversation data, not executed test results.

## Run the gates

1. Run `python3 tests/check_structure.py` from the skill root. It checks packaging, routing links, substantial exact duplication, entrypoint budget, generic scope, source hash and case coverage. This is structural evidence only.
2. Run the skill-creator `quick_validate.py` against the skill root when that tool is available. It validates skill packaging, not design behavior.
3. Give a fresh evaluator only `tests/prompts.json` and the candidate skill path. Ask for actual user-facing decisions and modules loaded per case, saved as `{id,response,modules_loaded}`. Give the unguided control only prompts. Do not reveal criteria, historical responses or scores to either responder. Use the same model/settings; record actual configuration or say inherited/unreported.
4. A separate evaluator reads `tests/cases.json` and anonymous responses. Score every criterion semantically, with response quotes or missing-behavior evidence. Exact phrasing is not required. A case passes only when all its criteria pass. A proposed verification plan must never be scored as executed runtime evidence. Keep raw responses, judgments, and reviewer adjudications.
5. Run positive/negative discovery examples using the description alone. This tests semantic trigger quality, not actual host selection. Check local advice, full architecture, and unrelated-task boundaries.
6. For a new failure, capture it before editing. Make the smallest correction; run the same failing case plus full regression after refactoring. Version any kernel semantic migration; dynamic knowledge updates must retain the frozen invariants. Failed checks cannot be waived by changing the rubric to fit the answer.

For wording experiments, use one fresh context per sample, a no-guidance control and at least five repetitions per compared variant when the control demonstrates the targeted behavior-shaping failure. Inspect every flagged match and variance manually. If a control does not fail, do not invent a guidance improvement. Batch scenario runs are cheaper smoke tests but are correlated; use fresh per-case runs for stronger release assurance.

## Coverage and provenance

T1–T8 come from the source pressure-test plan: unusable landing, visible-only accessibility, mobile product decisions, booking forms, Arabic RTL, enterprise dashboard, existing design system and generic AI UI. T9 is the later Liquid Glass trap; T10–T13 are conversion conflict, extreme states, design/code drift and preference conflict. A1–A8 preserve the source adversarial intents: instruction literalism, authority transfer, fake evidence, conflicting research, brand/accessibility conflict, RTL trap, numeric-rule attack and unspecified beauty.

Prompts are engineering adaptations, not verbatim source quotations. The original project-specific tour example is generalized; source project rules are not runtime skill defaults. R1–R5 add explicit evidence theater, prioritization, poisoned artifact, fast routing and high uncertainty coverage. The failure-mode arrays preserve FM-01 through FM-18 from the frozen register. Test rubrics describe observable decisions, not required word matches.

## Limits and release record

A model-response suite validates sampled reasoning behavior; it does not establish product usability, accessibility conformance, real-browser execution or universal reliability. Record those separately if a future campaign supplies an actual implementation. Preserve negative results, baseline successes and judge disagreements. Do not describe the skill as statistically proven or bulletproof from a finite campaign.

Required release record: date; candidate hash; source identity; model/settings availability; raw response/score paths; control and guided case/criterion totals; refactor reason; final retest; structural/trigger/token checks; known limits. No kernel reduction without a new failing test and evidence-backed migration rationale.
