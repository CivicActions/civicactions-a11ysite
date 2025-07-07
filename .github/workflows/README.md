# Workflows

## check-all.yml

Checking all markdown and links site-wide weekly using `umbrelladocs/action-linkspector` and remark-lint.

## codespell.yml

Checking for common typos using `codespell-project/actions-codespell`. Configuration in the `.config` folder.

## deploy-to-ghpages.yml

Build the 11ty site, cache dependencies, and deploy it to the `gh-pages` branch using `peaceiris/actions-gh-pages`.

## link-check-pr.yml

Checking links using `umbrelladocs/action-linkspector`. Configuration in the `.config` folder.

## reviewdog.yml

Run remark-lint with reviewdog on pull requests to check for readability and other text checks. Configuration in the `.config/remark` folder.
