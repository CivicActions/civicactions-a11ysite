#!/bin/bash
set -euo pipefail

if [[ -n "${GITHUB_WORKSPACE:-}" ]]; then
  # Add global git config entry for GITHUB_WORKSPACE as a safe.directory.
  git config --global --add safe.directory "$GITHUB_WORKSPACE"
fi

LOCAL_MAIN=$(git branch --list main)
# Use local main if it exists, otherwise
MAIN=main
if [[ -z ${LOCAL_MAIN} ]]; then
  MAIN=origin/main
fi
# Only check markdown files changed on branch to avoid excessive output.
export REMARK_PATHS=$(git diff --diff-filter=AM --name-only "${MAIN}" ':*.md')

if [[ -n "${INPUT_GITHUB_TOKEN:-}" ]]; then
  export REVIEWDOG_GITHUB_API_TOKEN="${INPUT_GITHUB_TOKEN}"
  remark --rc-path=/usr/src/remarkrc.suggestion --no-color ${REMARK_PATHS} 2>&1 >/dev/null |
    reviewdog -f=remark-lint \
      -name="remark-lint-suggestions" \
      -reporter="github-pr-check" \
      -fail-on-error="false" \
      -level="info" \
      -tee

  remark --rc-path=/usr/src/remarkrc.problem --no-color ${REMARK_PATHS} 2>&1 >/dev/null |
    reviewdog -f=remark-lint \
      -name="remark-lint-problem" \
      -reporter="github-pr-check" \
      -fail-on-error="true" \
      -level="error" \
      -tee
else
  remark --quiet --rc-path=/usr/src/remarkrc.suggestion ${REMARK_PATHS} 2>&1 >/dev/null |
    sed -e 's/warning/suggestion/g'
  remark --frail --quiet --rc-path=/usr/src/remarkrc.problem ${REMARK_PATHS} 2>&1 >/dev/null |
    sed -e 's/warning/problem/g'
fi
