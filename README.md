# Trickstar Plugins

Plugin marketplace for tools maintained by `trickstar0301`.

This repository is intentionally not specific to one tool. Agent-specific plugin
packages live under `plugins/<agent>/<plugin-name>`, and the marketplace
catalogs list the plugins that Claude Code, GitHub Copilot CLI, and Codex can
install.

## Install the Marketplace

Claude Code:

```bash
claude plugin marketplace add trickstar0301/trickstar-plugins
claude plugin install capnp-ls@trickstar-plugins
```

GitHub Copilot CLI:

```bash
copilot plugin marketplace add trickstar0301/trickstar-plugins
copilot plugin install capnp-ls@trickstar-plugins
```

Codex:

```bash
codex plugin marketplace add trickstar0301/trickstar-plugins
codex plugin install capnp-ls@trickstar-plugins
```

## capnp-ls

The Claude plugin starts the `capnp-ls` language server from `PATH`. The Codex
plugin provides installation and configuration guidance. Install the binary
before enabling editor or agent integrations:

```bash
curl -fsSL https://raw.githubusercontent.com/trickstar0301/capnp-ls/main/install.sh | sh
```

The plugin does not bundle the language server binary.

## Repository Layout

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/
  claude/
    capnp-ls/
      .claude-plugin/plugin.json
      .lsp.json
  codex/
    capnp-ls/
      .codex-plugin/plugin.json
      skills/capnp-ls/SKILL.md
```
