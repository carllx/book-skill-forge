---
name: book-skill-forge
description: A composite hybrid engine that integrates Graphify, Cangjie, and Book-to-Skill to forge high-quality Agent skills from books.
---

# Book-Skill-Forge (BSF)

This skill is the **Master Orchestrator** for transforming books (methodology, narrative, or technical) into highly usable, self-verifying Agent Skills. It fuses the breadth of AST-based knowledge graphs (Graphify), the depth of methodology extraction (Cangjie), and the generic structural capabilities of Book-to-Skill.

## Invocation Requirements

When the user asks to "convert this book into a skill using the composite engine", or mentions "BSF" / "book-skill-forge":

1. **Verify Source**: Check that the source text and metadata exist.
2. **Execute Pipeline**: Follow the 5-phase execution pipeline below.

## Pipeline (5 Phases)

### Phase 1: Ingestion & Dual Extraction
- **Subagent/Tool 1**: Invoke `engines/graphify_adapter.py` to run the book through Graphify. This will produce a `graph.json` containing the semantic AST and community clusters.
- **Subagent/Tool 2**: In parallel, invoke `engines/cangjie_adapter.py` (Adler reading & Stage 0+1) to produce a set of candidate methodological skills.

### Phase 2: Cross-Validation & Fusion
- Use `fusion/fusion_router.py` to determine the book type (Methodology, Narrative, Technical).
- Invoke `fusion/graph_augmented_ria.py` to inject graph context from `graph.json` into the Cangjie candidate skills. This ensures long-tail knowledge discovered by Graphify is not lost during Cangjie's rigid extraction.
- Run `fusion/cross_engine_dedup.py` to merge similar concepts and avoid redundancy.

### Phase 3: Skill Assembly
- Map the fused concepts into the Book-to-Skill templates (`templates/skill_md.template`, `templates/chapter_standard.template`).
- Ensure the output strictly follows the RIA++ (Role, Intent, Action) structures.

### Phase 4: Quality Gate
- Trigger the Dual-Judge semantic evaluator (`evaluator/dual_judge_runner.py`) to score the resulting skill against the Ground Truth (if available).
- If the usability score is below 80%, refine the instructions or prompt the user for clarification.

### Phase 5: Delivery
- Generate `SKILL.md`.
- Produce a `DIGEST.md` (long-form summary).
- Print a summary for the user indicating completion, metrics, and locations of the generated files.

## References
- See `EVALUATION_GUIDELINE.md` for metrics logic.
- See `config/pipeline_registry.json` for engine options.
