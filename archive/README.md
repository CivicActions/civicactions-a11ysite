# Archived Content

This directory contains content that was discontinued during the site migration or marked for archival in the content audit.

## Archive Policy

Content in this directory:
- Is not linked from the main site navigation
- Should not be publicly accessible in production
- Is preserved for historical reference and potential future use
- Maintains original metadata for context

## What's Archived

Content was archived for the following reasons:
- **Superseded by new structure**: Old directories migrated to reorganized structure
- **Low value/engagement**: Pages marked "3 Low" in content audit with low click-through rates
- **Outdated**: Content marked as potentially outdated or internal-only
- **Minimal content**: Pages with little substantive information

## Contents

### Directories

#### /guide/
Old `/guide/` directory superseded by new `/guides/` structure (design, development, strategy, reporting subdirectories).

Archived files include:
- defect-priority.md → migrated to `/guides/development/defect-priority.md`
- events.md (marked "Possibly outdated. Could be removed.")
- glossary.md → migrated to `/guides/strategy/glossary.md`
- identity-language.md → migrated to `/champions/identity-language.md`
- introduction.md
- organizations.md
- Plus subdirectories: documents/, manual-testing/, pdf/, social-media/

#### /playbook/
Old `/playbook/` directory superseded by `/guides/` structure.

Archived files include:
- distributed-teams.md → migrated to `/guides/strategy/distributed-teams.md`
- documents.md → migrated to `/guides/design/documents.md`
- pdf.md → migrated to `/guides/design/pdf.md`
- personalization.md → migrated to `/guides/development/personalization.md`
- pwd.md → migrated to `/guides/strategy/pwd.md`
- And others: community.md, practice.md, statements.md, etc.

#### /roles/
Original role-based accessibility content that was consolidated into other sections.

### Individual Files

- **accessibility.md** - Old accessibility statement (replaced by `/site/accessibility-statement.md`)
- **news/hello-world.md** - Initial blog post (marked "Low click-through rate. Could be removed")
- **site/license.md** - Minimal license page (marked "No content" in content audit)

## Migration Context

Files were archived on December 12, 2025 as part of content migration cleanup. The content audit CSV identified ~200 URLs with value ratings, and low-value or superseded content was moved here.

---

## Implementation Notes

In production, this directory should either:
1. Return 404 errors for all requests
2. Be password protected for internal access only  
3. Be excluded from the web server document root entirely

The content is preserved in Git history and this archive for reference purposes.