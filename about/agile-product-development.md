---
title: "Agile Product Development with Accessibility"
description: "How to integrate accessibility into agile development processes and sprint planning."
layout: base
eleventyNavigation:
  key: Agile Product Development
  parent: About

# Migration Metadata
original_url: "https://accessibility.civicactions.com/agile"
audit_category: "About"
audit_format: "Detail"
audit_topic: "Methods"
audit_value: "2 Normal"
audit_notes: "Links to internal page."
audit_action: "Combine with existing"
content_status: "Migrate"
http_status: 301
migration_approved: true

# Editor Notes  
recommendations: "Combined content about agile accessibility approaches with practical implementation guidance"
---

# Agile Product Development with Accessibility

How to integrate accessibility considerations into agile development workflows, sprint planning, and product delivery processes.

## Accessibility in Agile Principles

### Shift Left Approach
**Integrate accessibility early** in the development cycle rather than treating it as a late-stage requirement:
- **Product planning** includes accessibility user stories and acceptance criteria
- **Design sprints** incorporate inclusive design principles from the start
- **Development sprints** include accessibility testing and validation
- **Quality assurance** verifies accessibility alongside functionality

### Continuous Integration
- **Automated testing** catches accessibility issues in every build
- **Manual testing** validates user experience with assistive technology
- **Regular audits** ensure accessibility standards are maintained
- **User feedback** from people with disabilities informs iterations

## Sprint Planning for Accessibility

### User Story Development
Write accessibility requirements into user stories:

**Example**: "As a keyboard-only user, I need to navigate the checkout process using only Tab, Enter, and arrow keys so I can complete purchases independently."

**Acceptance Criteria**:
- All interactive elements are keyboard accessible
- Focus indicators are clearly visible
- Tab order follows logical sequence
- Screen reader announcements are meaningful

### Definition of Done
Include accessibility criteria in your Definition of Done:
- ✅ **Automated tests** pass (axe-core, Pa11y)
- ✅ **Keyboard navigation** works completely
- ✅ **Screen reader testing** confirms usable experience
- ✅ **Color contrast** meets WCAG 2.1 AA standards
- ✅ **Form validation** works with assistive technology

### Estimation and Velocity
- **Accessibility tasks** should be estimated alongside feature work
- **Testing time** includes both automated and manual accessibility validation
- **Learning curve** accounts for team accessibility skill development
- **Velocity tracking** includes accessibility debt and improvements

## Team Roles and Responsibilities

### Product Owner
- **Prioritize accessibility** in product backlog
- **Define acceptance criteria** that include accessibility requirements
- **Advocate with stakeholders** for accessibility investment
- **Review and approve** accessibility-focused user stories

### Scrum Master
- **Facilitate accessibility discussions** in sprint planning and retrospectives
- **Remove impediments** to accessibility implementation
- **Track accessibility metrics** as part of team performance
- **Coordinate accessibility training** and knowledge sharing

### Development Team
- **Implement accessible code** following semantic HTML and ARIA best practices
- **Write accessibility tests** as part of test-driven development
- **Review code** for accessibility compliance
- **Collaborate with designers** on inclusive interaction patterns

### UX/Design Team
- **Research with diverse users** including people who use assistive technology
- **Design inclusive interfaces** that work across abilities and technologies
- **Create accessible prototypes** for testing and validation
- **Document interaction patterns** with accessibility specifications

## Sprint Activities

### Sprint Planning
- **Review accessibility debt** from previous sprints
- **Identify accessibility risks** in upcoming features
- **Estimate accessibility work** as part of story pointing
- **Plan accessibility testing** activities and resources

### Daily Standups
- **Surface accessibility blockers** that need team attention
- **Share accessibility discoveries** and learning opportunities
- **Coordinate accessibility reviews** and testing activities
- **Update on accessibility tool and process improvements**

### Sprint Reviews
- **Demo accessibility features** using assistive technology
- **Gather feedback** from users with disabilities when possible
- **Showcase accessibility improvements** and metrics
- **Identify accessibility enhancement opportunities** for future sprints

### Retrospectives
- **Reflect on accessibility practices** and team capability
- **Identify process improvements** for better accessibility integration
- **Celebrate accessibility wins** and learning achievements
- **Plan accessibility skill development** activities

## Tools and Processes

### Development Tools
- **Linting rules** catch accessibility issues during coding (eslint-plugin-jsx-a11y)
- **Browser extensions** provide in-context accessibility checking (axe DevTools)
- **Automated testing** runs accessibility audits in CI/CD pipeline
- **Design tools** include accessibility plugins and color contrast checkers

### Testing Integration
- **Unit tests** verify ARIA attributes and keyboard interactions
- **Integration tests** validate complete user workflows with assistive technology
- **Visual regression testing** catches color contrast and layout accessibility issues
- **User acceptance testing** includes people who use assistive technology

### Documentation
- **Accessibility playbook** guides team implementation decisions
- **Component library** documents accessible usage patterns
- **Testing protocols** ensure consistent accessibility validation
- **Lessons learned** capture accessibility insights for future reference

## Managing Accessibility Debt

### Identification and Tracking
- **Accessibility audits** identify existing issues and technical debt
- **Issue prioritization** considers user impact and implementation complexity
- **Debt visualization** makes accessibility work visible in sprint planning
- **Progress tracking** shows accessibility improvement over time

### Remediation Approach
- **Critical fixes** address issues blocking assistive technology users
- **Incremental improvements** enhance accessibility in each sprint
- **Systematic refactoring** updates components to accessible patterns
- **Prevention measures** stop new accessibility debt from accumulating

## Measuring Success

### Sprint Metrics
- **Accessibility test coverage** shows validation completeness
- **Issue discovery rate** indicates testing effectiveness
- **Remediation velocity** tracks team improvement capability
- **User satisfaction** from accessibility testing and feedback

### Product Metrics
- **WCAG compliance** measured through automated and manual audits
- **User task completion** rates for people using assistive technology
- **Support requests** related to accessibility barriers
- **Feature adoption** among users with disabilities

## CivicActions Approach

Our agile accessibility practices include:
- **Accessibility champions** embedded in each scrum team
- **Regular accessibility training** as part of professional development
- **User research** that includes people with disabilities
- **Automated testing** integrated into CI/CD pipelines
- **Cross-team collaboration** on accessibility standards and practices

### Government Context
For government clients, we ensure:
- **Section 508 compliance** built into acceptance criteria
- **Procurement language** includes accessibility requirements
- **Vendor coordination** on accessibility implementation
- **Ongoing monitoring** maintains compliance throughout product lifecycle

---

**Editorial Notes:**
- Format: Detail page with comprehensive agile accessibility guidance
- Priority: Normal value - foundational process content
- Action: Combined multiple agile-related pages per audit recommendations
- Content covers practical implementation for government and private sector contexts