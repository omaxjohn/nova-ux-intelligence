# Adaptive experience and localization

Adapt to device, input, viewport, zoom/font scale, orientation, network and content, not just named breakpoints. Preserve task completion and information hierarchy; touch, keyboard and pointer can coexist. Inspect sticky elements against content, focused fields and virtual keyboards.

RTL requires semantic mirroring, not blind mirroring. Decide layout/navigation direction, icon semantics, reading and focus order, numbers, dates, currency, phone identifiers, mixed Arabic/Latin text, image meaning, alignment and directional motion. Do not reverse digit strings or all media icons. Use locale-aware formatting, suitable fonts and logical layout properties; allow expansion and wrapping. Verify with realistic mixed content in runtime.

The [W3C HTML direction guidance](https://www.w3.org/International/questions/qa-html-dir) explains structural direction and bidirectional markup (checked 2026-09-08). For HTML, set appropriate language and direction and isolate mixed-direction runs as needed. Platform-specific layout and icon conventions require their own applicable guidance; web recommendations do not automatically define native behavior.
