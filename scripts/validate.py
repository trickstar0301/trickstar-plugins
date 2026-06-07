#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require_path(path: Path, description: str) -> None:
    if not path.exists():
        raise SystemExit(f"Missing {description}: {path.relative_to(ROOT)}")


def require_mapping(value: object, description: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise SystemExit(f"{description} must be a JSON object")
    return value


def require_list(value: object, description: str) -> list[object]:
    if not isinstance(value, list):
        raise SystemExit(f"{description} must be a JSON array")
    return value


def require_string(value: object, description: str) -> str:
    if not isinstance(value, str) or not value:
        raise SystemExit(f"{description} must be a non-empty string")
    return value


def require_repo_path(path: Path, description: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        raise SystemExit(f"{description} must stay inside the repository: {path}") from None
    require_path(resolved, description)
    return resolved


def require_author(manifest: dict[str, object], description: str) -> None:
    author = require_mapping(manifest.get("author"), f"{description} author")
    require_string(author.get("name"), f"{description} author.name")


def require_keywords(manifest: dict[str, object], description: str) -> None:
    keywords = require_list(manifest.get("keywords"), f"{description} keywords")
    for keyword in keywords:
        require_string(keyword, f"{description} keyword")


def validate_claude_marketplace() -> None:
    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = require_mapping(load_json(marketplace_path), "Claude marketplace")

    plugins = require_list(marketplace.get("plugins"), "Claude marketplace plugins")

    for plugin in plugins:
        plugin = require_mapping(plugin, "Claude marketplace plugin")
        name = require_string(plugin.get("name"), "Claude marketplace plugin name")
        require_string(plugin.get("description"), f"Claude marketplace plugin {name} description")
        require_string(plugin.get("version"), f"Claude marketplace plugin {name} version")
        require_string(plugin.get("repository"), f"Claude marketplace plugin {name} repository")
        require_string(plugin.get("license"), f"Claude marketplace plugin {name} license")
        require_string(plugin.get("category"), f"Claude marketplace plugin {name} category")
        require_keywords(plugin, f"Claude marketplace plugin {name}")
        source = require_string(plugin.get("source"), f"Claude plugin {name} source")

        plugin_dir = require_repo_path(ROOT / source, f"Claude plugin source for {name}")

        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        require_path(manifest_path, f"Claude plugin manifest for {name}")
        manifest = require_mapping(load_json(manifest_path), f"Claude plugin manifest for {name}")
        require_string(manifest.get("name"), f"Claude plugin {name} name")
        require_string(manifest.get("displayName"), f"Claude plugin {name} displayName")
        require_string(manifest.get("description"), f"Claude plugin {name} description")
        require_string(manifest.get("version"), f"Claude plugin {name} version")
        require_author(manifest, f"Claude plugin {name}")
        require_string(manifest.get("repository"), f"Claude plugin {name} repository")
        require_string(manifest.get("license"), f"Claude plugin {name} license")
        require_keywords(manifest, f"Claude plugin {name}")

        lsp_servers = manifest.get("lspServers")
        lsp_path = plugin_dir / require_string(lsp_servers, f"Claude plugin {name} lspServers")
        require_repo_path(lsp_path, f"Claude lspServers for {name}")
        require_mapping(load_json(lsp_path), f"Claude lspServers for {name}")


def validate_codex_marketplace() -> None:
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    marketplace = require_mapping(load_json(marketplace_path), "Codex marketplace")

    plugins = require_list(marketplace.get("plugins"), "Codex marketplace plugins")

    for plugin in plugins:
        plugin = require_mapping(plugin, "Codex marketplace plugin")
        name = require_string(plugin.get("name"), "Codex marketplace plugin name")
        require_string(plugin.get("category"), f"Codex marketplace plugin {name} category")
        source = plugin.get("source")
        if not isinstance(source, dict):
            raise SystemExit(f"Codex plugin {name} must use an object source")

        require_string(source.get("source"), f"Codex plugin {name} source.source")
        path = require_string(source.get("path"), f"Codex plugin {name} source.path")

        plugin_dir = require_repo_path(ROOT / path, f"Codex plugin source for {name}")

        manifest_path = plugin_dir / ".codex-plugin" / "plugin.json"
        require_path(manifest_path, f"Codex plugin manifest for {name}")
        manifest = require_mapping(load_json(manifest_path), f"Codex plugin manifest for {name}")
        require_string(manifest.get("name"), f"Codex plugin {name} name")
        require_string(manifest.get("version"), f"Codex plugin {name} version")
        require_string(manifest.get("description"), f"Codex plugin {name} description")
        require_author(manifest, f"Codex plugin {name}")
        require_string(manifest.get("repository"), f"Codex plugin {name} repository")
        require_string(manifest.get("license"), f"Codex plugin {name} license")
        require_keywords(manifest, f"Codex plugin {name}")

        interface = require_mapping(manifest.get("interface"), f"Codex plugin {name} interface")
        require_string(interface.get("displayName"), f"Codex plugin {name} interface.displayName")
        require_string(interface.get("shortDescription"), f"Codex plugin {name} interface.shortDescription")
        require_string(interface.get("longDescription"), f"Codex plugin {name} interface.longDescription")
        require_string(interface.get("developerName"), f"Codex plugin {name} interface.developerName")
        require_string(interface.get("category"), f"Codex plugin {name} interface.category")
        require_list(interface.get("capabilities"), f"Codex plugin {name} interface.capabilities")
        require_string(interface.get("defaultPrompt"), f"Codex plugin {name} interface.defaultPrompt")

        skills_dir = plugin_dir / require_string(manifest.get("skills"), f"Codex plugin {name} skills")
        require_repo_path(skills_dir, f"Codex skills directory for {name}")
        if not any(skills_dir.glob("*/SKILL.md")):
            raise SystemExit(f"Codex plugin {name} must include at least one skill")


def main() -> None:
    validate_claude_marketplace()
    validate_codex_marketplace()


if __name__ == "__main__":
    main()
