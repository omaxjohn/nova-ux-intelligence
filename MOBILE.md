# Phone, iPad and remote use

Nova UX Intelligence has no MCP server, external authentication or desktop-only product restriction. Its skill instructions can run in Chat or Work on iPhone and iPad after the plugin is available to the signed-in ChatGPT account.

## Use in mobile Chat or Work

1. Open Plugins in the latest ChatGPT app.
2. Install `nOva UX Intelligence` after it becomes available to the account through the public plugin directory.
3. Start a new Chat or Work conversation.
4. Select the plugin or invoke `@nOva UX Intelligence`, then attach a screenshot or describe the interface.

A GitHub repository or local personal-marketplace installation does not publish a plugin to a mobile account. Public availability requires OpenAI review and publication. The prepared submission materials are in [`submission/`](submission/).

## Use Codex remotely from iPhone or iPad

1. Keep the latest ChatGPT desktop app running on the Mac, signed in to the same account and workspace as the mobile app.
2. On the Mac, enable remote connections in ChatGPT settings and keep the host awake and online.
3. Open **Remote** in the latest ChatGPT mobile app and pair the device.
4. Open or continue a Codex task on the connected host. The remote session uses that host's projects, files, credentials, permissions, plugins and local tools.
5. Start a new task after a plugin install or update so the refreshed skill catalog is loaded.

Remote feature availability can vary by rollout and workspace controls. If Remote is absent, update both apps and check that both devices use the same account and workspace.

## Product verification contract

When Nova reviews or implements an interface intended for phones or tablets, it selects applicable checks from:

- portrait and landscape;
- iPad full screen and constrained split view;
- safe areas and browser/system chrome;
- touch target size and spacing;
- controls that do not depend on hover;
- virtual and attached keyboards, focus and occlusion;
- zoom and text scaling;
- slow network, interruption and resume;
- representative content extremes, localization and RTL.

These are risk-based checks. Nova reports which environments were executed, planned or blocked rather than claiming blanket device coverage.

Official references: [Plugins](https://learn.chatgpt.com/docs/plugins), [Remote connections](https://learn.chatgpt.com/docs/remote-connections), and [plugin submission](https://developers.openai.com/plugins/deploy/submission).
