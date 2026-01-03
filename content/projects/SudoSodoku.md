---
title: "SudoSodoku"
date: 2025-12-05
tags: ["projects", "swift development", "ios development"]
summary: "A terminal-style Sudoku experience for iOS, designed for logical purists."
---

**Last Updated**

2026.01.02

---

**Status**

Maintaining.

---

**SudoSodoku** is a minimalist, keyboard-centric (conceptually) puzzle game that brings the Linux terminal aesthetic to your iPhone. It strips away the distractions of modern casual games, offering a raw, focus-driven environment powered by a robust algorithmic core.

### **🎉 v1.0.0 - First Official Release**

We are thrilled to announce the first stable release of SudoSodoku\! This version represents a complete, polished game with all core features implemented and tested:

* **Procedural Puzzle Generation**: Real-time generation of unique, solvable puzzles.  
* **Four Difficulty Levels**: Easy, Medium, Hard, and Master with intelligent scoring.  
* **Pencil Mode**: Toggle candidate notes for complex deduction strategies.  
* **Undo/Redo System**: Full history stack for fearless experimentation.  
* **Smart Archives**: Automatic saving with favorites and replay functionality.  
* **ELO Rating System**: Competitive ranking from SCRIPT\_KIDDIE to THE\_ARCHITECT.  
* **Terminal Aesthetic**: Authentic green phosphor UI with haptic feedback.  
* **Modular Architecture**: Clean, maintainable codebase organized by feature.

## **✨ Features**

### **🖥️ Immersive Terminal Aesthetic**

* **Visuals**: Authentic Green Phosphor (\#00FF00) on Deep Dark Background (\#0D121A).  
* **Feedback**: "Juice" interaction model with UIImpactFeedbackGenerator providing mechanical-keyboard-like haptics for every input.  
* **Animations**: Matrix-style victory effects and CRT-like glow pulses.

### **♾️ Infinite Procedural Generation**

* **Real-time Engine**: Generates unique, solvable puzzles on-the-fly using a randomized **Backtracking Algorithm**.  
* **Human-like Grading**: Difficulty is not determined by random holes, but by a **Logical Solver** that simulates human techniques (Naked Singles, Hidden Singles, etc.) to assign a precise difficulty score (0-100).

### **🏆 Competitive ELO System**

* **Dynamic Rating**: Starts at 1200 (USER). Beats puzzles to rank up.  
* **Adaptive K-Factor**: Rating changes stabilize as you reach higher tiers (Master/Grandmaster).  
* **Anti-Smurfing**: High-level players gain zero rating from solving low-level puzzles.  
* **Rank Titles**:  
  * \< 1200: SCRIPT\_KIDDIE  
  * 1200 \- 1400: USER  
  * ...  
  * 2000+: THE\_ARCHITECT

### **💾 Robust Persistence**

* **Game Center Integration**: Seamless, password-less login and user profile management.  
* **Cloud Sync**: Leveraging **iCloud Documents** to sync game states and archives across devices (automatically degrades to local storage if iCloud is unavailable).  
* **JSON Serialization**: All game records are stored as Codable JSON structs, ensuring backward compatibility and easy migration.

## **🛠️ Technical Architecture**

SudoSodoku is built with modern iOS technologies, designed for maintainability and performance:

* **Language**: Swift 5.9  
* **UI Framework**: SwiftUI (Apple's modern declarative UI framework)  
* **Architecture**: MVVM (Model-View-ViewModel) pattern for clean code organization  
* **State Management**: Reactive updates using Combine framework  
* **Data Persistence**:  
  * Automatic cloud sync via iCloud (with local fallback)  
  * Safe file operations with atomic writes  
  * Backward-compatible data migration  
* **User Experience**: Custom animations and haptic feedback for a polished feel

### **Directory Structure**

```
SudoSodoku/
├── Models/
│   ├── GameRecord.swift          # Codable save data structure
│   ├── SudokuCell.swift          # Unit cell model
│   ├── MoveHistory.swift         # Move history for undo/redo
│   └── Difficulty.swift          # Enum with rating ranges
├── ViewModels/
│   └── SudokuGame.swift          # Core game logic & state machine
├── Managers/
│   ├── GameCenterManager.swift   # GameKit authentication
│   ├── RatingManager.swift       # ELO calculation algorithms
│   ├── HapticManager.swift      # Haptic feedback engine
│   └── StorageManager.swift      # File I/O & Cloud syncing
├── Views/
│   ├── ContentView.swift         # Main entry & NavigationStack
│   ├── LandingView.swift         # Landing page
│   ├── GameView.swift            # The game board
│   ├── UserProfileView.swift     # User profile & statistics
│   ├── ArchiveView.swift         # History & Favorites list
│   ├── ModeSelectionView.swift   # Difficulty selection
│   ├── BoardView.swift           # Sudoku board rendering
│   ├── ControlPanelView.swift    # Game controls (undo/redo/numpad)
│   ├── Components/
│   │   ├── TerminalBackground.swift    # Terminal-style background
│   │   ├── MatrixVictoryOverlay.swift  # Victory animation
│   │   ├── NoteGridView.swift          # Note display grid
│   │   ├── GridLinesOverlay.swift      # Board grid lines
│   │   ├── StatCard.swift              # Statistics card component
│   │   ├── RankRow.swift               # Rank display row
│   │   └── RecordRow.swift             # Archive record row
│   └── Styles/
│       └── BouncyButtonStyle.swift     # Button animation style
└── Algorithms/
    └── SudokuGenerator.swift     # Backtracking & Digging logic
```

---

## Resources

* 📂 **GitHub Repository**:  

  <https://github.com/kaiiiichen/SudoSodoku>
  
* 🌱 **Latest Release**:

  [2026.01.02] [SudoSodoku v1.0.0: First Official Release](https://github.com/kaiiiichen/SudoSodoku/releases/tag/v1.0.0)
  
* 📜 **Release History**:

  * [2026.01.02] [SudoSodoku v1.0.0: First Official Release](https://github.com/kaiiiichen/SudoSodoku/releases/tag/v1.0.0)  
  * [2025.12.22] [SudoSodoku v0.5.0 Beta: The Terminal Awakening](https://github.com/kaiiiichen/SudoSodoku/releases/tag/v0.5.0)
