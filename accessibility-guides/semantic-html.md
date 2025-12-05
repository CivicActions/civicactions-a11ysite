---
title: "Semantic HTML"
description: "CivicActions Accessibility Site: A collection of resources about digital accessibility and how it aligns with open source, CivicTech and Digital Transformation."
layout: base
eleventyNavigation:
  key: Semantic HTML
  parent: Accessibility Guides

# Migration Metadata
original_url: "https://accessibility.civicactions.com/guide/semantic-html"
audit_category: "Accessibility Guides"
audit_format: "Detail"
audit_topic: "General accessibility"
audit_value: "2 Normal"
audit_notes: "Redirects"
audit_action: "Update in place now"
content_status: "Migrate"

editor_status: "TRUE"
readability_score: "Normal"
migration_approved: true
original_author: "Jennifer"

# Editor Notes
recommendations: "Suggest reframing this page as a way to prevent accessibility issues or cut down on them out of the gate. Talk about native element semantics and how they map to browser accessibility APIs, doing a lot of the hard work for you. Mention first rule of ARIA. Mention HTML Validator as first line of defence against accessibility errors."
---

# Semantic HTML

Using proper HTML elements to prevent accessibility issues and build inclusive experiences from the ground up.

## Why Semantic HTML Matters for Accessibility

Semantic HTML is your first and most powerful line of defense against accessibility issues. When you use the right HTML elements for their intended purpose, you get accessibility features for free through the browser's built-in accessibility APIs.

## The Power of Native Semantics

### Browser APIs Do the Heavy Lifting
When you use semantic HTML elements, browsers automatically:
- **Communicate roles** to assistive technologies (button, heading, list, etc.)
- **Provide keyboard interactions** (buttons can be activated with Space/Enter)
- **Establish relationships** between elements (labels and form controls)
- **Create navigation shortcuts** (headings become screen reader navigation points)

### The First Rule of ARIA
**"If you can use a native HTML element or attribute with the semantics and behavior you require already built in, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, then do so."**

This means: `<button>` is better than `<div role="button">`

## Essential Semantic Elements

### Headings (h1-h6)
**Purpose**: Create document outline and navigation structure
```html
<h1>Main Page Title</h1>
  <h2>Major Section</h2>
    <h3>Subsection</h3>
    <h3>Another Subsection</h3>
  <h2>Another Major Section</h2>
```

**Accessibility benefit**: Screen readers use headings to navigate and understand content structure

### Buttons and Links
**Use buttons for actions**:
```html
<button type="submit">Save Changes</button>
<button onclick="openDialog()">Edit Profile</button>
```

**Use links for navigation**:
```html
<a href="/contact">Contact Us</a>
<a href="#main-content">Skip to content</a>
```

**Accessibility benefit**: Correct expectations for keyboard users and screen reader users

### Lists (ul, ol, dl)
**For grouped information**:
```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

**Accessibility benefit**: Screen readers announce list length and current position

### Form Elements
**Proper labeling**:
```html
<label for="email">Email Address</label>
<input type="email" id="email" required>

<fieldset>
  <legend>Preferred Contact Method</legend>
  <input type="radio" id="email-pref" name="contact" value="email">
  <label for="email-pref">Email</label>
  <input type="radio" id="phone-pref" name="contact" value="phone">
  <label for="phone-pref">Phone</label>
</fieldset>
```

**Accessibility benefit**: Clear relationships between labels and controls

### Landmarks (main, nav, header, footer, section, article)
**Document structure**:
```html
<header>
  <nav aria-label="Main navigation">...</nav>
</header>
<main>
  <article>
    <h1>Article Title</h1>
    <section>
      <h2>Section Title</h2>
    </section>
  </article>
</main>
<footer>...</footer>
```

**Accessibility benefit**: Assistive technology navigation shortcuts

## Validation as Accessibility Testing

### HTML Validator - Your First Line of Defense
**Why validation matters**:
- Invalid HTML can break assistive technology parsing
- Semantic errors often indicate accessibility problems
- Validation catches issues before they reach users

**Recommended validators**:
- [W3C Markup Validator](https://validator.w3.org/) - The gold standard
- [Nu Html Checker](https://validator.w3.org/nu/) - Modern HTML5 validation
- Browser DevTools - Built-in validation warnings

### Common Validation Errors That Impact Accessibility
- **Missing alt attributes** on images
- **Duplicate IDs** (breaks label/input relationships)
- **Improperly nested elements** (can break screen reader parsing)
- **Missing required attributes** (lang, labels, etc.)

## Implementation Strategy

### Start with Structure
1. **Use proper document outline** with heading hierarchy
2. **Add semantic landmarks** (header, nav, main, footer)
3. **Structure content** with lists, paragraphs, and sections
4. **Validate early and often** to catch issues immediately

### Enhance Progressively
1. **Add ARIA only when needed** - start with semantic HTML
2. **Test with keyboard navigation** to verify interactions work
3. **Use accessibility testing tools** to identify gaps
4. **Test with real assistive technology** when possible

### Common Pitfalls to Avoid
- **Don't use divs and spans** when semantic elements exist
- **Don't skip heading levels** (h1 → h3 without h2)
- **Don't remove focus indicators** without providing alternatives  
- **Don't rely only on color** to convey information

## Tools for Semantic HTML Success

### Development Tools
- **HTML validators** for catching syntax and semantic errors
- **Browser accessibility inspectors** for reviewing element roles
- **axe DevTools** for comprehensive accessibility scanning
- **Lighthouse accessibility audit** built into Chrome DevTools

### Testing Approaches
- **Keyboard-only navigation** to verify semantic interactions
- **Screen reader testing** to ensure proper element communication
- **Automated accessibility testing** integrated into development workflow
- **Manual code review** focusing on semantic element choices

---

**Editorial Notes:**
- Original author: Jennifer
- Format: Detail page (comprehensive implementation guide)
- Priority: Normal value content
- Memorial: Laura's contributions to accessibility fundamentals continue to guide inclusive development
- Focus: Prevention-focused approach emphasizing native HTML benefits and validation