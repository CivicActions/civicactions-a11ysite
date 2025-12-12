# Agents

This repository can be explored and extended using AI agents in VS Code (GitHub Copilot / AI Toolkit). Below are quick notes to help you leverage agent workflows for this project.

## Purpose
- Provide a single reference for using agents to assist with development, documentation, and site maintenance.
- Point to relevant tools and best practices available in the local AI Toolkit installation.

## AI Toolkit Tools
The local AI Toolkit provides guidance-focused tools (available when AI Toolkit is installed). To verify the local instructions exist:
```sh
ls -la ~/.aitk/instructions/tools.instructions.md
```
If present, see `~/.aitk/instructions/tools.instructions.md` for details:
- aitk-get_agent_code_gen_best_practices: Best practices and steps for agent development.
- aitk-get_tracing_code_gen_best_practices: Guidance for adding tracing/observability to AI applications.
- aitk-get_ai_model_guidance: Model selection and usage patterns.
- aitk-evaluation_planner: Helps clarify evaluation metrics and datasets.
- aitk-get_evaluation_code_gen_best_practices: Best practices for building evaluation code.
- aitk-evaluation_agent_runner_best_practices: Running agents over datasets to collect responses.

## Typical Workflows
- Planning: Use evaluation_planner to define goals before building.
- Building: Use get_agent_code_gen_best_practices and get_ai_model_guidance.
- Tracing: Use get_tracing_code_gen_best_practices for observability.
- Evaluating: Use get_evaluation_code_gen_best_practices + evaluation_agent_runner_best_practices.

## Tips
- Keep changes minimal and aligned with repo style.
- Prefer adding small, focused scripts or docs instead of broad refactors.
- When editing files, validate with local build (see below).

## Local Development (Eleventy)
This site uses Eleventy. To run locally:

1. Install Node.js 18+.
   - Verify your environment:
     ```sh
     node -v
     npm -v
     ```
     If Node is older than v18, update via nvm or your package manager.
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the local dev server:
   ```sh
   npm run serve
   ```
4. Build static output:
   ```sh
   npm run build
   ```

The dev server will watch files and reload on changes.

## Notes
- GitHub Pages builds may require `npm run build-ghpages` for path prefixing.
- See `package.json` for available scripts.
