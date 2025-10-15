#!/usr/bin/env python3
"""
Placeholder hook for `/task_hard` prompts.

The original Phase 4 automation lives in `.claude/archive/phase4/hooks/`.
This lightweight stub keeps Claude responsive while the advanced workflow
is archived. It simply acknowledges the hook invocation and exits without
performing any filesystem changes.

When you begin Phase 4 (after completing Project 8), replace this file with
the archived version and enable the full workflow per `TRANSITION.md`.
"""

from __future__ import annotations

import json
import sys


def main() -> None:
    """Consume hook input and exit successfully without side effects."""
    try:
        # Drain stdin to avoid broken pipe errors if Claude sends input.
        _ = sys.stdin.read()
        # If JSON was provided, this will keep validation noise out of logs.
        if _:
            json.loads(_)
    except json.JSONDecodeError:
        # Ignore non-JSON payloads; legacy clients sometimes send plain text.
        pass

    # Silently allow the prompt to proceed.
    sys.exit(0)


if __name__ == "__main__":
    main()
