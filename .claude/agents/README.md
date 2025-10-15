# Claude Code Agents

Agents are specialized AI assistants with specific roles, restricted toolsets, and focused expertise. This folder contains agents that activate progressively as you advance through the learning phases.

---

## What Are Agents?

Agents are sub-instances of Claude with:
- **Specific roles**: Defined in YAML frontmatter (name, description)
- **Restricted tools**: Limited to only what they need (Read, Grep, Bash, etc.)
- **Focused context**: Isolated from main conversation to stay specialized

**Example**: The learning-reviewer agent only has Read/Grep/Glob/Bash tools and focuses solely on educational code feedback.

---

## Available Agents

### ✅ ACTIVE: learning-reviewer.md
**Phase:** 1-2 (Always active during fundamentals)
**Purpose:** Educational code review with encouraging, explanatory feedback
**Focus:**
- Readability and naming conventions
- Modern Python idioms (pathlib, f-strings, list comprehensions)
- Basic error handling
- Modern tooling usage (uv, Ruff)
- Building good habits early

**When to Use:** After completing each project feature or before commits during Phase 1-2

**Invoke:** `Task(subagent_type="learning-reviewer", prompt="Review my current changes")`

---

### ⏸️ DORMANT: code-reviewer.md
**Phase:** 3+ (Enable after completing Project 6)
**Purpose:** Production-focused code review for Phase 3+ projects
**Focus:**
- Async/await patterns and concurrency
- Security vulnerabilities and best practices
- Performance and scalability considerations
- Production patterns (observability, error handling, testing)
- No backward compatibility or band-aid fixes

**Prerequisites:**
- Completed Projects 1-6
- Comfortable with async patterns, testing, security basics
- Ready for production-grade standards

**When to Activate:**
After completing Project 6, update `CLAUDE.md` under "Current Setup" to mark as ACTIVE:
```markdown
## Active Components
- agents/learning-reviewer.md
- agents/code-reviewer.md  # ADD THIS
```

**When to Use:** Before commits in Phase 3+ projects, especially for async code and APIs

**Invoke:** `Task(subagent_type="code-reviewer", prompt="Review for production readiness")`

---

## 📦 ARCHIVED: Phase 4 Workflow Agents

These agents are stored in `archive/phase4/agents/` and designed for complex, multi-file codebase analysis:

### investigator.md
**Phase:** 4 (Restore after completing Project 8)
**Purpose:** Tracks down code related to specific problems across large codebases
**Focus:**
- Keyword-prioritized file discovery
- Related code identification
- Progressive investigation reports
- Minimal redundancy (no code snippets, just connections)

### code-flow-mapper.md
**Phase:** 4 (Restore after completing Project 8)
**Purpose:** Traces execution paths and file interconnections
**Focus:**
- Dependency graph analysis
- Execution flow documentation
- File relationship mapping
- Integration point identification

### planner.md
**Phase:** 4 (Restore after completing Project 8)
**Purpose:** Creates detailed plans based on investigation and flow analysis
**Focus:**
- Combines investigation + flow reports
- Verifies information against actual files
- Super detailed, actionable plans
- Minimal changes philosophy (no overengineering)

**Workflow:**
`investigator` → `code-flow-mapper` → `planner` → `present plan to user`

**When to Restore:** See `archive/phase4/README.md` for activation instructions

---

## Activation Schedule

| Phase | Projects | Active Agents | Available to Enable |
|-------|----------|---------------|---------------------|
| 1 | 0-3 | learning-reviewer | - |
| 2 | 4-6 | learning-reviewer | - |
| 3 | 7-8 | learning-reviewer | code-reviewer (after Project 6) |
| 4 | 9+ | learning-reviewer, code-reviewer | Restore archived workflow agents |

---

## Creating Your Own Agents

You can create custom agents for specific needs. See `../guide.md` for detailed instructions.

**Example: Database optimization agent**
```markdown
---
name: db-optimizer
description: Analyzes and optimizes database queries and schemas
tools: Read, Grep, Bash
---

You are a database optimization expert focused on query performance...
```

Save as `.claude/agents/db-optimizer.md` and invoke with:
```python
Task(subagent_type="db-optimizer", prompt="Analyze slow queries in api/queries.py")
```

---

## Best Practices

1. **Use the right agent for the phase:** learning-reviewer for Phase 1-2, code-reviewer for Phase 3+
2. **Invoke after meaningful changes:** Don't micro-review every line, review after feature completion
3. **Read feedback carefully:** Agents explain *why*, not just *what* - this is educational
4. **Update CLAUDE.md when activating:** Keep the "Current Setup" section synchronized
5. **Don't activate Phase 3+ agents prematurely:** Prerequisites exist for good reasons

---

## Questions?

- **"Can I use multiple agents on the same code?"**
  Yes! learning-reviewer for fundamentals, code-reviewer for production patterns. They complement each other.

- **"Do agents remember previous conversations?"**
  No, agents are stateless. Each invocation is independent. This keeps them focused.

- **"Can I modify agent prompts?"**
  Absolutely! Edit the .md files to customize focus, tone, or checklist items.

- **"What if an agent's feedback is too advanced?"**
  Stick with learning-reviewer for Phase 1-2. Don't activate code-reviewer until Phase 3.

---

**Remember:** Agents are tools to enhance learning and maintain quality. Use them, learn from them, and gradually enable more as your skills grow.
