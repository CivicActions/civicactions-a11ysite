# Missing Pages from Live Site

This directory contains markdown source files from pages that exist on the live site (https://accessibility.civicactions.com/) but were not migrated to the new repository structure or included in the migration plan.

## Pages Archived

Total: 38 markdown files preserved from the live site.

### Guide Pages (11 files)
- **guide-champions-program.md** - Champions program guide from `/guide/champions-program`
- **guide-design.md** - Design systems guide from `/guide/design`
- **guide-documents.md** - Document accessibility from `/guide/documents`
- **guide-history.md** - History of accessibility from `/guide/history`
- **guide-onboarding-staff.md** - Staff onboarding guide from `/guide/onboarding-staff`
- **guide-plain-language.md** - Plain language guide from `/guide/plain-language`
- **guide-resources.md** - Resources page from `/guide/resources` with books, newsletters, podcasts, videos, and Drupal modules
- **guide-semantic-html.md** - Semantic HTML guide from `/guide/semantic-html`
- **guide-social-media.md** - Social media accessibility from `/guide/social-media`
- **guide-tools.md** - Accessibility tools from `/guide/tools`
- **guide-training.md** - Training and certifications from `/guide/training`

### Playbook Pages (6 files)
- **playbook-AT.md** - Screen reader testing guide from `/playbook/AT`
- **playbook-ai-and-ia.md** - AI and IA guide from `/playbook/ai-and-ia`
- **playbook-authoring.md** - Authoring tools guide from `/playbook/authoring`
- **playbook-automated-testing.md** - Automated testing guide from `/playbook/automated-testing`
- **playbook-checklists.md** - Checklists guide from `/playbook/checklists`
- **playbook-roles.md** - Role-based evaluations from `/playbook/roles`

### People Pages (21 files)
Low-engagement person pages marked as "3 Low" value in content audit.

From `/about/people/*`:
- **about-people-allison-carroll.md**
- **about-people-civicactions.md**
- **about-people-daniel-mundra.md**
- **about-people-jack-haas.md**
- **about-people-jennifer-houde.md**
- **about-people-jonathan-bourland.md**
- **about-people-luke-fretwell.md**
- **about-people-michelle-kang.md**
- **about-people-nira-datta.md**
- **about-people-vanessa-luxen.md**

From `/_people/*` (original source):
- **people-allison-carroll.md**
- **people-civicactions.md**
- **people-daniel-mundra.md**
- **people-jack-haas.md**
- **people-jennifer-houde.md**
- **people-jonathan-bourland.md**
- **people-luke-fretwell.md**automated validation using Beautiful Soup:

1. **Crawl Process:**
   - Fetched all 141 URLs from sitemap.xml
   - Compared against migration plan (48 URLs documented)
   - Checked for corresponding files in new repository structure
   - Validated against already-archived content

2. **Validation Results:**
   - Total URLs in sitemap: 141
   - Migrated pages (found): 27
   - Already archived: 24
   - Missing from plan: 50
   - **Newly archived: 20 pages**

3. **Archival Criteria:**
   - Not included in migration plan (redirects-plan.txt)
   - No corresponding file in new repo structure
   - Had low engagement ("3 Low" value rating in audit)
   - Were superseded by content in new locations

See `/python/crawl_and_validate.py` for the validation script.

## Date Archived

- Initial archival: December 12, 2025
- Validation crawl: December 12, 2025 (added 20 additional pages)
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
