# Interaction and forms

Use native semantics and supported components where they meet the task. Make action outcome, loading and completion understandable; account for cancellation, back navigation and undo where appropriate. Recognition aids should reduce actual memory burden rather than decorate the interface.

Collect information only when necessary for the current step. Accept reasonable phone/date/name variations and normalize without silently changing meaning. Constrain impossible choices rather than requiring users to recover from preventable errors. Explain format requirements before submission; use associated text errors, preserve input and move focus deliberately after errors. Avoid using color alone.

For consequential transactions, provide status reconciliation and a safe retry path, including session expiry and network uncertainty. Prevent duplicate operations in the underlying system as well as the interface. Do not fabricate availability or prices to make an incomplete state look finished.

The [W3C Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/) covers labels, grouping, instructions, validation and feedback (checked 2026-09-08). It is practical guidance; verify applicable normative requirements separately. Use task evidence to choose a single screen, progressive disclosure or multiple steps instead of treating a form pattern as universal.
