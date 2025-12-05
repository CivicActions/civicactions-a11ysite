module.exports = function(eleventyConfig) {
  const pathPrefix = process.env.PATH_PREFIX || process.env.ELEVENTY_PATH_PREFIX || "";

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
      output: "_site"
    }
  };
};
