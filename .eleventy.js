module.exports = function(eleventyConfig) {
  const pathPrefix = process.env.PATH_PREFIX || process.env.ELEVENTY_PATH_PREFIX || "";

  return {
    pathPrefix,
    dir: {
      input: ".",
      output: "_site"
    }
  };
};
