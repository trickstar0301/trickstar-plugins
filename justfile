validate:
    python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
    python3 -m json.tool plugins/capnp-ls/.claude-plugin/plugin.json >/dev/null
    python3 -m json.tool plugins/capnp-ls/.lsp.json >/dev/null

