---
title: "Authoring Tools"
description: "Accessible authoring tools and platforms for creating inclusive content."
layout: base
eleventyNavigation:
  key: Authoring Tools
  parent: Accessibility Guides

# Migration Metadata
original_url: "https://accessibility.civicactions.com/guide/authoring-tools"
audit_category: "Accessibility Guides"
audit_format: "Guide"
audit_topic: "Tools"
audit_value: "2 Normal"
audit_action: "Update in place now"
content_status: "Migrate"
editor_assigned: ""
editor_status: "FALSE"
readability_score: "Normal"
migration_approved: true
original_author: "Jennifer, Jenna"

# Editor Notes
recommendations: "Focus on tools that help authors create accessible content without requiring deep technical knowledge. Include CMS guidance and document creation tools."
---

# Accessible Authoring Tools

Tools and platforms that help content creators produce accessible materials without requiring deep technical accessibility knowledge.

## What Are Authoring Tools?

**Authoring tools** are software applications used to create digital content, from simple text editors to complex content management systems. Accessible authoring tools:
- **Produce accessible content** by default
- **Guide authors** toward inclusive content practices  
- **Prevent common accessibility barriers** from being created
- **Support authors with disabilities** in creating content

## Content Management Systems (CMS)

### WordPress
**Accessibility features**:
- Built-in alt text fields for images
- Heading structure enforcement in block editor
- Color contrast checking in theme customizer
- Keyboard navigation support in admin interface

**Recommended plugins**:
- **WP Accessibility**: Fixes common accessibility issues
- **Accessibility Checker**: Scans content for problems
- **One Click Accessibility**: Quick accessibility improvements

**Best practices**:
- Choose accessibility-ready themes
- Test admin interface with keyboard navigation
- Train content authors on accessible practices
- Regular accessibility audits of published content

### Drupal
**Accessibility features**:
- WCAG 2.1 AA compliance in core admin interface
- Semantic HTML output by default
- Accessible form validation and error messaging
- Screen reader optimized content editing experience

**Accessibility modules**:
- **Accessibility Scanner**: Automated content checking
- **Block Accessibility**: Improves block-based layouts
- **CKEditor Accessibility Checker**: Content editor validation

### Government CMS Platforms

#### USWDS-Based Systems
- **Federalist**: Cloud-based static site generator
- **Cloud.gov**: Government platform-as-a-service
- **USWDS Jekyll**: Template with accessibility built-in

#### Drupal GovCMS
- Government-focused Drupal distribution
- Section 508 compliance built into templates
- Accessibility testing integrated into workflow

## Document Creation Tools

### Microsoft Office 365
**Accessibility Checker**:
- Built-in accessibility scanning in Word, PowerPoint, Excel
- Real-time suggestions for improvements
- Alternative text prompts for images and media
- Heading structure validation

**Accessible document creation**:
- Use built-in heading styles (never manual formatting)
- Add meaningful alt text to all images
- Create accessible tables with proper headers
- Use sufficient color contrast in design elements
- Provide captions for embedded videos

### Google Workspace
**Google Docs accessibility**:
- Voice typing for hands-free document creation  
- Screen reader support with keyboard shortcuts
- Automatic heading and list structure
- Comment and suggestion features work with assistive technology

**Google Slides accessibility**:
- Alt text for images and shapes
- Slide layout templates with proper structure
- Speaker notes for additional context
- Captions for embedded videos

### Adobe Creative Suite

#### Adobe Acrobat Pro
**PDF accessibility features**:
- Accessibility Checker with detailed reporting
- Auto-tagging for document structure
- Reading order adjustment tools
- Form field accessibility properties

#### Adobe InDesign
**Accessible publishing**:
- Export to accessible PDF formats
- Tag structure for screen reader navigation
- Alt text assignment for images and graphics
- Table accessibility features

## Web-Based Authoring Platforms

### Notion
**Accessibility considerations**:
- Keyboard navigation throughout interface
- Screen reader compatibility with most content
- Alt text support for images
- Structured content with headings and lists

**Limitations**:
- Complex layouts may not translate to accessible exports
- Database views can be challenging with assistive technology
- Custom blocks may lack proper ARIA labeling

### Confluence
**Atlassian accessibility features**:
- Editor accessibility toolbar
- Keyboard shortcuts for formatting
- Image alt text requirements
- Table accessibility helpers

### GitHub and GitLab

#### Markdown Accessibility
**Best practices for accessible Markdown**:
- Use proper heading hierarchy (# ## ### etc.)
- Write descriptive link text (avoid "click here")
- Include alt text for images: `![Alt text](image.jpg)`
- Create accessible tables with headers
- Use semantic HTML when Markdown isn't sufficient

#### Documentation Platforms
- **GitBook**: Accessible documentation with navigation aids
- **Docusaurus**: React-based docs with accessibility features
- **MkDocs**: Python-based generator with accessible themes

## Email and Newsletter Tools

### Accessible Email Design

#### Mailchimp
**Accessibility features**:
- Alt text requirements for images
- Accessible email templates
- Color contrast checking
- Plain text versions automatically generated

#### Constant Contact
**Inclusive email tools**:
- Screen reader optimized templates
- Accessibility guidance in editor
- Mobile-responsive design by default
- Testing tools for various email clients

### Best Practices for Email Accessibility
- **Use semantic HTML** structure in email templates
- **Provide alt text** for all informative images
- **Ensure sufficient contrast** in text and background colors
- **Include plain text versions** of all HTML emails
- **Test with email clients** used by your audience

## Learning Management Systems (LMS)

### Canvas
**Accessibility features**:
- Built-in accessibility checker for content
- Keyboard navigation throughout platform
- Screen reader optimized interface
- Captioning tools for video content

### Moodle
**Inclusive learning design**:
- Accessibility guidelines built into content creation
- Multiple format support (text, audio, video)
- Customizable interface for different needs
- Activity completion tracking for various interaction methods

## Social Media Management

### Accessible Social Media Tools

#### Hootsuite
- Alt text support for images across platforms
- Character count includes accessibility considerations  
- Scheduling posts with accessibility review
- Analytics include accessibility engagement metrics

#### Buffer
- Image alt text reminders
- Accessibility-focused content templates
- Cross-platform accessibility optimization
- Team collaboration on inclusive content

### Platform-Specific Guidance

#### Twitter/X
- Always add alt text to images
- Use camelCase for hashtags (#AccessibilityMatters vs #accessibilitymatters)
- Describe visual content in text
- Avoid emoji overuse that creates screen reader clutter

#### LinkedIn  
- Professional image alt text
- Document uploads should be accessible PDFs
- Video captions for professional content
- Clear, descriptive link previews

## Evaluation and Selection

### Choosing Accessible Authoring Tools

#### Evaluation Criteria
- **Produces accessible output** by default
- **Supports authors with disabilities** in the creation process
- **Provides accessibility guidance** during content creation
- **Includes accessibility checking** or validation features
- **Allows manual accessibility improvements** when needed

#### Questions to Ask Vendors
1. Does the tool produce WCAG 2.1 AA compliant content?
2. Is the authoring interface itself accessible to users with disabilities?
3. What accessibility training and support do you provide?
4. How do you handle accessibility updates and improvements?
5. Can we customize accessibility settings for our organization's needs?

### Implementation Planning
- **Pilot testing** with diverse users including people with disabilities
- **Training plan** for authors on accessibility features
- **Workflow integration** with existing content review processes
- **Accessibility monitoring** and continuous improvement processes

## CivicActions Recommendations

### For Government Clients
- **USWDS-compliant systems** for federal agencies
- **Section 508 testing** integrated into content workflows
- **Author training** on government accessibility requirements  
- **Procurement guidance** for selecting accessible authoring tools

### For All Organizations
- **Start with accessible defaults** - choose tools that create accessible content by design
- **Train content creators** on accessibility principles, not just tool features
- **Regular auditing** of published content for accessibility compliance
- **User feedback integration** from people who use assistive technology

---

**Editorial Notes:**
- Format: Guide with practical tool selection and implementation guidance  
- Priority: Normal value - important for content creation workflows
- Assigned to: Jenna Waszak (pending completion)
- Content covers both technical tools and content creation guidance for inclusive authoring