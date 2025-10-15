# Phase 4 Advanced Workflow Tools

This archive contains sophisticated workflow automation tools designed for Phase 4 (Projects 9+) when working on complex, multi-file codebases.

---

## What's Archived Here?

### Agents (3 files)
- **investigator.md** - Tracks down code related to problems across large codebases
- **code-flow-mapper.md** - Traces execution paths and file interconnections
- **planner.md** - Creates detailed plans based on investigation and flow analysis

### Commands (2 files)
- **task_easy.md** - Sequential thinking with best practices enforcement
- **task_hard.md** - Full investigation → flow → planning orchestration

### Hooks (1 file)
- **task_hard_prep_hook.py** - Automatic directory setup for workflow orchestration

### Settings
- **settings.json** - Original configuration with 63+ permissions

---

## When to Restore

**After completing Project 8**, when transitioning to Phase 4 capstone projects.

**Only restore if:**
- Working on large, complex codebases (10+ files)
- Need systematic investigation of interconnected code
- Want orchestrated workflows for multi-step problems
- Ready for advanced automation

**Don't restore if:**
- Projects are relatively small (< 10 files)
- Simpler workflows suffice (Phase 1-3 tools work fine)
- You prefer more direct control over the process

---

## What These Tools Do

### The Workflow: investigator → code-flow-mapper → planner

**Step 1: Investigation**
```bash
/task_hard Fix the authentication timeout issue in the API. Keywords: auth, token, session
```

The investigator agent:
- Searches for files containing keywords (auth, token, session)
- Identifies related code across the codebase
- Creates `INVESTIGATION_REPORT.md` with findings
- Prioritizes keyword-matching files

**Step 2: Flow Mapping**

The code-flow-mapper agent:
- Reads the investigation report
- Traces execution paths and dependencies
- Maps file interconnections
- Creates `FLOW_REPORT.md` with flow analysis

**Step 3: Planning**

The planner agent:
- Combines investigation + flow reports
- Verifies information against actual files
- Creates super-detailed `PLAN.md` with all affected files
- Focuses on minimal necessary changes

**Result:** Comprehensive plan you can review and approve before implementation.

---

## Restoration Instructions

### Option 1: Full Restoration (Recommended for Phase 4)

**Step 1: Copy Agents**
```bash
cp .claude/archive/phase4/agents/* .claude/agents/
```

**Step 2: Copy Commands**
```bash
cp .claude/archive/phase4/commands/* .claude/commands/
```

**Step 3: Copy Hooks**
```bash
cp .claude/archive/phase4/hooks/* .claude/hooks/
```

**Step 4: Update settings.json**

Add the UserPromptSubmit hook for task_hard:
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
  ],
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
}
```

**Step 5: Update CLAUDE.md**

Mark all as ACTIVE in "Current Setup":
```markdown
## Active Components
- agents/learning-reviewer.md
- agents/code-reviewer.md
- agents/investigator.md
- agents/code-flow-mapper.md
- agents/planner.md
- hooks/tool_validator.py
- hooks/task_hard_prep_hook.py
```

**Step 6: Test**
```bash
/task_hard Analyze the database connection pooling logic. Keywords: pool, connection, database
```

You should see:
1. Automatic directory creation (claude-instance-1)
2. Investigation report generation
3. Flow mapping
4. Detailed plan creation

---

### Option 2: Selective Restoration

Restore only what you need:

**Just the workflow agents (no commands/hooks):**
```bash
cp .claude/archive/phase4/agents/{investigator,code-flow-mapper,planner}.md .claude/agents/
```

Then invoke manually:
```python
Task(subagent_type="investigator", prompt="Investigate authentication flow. Keywords: auth, login")
Task(subagent_type="code-flow-mapper", prompt="Map flow based on investigation")
Task(subagent_type="planner", prompt="Create detailed plan")
```

**Just task_easy (no full workflow):**
```bash
cp .claude/archive/phase4/commands/task_easy.md .claude/commands/
```

Use for simpler problems that don't need full investigation:
```bash
/task_easy Refactor the error handling in api/routes.py
```

---

## File Descriptions

### agents/investigator.md
**Purpose:** Code archaeology for large codebases
**Tools:** Task, Bash, Glob, Grep, Read, Write (for report)
**Output:** INVESTIGATION_REPORT.md in claude-instance-{id}/
**Best For:** Finding all code related to a specific feature or bug

**Behavior:**
- Prioritizes keyword-matching files
- Updates report progressively (not batch)
- Focuses on relationships, not code snippets
- Excludes irrelevant files

### agents/code-flow-mapper.md
**Purpose:** Execution path tracing
**Tools:** Task, Bash, Glob, Grep, Read, Write (for report)
**Input:** INVESTIGATION_REPORT.md
**Output:** FLOW_REPORT.md in claude-instance-{id}/
**Best For:** Understanding how code flows through multiple files

**Behavior:**
- Reads investigation report first
- Traces dependencies and call chains
- Updates report progressively
- Creates visual flow descriptions

### agents/planner.md
**Purpose:** Detailed plan creation with verification
**Tools:** Task, Bash, Glob, Grep, Read, Edit, Write
**Input:** INVESTIGATION_REPORT.md + FLOW_REPORT.md
**Output:** PLAN.md in claude-instance-{id}/
**Best For:** Complex refactorings or features touching many files

**Behavior:**
- Reads both reports
- Verifies against actual code
- Updates plan progressively as verification happens
- Super detailed with all affected files
- Minimal changes philosophy (no overengineering)

### commands/task_easy.md
**Purpose:** Sequential thinking problem solving
**Workflow:** ultrathink → solve with best practices
**Best For:** Single-feature problems not needing full investigation

**Enforces:**
- No band-aid fixes
- No fallbacks
- No backwards compatibility
- Self-documenting code

### commands/task_hard.md
**Purpose:** Orchestrated full workflow
**Workflow:** investigator → mapper → planner → plan mode
**Best For:** Complex problems spanning multiple files
**Requires:** task_hard_prep_hook.py for auto-directory creation

**Features:**
- Automatic claude-instance-{id} directories
- Sequential agent execution (never parallel)
- Keyword extraction and prioritization
- Final plan presentation for approval

### hooks/task_hard_prep_hook.py
**Purpose:** Automates directory setup for /task_hard
**Trigger:** UserPromptSubmit (runs on every prompt)
**Behavior:** Detects `/task_hard`, creates numbered instance directory

**Dependencies:**
- Requires task_hard.md command to be useful
- Creates claude-code-storage/claude-instance-{n}/

---

## Prerequisites

Before restoring, ensure you have:

✅ Completed Projects 1-8 (all three phases)
✅ Comfortable with Python workflow automation
✅ Working on projects with 10+ interconnected files
✅ Ready to debug hook issues if they arise
✅ Understand the investigation → flow → planning workflow

---

## Troubleshooting

### Hook Not Running
```bash
# Check if hook is executable
chmod +x .claude/hooks/task_hard_prep_hook.py

# Test standalone
echo '{"prompt":"/task_hard Test problem"}' | uv run .claude/hooks/task_hard_prep_hook.py
```

### Agents Not Finding Each Other
Ensure agent names match exactly:
- `investigator` not `Investigator`
- `code-flow-mapper` not `code_flow_mapper`
- `planner` not `Planner`

### Reports Not Generated
Check claude-code-storage directory exists and is writable:
```bash
mkdir -p claude-code-storage
chmod 755 claude-code-storage
```

---

## Alternative: Keep It Simple

If Phase 4 workflow feels too complex, you can stay with Phase 3 tools:

- **learning-reviewer** for fundamentals
- **code-reviewer** for production patterns
- **Manual investigation** using Grep/Glob/Read directly
- **Simple custom commands** for repetitive tasks

**There's no requirement to restore Phase 4 tools.** Use what works for your project complexity.

---

## Questions?

- **"Do I need all three agents?"**
  For the `/task_hard` workflow, yes. But you can use them individually if you manually invoke each one.

- **"Can I modify the workflow?"**
  Absolutely! Edit task_hard.md to change the sequence or add steps.

- **"What if I don't want hooks?"**
  Manually create claude-instance directories and invoke agents individually.

- **"Is there a performance impact?"**
  Yes, the full workflow (investigator → mapper → planner) takes several minutes for large codebases. Worth it for complex problems.

---

**Remember:** These are power tools for complex work. Restore when the Phase 1-3 setup no longer matches your project complexity. Until then, the simpler structure serves you better.
