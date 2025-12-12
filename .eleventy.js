const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");

module.exports = function(eleventyConfig) {
  const pathPrefix = process.env.PATH_PREFIX || process.env.ELEVENTY_PATH_PREFIX || "";

  // Enable Eleventy Navigation plugin for filters/shortcodes in templates
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  // Layout aliases to map legacy layout names onto existing templates
  eleventyConfig.addLayoutAlias("page", "base.html");
  eleventyConfig.addLayoutAlias("post", "base.html");
  eleventyConfig.addLayoutAlias("guide", "base.html");
  eleventyConfig.addLayoutAlias("playbook", "base.html");
  eleventyConfig.addLayoutAlias("role", "base.html");
  eleventyConfig.addLayoutAlias("role-default", "base.html");
  eleventyConfig.addLayoutAlias("about", "base.html");

  // Passthrough static assets (CSS, etc.)
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("_redirects");

  // Collection: primary nav pages (exclude legacy/duplicate dirs)
  eleventyConfig.addCollection('navPrimary', (collectionApi) => {
    const excludePrefixes = [
      './guide/',
      './accessibility-guides/',
      './champion-accessibility/'
    ];
    return collectionApi.getAll().filter((item) => {
      if (!item.data || !item.data.eleventyNavigation) return false;
      const p = item.inputPath;
      return !excludePrefixes.some((prefix) => p.startsWith(prefix));
    });
  });

  // Transform: prefix absolute href/src with pathPrefix for GitHub Pages
  eleventyConfig.addTransform('applyPathPrefix', (content, outputPath) => {
    if (!pathPrefix || !outputPath || !outputPath.endsWith('.html')) return content;
    // Only adjust absolute site-relative URLs
    const prefix = `/${pathPrefix}`.replace(/\/+$/, '');
    return content
      .replace(/href="\/(?!\/)([^"]*)"/g, (m, p1) => `href="${prefix}/${p1}"`)
      .replace(/src="\/(?!\/)([^"]*)"/g, (m, p1) => `src="${prefix}/${p1}"`)
      .replace(/action="\/(?!\/)([^"]*)"/g, (m, p1) => `action="${prefix}/${p1}"`);
  });

  return {
    pathPrefix,
    dir: {
      input: ".",
      includes: "_includes",
      data: "_data",
      output: "_site"
    }
  };
};
