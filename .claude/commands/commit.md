**WHEN TO ENABLE:** Phase 2+ (after completing Project 3)

**PREREQUISITES:**

- Completed Projects 1-3 with basic git workflow experience
- Comfortable with commit message conventions

**TO USE:**

```bash
/commit
```

This command guides you through creating a well-structured git commit using Conventional Commits format.

---

## Commit Workflow

Follow these steps to create a proper commit:

### Step 1: Review Changes

Run these commands to see what you're committing:

```bash
git status
git diff
```

Analyze the changes and prepare to describe them clearly.

### Step 2: Stage Files

If not already staged, add the files you want to commit:

```bash
git add <files>
```

### Step 3: Draft Commit Message

Follow Conventional Commits specification (<https://www.conventionalcommits.org/en/v1.0.0/>):

**Format:**

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Common types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**

```
feat(monitoring): Add CPU and memory metrics collection

Implement system metrics gathering using psutil library.
Metrics are displayed in formatted tables using tabulate.

Closes #123
```

### Step 4: Create Commit

Execute the commit with your message:

```bash
git commit -m "type(scope): description"
```

**Important:** Do NOT add co-authored-by or generated-by footers. Keep commits clean and focused.

### Step 5: Push (Optional)

If ready to push:

```bash
git push
```

---

## Best Practices

- **Keep it atomic**: One logical change per commit
- **Be descriptive**: Explain WHY, not just WHAT
- **Reference issues**: Use "Closes #123" or "Fixes #456" in footer
- **Test before committing**: Ensure code works
- **Run quality checks**: `ruff check .` and `ruff format .` before committing

---

**See Also:**

- Conventional Commits: <https://www.conventionalcommits.org/>
- CLAUDE.md "Reflection & Next Steps" for project-specific patterns
