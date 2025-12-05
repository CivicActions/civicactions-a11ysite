---
title: "FOSDEM: Accessibility and Open Source"
description: "Highlights from Mike Gifford's presentation at FOSDEM on the intersection of accessibility and open source software development."
layout: base
eleventyNavigation:
  key: FOSDEM Accessibility Open Source
  parent: News

# Migration Metadata
original_url: "https://accessibility.civicactions.com/posts/FOSDEM-ccessibility-OpenSource"
audit_category: "About"
audit_format: "Article"
audit_topic: "General accessibility"
audit_value: "2 Normal"
audit_notes: "No changes its perfect"
audit_action: "No changes its perfect"
content_status: "Migrate"
http_status: 301
migration_approved: true

# Article Metadata
publish_date: "2023-02-08"
author: "Mike Gifford"
tags: ["FOSDEM", "open source", "conference", "accessibility"]
---

# FOSDEM: Accessibility and Open Source

Highlights from Mike Gifford's presentation at FOSDEM 2023 on how open source software development can lead accessibility innovation and create more inclusive technology for everyone.

## About FOSDEM

FOSDEM (Free and Open Source Developers' European Meeting) is one of the world's largest gatherings of open source software developers, attracting thousands of contributors, maintainers, and enthusiasts to Brussels each February. The conference celebrates the collaborative spirit of open source development and showcases innovations across every area of technology.

### Why Accessibility Matters at FOSDEM

Open source software powers much of the digital infrastructure that people with disabilities depend on daily:
- **Operating systems** like Linux that support diverse assistive technologies
- **Web browsers** that implement accessibility standards and APIs
- **Development tools** that help create accessible applications and websites
- **Assistive technology** itself, with many tools being open source projects

## Presentation Overview: "Building Accessibility Into Open Source"

### The Accessibility Challenge in Open Source

Open source projects face unique accessibility challenges:
- **Volunteer contributors** may lack accessibility expertise or awareness
- **Limited resources** for comprehensive accessibility testing and validation
- **Rapid iteration** that can introduce accessibility regressions
- **Diverse user bases** with varying accessibility needs and assistive technology

### The Open Source Accessibility Advantage

However, open source also offers unique advantages for accessibility:
- **Transparency** allowing accessibility experts to identify and fix issues
- **Community contributions** from users with disabilities who understand real needs
- **Shared knowledge** with accessibility improvements benefiting multiple projects
- **Innovation speed** enabling rapid development of new accessibility solutions

## Key Themes from the Presentation

### 1. Accessibility as a Quality Issue

Accessibility shouldn't be treated as an optional feature but as a fundamental aspect of software quality:

#### Code Quality Parallel
Just as we use linters for code quality:
```bash
# Traditional code quality
eslint src/
prettier --check src/

# Accessibility quality  
axe-core src/
pa11y-ci --sitemap https://yoursite.com/sitemap.xml
```

#### Testing Integration
Accessibility testing should be part of standard development workflows:
- **Unit tests** that verify ARIA attributes and keyboard interactions
- **Integration tests** that validate screen reader compatibility
- **Visual regression tests** that catch color contrast and layout issues
- **User acceptance tests** that include people using assistive technology

### 2. Community-Driven Accessibility

Open source communities can drive accessibility innovation:

#### User Contributions
People with disabilities are often the most motivated contributors to accessibility improvements:
- **Bug reports** from real users identifying accessibility barriers
- **Feature requests** for assistive technology compatibility
- **Code contributions** from developers who use accessibility features daily
- **Documentation improvements** making accessibility guidance more practical

#### Mentorship and Education
Experienced accessibility contributors can guide newcomers:
- **Accessibility reviews** in pull request processes
- **Educational comments** explaining accessibility principles and techniques
- **Shared resources** like accessibility testing scripts and documentation
- **Cross-project collaboration** sharing solutions between related projects

### 3. Tools and Infrastructure

Open source accessibility requires good tooling:

#### Development Tools
- **Linting rules** for accessibility (eslint-plugin-jsx-a11y, axe-linter)
- **Browser extensions** for real-time accessibility testing (axe DevTools)
- **Automated testing** frameworks (Pa11y, axe-core, Lighthouse)
- **Design tools** with accessibility plugins (Figma a11y, Stark)

#### CI/CD Integration
Making accessibility testing as easy as running tests:
```yaml
name: Accessibility Testing
on: [push, pull_request]
jobs:
  accessibility:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: npm ci
      - name: Build project  
        run: npm run build
      - name: Run accessibility tests
        run: npm run test:a11y
```

### 4. Government and Open Source Accessibility

Government adoption of open source creates opportunities:

#### Policy Influence
Government accessibility requirements drive open source improvements:
- **Section 508 compliance** motivating accessibility features in open source projects
- **Procurement requirements** creating market demand for accessible open source solutions
- **Standards development** with government agencies participating in accessibility specification work
- **Public sector collaboration** sharing accessibility improvements across agencies

#### Resource Sharing
Government agencies can contribute to open source accessibility:
- **Funding accessibility work** through grants and contracts
- **Contributing expertise** from government accessibility professionals
- **Sharing solutions** that benefit both public and private sectors
- **Policy coordination** aligning government needs with open source development

## Case Studies Presented

### 1. Drupal Accessibility Initiative

How the Drupal community has systematically improved accessibility:
- **Accessibility team** coordinating improvements across the project
- **Core accessibility** built into Drupal's administrative interface and output
- **Contributed modules** evaluated and improved for accessibility compliance
- **Community training** at conferences and through online resources

#### Impact Metrics
- **WCAG 2.1 AA compliance** for Drupal core administrative interface
- **Accessibility testing** integrated into Drupal's continuous integration
- **Government adoption** with agencies choosing Drupal partly for accessibility features
- **Community growth** with more contributors focused on accessibility

### 2. axe-core Development

How Deque's open source accessibility testing engine benefits everyone:
- **Free accessibility testing** available to all developers regardless of budget
- **Community contributions** improving test accuracy and coverage
- **Widespread adoption** making accessibility testing more common
- **Standards alignment** keeping pace with evolving accessibility guidelines

#### Ecosystem Benefits
- **Multiple implementations** (axe DevTools, axe-cli, integrations with testing frameworks)
- **Language bindings** for JavaScript, Python, Java, and other platforms
- **CI/CD integration** making automated accessibility testing standard practice
- **Education impact** helping developers learn accessibility through tool feedback

### 3. NVDA Screen Reader

The power of open source assistive technology:
- **Community development** by users who understand screen reader needs
- **Rapid innovation** with new features and improvements released frequently
- **Global accessibility** with translations and international contributions
- **Cost accessibility** providing free access to essential assistive technology

#### Government Impact
- **Public sector adoption** reducing costs for government accessibility
- **Educational use** enabling accessibility training without licensing costs
- **Development testing** allowing developers to test with real screen reader technology
- **Standards influence** with NVDA development informing accessibility specifications

## Key Recommendations from the Presentation

### For Open Source Projects

#### Start with Foundations
1. **Add accessibility linting** to your development process
2. **Include accessibility in contributing guidelines** with examples and resources  
3. **Test with screen readers** during development, not just before release
4. **Document accessibility decisions** explaining choices for future contributors

#### Build Community
1. **Welcome accessibility contributors** regardless of technical background
2. **Provide mentorship** for contributors learning accessibility
3. **Share knowledge** through documentation, blog posts, and conference talks
4. **Collaborate with other projects** on shared accessibility challenges

#### Maintain Quality
1. **Automate accessibility testing** in continuous integration pipelines
2. **Monitor for regressions** with regular accessibility audits
3. **Respond quickly** to accessibility bug reports and user feedback
4. **Plan accessibility** in feature development, not as an afterthought

### For Government Agencies

#### Support Open Source Accessibility
1. **Contribute to projects** you use through funding, development, or expertise
2. **Share accessibility solutions** that could benefit other organizations
3. **Participate in standards development** to align government and community needs
4. **Advocate for accessibility** in procurement and policy decisions

#### Build Internal Capability
1. **Train staff** on open source accessibility tools and practices
2. **Develop expertise** in accessibility testing and validation
3. **Create communities of practice** for sharing knowledge across agencies
4. **Document lessons learned** for future projects and other organizations

## Audience Response and Questions

### Developer Engagement
FOSDEM attendees were particularly interested in:
- **Practical tools** they could immediately use in their projects
- **Getting started guidance** for projects without existing accessibility expertise
- **Resource recommendations** for learning accessibility development practices
- **Community connections** with other developers working on accessibility

### Accessibility Advocacy
Questions revealed growing awareness:
- **Legal requirements** and how they apply to open source projects
- **User impact** understanding how accessibility barriers affect real people
- **Testing approaches** balancing automated tools with manual validation
- **Sustainability** maintaining accessibility improvements over time

## Follow-Up Resources

### Tools Demonstrated
- **axe DevTools**: Browser extension for accessibility testing
- **Pa11y CLI**: Command-line accessibility testing tool
- **NVDA screen reader**: Free, open source screen reader for testing
- **Lighthouse**: Google's accessibility auditing tool

### Learning Resources
- **Web Accessibility Initiative (WAI)**: W3C's accessibility guidance and standards
- **Accessibility Developer Guide**: Practical implementation guidance
- **Inclusive Design Principles**: Microsoft's accessibility design guidance
- **Government accessibility**: Section 508 and international standards

### Community Connections
- **A11y Slack**: Online community for accessibility discussions
- **IAAP**: International Association of Accessibility Professionals
- **Local meetups**: Accessibility groups in cities worldwide
- **Conference speaking**: Opportunities to share accessibility knowledge

## Impact and Next Steps

### Conference Outcomes
The presentation sparked several follow-up initiatives:
- **New project accessibility audits** by FOSDEM attendees
- **Collaboration connections** between accessibility professionals and open source maintainers
- **Resource sharing** with presentation materials adapted for different communities
- **Policy discussions** about government support for open source accessibility

### Ongoing Work
CivicActions continues building on FOSDEM connections:
- **Open source contributions** to accessibility testing tools and documentation
- **Community building** through conferences, meetups, and online collaboration
- **Government advocacy** for policies supporting open source accessibility
- **Training development** helping more developers learn accessibility practices

## Presentation Materials

### Slides and Resources
- **Presentation slides**: [Available on GitHub](https://github.com/civicactions/fosdem-2023-accessibility)
- **Demo code**: Examples of accessibility testing integration
- **Resource links**: Curated list of accessibility tools and learning materials
- **Community contacts**: Connections for accessibility questions and collaboration

### Video Recording
The presentation was recorded and is available:
- **FOSDEM video archive**: Official conference recording
- **Accessibility-focused edit**: Shortened version highlighting key points
- **Transcript**: Full text for accessibility and searchability
- **Presentation notes**: Additional context and resources

## Connect and Continue the Conversation

Interested in open source accessibility or government technology collaboration?

- **GitHub**: [CivicActions open source work](https://github.com/civicactions)
- **Speaking opportunities**: [Contact Mike Gifford](/about/people/mike-gifford/) for conference presentations
- **Consulting services**: [CivicActions accessibility practice](/about/)
- **Community participation**: [Get accessibility help](/about/get-accessibility-help/)

FOSDEM 2023 demonstrated the growing momentum behind open source accessibility. By working together, the global development community can create technology that's truly inclusive and accessible to everyone.

---

**Editorial Notes:**
- Format: Conference presentation summary with practical guidance and community building focus
- Priority: Normal value - demonstrates thought leadership and community engagement
- Action: No changes needed - content preserved as-is per audit recommendation
- Author: Mike Gifford, establishing expertise in open source accessibility advocacy