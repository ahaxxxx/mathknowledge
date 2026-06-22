# English Grammar, Reading, and Listening System Design

## 1. Purpose

Build a permanent, static English learning system for repeated self-study rather than a daily course or disposable exercise bank. The system should support progression from an upper-intermediate foundation toward educated native-level academic reading and research discourse while preserving substantial exposure to ordinary American life.

The content ratio is fixed at:

- 60% academic and research contexts.
- 40% authentic everyday contexts.

The system must distinguish grammatical complexity, discourse complexity, acoustic difficulty, and domain familiarity. These dimensions must not be collapsed into a single label such as "PhD level."

## 2. Design Principles

1. Grammar is taught as a form-meaning-function system, not as a list of prescriptions.
2. Every important form must be connected to an interpretation it licenses and a reading error it prevents.
3. Reading practice must reveal sentence structure, information structure, discourse relations, stance, and evidential strength.
4. Exercises remain available permanently and reveal complete explanations only on demand.
5. Listening levels must be justified by measurable and observable properties, not by topic prestige.
6. Synthetic speech must be identified as synthetic speech. It must not be presented as equivalent to spontaneous native interaction.
7. Existing clear TTS recordings remain useful as controlled input but must be relabelled accurately.

## 3. Information Architecture

The English landing page keeps two principal branches:

1. Grammar and reading.
2. Listening.

Each branch has a tree-shaped learning entrance. Pages are generated from Markdown by the existing static-note builder. The site requires no login, progress database, daily update, or server-side application.

## 4. Grammar and Reading Curriculum

The grammar and reading branch contains fourteen modules:

1. Clause skeletons and verb argument structure.
2. Tense, aspect, and temporal viewpoint.
3. Modality, counterfactuality, and hypothetical meaning.
4. Noun phrases, determiners, reference, and quantification.
5. Complement clauses and subordinate clause systems.
6. Relative clauses, apposition, and postmodification.
7. Non-finite clauses and structural downgrading.
8. Negation, scope, ambiguity, and interpretation.
9. Comparison, parallelism, coordination, and ellipsis.
10. Inversion, cleft constructions, emphasis, and information focus.
11. Nominalization and academic information compression.
12. Cohesion, reference chains, and paragraph-level continuity.
13. Stance, hedging, evidentiality, and strength of commitment.
14. Academic argument moves and research genres.

Morphology is integrated as a supporting layer across the modules and also receives a reference page covering productive roots, prefixes, suffixes, word families, and the limits of morphological inference.

### 4.1 Required Structure of Every Module

Each module contains:

1. The interpretive problem being solved.
2. Definitions and necessary terminology.
3. The relation between form, meaning, and discourse function.
4. Eight to twelve progressively denser sentence analyses.
5. At least one academic or research passage.
6. At least one everyday passage or dialogue excerpt where appropriate.
7. Boundary cases, ambiguities, and common misreadings.
8. Eight to twelve permanent self-training questions.
9. Expandable complete explanations.
10. Transfer questions asking the learner to explain why an analysis works and when it fails.

The initial release target is approximately 150 exercises and fourteen substantial reading sets. Exercises are not organized by date and do not expire.

## 5. Listening Taxonomy

Listening materials use two independent labels.

### 5.1 Language and Discourse Complexity

- B2-oriented.
- C1-oriented.
- C2-oriented.
- Research discourse.

"Research discourse" is a domain label, not a CEFR level above C2.

### 5.2 Acoustic Difficulty

- A1 Controlled: careful delivery with clear boundaries.
- A2 Natural: ordinary connected speech with weak forms and contractions.
- A3 Fast spontaneous: faster delivery, reductions, hesitation, repair, and implicit transitions.
- A4 Interactional: multiple speakers, interruptions, overlap, accent variation, and context-dependent omission.

A recording receives both labels, for example "C1-oriented / A3 Fast spontaneous."

### 5.3 Existing Audio

The current eight recordings are retained as controlled academic input. Their present B2, C1, C2, and PhD labels are revised so that the pages do not imply formal CEFR certification. Their measured speaking rates and synthetic origin are disclosed.

## 6. New Listening Library

The first natural-speech expansion contains fifteen scenarios.

### 6.1 Academic and Research: Nine Scenarios

1. Undergraduate lecture explanation.
2. Graduate lecture qualification of a claim.
3. Office-hour clarification.
4. Research-method discussion.
5. Laboratory or group meeting.
6. Seminar disagreement and reformulation.
7. Conference presentation transition.
8. Conference question and answer.
9. Dissertation-defense exchange.

### 6.2 Everyday American Life: Six Scenarios

1. Rescheduling an appointment.
2. Reporting a housing maintenance problem.
3. Resolving a banking or insurance misunderstanding.
4. Informal conversation between colleagues.
5. Responding to a travel disruption.
6. Negotiating a return, complaint, or service correction.

### 6.3 Required Structure of Every Listening Page

Each listening item contains:

1. Scenario and relationship between speakers.
2. Language-complexity and acoustic-difficulty labels.
3. Audio player with the transcript initially hidden.
4. First-listen questions about situation, purpose, and stance.
5. A complete transcript.
6. Connected-speech notes covering reductions, weak forms, linking, stress, and boundary loss.
7. Discourse notes covering implication, repair, qualification, and speaker intention.
8. A replay task focused on a different processing layer.
9. A complete expandable explanation.

## 7. Speech Generation and Source Policy

### 7.1 Preferred Synthetic Model

Use `gpt-4o-mini-tts` for new controlled synthetic recordings because instruction-based delivery control is required. Prefer `marin` or `cedar` after a short voice comparison. Do not use `tts-1` or `tts-1-hd` for instruction-dependent speaking style.

The currently configured `api.gptsapi.net` provider was tested on 2026-06-23 and returned `HTTP 400: model not found gpt-4o-mini-tts`. Bulk generation must not begin through this provider.

An acceptable provider must expose `gpt-4o-mini-tts` through the speech endpoint and honor the `instructions` field. API credentials remain outside the repository and are loaded from a local environment file.

### 7.2 Generation Validation

Before batch generation:

1. Generate one short academic sample and one short everyday sample.
2. Confirm that delivery instructions materially change the result.
3. Measure actual words per minute.
4. Inspect connected speech, pauses, and over-enunciation.
5. Approve the voice and acoustic target before generating the full set.

Synthetic speech is labelled "controlled synthetic speech." Authentic external recordings may be linked only from lawful, stable sources and must not be copied into the repository without an appropriate license.

## 8. Failure Handling

1. If the configured provider does not support the required model, stop before batch generation and report the model error without exposing credentials.
2. If a generated file falls outside its intended rate or style, regenerate it rather than changing the label to fit the output.
3. If multi-speaker synthesis sounds artificial, keep it in the controlled track and use a lawful authentic source for the A4 interactional track.
4. If a source link is unstable or its reuse rights are unclear, omit it.

## 9. Verification

Before publication:

1. Build every Markdown page successfully.
2. Verify that all internal links and audio paths resolve.
3. Scan generated pages for encoding errors and mojibake.
4. Confirm that every exercise has an expandable complete explanation.
5. Measure and record the duration and words per minute of every generated audio file.
6. Check that listening labels match observable features.
7. Inspect representative desktop and mobile pages in the browser for navigation, overflow, and readable mathematical or linguistic notation.
8. Confirm that no API key, environment value, or local secret path is committed.

## 10. Explicit Non-Goals

This release does not include:

- Daily assignments or automatic scheduling.
- Accounts, cloud progress tracking, or spaced-repetition state.
- A claim that synthetic recordings constitute a CEFR-certified examination.
- A claim that research subject matter alone makes a recording C2.
- Bulk audio generation before the target model and voice pass the two-sample validation gate.

