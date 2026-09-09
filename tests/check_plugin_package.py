import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
BUNDLED = ROOT / "skills" / "nova-ux-intelligence"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


require(MANIFEST.exists(), "missing .codex-plugin/plugin.json")
manifest = json.loads(MANIFEST.read_text())
require(manifest["name"] == "nova-ux-intelligence", "plugin name must be canonical")
require(manifest["version"] == "1.0.0", "plugin version must be 1.0.0")
require(manifest["skills"] == "./skills/", "manifest must expose bundled skills")
require(manifest["interface"]["displayName"] == "Nova UX Intelligence", "display name mismatch")
require(manifest["interface"]["category"] == "Productivity", "category mismatch")
require(len(manifest["interface"].get("defaultPrompt", [])) >= 2, "default prompts required")

require(MARKETPLACE.exists(), "missing repo marketplace")
marketplace = json.loads(MARKETPLACE.read_text())
entry = next(p for p in marketplace["plugins"] if p["name"] == "nova-ux-intelligence")
require(entry["source"]["source"] == "git-subdir", "marketplace must be Git-backed")
require(entry["source"]["url"] == "https://github.com/omaxjohn/nova-ux-intelligence.git", "marketplace repo mismatch")
require(entry["source"]["path"] == "./", "plugin lives at repository root")
require(entry["policy"]["installation"] == "AVAILABLE", "plugin must be installable")

required = [
    "SKILL.md",
    "operations/design.md",
    "operations/diagnose.md",
    "operations/verify.md",
    "references/adaptive.md",
    "references/domains.md",
    "references/evidence.md",
    "references/interaction.md",
    "references/materials.md",
    "references/quality.md",
]
for rel in required:
    canonical = ROOT / rel
    bundled = BUNDLED / rel
    require(bundled.exists(), f"missing bundled skill resource: {rel}")
    require(bundled.read_bytes() == canonical.read_bytes(), f"bundled resource drift: {rel}")

print("PASS: ChatGPT plugin package contract")
