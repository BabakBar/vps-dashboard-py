# Claude Code Hooks

Hooks are Python scripts that run at specific points during Claude Code execution. They can validate, transform, or enhance tool calls and user interactions.

---

## What Are Hooks?

Hooks intercept Claude Code operations:
- **PreToolUse**: Runs before a tool executes (validation, suggestions)
- **UserPromptSubmit**: Runs when you submit a prompt (context enhancement, automation)

Hooks receive JSON input via stdin and can:
- ✅ Allow the operation (exit 0)
- ❌ Block the operation (exit 2)
- 💬 Add context messages (print to stdout)

---

## Available Hook: tool_validator.py

**Phase:** 3+ (Enable after completing Project 6)

**Purpose:** Enforces modern CLI tools (rg, bat, fd, sd) and blocks legacy commands (grep, cat, find, sed)

### What It Does

**Blocks prohibited tools:**
```bash
$ grep "error" logs.txt
❌ Prohibited tool 'grep' detected in command.
✅ Use rg (ripgrep) instead.
💡 Common flags: -i (ignore case), -n (line numbers), -A/-B/-C (context lines)
```

**Suggests modern alternatives:**
```bash
$ cat file.py
ℹ️  Consider using Bash tool with bat command for better performance.
💡 Use: bat filename [-n line numbers] [-p plain] [-r start:end range]
```

**Context-aware for file types:**
```bash
$ grep "key" data.csv
ℹ️  Consider using xsv for CSV files.
💡 xsv select (columns), xsv search (filter), xsv stats (analysis)
```

### Prerequisites

**You should be comfortable with:**
- Reading and understanding Python code (regex, error handling, JSON)
- Completed Projects 1-6 with solid Python fundamentals
- Understanding of modern CLI tools (rg, bat, fd, sd)

### What You'll Learn

By reading `tool_validator.py`, you'll see real-world examples of:
- Command-line argument parsing and JSON input handling
- Regular expressions for extracting commands from shell strings
- Error handling patterns with `sys.exit` codes
- Dictionary-based tool mappings and validation logic
- Context-aware suggestions (file type detection)

**Educational Value:** This hook serves as a Python code example you can study and modify.

### Activation Instructions

**Step 1: Test the Hook Standalone**
```bash
# Test with a prohibited command
echo '{"tool_name":"Bash","tool_input":{"command":"grep foo bar.txt"}}' | uv run .claude/hooks/tool_validator.py

# Expected output:
# ❌ Prohibited tool 'grep' detected in command.
# ✅ Use rg (ripgrep) instead.
# 💡 Common flags: -i (ignore case), -n (line numbers), -A/-B/-C (context lines)
```

**Step 2: Uncomment Hooks Section in settings.json**

Edit `.claude/settings.json` and uncomment:
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

**Step 3: Update CLAUDE.md**

Mark as ACTIVE in `CLAUDE.md` under "Current Setup":
```markdown
## Active Components
- agents/learning-reviewer.md
- agents/code-reviewer.md
- hooks/tool_validator.py  # ADD THIS
```

**Step 4: Verify**

Try using a legacy command:
```bash
grep "test" file.txt
```

You should see the validation message and modern tool suggestion.

---

## Why This Hook?

**Benefits:**
1. **Builds muscle memory:** Forces use of modern tools (rg, bat, fd, sd)
2. **Educational:** Shows real Python you can read, understand, and modify
3. **Immediate feedback:** Learn about modern tools as you code
4. **2025 best practices:** Aligns with industry standards

**When NOT to enable:**
- Phase 1-2: Focus on Python fundamentals first
- Before Project 6: You need solid Python to understand/debug the hook
- If you're not ready to commit to modern tooling

---

## 📦 ARCHIVED: Phase 4 Workflow Hook

### task_hard_prep_hook.py

**Location:** `archive/phase4/hooks/`
**Phase:** 4 (Restore after completing Project 8)

**Purpose:** Automatically creates `claude-instance-{id}` directories when you use `/task_hard` command, setting up the investigation → flow → planning workflow.

**Features:**
- Automatic directory creation with incremental IDs
- Extracts problem statement from command
- Provides context to orchestrated agents
- UserPromptSubmit hook (runs on every prompt)

**When to Restore:** After completing Project 8, if you need complex workflow orchestration. See `archive/phase4/README.md`.

---

## Creating Your Own Hooks

Hooks are Python scripts that follow a specific contract:

**Input:** JSON via stdin
```json
{
  "tool_name": "Bash",
  "tool_input": {"command": "ls -la"}
}
```

**Output:** Print to stdout (context messages) or stderr (errors)

**Exit Codes:**
- `0` - Allow operation
- `2` - Block operation

**Example: Simple validation hook**
```python
#!/usr/bin/env python3
import json
import sys

def main():
    hook_input = json.loads(sys.stdin.read())
    tool_name = hook_input.get('tool_name')

    if tool_name == 'Bash':
        command = hook_input['tool_input'].get('command', '')
        if 'rm -rf' in command:
            print("⚠️  Warning: Destructive command detected!", file=sys.stderr)
            print("Consider using a safer alternative.", file=sys.stderr)
            # Still allow (exit 0), but warn

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Best Practices

1. **Keep hooks fast:** They run on every tool call, so performance matters
2. **Fail gracefully:** If your hook errors, it shouldn't break Claude Code
3. **Use timeouts:** Set reasonable timeouts in settings.json (5-10 seconds max)
4. **Test standalone:** Always test hooks with example JSON before enabling
5. **Document behavior:** Add docstrings explaining what the hook does
6. **Start simple:** Begin with allow-all hooks that just log, then add logic

---

## Questions?

- **"Can I disable a hook temporarily?"**
  Yes! Comment out the hooks section in settings.json. Changes take effect immediately.

- **"What if my hook has a bug?"**
  Claude Code will show the error. Fix the script and try again. Hooks are isolated.

- **"Can I have multiple hooks?"**
  Yes! Add multiple entries to the hooks array. They run sequentially.

- **"Should I enable hooks in Phase 1?"**
  No. Wait until Phase 3 when you have the Python skills to understand and debug them.

---

**Remember:** Hooks are powerful but add complexity. Enable tool_validator in Phase 3+ to reinforce modern tooling habits, and only restore Phase 4 hooks if you need advanced workflow automation.
