# STYLES.md: Design and content standards

This file defines how the CivicActions Accessibility site is designed, written, and
published. It is the authoritative reference for both humans and AI coding agents
contributing to this repository.

This project uses [CivicActions](https://civicactions.com/) brand identity and adheres
to the [CivicActions Style Guide](https://civicactions-style-guide.readthedocs.io/en/latest/).
Designers should refer to that guide as the canonical source for brand assets, full color
palettes, typography specimens, and Figma resources.

---

## Scope: documentation files vs. the website

This project has two surfaces that share the same standards:

| Surface | Files | Audience |
| :--- | :--- | :--- |
| **Eleventy site** | `index.md`, `_includes/base.html`, `assets/styles.css` | Public visitors |
| **Repository documentation** | `README.md`, `AGENTS.md`, `STYLES.md`, `ACCESSIBILITY.md` | Contributors, adopters, and AI agents reading files on GitHub |

**What applies to both surfaces:**
- Section 2 — Content and voice standards
- Section 4 — Accessibility and semantic logic
- Section 5 — AI agent instructions
- Section 6 — Content governance

**What applies to the website only:**
- Section 3 — Design foundations (color tokens, typography, breakpoints, page layout)

---

## 1. Core philosophy

We design for the reader, not the institution. The goal is to reduce cognitive load
through consistency, clarity, and radical accessibility.

CivicActions advances the greater good through technology built for humans. The
CivicActions Accessibility site reflects these core brand values:

- **Confidence**: we have the experience and drive to solve hard problems.
- **Curiosity**: we are agile, innovative, and inquisitive.
- **Humanity**: we put people first and share our work openly.

Design and writing principles derived from those values:

1. **Reader-first.** Start with the reader's need, not the organization's structure.
2. **Plain language.** If a 12-year-old cannot understand it, it is a barrier.
3. **Inclusive by default.** See [ACCESSIBILITY.md](./ACCESSIBILITY.md) for all interaction and visual standards.
4. **Consistency is trust.** AI agents and humans must use the same tokens, patterns, and vocabulary.
5. **Radically open.** Work transparently; share methods, data, and findings openly.

---

## 2. Content and voice standards

Derived from UK GDS and Digital.gov plain language standards, and aligned with the
[CivicActions Style Guide](https://civicactions-style-guide.readthedocs.io/en/latest/).

### 2.1 Voice and tone

We use an **authoritative peer** tone: professional and knowledgeable, but accessible
and supportive. This reflects CivicActions' brand personality: modern, clean,
professional, friendly, and optimistic.

| Context | Tone | Strategy |
| :--- | :--- | :--- |
| **Onboarding** | Encouraging | Focus on the benefit to the reader |
| **Technical / legal** | Precise | Be unambiguous; explain "why" if a rule is complex |
| **Error states** | Calm / helpful | Do not blame the reader; provide a clear path forward |
| **Data / impact** | Confident and grounded | Let numbers speak; contextualize without overstating |

### 2.2 Plain language and word choice

AI agents must prioritize these substitutions:

| Avoid | Use instead |
| :--- | :--- |
| Utilize / leverage | Use |
| Facilitate / implement | Help / carry out |
| At this point in time | Now |
| In order to | To |
| Notwithstanding | Despite / even though |
| Requirements | Rules / what you need |

### 2.3 Grammar and mechanics

- **Active voice:** "The scanner checks the link" — not "The link is checked by the scanner."
- **Sentence case:** Use sentence case for all headings and buttons. "Save and continue" — not "Save and Continue."
- **Lists:** Use bullets for unordered items. Use numbered lists only for sequential steps.
- **Oxford comma:** Always use the serial comma in lists of three or more.

### 2.4 Spelling convention

This project uses **American English** as its default spelling standard.

| Variant | Example spellings | When to use |
| :--- | :--- | :--- |
| **American English** (default) | color, center, optimize, behavior | All documentation in this project |

> **AI agents:** Always apply American English spelling rules throughout all documents.

### 2.5 Abbreviations, numbers, and dates

#### Abbreviations

- Spell out an abbreviation on first use, then use the short form: "Web Content
  Accessibility Guidelines (WCAG)."
- Do not use periods in acronyms: "HTML," "CSS," "AI" — not "H.T.M.L."
- Avoid jargon-only abbreviations without explanation unless writing for a specialist
  audience.

#### Numbers

| Context | Rule | Example |
| :--- | :--- | :--- |
| **In body text** | Spell out one through nine; use numerals for 10 and above | "three pillars," "12 tokens" |
| **Starts a sentence** | Always spell out | "Twelve steps are required." |
| **Percentages** | Use numerals and the % symbol | "4.5% contrast ratio" |
| **Versions and technical values** | Always use numerals | "WCAG 2.1," "font-size: 1rem" |

#### Dates

- Use **ISO 8601** for machine-readable dates: `2025-06-01`.
- Use **spelled-out months** for human-readable dates: "June 1, 2025."
- Do not use all-numeric dates that could be ambiguous across locales (01/06/2025).

### 2.6 Attribution and citation

- **Quote directly** only when the original wording matters and cannot be improved.
- **Paraphrase** when the idea is what matters; credit the source regardless.
- **Link to the source** rather than reproducing large portions of external content.
- **Do not reproduce** entire copyrighted works, style guides, or specifications.

> **AI agents:** Do not reproduce large passages from external style guides or
> specifications verbatim. Summarize, paraphrase, and link to the canonical source.

### 2.7 Content structure and document types

| Document type | Purpose | Structure pattern |
| :--- | :--- | :--- |
| **Reference** (STYLES.md, ACCESSIBILITY.md) | Authoritative rules; consulted, not read cover-to-cover | Numbered sections, tables, bullet rules |
| **Guide or how-to** (guides/) | Step-by-step walkthrough for a specific audience | Numbered steps, "you" voice, outcome-focused |
| **Feature catalog** (AGENTS.md) | Technical inventory for contributors and AI agents | Categorized sections, file paths, option tables |
| **Content pages** (index.md, champions/, roles/) | Public-facing site content | Prose with headings, links, and lists |

Rules that apply to all document types:

- Use heading levels in order (`#` then `##` then `###`). Do not skip levels.
- Open each document with a one-sentence purpose statement.
- Keep paragraphs short: three to five sentences is a good maximum.

---

## 3. Design foundations (site surface only)

These rules apply to the Eleventy site (`_includes/base.html`, `assets/styles.css`,
and Markdown content files). They do not govern plain Markdown documentation files.

### 3.0 Brand profile

**Active brand:** CivicActions

- **Brand site:** [civicactions.com](https://civicactions.com/)
- **Full style guide:** [civicactions-style-guide.readthedocs.io](https://civicactions-style-guide.readthedocs.io/en/latest/)
- **Writing style guide:** [guidebook.civicactions.com](https://guidebook.civicactions.com/en/latest/about-this-guidebook/writing-style-guide/)

**Brand personality:** Modern, clean, professional, friendly, optimistic.

**Brand values expressed in design:**
- Use clear hierarchy and ample white space (clean, professional).
- Use accessible color contrast and generous touch targets (humanity, inclusive).
- Keep layouts simple and scannable (friendly, optimistic).

### 3.1 Design tokens

The canonical values live in `assets/styles.css`. This table documents the design
intent aligned with the CivicActions brand palette.

For the full CivicActions palette including CMYK, RGB, and USWDS equivalents, see the
[Colors page in the CivicActions Style Guide](https://civicactions-style-guide.readthedocs.io/en/latest/brand/colors/).

#### CivicActions brand colors

| Token name | Hex | Role |
| :--- | :--- | :--- |
| CA red | `#d83933` | Primary brand red; calls to action |
| CA red secondary | `#8b0a03` | Hover state on red elements |
| CA blue dark | `#162e51` | Primary brand blue; headings, strong text |
| CA blue secondary | `#1a4480` | Links, interactive elements |
| CA blue light | `#73b3e7` | Supporting accents |
| CA gold | `#fa9441` | Warm accent; warnings, secondary highlights |

#### Site color tokens (current `assets/styles.css` values)

| Role | Value | Element |
| :--- | :--- | :--- |
| Header background | `#1f2937` | `header` |
| Header border | `#3b82f6` | Bottom border |
| Nav link | `#e5e7eb` | `nav a` |
| Nav hover / focus background | `#374151` | `nav a:hover`, `nav a:focus` |
| Nav active background | `#3b82f6` | `nav a[aria-current="page"]` |
| Body background | `#ffffff` | `body` |
| Body text | `#333333` | `body` |
| Heading h1 | `#1f2937` | `h1` |
| Heading h2 | `#374151` | `h2` |
| Link | `#3b82f6` | `a` (default) |
| Footer background | `#f9fafb` | `footer` |
| Footer text | `#6b7280` | `.footer-content` |
| Breadcrumb text | `#6b7280` | `.breadcrumb` |
| Editorial note background | `#f3f4f6` | `.editorial-notes` |
| Editorial note border | `#fbbf24` | Left border |
| Skip link background | `#000000` | `.skip-link:focus` |

### 3.2 Typography

- **Font stack:** `system-ui, -apple-system, sans-serif`
- **Line height:** `1.6` for body text.
- **Text alignment:** Left-aligned. Do not use `text-align: justify`.
- **Heading color:** `#1f2937` (h1), `#374151` (h2) in light mode.

### 3.3 Responsive design (mobile-first)

Write base CSS for the smallest screen first, then enhance with `min-width` queries.

| Layer | Breakpoint | Intent |
| :--- | :--- | :--- |
| **Mobile** | `0`–`767px` (base, no query) | Single-column navigation, touch targets ≥ 44 × 44 px |
| **Desktop** | `min-width: 768px` | Horizontal navigation, side panel layout |

- **Never block zoom.** The viewport meta tag must not include `maximum-scale=1`
  or `user-scalable=no`.

### 3.4 Component standards

#### Navigation

- Active page link uses `aria-current="page"` and is styled with the primary
  interactive color (`#3b82f6`).
- Hover and focus states share the same background (`#374151`) and white text.
- On mobile (under 768 px) navigation links stack vertically.

#### Skip link

- Visually hidden by default (`top: -40px`).
- Becomes visible on focus (`top: 6px`).
- Black background (`#000`) with white text, z-index `1000`.

#### Editorial notes

- Left-bordered panel (`4px solid #fbbf24`) on `#f3f4f6` background.
- Used to surface migration notes, editor assignments, and audit status.

#### Breadcrumb

- `<nav aria-label="Breadcrumb">` wrapping a sequence of links.
- Uses `›` separator character (not a decorative image).
- Current page is represented as plain text, not a link.

---

## 4. Accessibility and semantic logic

These rules apply to **both surfaces**. This project exists to support accessibility
practitioners; our outputs must meet or exceed the same standards we help others measure.

- Use heading levels in order: `h1` → `h2` → `h3`. Do not skip levels.
- Write descriptive link text. "Learn more about accessibility guides" — not "click here."
- Every image needs meaningful alt text. Decorative images use `alt=""`.
- Use `aria-label` on landmark elements when the role is ambiguous.
- Minimum color contrast: 4.5:1 for body text, 3:1 for large text and UI components.
- Do not convey information by color alone. Always pair color with a secondary indicator.
- Ensure touch and click targets are at least 44 × 44 pixels for all interactive elements.
- Use underlines only for links, not for decorative or non-link text.
- Include a `<main id="main-content">` element so users can skip directly to content.

See [ACCESSIBILITY.md](./ACCESSIBILITY.md) for the full accessibility commitment and
conformance target (WCAG 2.1 AA).

---

## 5. AI agent instructions

These rules apply to both surfaces. Agents editing documentation and agents
generating site content must follow all of them.

- Read [AGENTS.md](./AGENTS.md) before making any change to this repository.
- Identify which surface is being edited (site or documentation) and apply the correct
  rule set.
- Never override [ACCESSIBILITY.md](./ACCESSIBILITY.md) constraints.
- Use American English throughout.
- Keep changes scoped to the minimum necessary to fulfill the user's request.
- Verify all cross-file references resolve before committing.
- Use UTF-8 encoding only. Do not use smart quotes or Windows-1252 characters.
- Use project-relative paths (for example, `assets/styles.css`), never bare filenames.
- When modifying `assets/styles.css`, use or extend the color token table in
  Section 3.1. Do not hard-code hex values outside the token definitions.
- Add new documentation files to `.eleventyignore` so they are not processed as
  site pages.

---

## 6. Content governance

### 6.1 When to update this file

Update STYLES.md when you:

- Add a new CSS color value or change an existing value.
- Add a new UI component pattern (new color usage, new focus style, new layout pattern).
- Change the font stack or typographic scale.
- Add a new document type to the repository.
- Revise voice, tone, or word-choice guidance.

### 6.2 Cross-file consistency

| This file governs | Must stay in sync with |
| :--- | :--- |
| CSS color values | `assets/styles.css` |
| Color contrast ratios | `ACCESSIBILITY.md § Color and contrast` |
| Focus outline rules | `ACCESSIBILITY.md § Focus management` |
| Font stack | `assets/styles.css` `body` rule |

### 6.3 Versioning

This file does not carry its own version number. Its effective version is the git
commit SHA of the most recent change. To find the history of this file, run:

```bash
git log --follow STYLES.md
```
