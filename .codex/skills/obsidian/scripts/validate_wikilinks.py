#!/usr/bin/env python3
"""Validate simple Obsidian wikilinks against filenames and frontmatter aliases."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


SKIP_DIRS = {".git", ".obsidian", "node_modules", ".venv", "__pycache__"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def iter_markdown(root: Path):
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def parse_aliases(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---", 4)
    if end == -1:
        return []
    fm = text[4:end]
    aliases: list[str] = []
    lines = fm.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith("aliases:"):
            value = line.split(":", 1)[1].strip()
            if value.startswith("["):
                try:
                    parsed = ast.literal_eval(value)
                    aliases.extend(str(item).strip() for item in parsed)
                except Exception:
                    inner = value.strip("[]")
                    aliases.extend(item.strip().strip("'\"") for item in inner.split(",") if item.strip())
            elif not value:
                for child in lines[idx + 1 :]:
                    if child.startswith("  - "):
                        aliases.append(child[4:].strip().strip("'\""))
                    elif child and not child.startswith(" "):
                        break
    return [alias for alias in aliases if alias]


def strip_code(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    known: set[str] = set()
    files: list[Path] = []

    for path in iter_markdown(root):
        files.append(path)
        rel = path.relative_to(root)
        known.add(path.stem)
        known.add(str(rel.with_suffix("")))
        text = path.read_text(encoding="utf-8")
        known.update(parse_aliases(text))

    unresolved: list[tuple[Path, str]] = []
    for path in files:
        text = strip_code(path.read_text(encoding="utf-8"))
        for target in WIKILINK_RE.findall(text):
            target = target.strip()
            if target and target not in known:
                unresolved.append((path.relative_to(root), target))

    if unresolved:
        for path, target in unresolved:
            print(f"UNRESOLVED {path}: [[{target}]]")
        return 1

    print(f"OK: {len(files)} markdown files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
