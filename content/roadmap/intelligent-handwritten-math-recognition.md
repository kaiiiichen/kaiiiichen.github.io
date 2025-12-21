---
title: "Intelligent Handwritten Math Recognition"
date: 2025-12-22
tags: ["roadmap", "LaTeX", "machine-learning"]
summary: "To build a cross-platform tool that translates handwritten mathematical symbols into LaTeX with high visual accuracy and context-aware semantic precision."
---

**Last Updated**

2025.12.22

---

# Project Roadmap: Intelligent Handwritten Math Recognition

**Core Objective:** 

To build a cross-platform tool that translates handwritten mathematical symbols into LaTeX with high visual accuracy and context-aware semantic precision.

---

## 1. Problem Statement & Philosophy

Existing handwriting recognition tools for mathematics often suffer from two major flaws:
1.  **Low Accuracy:** Generic OCR models struggle with the subtle nuances of handwritten mathematical glyphs.
2.  **Lack of Mathematical Context:** They treat symbols as mere images (Image Classification) rather than mathematical entities. For example, they fail to distinguish between the visual shape of a Sigma ($\Sigma$) and the summation operator ($\sum$), or a generic arrow ($\rightarrow$) versus an implication ($\implies$).

**Our Philosophy: The Decoupled Architecture** 

Instead of forcing a single model to learn both shape and context, we decouple the system into two distinct layers:

* **The Vision Layer:** A CNN-based model dedicated purely to high-precision shape recognition.

* **The Semantic Layer:** A logic-based post-processing engine that maps shapes to LaTeX code based on user-selected mathematical contexts (e.g., Calculus, Algebra, Logic).

---

## 2. Technical Stack

* **Machine Learning (The "Brain"):**
    * **Framework:** PyTorch (Training), ONNX (Interoperability).
    * **Architecture:** Customized CNN (ResNet/MobileNet variants optimized for character recognition).
    * **Datasets:** HASYv2 (primary), CROHME (extracted symbols), MNIST (prototyping).
* **macOS Client (The "MVP"):**
    * **Language:** Swift.
    * **UI Framework:** SwiftUI.
    * **Inference:** CoreML (utilizing Apple Neural Engine).
* **Cross-Platform (Future):**
    * **Framework:** Electron or Flutter.
    * **Inference:** ONNX Runtime.

---

## 3. Development Roadmap

### Phase 1: The Vision Engine (Python/PyTorch)

*Goal: Train a model that can distinguish 300+ mathematical symbol shapes with >95% accuracy.*

- [ ] **Data Pipeline Setup:** 
    - Implement data loaders for HASYv2 and CROHME.
    - Develop a robust Data Augmentation pipeline (rotation, noise, stroke width variation) to simulate real-world handwriting.
- [ ] **Model Prototyping:**
    - Train a baseline model on MNIST/EMNIST to validate the training loop.
    - Train Deep CNN on mathematical symbol datasets.
- [ ] **Model Export:** 
    - Convert trained PyTorch models to `.onnx` and `.mlpackage` (CoreML) formats.

### Phase 2: The Semantic Mapping Layer (Logic)

*Goal: Solve the "Context Problem" (e.g., \Sigma vs. \sum).*

- [ ] **Mapping Database:**
    - Create a strictly typed dictionary mapping `Visual_Class_ID` to multiple `LaTeX_Candidate` outputs.
- [ ] **Context Engine:**
    - Implement "Mode Switching" logic (e.g., *Calculus Mode*, *Linear Algebra Mode*, *Set Theory Mode*).
    - Design a probability boosting algorithm: if `Mode == Logic`, boost rank of `\implies` over `\rightarrow`.

### Phase 3: macOS MVP Implementation (Swift)

*Goal: A native, high-performance Mac app.*

- [ ] **Canvas Logic:**
    - Build a high-performance drawing canvas in SwiftUI (Path/Stroke handling).
    - Implement image pre-processing on the client side (grayscale, resizing) to match model input requirements.
- [ ] **CoreML Integration:**
    - Hook up the `.mlpackage` model for real-time or on-demand inference.
- [ ] **UI/UX:**
    - Display "Top-k" candidates sorted by our Semantic Engine.
    - One-click copy to clipboard functionality.

### Phase 4: Cross-Platform Expansion

*Goal: Bring the experience to Windows and Linux.*

- [ ] **Tech Evaluation:** Assess Electron vs. Flutter for desktop targets.
- [ ] **Runtime Migration:** Implement ONNX Runtime for non-Apple hardware acceleration.
- [ ] **UI Porting:** Replicate the macOS minimal aesthetic on Windows/Linux.

---

## 4. Future Outlook

* **Offline LaTeX Rendering:** Preview the rendered math symbol locally without needing an internet connection.
* **Full Equation Recognition:** Expanding from single symbol recognition to full equation sequence parsing (seq2seq models).
* **User Personalization:** Allow the model to "finetune" on the specific user's handwriting style over time.

---

**Status**

Getting Started.
