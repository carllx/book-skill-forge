---
name: bsf-eval-orchestrator
description: Orchestrates the Book-Skill-Forge (BSF) evaluation pipeline natively using subagents, bypassing Python LLM calls.
---

# BSF Evaluation Orchestrator

You are the master orchestrator for testing the Book-Skill-Forge pipeline. When a user asks you to run the BSF evaluation pipeline (e.g., via `/run-eval` or directly), follow these steps strictly.

## Inputs required
- `book_id` (e.g., `jiangouwenhua`)
- `book_path` (e.g., `e:\Download\book-skill-test-bench\test-bench\runs\jiangouwenhua\text.md`)
- `ground_truth_path` (e.g., `e:\Download\book-skill-test-bench\test-bench\ground-truth\jiangouwenhua\concepts.json`)

## Execution Steps

### 1. Invoke Extraction Subagents
You need to generate candidates from the book using two parallel pipelines: Graphify and Cangjie.

* **Pre-computation (Dynamic Watchdog Timer)**: Check the size of the `book_path` file (e.g. using `list_dir` or file stats). Calculate a dynamic timeout proportional to the file size (e.g., base 300s + 30s per 10KB of text). Use this timeout when setting up the watchdog timer for the subagents.
* **Graphify**: Use `invoke_subagent` to spawn a subagent with the `graphify` skill. 
  * Task: "Run graphify on the book_path and output the resulting graph to `test-bench/evaluation/out/{book_id}_A1/graph.json`"
* **Cangjie**: Use `invoke_subagent` to spawn a subagent with the `cangjie-skill`. 
  * Task: "Extract methodologies from the book_path and output the resulting SKILL.md to `test-bench/evaluation/out/{book_id}_A2/SKILL.md`"

### 2. Wait for Completion
Wait for both subagents to report completion. You MUST use the `schedule` tool to set the dynamic watchdog timer calculated in Step 1.

### 3. Invoke Semantic Judge Subagent
Once extraction is done, you need to match the extracted concepts against the ground truth.
* Read the `ground_truth_path` using `view_file`.
* Read the extracted outputs (`graph.json` and `SKILL.md`) using `view_file`.
* Use `invoke_subagent` to spawn a `semantic_judge` subagent.
  * Task: "Compare the following extracted concepts with the ground truth candidates. **CRITICAL SCHEMA REQUIREMENT**: You MUST output a strictly formatted JSON object with a single root key `\"mappings\"` whose value is an array of match objects (each having `matched`, `gt_id`, `confidence`, and `reasoning`). Do NOT return a bare JSON list `[...]`. Save it to `test-bench/evaluation/out/{book_id}_BSF/matches.json`"

### 4. Run Python Metric Calculator
Once `matches.json` is generated, the LLM work is done!
* Run the python command: `python test-bench/evaluation/run_eval_suite.py --book {book_id} --book-path {book_path} --gt {ground_truth_path}`.
*(Since we removed LLM from adapters, it will just read the outputs you generated and calculate metrics).*

### 5. Report Results
* Read `test-bench/evaluation/scores_table.md`.
* Present the markdown table to the user.
