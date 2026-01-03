---
title: "Intelligent-Handwritten-Math-Recognition"
date: 2025-12-21
draft: false
tags: ["roadmap", "LaTeX", "machine learning", "swift development"]
summary: "A cross-platform LaTeX input assistant: users draw a single math symbol, and the app suggests ranked LaTeX candidates with a mathematically-informed preference order."
---

**Last Updated**

2025.12.23

---

**Status**

Getting Started.

---

## Core Objective

Build a **cross-platform LaTeX input assistant**: the user intentionally draws **one mathematical symbol**, and the system returns a **ranked suggestion list** of possible LaTeX commands (each with rendered preview), so the user can **choose the intended one** quickly and reliably.

> **Scope boundary (important):** this project targets **single-symbol recognition for LaTeX input assistance**, *not* full handwritten formula-to-LaTeX conversion.

---

## 1. Problem Statement & Philosophy

### 1.1 What’s broken in existing tools

Many handwriting/OCR tools for math fail in two recurring ways:

1. **Visual fragility:** subtle glyph differences in handwriting cause high error rates.
2. **Math-unaware outputs:** they treat symbols as images rather than mathematical entities (e.g., `\Sigma` vs. `\sum`, or `\Rightarrow` vs. `\implies`).

This roadmap is designed around a pragmatic truth:

> **For single symbols, ambiguity is normal.** A great tool shouldn’t pretend ambiguity doesn’t exist — it should present *good candidates*, ordered by mathematical sense, and let the user decide.

### 1.2 The Technical Rationale: Vision vs. Trajectory

Why prefer **offline-style vision recognition** (shape-based) over **trajectory/pen-order** approaches?

- **The stroke-order dilemma:** unlike Chinese characters, mathematical symbols have *no canonical stroke order*, and personal style variance is huge.
  - Sigma (`\Sigma`) can be 1 stroke or multiple strokes.
  - Integral (`\int`) can be top-down or bottom-up.
- **Design decision:** even if we collect input on-device (finger/stylus), we intentionally treat the drawing as a **final geometric shape**.
  - We can rasterize strokes into an image and run a CNN/ViT-style classifier.
  - Time order becomes (at most) a weak auxiliary signal — never a hard assumption.

Result: **stroke-order invariance** and a cleaner engineering path for a robust MVP.

### 1.3 Our Philosophy: A Decoupled, Tool-First Architecture

Instead of forcing one model to learn *everything*, we split the system into:

- **Vision Engine (Shape → Symbol hypotheses):** classify the drawn shape into a shortlist of likely symbol classes.
- **Semantic Suggestion Engine (Symbol hypotheses → LaTeX candidates):** map each symbol class to **multiple LaTeX candidates**, then **rank them** with mathematically informed heuristics (and light personalization).

Crucially, the system is a **suggestion tool**, not an oracle:

- We aim for *high-quality top-k* recommendations.
- The final selection remains user-controlled.

---

## 2. User Experience Spec (the product contract)

### 2.1 Output format: ranked candidate list

For each user input, show a list like:

1. `\implies`  ⇒  (Rendered preview)   **Recommended**
2. `\Rightarrow`  ⇒  (Rendered preview)
3. `\rightarrow`  →  (Rendered preview)

Each item includes:

- LaTeX command
- Rendered preview (offline if possible)
- Optional short hint (e.g., “logical implication”, “mapping”, “derivation arrow”)

### 2.2 Mathematical preference order (not just “most likely”)

Ranking is **not purely visual**. Some commands are more mathematically appropriate defaults:

- Double arrow is visually similar across contexts, but `\implies` is often the best default in logic-heavy use.
- `\rightarrow` is common for functions/mappings; it shouldn’t silently replace implication.

So the system ranks by a blend of:

- **visual confidence** (Vision Engine)
- **math preference** (Semantic Suggestion Engine, by mode or heuristics)
- **light personalization** (see next section)

### 2.3 Interaction memory: “Last time you chose …”

Add a lightweight user history feature:

- When the user selects a candidate for a given symbol (or symbol cluster), store that choice.
- Next time the user draws a similar symbol, the suggestion list stays **mathematically ranked**, but the previously chosen candidate gets a subtle marker, e.g.:
  - “★ last chosen”
  - or a small badge “last time”

This preserves mathematical correctness **and** respects the user’s personal habits.

---

## 3. Technical Stack

### Machine Learning (The “Brain”)

- **Framework:** PyTorch (training), ONNX (interoperability).
- **Architecture:** CNN baseline (ResNet/MobileNet variants optimized for symbol classification).
  - Future upgrade path: lightweight ViT / attention-augmented CNN if needed.
- **Datasets:** HASYv2 (primary), CROHME (symbol extraction), MNIST/EMNIST (prototyping).

### macOS Client (The MVP)

- **Language:** Swift
- **UI:** SwiftUI
- **Inference:** CoreML (Apple Neural Engine where available)

### Cross-Platform (Future)

- **Framework:** Electron or Flutter (evaluate)
- **Inference:** ONNX Runtime

---

## 4. Development Roadmap

### Phase 1: Vision Engine (Python/PyTorch)

*Goal: robust top-k symbol hypotheses over 300+ symbols (optimize for top-1 and top-5).*

- [ ] **Data pipeline**
  - Load HASYv2 + extracted CROHME symbols
  - Augmentation: rotation, translation, noise, stroke-width variation, erosion/dilation
- [ ] **Model baselines**
  - MNIST/EMNIST sanity run (training loop validation)
  - CNN baseline on symbol dataset (report top-1/top-5)
- [ ] **Export**
  - Convert to `.onnx` and `.mlpackage`

### Phase 2: Semantic Suggestion Engine (Logic + Ranking)

*Goal: map symbol hypotheses to ranked LaTeX candidates with mathematical preferences.*

- [ ] **Mapping database**
  - `Visual_Class_ID -> [LaTeX_Candidate...]`
  - Keep it strictly typed and auditable
- [ ] **Ranking**
  - Combine `VisionScore` + `MathPreferenceScore` (+ optional mode boosts)
  - Example: in “Logic Mode”, boost `\implies` above `\rightarrow`
- [ ] **Candidate rendering**
  - Render preview for each candidate (prefer offline rendering where feasible)

### Phase 3: Personalization Layer (Interaction Memory)

*Goal: improve UX without corrupting math ranking.*

- [ ] Store per-user last-choice records keyed by symbol class (and optionally style cluster).
- [ ] In UI, mark “last chosen” candidate while keeping the canonical ranked order.
- [ ] Provide an option to clear history.

### Phase 4: macOS MVP (Swift)

*Goal: a native, fast Mac app that feels like a real tool, not a demo.*

- [ ] **Canvas**
  - High-performance drawing canvas (stroke capture + rasterization)
  - Client-side preprocessing (grayscale, resize, normalize)
- [ ] **CoreML integration**
  - On-demand inference + top-k outputs
- [ ] **UI/UX**
  - Suggestion list (LaTeX + rendered symbol)
  - Copy-to-clipboard
  - “last chosen” marker + optional tooltip

### Phase 5: Cross-Platform Expansion

*Goal: bring it to Windows and Linux.*

- [ ] Evaluate Electron vs. Flutter
- [ ] Adopt ONNX Runtime on non-Apple devices
- [ ] Port UI while preserving minimal aesthetics

---

## 5. Future Outlook

### 5.1 Offline LaTeX rendering improvements

- Better local rendering quality
- Faster previews
- Optional caching of frequent symbols

### 5.2 From single symbol → full handwritten formula to LaTeX (HMER)

After the single-symbol tool is stable, a natural next step is expanding toward **full handwritten mathematical expression recognition (HMER)**: converting complete handwritten formulas into LaTeX.

A realistic, extensible path is **structure-aware and modular**:

- segmentation / symbol grouping
- symbol classification (reusing this project’s Vision Engine)
- spatial relation prediction (superscripts, fractions, radicals, etc.)
- structure tree/graph construction
- LaTeX generation

Recent work on **structural** HMER (e.g., arXiv:2508.19773) suggests that modular, structure-aware pipelines can provide stronger interpretability and extensibility than purely end-to-end generation.

### 5.3 Personalization beyond memory (optional)

- Carefully explore per-user adaptation only after we have strong baselines
- Default stance: **don’t overfit to one user** unless the UX clearly benefits
