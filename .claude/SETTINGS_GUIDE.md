# settings.json Configuration Guide

This guide explains the phase-gated permissions in `.claude/settings.json` and when to enable additional features.

---

## Current Configuration (Phase 1-3)

### Core Permissions (Always Active)
- **File Operations**: Read, Write, Edit, Grep, Glob
- **Git Commands**: add, commit, push, pull, status, diff, log, checkout, reset, rm
- **Python Tooling**: uv, ruff, pyright, pytest
- **Modern CLI Tools**: rg, bat, fd, sd, jq, yq, xsv
- **Essential Bash**: rm, mv, mkdir, ls, diff
- **Documentation**: docs.python.org, docs.astral.sh, fastapi.tiangolo.com, docs.pydantic.dev, docs.anthropic.com, github.com
- **MCP Servers**: context7, sequential-thinking

---

## Phase 2 Additions (After Project 3)

When starting Project 2 (Docker Inspector) or Project 4 (Metrics API), add:

```json
"Bash(docker:*)",
"Bash(docker-compose:*)"
```

**Why**: Projects 2, 4, and 6 require Docker for containerization.

---

## Phase 2 Additions (After Project 4)

When starting Project 5 (IaC Provisioning), add cloud documentation access:

```json
"WebFetch(domain:docs.aws.amazon.com)",
"WebFetch(domain:boto3.amazonaws.com)",
"WebFetch(domain:learn.microsoft.com)",
"WebFetch(domain:docs.microsoft.com)"
```

**Why**: Projects 5-6 interact with AWS/Azure cloud services.

---

## Phase 3 Additions (After Project 6)

### Enable Tool Validator Hook

Add to the root object (after `enabledMcpjsonServers`):

```json
"hooks": {
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "uv run .claude/hooks/tool_validator.py",
          "timeout": 5
        }
      ]
    }
  ]
}
```

**Why**: Enforces modern CLI tools (rg, bat, fd, sd) and provides educational Python example.

**See**: `.claude/hooks/README.md` for activation details.

### Enable IDE Diagnostics

Add to permissions.allow:

```json
"mcp__ide__getDiagnostics",
"mcp__ide__executeCode"
```

**Why**: Projects 7-8 benefit from IDE integration for async debugging and diagnostics.

---

## Phase 4 Additions (After Project 8)

### Enable Workflow Orchestration Hook

Add to `hooks.UserPromptSubmit` (create if doesn't exist):

```json
"UserPromptSubmit": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "uv run .claude/hooks/task_hard_prep_hook.py"
      }
    ]
  }
]
```

**Why**: Automates directory setup for complex workflow orchestration (/task_hard command).

### Additional Permissions

See `archive/phase4/settings.json` for the full Phase 4 configuration with 63+ permissions.

**Only restore if**: Working on large, complex codebases requiring advanced automation.

---

## How to Edit settings.json

1. **Open**: `.claude/settings.json`
2. **Add permissions**: Insert into the `permissions.allow` array
3. **Add hooks**: Insert `hooks` object at root level (same level as `permissions`)
4. **Save**: Changes take effect immediately
5. **Update CLAUDE.md**: Mark new features as ACTIVE in "Current Setup"

### Example: Adding Docker Support

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      ...existing permissions...,
      "Bash(docker:*)",          // ADD THIS
      "Bash(docker-compose:*)"   // ADD THIS
    ],
    "deny": []
  },
  ...rest of config...
}
```

---

## Troubleshooting

### "Permission denied" errors
Check if the command is in the `allow` array. Add it if missing.

### Hooks not running
1. Verify hook file exists and is executable: `chmod +x .claude/hooks/tool_validator.py`
2. Test standalone: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | uv run .claude/hooks/tool_validator.py`
3. Check timeout value (5 seconds is usually sufficient)

### Invalid JSON errors
JSON does not support `//` comments. Use this guide for documentation instead of inline comments.

---

## Quick Reference

| Phase | Project | Add to settings.json |
|-------|---------|----------------------|
| 2 | 2-4 | Docker commands |
| 2 | 5-6 | Cloud docs access |
| 3 | 7+ | tool_validator hook, IDE diagnostics |
| 4 | 9+ | task_hard hook, restore from archive |

---

**See Also:**
- `CLAUDE.md` - Current setup status
- `TRANSITION.md` - Phase-by-phase evolution guide
- `archive/phase4/README.md` - Phase 4 restoration instructions
