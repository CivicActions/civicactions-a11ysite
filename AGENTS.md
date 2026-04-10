# AGENTS.md

This file provides guidance for AI coding agents (such as GitHub Copilot, Claude,
ChatGPT, and similar tools) working in this repository. It describes the project's
purpose, architecture, key files, build and test commands, and coding conventions
to follow when contributing changes.

---

## Project overview

**CivicActions Accessibility** is a publicly available collection of resources about
digital accessibility and how it aligns with open source and government technology.
The site provides guides, champion profiles, and practical tools for teams working to
improve the accessibility of their products and services.

- Live site: <https://accessibility.civicactions.com/>
- Source repository: <https://github.com/CivicActions/accessibility>

---

## Repository layout

```
civicactions-a11ysite/
├── _includes/
│   ├── base.html            # Primary HTML shell (header, nav, footer, skip link)
│   └── layout.njk           # Nunjucks layout wrapper
├── assets/
│   └── styles.css           # All site styles (colors, typography, components)
├── about/                   # About section pages
├── champions/               # Accessibility champion profiles
├── guides/                  # Accessibility guides and how-tos
├── projects/                # Accessibility project pages
├── roles/                   # Role-specific accessibility content
├── search/                  # Site search functionality
├── ACR/                     # Accessibility Conformance Reports
├── VPAT/                    # Voluntary Product Accessibility Templates
├── index.md                 # Home page content
├── accessibility.md         # Accessibility statement page
├── AGENTS.md                # This file — guidance for AI coding agents
├── ACCESSIBILITY.md         # Accessibility standards for contributors and agents
├── STYLES.md                # Design and content standards
├── README.md                # General project documentation
├── SECURITY.md              # Security policy
├── .eleventy.js             # Eleventy configuration (legacy)
├── eleventy.config.js       # Eleventy configuration (current)
├── .eleventyignore          # Files excluded from Eleventy processing
├── .pre-commit-config.yaml  # Pre-commit hook configuration
└── package.json             # Node.js dependencies and scripts
```

---

## Local development

### Prerequisites

- Node.js ≥ 18

### Install dependencies

```bash
npm install
```

### Start the local development server

```bash
npm run serve
# Open http://localhost:8080
```

### Build static output

```bash
npm run build
```

### Build for GitHub Pages (with path prefix)

```bash
npm run build-ghpages
```

---

## Coding conventions

- **Templates**: Pages use Markdown with YAML front matter, rendered by Eleventy.
  Layouts are written in Nunjucks (`.njk`) and HTML.
- **CSS**: All site styles live in `assets/styles.css`. Use CSS custom properties
  for colors and spacing. See [STYLES.md](./STYLES.md) for the token reference.
- **Front matter keys**: Standard keys include `title`, `description`, `layout`,
  `permalink`, `migration_notes`, and `editor_notes`. Match the style of existing pages.
- **Eleventy ignore**: Files listed in `.eleventyignore` are not processed as site
  pages. Documentation files such as `AGENTS.md`, `ACCESSIBILITY.md`, and `STYLES.md`
  must remain in that list.
- **Pre-commit hooks**: The repository uses pre-commit hooks (remark-lint, codespell,
  search-and-replace). Run `pre-commit install` before making commits.
- **American English**: Use American English spelling throughout all documentation
  and content files.

---

## Accessibility requirements

**Accessibility is a first-class requirement of this project.** Every change that
touches HTML, CSS, or Markdown content must be reviewed against the standards in
[ACCESSIBILITY.md](./ACCESSIBILITY.md).

Key obligations for AI agents making changes:

1. **WCAG 2.1 Level AA compliance** — all new or modified UI must meet Perceivable,
   Operable, Understandable, and Robust criteria.
2. **Color contrast** — normal text ≥ 4.5:1, large text ≥ 3:1, UI components ≥ 3:1.
   Approved palette values are listed in [STYLES.md § 3.1](./STYLES.md#31-design-tokens).
3. **Keyboard accessibility** — every interactive element must be reachable and
   operable via keyboard alone.
4. **Skip link** — the `base.html` template includes a skip link; do not remove it.
5. **Semantic HTML** — use semantic elements (`<main>`, `<nav>`, `<header>`,
   `<footer>`, `<section>`, `<article>`) rather than generic `<div>` wrappers.
6. **Heading hierarchy** — use heading levels in order (`h1` → `h2` → `h3`). Do
   not skip levels.
7. **Alt text** — every image must have meaningful alt text; decorative images use
   `alt=""`.
8. **Focus indicators** — all focusable elements must have a visible focus indicator.
9. **Testing** — after making UI changes, run automated checks with axe DevTools or
   Lighthouse and verify keyboard navigation manually.
10. **Update `ACCESSIBILITY.md`** — if you add new UI patterns or color usage, update
    [ACCESSIBILITY.md](./ACCESSIBILITY.md) to document them.

See [ACCESSIBILITY.md](./ACCESSIBILITY.md) for the full reference.

---

## GitHub Actions workflows

| Workflow | Trigger | Purpose |
| :--- | :--- | :--- |
| `deploy-to-ghpages` | Push to `main` | Build and deploy site to GitHub Pages |

---

## Before opening a pull request

1. Verify the site builds without errors (`npm run build`).
2. Confirm all accessibility requirements above are met.
3. Update [ACCESSIBILITY.md](./ACCESSIBILITY.md) if your change adds or modifies
   accessibility-relevant behavior.
4. Update [README.md](./README.md) if your change affects setup, configuration, or
   user-facing behavior.
5. Run `pre-commit run --all-files` to check for linting issues before committing.
6. **AI disclosure**: If you are an AI agent making changes to this repository, note
   which model was used and what it did in the pull request description.
