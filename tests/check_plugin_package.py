import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
BUNDLED = ROOT / "skills" / "nova-ux-intelligence"
REVIEW_TESTS = ROOT / "submission" / "review-tests.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


require(MANIFEST.exists(), "missing .codex-plugin/plugin.json")
manifest = json.loads(MANIFEST.read_text())
require(manifest["name"] == "nova-ux-intelligence", "plugin name must be canonical")
require(manifest["version"] == "1.1.0", "plugin version must be 1.1.0")
require(manifest["skills"] == "./skills/", "manifest must expose bundled skills")
require(manifest["interface"]["displayName"] == "nOva UX Intelligence", "display name mismatch")
require(manifest["interface"]["category"] == "Design", "category mismatch")
require(len(manifest["interface"].get("defaultPrompt", [])) >= 2, "default prompts required")
prompts = " ".join(manifest["interface"]["defaultPrompt"])
require("Chat:" in prompts and "Code:" in prompts, "chat and code prompts required")
for key in ("composerIcon", "logo", "logoDark"):
    require((ROOT / manifest["interface"][key]).is_file(), f"missing plugin asset: {key}")

require(MARKETPLACE.exists(), "missing repo marketplace")
marketplace = json.loads(MARKETPLACE.read_text())
entry = next(p for p in marketplace["plugins"] if p["name"] == "nova-ux-intelligence")
require(entry["source"]["source"] == "git-subdir", "marketplace must be Git-backed")
require(entry["source"]["url"] == "https://github.com/omaxjohn/nova-ux-intelligence.git", "marketplace repo mismatch")
require(entry["source"]["path"] == "./", "plugin lives at repository root")
require(entry["policy"]["installation"] == "AVAILABLE", "plugin must be installable")
require("products" not in entry["policy"], "plugin must remain available across product surfaces")

for rel in ("MOBILE.md", "PRIVACY.md", "TERMS.md", "SUPPORT.md", "submission/listing.md", "submission/release-notes.md"):
    require((ROOT / rel).is_file(), f"missing cross-device publication resource: {rel}")
require(REVIEW_TESTS.is_file(), "missing submission/review-tests.json")
if REVIEW_TESTS.is_file():
    review_tests = json.loads(REVIEW_TESTS.read_text())
    require(len(review_tests.get("positive", [])) >= 5, "OpenAI submission needs at least 5 positive tests")
    require(len(review_tests.get("negative", [])) >= 3, "OpenAI submission needs at least 3 negative tests")

mobile_contract = (ROOT / "MOBILE.md").read_text() if (ROOT / "MOBILE.md").is_file() else ""
for marker in ("iPhone", "iPad", "Remote", "public plugin directory"):
    require(marker in mobile_contract, f"mobile contract missing: {marker}")

required = [
    "SKILL.md",
    "agents/openai.yaml",
    "assets/nova-small.svg",
    "assets/nova-large.svg",
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
