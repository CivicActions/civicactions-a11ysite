````markdown
# Python Tools

Utilities to assist content migration, navigation frontmatter, and small-content page population for the Eleventy site.

## Prerequisites
- Python 3.9+
- Recommended: create a virtual environment.
- Some scripts require `requests` (`pip install requests`).

## Scripts
- `crawl_compare_and_migrate.py`: Crawl the live site, compare against migration plan, and optionally auto-populate short pages.
  - Outputs: `live_vs_plan_report.csv`, migration logs.
  - Example:
    ```sh
    python3 python/crawl_compare_and_migrate.py --base https://accessibility.civicactions.com --root "$PWD" --max-pages 300 --migrate-stubs
    ```
- `migrate_from_old_site.py`: Replace minimal content with richer Markdown from `old-site/` while preserving frontmatter and adding migration notes.
  - Requires: `old-site/` folder at repo root and migration logs.
  - Example:
    ```sh
    python3 python/migrate_from_old_site.py --root "$PWD"
    ```
- `add_eleventy_navigation.py`: Add `eleventyNavigation` frontmatter to Markdown files missing it using folder-based heuristics.
  - Example:
    ```sh
    python3 python/add_eleventy_navigation.py --root "$PWD"
    ```
- `auto_populate_stubs.py`: Append brief intro text to short pages based on notes from migration plan CSVs.
  - Reads: `destination_coverage_report.csv` and selected files under `migration_plan/`.
  - Example:
    ```sh
    A11Y_SITE_ROOT="$PWD" python3 python/auto_populate_stubs.py
    ```
- `relaxed_match_verbose.py`: Helper for fuzzy path/content matching used during migration (verbose output).
- `remove_staff.py`: Utility to remove staff references/pages no longer needed.

## Setup
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # if present
pip install requests              # needed for crawl scripts
```

## Notes
- Run scripts from repo root so relative paths resolve.
- Back up or commit changes before running migration scripts.
- Review generated CSV reports to prioritize remaining work (`destination_coverage_report.csv`, `top_missing_destinations.csv`).

````
