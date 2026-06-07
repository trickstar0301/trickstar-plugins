# Trickstar Plugins

Plugin marketplace for tools maintained by `trickstar0301`.

This repository is intentionally not specific to one tool. Each plugin lives
under `plugins/<plugin-name>`, and the marketplace catalog lists the plugins
that Claude Code and GitHub Copilot CLI can install.

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

## capnp-ls

The `capnp-ls` plugin starts the `capnp-ls` language server from `PATH`. Install
the binary before enabling the plugin:

```bash
curl -fsSL https://raw.githubusercontent.com/trickstar0301/capnp-ls/main/install.sh | sh
```

The plugin does not bundle the language server binary.

## Repository Layout

```text
.claude-plugin/marketplace.json
plugins/
  capnp-ls/
    .claude-plugin/plugin.json
    .lsp.json
```

