---
title: "Automated Testing"
description: "CivicActions Accessibility Site: A collection of resources about digital accessibility and how it aligns with open source, CivicTech and Digital Transformation."
layout: base
eleventyNavigation:
  key: Automated Testing
  parent: Accessibility Guides

# Migration Metadata
original_url: "https://accessibility.civicactions.com/playbook/automated-testing"
audit_category: "Accessibility Guides"
audit_format: "Guide"
audit_topic: "Automated testing"
audit_value: "1 High"
audit_action: "Update in place now"
content_status: "Migrate"
editor_assigned: ""
editor_status: "TRUE"
readability_score: "Hard"
migration_approved: true
original_author: "Mike, Daniel"

# Editor Notes
recommendations: "This is close. Recommend applying guide format that answers what is automated testing and how to set it up. (see Plain Language for a good starting point on the format.)"
---

# Implement Automated Testing

A comprehensive guide to setting up automated accessibility testing in your development workflow.

## What is Automated Accessibility Testing?

Automated testing uses tools to scan your code and identify accessibility issues during development. While it can't catch everything, it finds about 30-40% of accessibility issues automatically.

## Why Automate?

- **Early detection** of accessibility issues
- **Consistent testing** across your codebase  
- **Cost effective** - catch issues before they reach users
- **Continuous integration** with your development workflow

## Getting Started

### Essential Tools

1. **axe-core** - Industry standard accessibility engine
2. **pa11y** - Command line accessibility testing
3. **Lighthouse** - Built into Chrome DevTools
4. **GitHub Actions** - For continuous integration

### Basic Setup

```bash
# Install pa11y globally
npm install -g pa11y

# Test a single page
pa11y https://example.com

# Test with axe-core
pa11y --runner axe https://example.com
```

### Integration Workflow

1. **Local development** - Run tests before commits
2. **Pull request checks** - Automated testing in CI
3. **Production monitoring** - Regular scans of live sites
4. **Reporting** - Track progress over time

## Advanced Configuration

Configure testing for your specific needs, including custom rules, multiple browsers, and integration with existing development tools.

---

**Editorial Notes:**
- Original authors: Mike, Daniel
- Assigned editor: Daniel Mundra (completed)
- Format: Guide (step-by-step implementation)
- Priority: High value content
- Action: Apply guide format answering "what" and "how to set up"