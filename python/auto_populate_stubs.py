#!/usr/bin/env python3
import csv
import os
from pathlib import Path

ROOT = Path(os.environ.get("A11Y_SITE_ROOT", os.getcwd()))

DEST_REPORT = ROOT / "destination_coverage_report.csv"
PLAN_DIR = ROOT / "migration_plan"
CONTENT_PLAN_FILES = [
    PLAN_DIR / "Content redesign of accessibility.civicactions.com - 🗺️ Content plan.csv",
    PLAN_DIR / "Content redesign of accessibility.civicactions.com - Content audit.csv",
]

def load_false_destinations():
    missing = []
    if not DEST_REPORT.exists():
        return missing
    with DEST_REPORT.open() as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if len(row) < 2:
                continue
            dest, exists = row[0], row[1]
            if exists.strip().lower() == "false":
                missing.append(dest.strip())
    return missing

def load_plan_notes():
    notes = {}
    for plan_file in CONTENT_PLAN_FILES:
        if not plan_file.exists():
            continue
        with plan_file.open() as f:
            r = csv.reader(f)
            header = next(r, None)
            # Try to detect columns
            if not header:
                continue
            # Heuristics: look for Destination URL and Notes/Action columns
            try:
                dest_idx = next(i for i, h in enumerate(header) if "Destination" in h or "destination" in h or "URL" in h)
            except StopIteration:
                dest_idx = None
            # choose first text column after destination as note
            note_idx = None
            if header:
                for i, h in enumerate(header):
                    if i == dest_idx:
                        continue
                    if any(k in h.lower() for k in ["note", "action", "plan", "summary", "description"]):
                        note_idx = i
                        break
            for row in r:
                if not row:
                    continue
                dest = row[dest_idx].strip() if dest_idx is not None and dest_idx < len(row) else None
                note = row[note_idx].strip() if note_idx is not None and note_idx < len(row) else ""
                if dest:
                    # normalize leading slash
                    if not dest.startswith("/"):
                        dest = "/" + dest
                    notes[dest] = note
    return notes

def repo_path_for_destination(dest: str) -> Path:
    # map destination paths to repo file paths under ROOT
    clean = dest.strip("/")
    if not clean:
        return ROOT / "index.md"
    parts = clean.split("/")
    # Prefer index.md for section roots
    if len(parts) == 1:
        return ROOT / parts[0] / "index.md"
    return (ROOT / clean).with_suffix(".md")

def ensure_intro(path: Path, note: str):
    if not path.exists():
        return False
    content = path.read_text()
    # If file already has content beyond frontmatter, skip adding duplicate intro
    # Simple heuristic: look for a blank line after frontmatter
    if "---" in content:
        fm_end = content.find("---", content.find("---") + 3)
        body = content[fm_end + 3:] if fm_end != -1 else content
    else:
        body = content
    # Only append if the body is short
    if len(body.strip()) < 60:
        intro = "\n\n" + (note if note else "Content pending migration per plan.") + "\n"
        path.write_text(content.rstrip() + intro)
        return True
    return False

def main():
    missing = load_false_destinations()
    plan_notes = load_plan_notes()
    updated = []
    for dest in missing:
        repo_path = repo_path_for_destination(dest)
        # If the stub exists, try adding intro from plan notes
        note = plan_notes.get(dest, "")
        if ensure_intro(repo_path, note):
            updated.append(str(repo_path.relative_to(ROOT)))
    print(f"Updated {len(updated)} stubs with intro text.")
    for u in updated:
        print("-", u)

if __name__ == "__main__":
    main()
