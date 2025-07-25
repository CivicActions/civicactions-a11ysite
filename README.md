# CivicActions Accessibility Site

A collection of resources about digital accessibility and how it aligns with open source, CivicTech and Digital Transformation.

## 11ty

Site is built with [11ty](https://www.11ty.dev/). Files in the `.eleventyignore` file are not processed by 11ty.

## How to set up a local 11ty environment

1. Clone the repository
2. Run `npm install` to install dependencies
3. Run `npm run serve` to start the local development server

## To commit changes

We use pre-commit hooks to ensure code quality and consistency. Follow these steps to install it and then commit your changes:

1. Run `pre-commit install` to set up pre-commit hooks
2. Commit your changes with a descriptive message

Pre-commit configuration file is `.pre-commit-config.yaml`. It includes some available pre-commit hooks and the following tools:

- [remark-lint](https://github.com/remarkjs/remark-lint)
- [codespell](https://github.com/codespell-project/codespell)
- [search-and-replace](https://github.com/mattlqx/pre-commit-search-and-replace) (Configuration is in `.config/pre-commit-search-and-replace.yaml`)

## Tugboat

Tugboat is used to preview pull requests. It builds the site and provides a temporary URL for review. You can find more information about Tugboat in the [Tugboat documentation](https://www.tugboatqa.com/).

## Dependabot

We use [Dependabot](https://docs.github.com/en/code-security/dependabot) to keep our dependencies up to date. It will automatically create pull requests for dependency updates. You can find the configuration in the `.github/dependabot.yml` file.

## GitHub Pages

This site is hosted on GitHub Pages. The source code is in the `main` branch, and the built site is in the `gh-pages` branch. The `gh-pages` branch is automatically updated by the GitHub action `.github/workflows/deploy-to-ghpages` when changes are pushed to the `main` branch.
