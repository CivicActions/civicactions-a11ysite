# Missing Pages from Live Site

This directory contains markdown source files from pages that exist on the live site (https://accessibility.civicactions.com/) but were not migrated to the new repository structure or included in the migration plan.

## Pages Archived

### Guide Pages
- **guide-resources.md** - Resources page from `/guide/resources` with books, newsletters, podcasts, videos, and Drupal modules

### Playbook Pages
- **playbook-AT.md** - Screen reader testing guide from `/playbook/AT`
- **playbook-ai-and-ia.md** - AI and IA guide from `/playbook/ai-and-ia`
- **playbook-authoring.md** - Authoring tools guide from `/playbook/authoring`
- **playbook-automated-testing.md** - Automated testing guide from `/playbook/automated-testing`
- **playbook-checklists.md** - Checklists guide from `/playbook/checklists`
- **playbook-roles.md** - Role-based evaluations from `/playbook/roles`

### People Pages
Low-engagement person pages marked as "3 Low" value in content audit:
- **people-allison-carroll.md**
- **people-daniel-mundra.md**
- **people-jack-haas.md**
- **people-jennifer-houde.md**
- **people-jonathan-bourland.md**
- **people-luke-fretwell.md**
- **people-michelle-kang.md**
- **people-nira-datta.md**
- **people-vanessa-luxen.md**
- **people-civicactions.md**

## Source

All files were fetched from the original GitHub repository:
`https://github.com/CivicActions/accessibility`

The live site at https://accessibility.civicactions.com/ is built from this source repository using Jekyll.

## Reason for Archival

These pages were identified through the following process:
1. Crawled sitemap.xml from live site
2. Compared URLs against:
   - Migration plan (redirects-plan.txt)
   - Existing files in new repository structure
3. Fetched original markdown source files for preservation

These pages either:
- Were not included in the original migration plan
- Had low engagement ("3 Low" value rating)
- Were superseded by new content in different locations

## Date Archived

December 12, 2025
