# English Grammar and Reading System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a permanent fourteen-module English grammar and reading curriculum with 150 self-training questions, complete expandable explanations, and a morphology reference page.

**Architecture:** Keep source material as focused UTF-8 Markdown files under `content/10_english/01_grammar_reading/`. The existing Python note builder converts each source file into a static HTML page and supplies expandable `:::solution` blocks. A content-contract script verifies module presence, required teaching sections, exercise totals, solution totals, context balance, links, and encoding before publication.

**Tech Stack:** Markdown, Python standard library, existing `scripts/build_notes.py`, static HTML/CSS, GitHub Pages.

---

## File Map

- Modify `content/10_english/01_grammar_reading/README.md`: curriculum map and permanent-study instructions.
- Create `content/10_english/01_grammar_reading/01_clause_skeletons_zh.md` through `14_academic_argument_zh.md`: fourteen teaching modules.
- Create `content/10_english/01_grammar_reading/15_morphology_reference_zh.md`: roots, affixes, word families, and inference limits.
- Create `scripts/check_english_reading_content.py`: deterministic content-contract checker.
- Modify `docs/english.html`: expose the complete reading tree and defer the listening branch.
- Generate `docs/notes/10-english/01-grammar-reading/*.html`: static output from the builder.

### Task 1: Content Contract

**Files:**
- Create: `scripts/check_english_reading_content.py`

- [ ] **Step 1: Define the exact curriculum manifest**

The checker declares the fourteen numbered module filenames plus `15_morphology_reference_zh.md`. Every core module must contain the headings `本章研究的问题`, `核心原理`, `逐句精读`, `精读材料`, `自我训练`, and `迁移与反思`.

- [ ] **Step 2: Define measurable completeness checks**

For each core module, assert at least eight `### 句子` analyses, exactly ten `### 训练` questions, and exactly ten `:::solution` blocks. Assert ten training questions and ten solutions in the morphology page. Across all source pages, assert exactly 150 training questions and 150 solution blocks.

- [ ] **Step 3: Run the checker and observe the expected failure**

Run: `python scripts/check_english_reading_content.py`

Expected: non-zero exit with missing-module diagnostics because the curriculum pages do not yet exist.

### Task 2: Foundation Modules 1-5

**Files:**
- Create: `content/10_english/01_grammar_reading/01_clause_skeletons_zh.md`
- Create: `content/10_english/01_grammar_reading/02_tense_aspect_zh.md`
- Create: `content/10_english/01_grammar_reading/03_modality_counterfactuals_zh.md`
- Create: `content/10_english/01_grammar_reading/04_noun_phrases_reference_zh.md`
- Create: `content/10_english/01_grammar_reading/05_complement_subordinate_clauses_zh.md`

- [ ] **Step 1: Write the five conceptual chapters**

Each chapter explains form, meaning, discourse function, interpretation boundaries, and common misreadings before presenting examples.

- [ ] **Step 2: Add sentence analyses and reading sets**

Each chapter includes eight progressively denser English sentences and one coherent passage. Analyses identify the structural head, scope, implied relation, and the reading error prevented by the analysis.

- [ ] **Step 3: Add ten questions and complete solutions per chapter**

Each solution states the answer, identifies evidence in the sentence, explains the interpretive consequence, and rejects at least one tempting misanalysis where relevant.

- [ ] **Step 4: Run the content checker**

Expected: Tasks 2 files pass their local checks; remaining module files are reported missing.

### Task 3: Structural Modules 6-10

**Files:**
- Create: `content/10_english/01_grammar_reading/06_relatives_apposition_zh.md`
- Create: `content/10_english/01_grammar_reading/07_nonfinite_clauses_zh.md`
- Create: `content/10_english/01_grammar_reading/08_negation_scope_zh.md`
- Create: `content/10_english/01_grammar_reading/09_comparison_parallelism_ellipsis_zh.md`
- Create: `content/10_english/01_grammar_reading/10_information_structure_zh.md`

- [ ] **Step 1: Write the five conceptual chapters**

Cover restrictive versus supplementary modification, reduced clauses, attachment and scope, parallel interpretation, ellipsis recovery, inversion, clefts, and focus.

- [ ] **Step 2: Add eight analyses and one reading set per chapter**

At least two examples per chapter must expose a genuine ambiguity or a boundary where punctuation or context changes the interpretation.

- [ ] **Step 3: Add ten questions and complete solutions per chapter**

Questions must mix structural identification, interpretation comparison, ambiguity diagnosis, and justified rewriting.

- [ ] **Step 4: Run the content checker**

Expected: Tasks 2 and 3 files pass; advanced modules and morphology remain missing.

### Task 4: Academic Reading Modules 11-14 and Morphology

**Files:**
- Create: `content/10_english/01_grammar_reading/11_nominalization_compression_zh.md`
- Create: `content/10_english/01_grammar_reading/12_cohesion_reference_zh.md`
- Create: `content/10_english/01_grammar_reading/13_stance_evidentiality_zh.md`
- Create: `content/10_english/01_grammar_reading/14_academic_argument_zh.md`
- Create: `content/10_english/01_grammar_reading/15_morphology_reference_zh.md`

- [ ] **Step 1: Write four advanced chapters**

Teach decompression of nominalized prose, reference-chain tracking, stance strength, source attribution, research-gap moves, claim-evidence-warrant relations, limitations, and counterargument.

- [ ] **Step 2: Write the morphology reference**

Organize productive prefixes, roots, suffixes, and word families by inference function. Explicitly explain false friends, historical opacity, multiple meanings, and why morphology cannot replace context.

- [ ] **Step 3: Complete the 150-question bank**

Add ten exercises and ten complete solutions to each of the four advanced modules and the morphology page.

- [ ] **Step 4: Run the complete content checker**

Expected: `PASS: 14 modules, 1 morphology reference, 150 exercises, 150 solutions.`

### Task 5: Navigation and Static Build

**Files:**
- Modify: `content/10_english/01_grammar_reading/README.md`
- Modify: `docs/english.html`
- Generate: `docs/notes/10-english/01-grammar-reading/*.html`

- [ ] **Step 1: Replace the overview with a curriculum map**

The overview groups modules into sentence foundation, structural expansion, discourse and academic reading, and morphology. It explains that pages are permanent references rather than scheduled lessons.

- [ ] **Step 2: Update the English landing tree**

Expose the grammar and reading curriculum as the primary branch. Mark listening as deferred without removing existing audio pages.

- [ ] **Step 3: Build static pages**

Run: `python scripts/build_notes.py`

Expected: exit code 0 and generated HTML for all fifteen new source pages.

### Task 6: Final Verification and Publication

**Files:**
- Verify all changed source and generated files.

- [ ] **Step 1: Run content and build checks**

Run:

```powershell
python scripts/check_english_reading_content.py
python scripts/build_notes.py
git diff --check
```

Expected: both Python commands exit 0; Git reports no whitespace errors.

- [ ] **Step 2: Verify generated HTML contracts**

Confirm all fifteen HTML pages exist, contain UTF-8 Chinese text, and together contain 150 `solution-toggle` elements.

- [ ] **Step 3: Inspect representative pages in the browser**

Inspect the curriculum index, one foundation module, one structural module, and one advanced module at desktop and mobile widths. Confirm tree navigation, readable English examples, non-overlapping text, and functional expandable explanations.

- [ ] **Step 4: Commit and publish**

Commit the source, checker, navigation, and generated HTML. Push to `origin/main`, synchronize the original local checkout, and verify the public HTTP pages after GitHub Pages deployment.

