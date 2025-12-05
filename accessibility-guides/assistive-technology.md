---
title: "Assistive Technology Testing"
description: "CivicActions Accessibility Site: A collection of resources about digital accessibility and how it aligns with open source, CivicTech and Digital Transformation."
layout: base
eleventyNavigation:
  key: Assistive Technology
  parent: Accessibility Guides

# Migration Metadata
original_url: "https://accessibility.civicactions.com/playbook/AT"
audit_category: "Accessibility Guides"
audit_format: "Detail"
audit_topic: "Tools"
audit_value: "2 Normal"
audit_action: "Update in place now"
content_status: "Migrate"

editor_status: "TRUE"
readability_score: "Normal"
migration_approved: true
original_author: "Mike, Daniel"

# Editor Notes
recommendations: "Consider whether this page should be converted into a how-to guide. Say more about VoiceOver: pragmatic since a lot of designers and developers have easy access to it. Add headers to better structure the content."
---

# Assistive Technology Testing

A practical guide to testing your digital products with the assistive technologies that real users depend on.

## Why Test with Assistive Technology

Automated testing tools catch many accessibility issues, but they can't tell you whether your site actually works for people using assistive technology. Real assistive technology testing reveals:

- **Navigation challenges** that tools miss
- **Content comprehension issues** in context  
- **User experience friction** points
- **Performance problems** with complex interactions

## Getting Started: VoiceOver on macOS

### Why Start with VoiceOver
VoiceOver is **pragmatic for most teams** because:
- **Available on every Mac** - no additional software needed
- **Widely used** by people with vision impairments
- **Well-documented** with extensive Apple resources
- **Regularly updated** with latest accessibility features

### Basic VoiceOver Testing
**Essential keyboard commands**:
- **⌘ + F5**: Turn VoiceOver on/off
- **⌃ + ⌥ + →**: Move to next element  
- **⌃ + ⌥ + ←**: Move to previous element
- **⌃ + ⌥ + Space**: Activate element (click)
- **⌃ + ⌥ + U**: Open rotor (navigation menu)

**Basic testing workflow**:
1. **Turn on VoiceOver** and close your eyes or look away
2. **Navigate your site** using only VoiceOver commands
3. **Complete key tasks** (find information, fill forms, make purchases)
4. **Note frustration points** where navigation becomes difficult
5. **Test error conditions** and dynamic content updates

### VoiceOver Rotor Navigation
The **rotor** (⌃ + ⌥ + U) provides navigation shortcuts:
- **Headings**: Navigate by heading levels
- **Links**: Jump between all links on page  
- **Form controls**: Find inputs and buttons quickly
- **Landmarks**: Move between page sections

**Test these navigation methods** to ensure your content structure supports them.

## Screen Reader Testing Strategy

### Testing Priorities
**Focus your limited testing time** on:
1. **Navigation and wayfinding** - can users orient themselves?
2. **Critical user tasks** - registration, purchasing, form completion
3. **Dynamic content** - updates, errors, loading states  
4. **Complex components** - carousels, modals, custom widgets

### Common Issues to Identify
- **Missing or poor heading structure** that breaks navigation
- **Unlabeled form controls** that provide no context
- **Focus management problems** in single-page applications
- **Dynamic content updates** not announced to screen readers
- **Complex widgets** that don't communicate their state

## Expanding Your Testing

### Windows Screen Reader Testing
**NVDA (Free)**:
- **Download**: [nvaccess.org](https://www.nvaccess.org/)
- **Primary navigation**: Arrow keys and Tab
- **Browse mode**: Automatic reading of web content
- **Forms mode**: Direct interaction with form controls

**JAWS (Paid)**:
- **Industry standard** for professional environments
- **Advanced features** for complex applications  
- **Extensive customization** options
- **Trial version available** for testing

### Mobile Screen Reader Testing

**iOS VoiceOver**:
- **Settings > Accessibility > VoiceOver** to enable
- **Gesture-based navigation** - swipe right/left to navigate
- **Rotor gestures** for quick navigation
- **Test with real devices** when possible

**Android TalkBack**:
- **Settings > Accessibility > TalkBack** to enable  
- **Explore by touch** - drag finger to hear elements
- **Swipe gestures** for navigation
- **Linear navigation** option for systematic review

## Voice Control and Switch Testing

### Voice Control Testing
**macOS Voice Control**:
- **System Preferences > Accessibility > Voice Control**
- **Tests keyboard accessibility** through voice commands
- **Reveals labeling issues** when elements can't be targeted
- **Simulates hands-free interaction** needs

### Switch Navigation Testing
**macOS Switch Control**:
- **Accessibility > Switch Control** in System Preferences
- **Tests sequential navigation** through all interactive elements
- **Reveals focus order problems** and unreachable elements
- **Simulates motor accessibility** needs

## Testing Methodology

### Structured Testing Approach
1. **Document your testing setup** - which tools, which browsers
2. **Create test scenarios** based on real user tasks
3. **Record issues systematically** with reproduction steps
4. **Prioritize findings** based on user impact
5. **Verify fixes** with the same assistive technology

### Building Testing Skills
**Start simple**:
- **Learn one screen reader well** before trying others
- **Practice on familiar sites** to understand normal behavior
- **Focus on major user journeys** rather than comprehensive testing
- **Connect with real users** when possible for validation

**Develop expertise**:
- **Join accessibility communities** for guidance and support
- **Attend training sessions** on assistive technology use
- **Practice regularly** to maintain familiarity with tools
- **Stay updated** on assistive technology improvements

## Integration with Development Workflow

### Making AT Testing Sustainable
- **Include in definition of done** for development stories
- **Train multiple team members** so testing doesn't bottleneck
- **Create testing checklists** for common scenarios  
- **Document findings** in accessible formats for team reference
- **Budget time** for assistive technology testing in project schedules

---

**Editorial Notes:**
- Original authors: Mike, Daniel  
- Format: Detail page converted to practical how-to guide
- Priority: Normal value content
- Memorial: Laura's assistive technology expertise continues to guide inclusive testing practices
- Focus: Pragmatic VoiceOver starting point with structured testing approach