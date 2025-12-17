const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");

module.exports = function(eleventyConfig) {
  // Add the navigation plugin
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  // Return your Object options:
  return {
    dir: {
      // Eleventy will process files in the root directory
      input: "."
    }
  };
};
