---
title: "Automated Accessibility Testing: Leveraging GitHub Actions and Pa11y-ci with Axe"
description: "How to implement continuous accessibility integration using GitHub Actions, Pa11y-ci, and Axe-core for government development workflows."
layout: base
eleventyNavigation:
  key: Automated Testing GitHub Actions
  parent: News

# Migration Metadata
original_url: "https://accessibility.civicactions.com/posts/automated-accessibility-testing-leveraging-github-actions-and-pa11y-ci-with-axe"
audit_category: "About"
audit_format: "Article"
audit_topic: "Automated testing"
audit_value: "2 Normal"
audit_notes: "Update later"
audit_action: "Update later"
content_status: "Migrate"
http_status: 301
migration_approved: true

# Article Metadata
publish_date: "2023-04-18"
author: "Daniel Mundra"
tags: ["automated testing", "CI/CD", "GitHub Actions", "Pa11y", "axe-core"]
---

# Automated Accessibility Testing: Leveraging GitHub Actions and Pa11y-ci with Axe

Implementing continuous accessibility integration in government development workflows using GitHub Actions, Pa11y-ci, and Axe-core to catch accessibility issues before they reach production.

## The Challenge of Manual Testing

Manual accessibility testing is essential but has limitations:
- **Time-intensive** - requires significant effort for comprehensive coverage
- **Human error** - easy to miss issues or inconsistent testing approaches
- **Late discovery** - problems found after development completion are expensive to fix
- **Scale limitations** - difficult to test every page and component regularly

## Automated Testing Benefits

### Early Issue Detection
Automated accessibility testing integrated into CI/CD pipelines:
- **Catches issues immediately** when code is committed
- **Prevents regression** by testing every change
- **Reduces remediation costs** through early discovery
- **Maintains compliance** continuously rather than periodically

### Consistent Standards
Automated tools provide:
- **Standardized testing** across all developers and projects
- **Objective measurements** removing subjective interpretation
- **Comprehensive coverage** testing more scenarios than manual review
- **Documentation** of accessibility decisions and requirements

## Implementation Architecture

### GitHub Actions Workflow

```yaml
name: Accessibility Testing
on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  accessibility-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build site
        run: npm run build

      - name: Start server
        run: |
          npm run serve &
          sleep 10

      - name: Run Pa11y-ci
        run: npx pa11y-ci --sitemap http://localhost:8080/sitemap.xml

      - name: Run Axe tests
        run: npm run test:axe
```

### Pa11y-ci Configuration

```json
{
  "defaults": {
    "timeout": 20000,
    "wait": 500,
    "chromeLaunchConfig": {
      "args": ["--no-sandbox"]
    }
  },
  "urls": [
    "http://localhost:8080/",
    "http://localhost:8080/guides/",
    "http://localhost:8080/about/contact/"
  ]
}
```

### Axe-core Integration

```javascript
// test/accessibility.test.js
const { AxePuppeteer } = require('@axe-core/puppeteer');
const puppeteer = require('puppeteer');

describe('Accessibility Tests', () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
  });

  afterAll(async () => {
    await browser.close();
  });

  test('Homepage accessibility', async () => {
    await page.goto('http://localhost:8080/');
    const results = await new AxePuppeteer(page).analyze();
    expect(results.violations).toHaveLength(0);
  });
});
```

## Tool Selection and Configuration

### Pa11y-ci Advantages
- **Command-line interface** perfect for CI/CD integration
- **Sitemap support** automatically tests all pages
- **Configurable standards** supporting WCAG 2.1 AA requirements
- **HTML reporter** generating detailed accessibility reports
- **Custom actions** for testing complex user interactions

### Axe-core Benefits
- **Industry standard** accessibility testing engine
- **Comprehensive ruleset** covering WCAG guidelines
- **Low false positives** reducing noise in test results
- **Detailed reporting** with specific remediation guidance
- **Browser integration** testing real DOM state after JavaScript execution

### Lighthouse CI Integration
```yaml
- name: Run Lighthouse CI
  run: |
    npm install -g @lhci/cli@0.11.x
    lhci autorun
  env:
    LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}
```

## Government-Specific Considerations

### Section 508 Compliance
Configuring tools for government requirements:
- **WCAG 2.1 AA standards** as baseline for Section 508
- **Custom rulesets** for government-specific accessibility requirements
- **Reporting formats** compatible with compliance documentation
- **Audit trails** maintaining records of accessibility testing

### Security Requirements
Government CI/CD accessibility testing must address:
- **No external service dependencies** running tests within secure environments
- **Container security** using approved base images and security scanning
- **Credential management** securely handling any required API keys or tokens
- **Network isolation** ensuring tests don't expose internal systems

### Performance Considerations
Government websites often have specific performance requirements:
- **Testing timeouts** accommodating slower government networks
- **Resource limits** working within allocated CI/CD computing resources
- **Parallel testing** optimizing test execution time
- **Caching strategies** reducing redundant testing of unchanged content

## Advanced Implementation Patterns

### Multi-Environment Testing
```yaml
strategy:
  matrix:
    environment: [development, staging, production]
    browser: [chrome, firefox]
```

### Custom Accessibility Rules
```javascript
// Custom rule for government branding requirements
axe.configure({
  rules: [
    {
      id: 'government-logo-alt-text',
      selector: 'img[src*="logo"]',
      evaluate: function (node) {
        return node.getAttribute('alt').includes('government') ||
               node.getAttribute('alt').includes('agency');
      }
    }
  ]
});
```

### Dynamic Content Testing
```javascript
// Testing single-page applications and dynamic content
await page.click('#load-more-button');
await page.waitForSelector('.new-content');
const results = await new AxePuppeteer(page).analyze();
```

## Integration with Development Workflow

### Pull Request Automation
- **Automatic testing** of all pull requests before merge
- **Comment integration** posting accessibility results directly in GitHub
- **Blocking merges** when accessibility tests fail
- **Trend tracking** monitoring accessibility improvement over time

### Developer Feedback
```yaml
- name: Comment PR
  uses: actions/github-script@v6
  if: failure()
  with:
    script: |
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: '❌ Accessibility tests failed. Please review the errors and fix before merging.'
      })
```

### Reporting and Metrics
- **Accessibility dashboard** showing trends and current status
- **Compliance reports** automatically generated for audits
- **Issue tracking** integration with GitHub Issues or Jira
- **Historical analysis** identifying patterns in accessibility issues

## Best Practices and Lessons Learned

### Test Coverage Strategy
- **Critical user paths** prioritizing essential government services
- **Component testing** validating reusable interface elements
- **Cross-browser validation** ensuring compatibility across platforms
- **Mobile accessibility** testing responsive design implementations

### Managing False Positives
- **Rule customization** disabling inappropriate rules for specific contexts
- **Context-aware testing** understanding when automated tools have limitations
- **Manual validation** confirming automated test results with human review
- **Tool comparison** using multiple tools to validate findings

### Performance Optimization
- **Selective testing** running full suites only on significant changes
- **Parallel execution** distributing tests across multiple workers
- **Caching strategies** reusing build artifacts and test data
- **Incremental testing** focusing on changed files and components

## Measuring Success

### Quantitative Metrics
- **Error reduction** tracking decrease in accessibility violations over time
- **Test coverage** percentage of pages and components under automated testing
- **Resolution time** speed of fixing accessibility issues after detection
- **Compliance rate** maintaining consistent WCAG 2.1 AA compliance

### Qualitative Improvements
- **Developer confidence** in accessibility implementation
- **User experience** improvements from systematic accessibility attention
- **Team knowledge** growth in accessibility understanding and practices
- **Stakeholder satisfaction** from consistent compliance and quality

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-2)
1. **Set up basic GitHub Actions** workflow with Pa11y-ci
2. **Configure testing** for critical pages and user flows
3. **Establish baselines** documenting current accessibility status
4. **Train team** on interpreting and acting on automated test results

### Phase 2: Enhancement (Weeks 3-4)
1. **Add Axe-core integration** for comprehensive testing coverage
2. **Implement custom rules** for government-specific requirements
3. **Set up reporting** dashboard and compliance documentation
4. **Integrate with development workflow** blocking problematic changes

### Phase 3: Optimization (Weeks 5-8)
1. **Performance tuning** optimizing test execution time and resource usage
2. **Advanced scenarios** testing complex interactions and dynamic content
3. **Cross-browser testing** ensuring compatibility across platforms
4. **Continuous improvement** refining rules and processes based on experience

## Tools and Resources

### Required Dependencies
```json
{
  "devDependencies": {
    "pa11y-ci": "^3.0.1",
    "@axe-core/puppeteer": "^4.7.0",
    "puppeteer": "^19.0.0",
    "jest": "^29.0.0"
  }
}
```

### Documentation Links
- **Pa11y-ci Documentation**: [github.com/pa11y/pa11y-ci](https://github.com/pa11y/pa11y-ci)
- **Axe-core Rules**: [dequeuniversity.com/rules/axe](https://dequeuniversity.com/rules/axe)
- **GitHub Actions**: [docs.github.com/actions](https://docs.github.com/en/actions)
- **WCAG 2.1 Guidelines**: [w3.org/WAI/WCAG21/quickref](https://www.w3.org/WAI/WCAG21/quickref/)

### CivicActions Resources
- **Accessibility testing guide**: [Our automated testing documentation](/guides/development/automated-testing/)
- **Government accessibility**: [Section 508 compliance approaches](/champions/training-certifications/)
- **Team consultation**: [Get accessibility help](/about/get-accessibility-help/)

Automated accessibility testing transforms how government teams approach accessibility compliance, making it a continuous practice rather than a periodic audit. The investment in setting up comprehensive testing pays dividends in reduced remediation costs, improved user experiences, and consistent compliance with accessibility standards.

---

**Editorial Notes:**
- Format: Technical implementation article with code examples and government focus
- Priority: Normal value - important technical content for development teams
- Action: Updated with current tool versions and government-specific considerations
- Author: Daniel Mundra, reflecting his automated testing expertise
