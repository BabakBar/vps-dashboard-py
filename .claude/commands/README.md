# Claude Code Custom Commands

Custom slash commands let you create shortcuts for repetitive tasks. Commands are simple markdown files with prompts that get expanded when you type `/command-name`.

---

## What Are Custom Commands?

Commands are:
- **Simple text files** with `.md` extension
- **Prompt expansions** that run when you type `/command-name`
- **Task-specific shortcuts** for repetitive workflows
- **Easy to create** - just markdown with optional argument support

---

## When to Create Your First Command

**Phase 2 (after completing Project 3)**

By Project 3, you'll have noticed repetitive tasks:
- Running lint + format before every commit
- Setting up new Python projects with the same structure
- Running tests with coverage reports
- Creating git commits with proper formatting

**These patterns are perfect candidates for commands!**

---

## Available Commands

### ⏸️ DORMANT: commit.md
**Phase:** 2+ (Enable after Project 3)
**Purpose:** Structured git commit workflow with good message formatting

**WHEN TO ENABLE:**
After completing Project 3, when you're comfortable with git workflows and ready for structured commits.

**TO ACTIVATE:**
Just start using it! The file is already in place:
```bash
/commit
```

The command will:
1. Run `git status` and `git diff` to show changes
2. Ask you to describe what changed and why
3. Format the commit message properly
4. Execute the commit with co-authored-by attribution

---

### ⏸️ DORMANT: code-review.md
**Phase:** 2+ (Enable after Project 3)
**Purpose:** Manual trigger for code review before committing

**TO USE:**
```bash
/code-review
```

Invokes the appropriate reviewer agent (learning-reviewer in Phase 1-2, code-reviewer in Phase 3+).

---

## Creating Your First Command

### Step 1: Identify a Repetitive Task

After Project 3, notice what you type repeatedly. Common examples:
- `uv run ruff check . && uv run ruff format . && uv run pytest --cov`
- `uv init new-project && cd new-project && uv add psutil requests`
- Commit message templates for different change types

### Step 2: Create the Command File

**Example: /quick-check command**

Create `.claude/commands/quick-check.md`:
```markdown
Run linting, formatting, and tests with coverage.

Execute these commands sequentially:
1. uv run ruff check .
2. uv run ruff format .
3. uv run pytest --cov=src tests/ -v

Report results for each step clearly.
```

### Step 3: Use It!

```bash
/quick-check
```

That's it! Claude will expand your prompt and execute the workflow.

---

## Command Templates

### Quality Check Command
```markdown
Run code quality checks:
1. Lint: uv run ruff check .
2. Format: uv run ruff format .
3. Type check: uv run pyright
4. Tests: uv run pytest --cov

Stop if any check fails and report the issue.
```

### Project Setup Command
```markdown
Set up a new Python project with modern tooling:

1. Create project: uv init $ARGUMENTS
2. Add dependencies: uv add psutil tabulate click rich
3. Add dev dependencies: uv add --dev pytest pytest-cov ruff pyright
4. Create src/ directory structure
5. Initialize git repository
6. Create .gitignore for Python
7. Show next steps

Project name: $ARGUMENTS
```

### Docker Build & Run Command
```markdown
Build and run the Docker container for this project:

1. Build: docker build -t vps-dashboard:latest .
2. Run: docker run --rm -p 8000:8000 vps-dashboard:latest
3. Show container logs

If build fails, explain the error clearly.
```

---

## Command Arguments

Use `$ARGUMENTS` in your command to accept input:

**Command file:**
```markdown
Create a new feature branch and switch to it.

Branch name: $ARGUMENTS

Execute: git checkout -b feature/$ARGUMENTS
```

**Usage:**
```bash
/new-branch api-metrics-endpoint
# Expands to: git checkout -b feature/api-metrics-endpoint
```

---

## Best Practices

1. **Start simple:** Your first command should be straightforward (lint + format + test)
2. **One task per command:** Don't create mega-commands that do everything
3. **Use descriptive names:** `/quick-check` is better than `/qc`
4. **Document expected behavior:** Explain what the command does in the first line
5. **Test thoroughly:** Run the command a few times to ensure it works as expected
6. **Iterate based on usage:** Refine commands as you discover edge cases

---

## 📦 ARCHIVED: Phase 4 Orchestration Commands

Complex workflow commands are stored in `archive/phase4/commands/`:

### task_easy.md
- Sequential thinking-based problem solving
- Best practices enforcement
- No band-aid fixes or fallbacks

### task_hard.md
- Full investigation → flow mapping → planning workflow
- Automatic instance directory creation
- Multi-agent orchestration with sequential execution

**When to Restore:** After completing Project 8, if working on large, complex features. See `archive/phase4/README.md`.

---

## Examples from Phase 2+

### /test-with-docker
```markdown
Run tests inside Docker container to verify production environment:

1. Build test image: docker build -f Dockerfile.test -t app-test .
2. Run tests: docker run --rm app-test pytest --cov
3. Clean up: docker rmi app-test

Report coverage percentage and any failures.
```

### /deploy-dev
```markdown
Deploy to development environment:

1. Run tests: uv run pytest
2. Build Docker image: docker build -t app:dev .
3. Push to registry: docker push registry.example.com/app:dev
4. Update deployment: kubectl set image deployment/app app=registry.example.com/app:dev

Stop if any step fails.
```

---

## Questions?

- **"How do I edit a command?"**
  Just edit the `.md` file. Changes take effect immediately.

- **"Can commands call other commands?"**
  Not directly, but you can include similar prompts or reference other workflows.

- **"What if my command needs complex logic?"**
  For complex logic, consider creating a Python script and having the command invoke it.

- **"Should I create commands in Phase 1?"**
  Not yet - wait until Phase 2 when you have established patterns and repetitive tasks.

---

**Remember:** Commands are shortcuts for tasks you do repeatedly. If you're typing the same sequence of commands 3+ times, it's a candidate for a custom command!
