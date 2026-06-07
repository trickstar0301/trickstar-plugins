---
name: capnp-ls
description: Use when the user asks about installing, configuring, or troubleshooting capnp-ls, including .capnp-ls.json import paths, capnp-v1/capnp-v2 release channels, and Claude/VS Code plugin setup.
---

# capnp-ls

Use this skill to help with `capnp-ls`, the Cap'n Proto language server.

## Binary Installation

Install the language server binary before configuring editor or agent plugins:

```bash
curl -fsSL https://raw.githubusercontent.com/trickstar0301/capnp-ls/main/install.sh | sh
```

The default compatibility channel is `capnp-v1`. Use `CAPNP_LS_CAPNP_VERSION=v2`
for the Cap'n Proto v2 channel:

```bash
CAPNP_LS_CAPNP_VERSION=v2 \
curl -fsSL https://raw.githubusercontent.com/trickstar0301/capnp-ls/main/install.sh | sh
```

## Project Configuration

Project-specific import paths belong in `.capnp-ls.json` at the workspace root:

```json
{
  "importPaths": [
    "schemas/common",
    "vendor/capnp"
  ]
}
```

Do not put project import paths in VS Code settings or plugin manifests.

## Plugin Behavior

Claude Code uses the plugin's `.lsp.json` to start `capnp-ls --stdio` from
`PATH`. This Codex plugin provides guidance only; it does not bundle, install,
or launch the language server automatically.
