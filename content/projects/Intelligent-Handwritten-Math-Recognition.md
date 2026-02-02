---
title: "Intelligent Handwritten Math Recognition"
date: 2025-12-21
tags: ["projects", "machine learning", "swift development", "LaTeX", "computer vision"]
summary: "A cross-platform LaTeX input assistant that recognizes handwritten mathematical symbols and provides ranked LaTeX command suggestions with live previews."
---

**Last Updated**

2025.01.04

---

**Status**

Production Ready (macOS), Cross-Platform Expansion Planned.

---

**Intelligent Handwritten Math Recognition** is a **cross-platform LaTeX input assistant** that recognizes handwritten mathematical symbols and provides ranked LaTeX command suggestions with live previews. Draw **one mathematical symbol** → Get **ranked LaTeX suggestions** with previews → **Quick selection** → **Copy to clipboard**.

> **Scope:** Single-symbol recognition for LaTeX input assistance (not full formula conversion)

## **🎉 Current Status: macOS App Complete & Ready**

The project has successfully delivered a fully functional macOS application with all core features implemented and tested:

* **Vision Engine**: CNN model trained (83.46% top-1, 98.08% top-5 accuracy)  
* **Semantic Engine**: Mathematical priority ranking with 369 symbol mappings  
* **macOS App**: Professional native app with LaTeX previews and auto-recognition  
* **Performance**: ~100ms recognition time on Apple Silicon, 2.9MB model size  
* **User Experience**: Keyboard shortcuts, choice memory, and professional UI

## **✨ Key Features**

### **🎨 Live LaTeX Previews**

* **Real-Time Rendering**: See exactly what each LaTeX command produces  
* **Unicode Support**: 100+ mathematical symbols rendered accurately  
* **Instant Feedback**: Live preview as you browse suggestions

### **🤖 Smart Auto-Recognition**

* **Configurable Delay**: 0.5-3.0s after drawing stops  
* **High Performance**: ~100ms recognition on Apple Silicon  
* **On-Device Processing**: Privacy-first, all processing happens locally

### **⭐ Intelligent Personalization**

* **Choice Memory**: Remembers your selections with "⭐ last chosen" markers  
* **User Preferences**: Adapts to your LaTeX command choices  
* **Smart Ranking**: Combines vision confidence (60%) + mathematical priority (40%)

### **⌨️ Efficient Workflow**

* **Keyboard Shortcuts**: Press 1-5 to select suggestions instantly  
* **Copy to Clipboard**: Seamless integration with LaTeX editors  
* **Professional UI**: Clean SwiftUI interface with numbered suggestions

## **🛠️ Technical Architecture**

The system is built with a modular, cross-platform architecture:

### **Vision Engine (PyTorch/CoreML)**

* **Model Performance**: 83.46% top-1, 98.08% top-5 accuracy (exceeded targets)  
* **Dataset**: HASYv2 with 369 mathematical symbol classes  
* **Architecture**: 4-layer CNN optimized for mobile deployment  
* **Export Formats**: CoreML (2.9MB) for iOS/macOS, ONNX (32KB) for Windows/Linux

### **Semantic Engine**

* **Ranking Algorithm**: Mathematical context-aware LaTeX candidate ranking  
* **Symbol Database**: Complete mappings for all 369 symbols with alternatives  
* **Integration API**: Clean interface for seamless UI integration  
* **Performance**: Optimized for real-time ranking operations

### **Cross-Platform Strategy**

* **macOS**: Native SwiftUI app with CoreML integration  
* **Windows/Linux**: Planned cross-platform expansion using ONNX Runtime  
* **Model Portability**: Single model, multiple deployment targets

### **Directory Structure**

```text
Intelligent-Handwritten-Math-Recognition/
├── vision_engine/          # ML model (PyTorch → ONNX/CoreML)
├── semantic_engine/        # LaTeX ranking and mapping
├── macos_app/             # Native macOS application
├── exports/               # Trained models (2.9MB CoreML, 32KB ONNX)
├── data/                  # HASYv2 dataset (369 symbol classes)
└── checkpoints/           # Training results and history
```

## **📊 Development Progress**

### **✅ Phase 1: Vision Engine (Complete)**

* **Model Training**: 50 epochs with MPS acceleration on Apple Silicon  
* **Data Augmentation**: Rotation, scaling, noise injection for robustness  
* **Validation**: Comprehensive testing on held-out data  
* **Export Optimization**: Model size optimized for on-device inference

### **✅ Phase 2: Semantic Engine (Complete)**

* **Mathematical Ranking**: Context-aware LaTeX command prioritization  
* **Extensible Mapping**: JSON-based symbol database for easy updates  
* **Performance**: Sub-millisecond ranking for real-time response  
* **Integration**: Clean API for UI components

### **✅ Phase 3: macOS App (Complete)**

* **SwiftUI Architecture**: Modern declarative UI with MVVM pattern  
* **CoreML Integration**: On-device inference with Apple Neural Engine  
* **User Experience**: Professional interface with haptic feedback  
* **Settings Panel**: Easy customization of preferences and behavior

### **📋 Phase 4: Cross-Platform Expansion (Planned)**

* **Framework Evaluation**: Electron vs Flutter vs Tauri for Windows/Linux  
* **ONNX Runtime**: Cross-platform model inference already prepared  
* **UI Consistency**: Maintain design language across platforms  
* **Platform Optimization**: Native file dialogs and system integration

## **🎮 Quick Start Guide**

### **macOS App (Ready Now)**

1. **Open**: `macos_app/MathSymbolRecognizer.xcodeproj`  
2. **Build**: Press ⌘B in Xcode  
3. **Run**: Press ⌘R to launch the application  
4. **Draw**: Sketch a mathematical symbol on the canvas  
5. **Select**: Click or press 1-5 to choose from suggestions  
6. **Paste**: LaTeX command is automatically copied to your clipboard!

### **Features to Try**

* **Auto-Recognition**: Draw and wait 1 second for automatic processing  
* **Settings**: Click gear icon to customize recognition delay and preferences  
* **Keyboard Shortcuts**: Use 1-5 for instant suggestion selection  
* **Choice Memory**: System learns and remembers your LaTeX preferences

## **📈 Performance Metrics**

* **Recognition Accuracy**: 83.46% top-1, 98.08% top-5  
* **Speed**: ~100ms recognition time on Apple Silicon  
* **Symbols Supported**: 369 mathematical symbols  
* **Memory Usage**: <50MB runtime footprint  
* **Model Size**: 2.9MB (CoreML), 32KB (ONNX)  
* **Drawing Performance**: 60fps smooth stroke capture

---

## Resources

* 📂 **GitHub Repository**:  

  <https://github.com/kaiiiichen/Intelligent-Handwritten-Math-Recognition>
  
* 🌐 **Project Documentation**:  

  See [README.md](https://github.com/kaiiiichen/Intelligent-Handwritten-Math-Recognition/blob/main/README.md) for detailed setup instructions
  
* 🗺️ **Development Roadmap**:  

  [ROADMAP.md](https://github.com/kaiiiichen/Intelligent-Handwritten-Math-Recognition/blob/main/ROADMAP.md) for complete progress tracking

---

## 🎯 Success Criteria: **Achieved**

✅ **High Accuracy**: Exceeded 70% target (achieved 83.46%)  
✅ **Fast Recognition**: Sub-second response time (~100ms)  
✅ **User-Friendly**: Intuitive interface with live LaTeX previews  
✅ **Personalized**: Learns user preferences with choice memory  
✅ **Professional**: Production-ready macOS app with polished UI  

The project has successfully delivered on its core promise: a practical, efficient tool for LaTeX symbol input that feels natural and professional to use.
