# mathKnowledge

This folder is designed to be a self-contained workspace for `math.bozhanli.com`.

It is intentionally separated from the current research-note site so the whole folder can be copied into a standalone repository later with minimal cleanup.

## Structure

```text
mathKnowledge/
  CNAME
  README.md
  site_plan.md
  workflow_zh.md
  scripts/         -> build tools for auto-publishing notes
  content/         -> source notes and lesson drafts
  docs/            -> publishable static pages
  templates/       -> reusable writing templates
```

## Current scope

- Calculus
- Linear Algebra
- Probability
- High School Math

The first version is focused on:

1. building a clear site skeleton
2. separating source content from published pages
3. making future migration to `math.bozhanli.com` easy

## Next suggested steps

1. fill the core framework notes for calculus / linear algebra / probability
2. refine the published overview and core pages in `docs/`
3. build the first stable FAQ and references pages
4. add a live Q&A archive once the first sessions exist

## Auto-published notes

Markdown drafts under `content/` can now be published automatically into `docs/notes/`.

Run:

```text
python scripts/build_notes.py
```

This scans `content/**/*.md`, renders note pages and directory indexes, and writes the generated site pages into `docs/notes/`.

For continuous rebuilds while editing:

```text
python scripts/build_notes.py --watch
```


## Free reading and training guide

Source guides live in `content/11_reading_guide/`; run `python3 scripts/build_notes.py` to regenerate `docs/notes/11-reading-guide/`. The directory README is the reading hub. Resource cards link to official sources; the convex optimization and reinforcement learning study notes contain original training examples.

The homepage, references, course overviews, and roadmap are hand-maintained HTML under `docs/`. Their guide links should be updated there when a guide is renamed. The notes builder does not regenerate those overview pages.
