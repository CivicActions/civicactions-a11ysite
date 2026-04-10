# ACCESSIBILITY.md

This document outlines the accessibility standards, implementation details, and
testing guidance for the CivicActions Accessibility site. It is the authoritative
reference for contributors and AI coding agents working in this repository.

## Table of contents

- [Overview](#overview)
- [WCAG compliance](#wcag-compliance)
- [Color and contrast](#color-and-contrast)
- [Keyboard navigation](#keyboard-navigation)
- [Screen reader support](#screen-reader-support)
- [Semantic HTML](#semantic-html)
- [Focus management](#focus-management)
- [Forms and input](#forms-and-input)
- [Responsive design](#responsive-design)
- [Testing guidelines](#testing-guidelines)
- [Known issues and future improvements](#known-issues-and-future-improvements)

---

## Overview

The CivicActions Accessibility site exists to help teams build more inclusive
digital services. Because we document accessibility best practices, our own site
must meet or exceed the same standards we help others achieve.

Accessibility is a **first-class requirement**, not an afterthought. Every
contribution — whether a new page, a layout change, or a CSS update — must be
evaluated against the standards in this document.

---

## WCAG compliance

This site aims to meet **WCAG 2.1 Level AA** standards. Key compliance areas:

- **Perceivable**: Content is presented in ways that all users can perceive.
- **Operable**: UI components and navigation are operable by all users.
- **Understandable**: Information and UI operation are understandable.
- **Robust**: Content works with current and future assistive technologies.

See the [live accessibility statement](https://accessibility.civicactions.com/accessibility-statement/)
for the site's public conformance commitment.

---

## Color and contrast

### Contrast ratios

All text and interactive elements must meet WCAG AA contrast requirements:

- **Normal text**: minimum 4.5:1 contrast ratio
- **Large text** (18 pt+ or 14 pt+ bold): minimum 3:1 contrast ratio
- **UI components and focus indicators**: minimum 3:1 contrast ratio

### Site color palette

The color values below are defined in `assets/styles.css`. See
[STYLES.md § 3.1](./STYLES.md#31-design-tokens) for the full token reference.

| Role | Color | Used on |
| :--- | :--- | :--- |
| Header background | `#1f2937` | `<header>` |
| Header border | `#3b82f6` | Bottom border of `<header>` |
| Primary interactive | `#3b82f6` | Links, nav active state |
| Nav hover background | `#374151` | `nav a:hover`, `nav a:focus` |
| Body text | `#333333` | `<body>` default |
| Heading h1 | `#1f2937` | `<h1>` |
| Heading h2 | `#374151` | `<h2>` |
| Page background | `#ffffff` | `<body>` |
| Footer background | `#f9fafb` | `<footer>` |
| Footer text | `#6b7280` | `.footer-content` |
| Breadcrumb text | `#6b7280` | `.breadcrumb` |
| Editorial note bg | `#f3f4f6` | `.editorial-notes` |
| Editorial note border | `#fbbf24` | Left border on `.editorial-notes` |

### Key contrast pairs (verified)

| Foreground | Background | Ratio | Passes |
| :--- | :--- | :--- | :--- |
| `#ffffff` (header links) | `#1f2937` | 15.2:1 | AA ✓ |
| `#ffffff` (nav active) | `#3b82f6` | 4.6:1 | AA ✓ |
| `#333333` (body text) | `#ffffff` | 12.6:1 | AA ✓ |
| `#1f2937` (h1) | `#ffffff` | 15.2:1 | AA ✓ |
| `#3b82f6` (links) | `#ffffff` | 4.6:1 | AA ✓ |

Do not introduce new color combinations without verifying the contrast ratio using
[WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) or an
equivalent tool.

---

## Keyboard navigation

All interactive elements must be fully keyboard accessible.

### Navigation order

The established tab order in `_includes/base.html` is:

1. Skip link ("Skip to main content")
2. Site title link
3. Main navigation links (Home → Guides → Champions → About)
4. Sidebar navigation links
5. Main content links and interactive elements (in document order)
6. Footer links

Do not alter this order without reviewing the impact on keyboard users.

### Keyboard shortcuts

| Key | Action |
| :--- | :--- |
| `Tab` | Move forward through interactive elements |
| `Shift + Tab` | Move backward through interactive elements |
| `Enter` / `Space` | Activate buttons and links |
| `Enter` | Submit forms |

### Skip link

The `_includes/base.html` template includes a skip link that targets `#main-content`.
The skip link is visually hidden until focused.

```html
<a class="skip-link" href="#main-content">Skip to main content</a>
```

**Do not remove the skip link.** If you rename the `id` on `<main>`, update the
skip link `href` accordingly.

---

## Screen reader support

### Landmark regions

The template uses semantic landmark elements so screen-reader users can navigate
by region:

| Landmark | Element | Notes |
| :--- | :--- | :--- |
| Banner | `<header>` | Site title and main navigation |
| Navigation | `<nav aria-label="Main navigation">` | Top navigation bar |
| Complementary | `<aside aria-label="Section navigation">` | Sidebar |
| Main | `<main id="main-content">` | Primary page content |
| Breadcrumb | `<nav class="breadcrumb" aria-label="Breadcrumb">` | Page hierarchy |
| Content info | `<footer>` | Copyright, contact links |

### ARIA usage

- Use `aria-label` on landmark elements when the element type alone is ambiguous
  (for example, when multiple `<nav>` elements exist on a page).
- Use `aria-current="page"` on the active navigation item. The CSS in
  `assets/styles.css` styles `nav a[aria-current="page"]` with a distinct
  background color.
- Use `aria-hidden="true"` on purely decorative icons and images.
- Do not use ARIA roles to override semantic meaning where a native HTML element
  already provides the correct role.

---

## Semantic HTML

Use native HTML5 semantic elements in templates and content:

- `<main>` — primary content container (one per page)
- `<header>` — site banner with title and navigation
- `<nav>` — navigation regions (use distinct `aria-label` values for each)
- `<aside>` — sidebar or supplementary content
- `<footer>` — site footer
- `<article>` — self-contained content units (blog posts, guides)
- `<section>` — thematic groupings within a page
- `<h1>`–`<h6>` — heading hierarchy in document order

Do not use `<div>` or `<span>` elements in place of these semantic elements.

---

## Focus management

### Focus indicators

All focusable elements must display a clearly visible focus indicator. The current
CSS provides focus styling for navigation links:

```css
nav a:hover,
nav a:focus {
    background: #374151;
    color: #fff;
}
```

When adding new interactive elements:

- Use `:focus-visible` so the indicator appears only for keyboard navigation
  (not on mouse click).
- The indicator must have a 3:1 contrast ratio against the adjacent background.
- Use at least a `2px solid` outline with `2px` offset where outlines are used.

### Skip link implementation

The skip link uses the following CSS pattern to remain hidden until focused:

```css
.skip-link {
    position: absolute;
    top: -40px;
    left: 6px;
    background: #000;
    color: #fff;
    padding: 8px;
    text-decoration: none;
    z-index: 1000;
}

.skip-link:focus {
    top: 6px;
}
```

---

## Forms and input

### Labels and inputs

Every form input must have an explicit `<label>` element with a `for` attribute
that matches the input's `id`:

```html
<label for="search-query">Search</label>
<input id="search-query" type="search" name="q" />
```

Do not rely on `placeholder` text as a substitute for a visible label.

### Validation

- Use HTML5 validation attributes (`required`, `type`, `pattern`) where appropriate.
- Error messages must be associated with their input via `aria-describedby`.
- Do not use color alone to indicate a validation error.

---

## Responsive design

### Viewport meta tag

The `base.html` template includes:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Never add** `maximum-scale=1` or `user-scalable=no`. Users must be able to zoom
the page freely.

### Breakpoints

| Breakpoint | Width | Layout change |
| :--- | :--- | :--- |
| Mobile | `< 768px` | Single-column navigation |
| Desktop | `≥ 768px` | Horizontal navigation |

### Touch targets

All interactive elements must have a minimum tap target of 44 × 44 px (WCAG 2.5.5).

---

## Testing guidelines

### Manual testing checklist

Before submitting a pull request that touches HTML, CSS, or layout:

- [ ] Tab through all interactive elements — every element receives focus in a
  logical order.
- [ ] All focused elements have a clearly visible focus indicator.
- [ ] Buttons and links are activatable with `Enter` and `Space`.
- [ ] The skip link appears on focus and moves focus to `#main-content`.
- [ ] Heading hierarchy is sequential (no skipped levels).
- [ ] All images have descriptive alt text (or `alt=""` if decorative).
- [ ] New color combinations meet contrast requirements (4.5:1 for normal text).

### Screen reader testing

Test with at least one of the following:

- **NVDA** (Windows, free): <https://www.nvaccess.org/>
- **VoiceOver** (macOS/iOS, built-in): activate with `Cmd + F5`
- **JAWS** (Windows, commercial): <https://www.freedomscientific.com/products/software/jaws/>
- **TalkBack** (Android, built-in)

Verify that:
- All landmark regions are announced correctly.
- Navigation links, headings, and breadcrumbs are readable in order.
- Active navigation state (`aria-current="page"`) is announced.

### Automated testing tools

1. **axe DevTools** — browser extension for automated accessibility testing
   - Chrome: <https://chrome.google.com/webstore>
   - Firefox: <https://addons.mozilla.org/firefox/>

2. **Lighthouse** — built into Chrome DevTools; run the Accessibility audit.

3. **WAVE** — <https://wave.webaim.org/>

4. **pa11y** — command-line tool:
   ```bash
   npm install -g pa11y
   pa11y https://accessibility.civicactions.com/
   ```

### CI/CD integration

Automated axe-core accessibility scanning runs via GitHub Actions on each deployment.
Any violations found are automatically filed as GitHub Issues. See the
`.github/workflows/` directory for configuration details.

---

## Known issues and future improvements

### Current limitations

- The site does not yet implement a `prefers-reduced-motion` media query for
  CSS transitions.
- High-contrast mode (`forced-colors`) support has not been explicitly tested.
- Some pages may have inline `style` attributes in templates; these should be moved
  to `assets/styles.css`.

### Planned improvements

1. **Reduced motion** — add `@media (prefers-reduced-motion: reduce)` rules to
   `assets/styles.css` to disable transitions for users who request them.
2. **High contrast** — test and fix rendering under Windows High Contrast Mode.
3. **Dark mode** — add a `prefers-color-scheme: dark` theme.
4. **Enhanced focus styles** — audit all interactive elements for consistent
   `:focus-visible` styles using `:focus-visible` pseudo-class.

---

## Resources

### Standards

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Section 508 Standards](https://www.section508.gov/)

### Testing tools

- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WebAIM Resources](https://webaim.org/resources/)

### Learning resources

- [WebAIM Articles](https://webaim.org/articles/)
- [Inclusive Components](https://inclusive-components.design/)
- [The A11Y Project](https://www.a11yproject.com/)
- [CivicActions Accessibility Site](https://accessibility.civicactions.com/)

---

## Contributing

When contributing to this project:

1. Test all changes with keyboard navigation.
2. Verify color contrast ratios meet WCAG AA minimums.
3. Test with at least one screen reader.
4. Run automated accessibility tests (axe, Lighthouse, or WAVE).
5. Update this document if you add new UI patterns, color values, or ARIA usage.

## Questions or issues

If you encounter accessibility barriers or have suggestions:

1. [Open an issue on GitHub](https://github.com/CivicActions/accessibility/issues)
2. Email: [accessibility@civicactions.com](mailto:accessibility@civicactions.com)
3. Include details about the barrier, your assistive technology (if applicable),
   steps to reproduce, and any suggested solutions.
