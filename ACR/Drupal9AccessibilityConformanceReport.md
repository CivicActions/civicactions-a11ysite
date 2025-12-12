---
title: "Drupal 9 Accessibility Conformance Report"
description: "Summary of CivicActions Drupal 9 site accessibility conformance against WCAG 2.1 and Section 508."
layout: base
eleventyNavigation:
  key: "Drupal 9 ACR"
  parent: "Accessibility Conformance Reports"
---

## Overview

This Accessibility Conformance Report (ACR) summarizes how our Drupal 9 implementation aligns with WCAG 2.1 Level AA and Section 508. It documents testing outcomes for templates, components, and editorial workflows.

- **Scope:** Drupal 9 site build using the CivicActions accessibility starter, including authenticated and unauthenticated flows.
- **Methodology:** Manual keyboard/screen-reader checks (NVDA + VoiceOver), automated scans (axe + pa11y-ci), and code review for semantic HTML and ARIA.
- **Status:** Meets or partially meets most WCAG 2.1 AA success criteria; minor issues noted for complex data tables and embedded media captions.

## Key findings

- Core navigation, forms, and authentication flows meet keyboard and screen reader expectations.
- Color palettes pass WCAG contrast thresholds; focus indicators are present and visible.
- Heading structure and landmarks are defined for all templated pages.
- Outstanding items: add expanded caption coverage for legacy videos; document a repeatable process for auditing third-party widgets.

For a signed copy or detailed test results, contact [accessibility@civicactions.com](mailto:accessibility@civicactions.com).
