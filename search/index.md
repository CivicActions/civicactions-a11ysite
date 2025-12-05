---
title: "Search"
description: "Search the CivicActions Accessibility site (placeholder)."
layout: base
eleventyNavigation:
  key: Search

# Migration Metadata
original_url: "https://accessibility.civicactions.com/search"
audit_category: "Utility"
audit_format: "Search"
audit_value: "2 Normal"
audit_notes: "Placeholder page for site search. Implement search integration (Algolia/Elastic/Lunr) later."
audit_action: "Create placeholder"
content_status: "New"
http_status: 200
migration_approved: true

# Article Metadata
publish_date: "2025-12-05"
author: "CivicActions"
---

# Search

This site currently does not have a production search engine configured. Options for adding search:

- Host-side search services: Algolia, Elastic Enterprise Search
- Static search: Lunr, Fuse.js with prebuilt index
- Serverless search integrations with hosted index

If you'd like, I can implement a basic Lunr-based client-side search with a generated index during Eleventy builds, or scaffold an Algolia integration.
