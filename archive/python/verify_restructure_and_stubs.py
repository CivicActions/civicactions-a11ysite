import csv
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "restructure_verification_report.csv"
STUBS_PATH = ROOT / "stub_pages_report.csv"


def find_restructure_csv() -> Path:
    plan_dir = ROOT / "migration_plan"
    for path in plan_dir.glob("*Restructure plan.csv"):
        return path
    raise FileNotFoundError("Restructure plan CSV not found under migration_plan/")
REPORT_PATH = ROOT / "restructure_verification_report.csv"
STUBS_PATH = ROOT / "stub_pages_report.csv"

STUB_MARKERS = [
    "content pending migration",
    "placeholder stub",
    "placeholder migrated stub",
]


def read_csv_rows(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def candidate_paths(dest_url: str):
    dest = dest_url.lstrip("/")
    if not dest:
        yield ROOT / "index.md"
        return
    if dest.endswith("/"):
        dest = dest[:-1]
    # Try file.md
    yield ROOT / f"{dest}.md"
    # Try index.md in folder
    yield ROOT / dest / "index.md"


def load_front_matter(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    if not text.startswith("---"):
        return None
    parts = text.split("\n---\n", 2)
    if len(parts) < 2:
        return None
    fm_block = parts[0].lstrip("-\n") + "\n" + parts[1]
    data = {}
    for line in fm_block.splitlines():
        if not line or line.strip().startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip().strip('"')
    return data


def is_stub(text: str):
    low = text.lower()
    return any(marker in low for marker in STUB_MARKERS)


def verify():
    csv_path = find_restructure_csv()
    rows = list(read_csv_rows(csv_path))
    report = []
    stubs = []
    for row in rows:
        dest_url = row.get("📍 Destination URL", "").strip()
        expected_title = row.get("🏷️ Destination Title", "").strip()
        found_path = None
        exists = False
        title_found = ""
        title_match = ""
        stub_flag = False

        for cand in candidate_paths(dest_url):
            if cand.exists():
                found_path = cand
                exists = True
                break
        if exists:
            text = found_path.read_text(encoding="utf-8", errors="ignore")
            fm = load_front_matter(found_path) or {}
            title_found = fm.get("title", "")
            title_match = str(title_found.strip() == expected_title.strip()) if title_found else ""
            stub_flag = is_stub(text)
            if stub_flag:
                stubs.append({
                    "path": str(found_path.relative_to(ROOT)),
                    "destination_url": dest_url,
                    "expected_title": expected_title,
                    "title_found": title_found,
                })
        report.append({
            "destination_url": dest_url,
            "destination_title_expected": expected_title,
            "path": str(found_path.relative_to(ROOT)) if found_path else "",
            "exists": str(exists),
            "title_found": title_found,
            "title_matches": title_match,
            "stub_detected": str(stub_flag),
        })

    with REPORT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=report[0].keys())
        writer.writeheader()
        writer.writerows(report)

    with STUBS_PATH.open("w", encoding="utf-8", newline="") as f:
        if stubs:
            writer = csv.DictWriter(f, fieldnames=stubs[0].keys())
            writer.writeheader()
            writer.writerows(stubs)
        else:
            f.write("path,destination_url,expected_title,title_found\n")


if __name__ == "__main__":
    verify()
