---
title: "SudoSodoku"
date: 2025-12-18
tags: ["projects", "swift development", "ios development"]
summary: "A terminal-style Sudoku experience for iOS, designed for logical purists."
---

### Last Updated

2025.12.17

---

**SudoSodoku** is a minimalist, keyboard-centric (conceptually) puzzle game that brings the Linux terminal aesthetic to your iPhone. It features a robust puzzle generator, an ELO rating system, and a "Juice" interaction model with haptic feedback.

### **✨ Features**

- **Terminal Aesthetic**: Green phosphor look on deep dark background (#0D121A).
- **Infinite Puzzles**: Real-time Sudoku generator with unique solutions.
- **ELO Rating System**:
  - **Dynamic Difficulty**: Easy, Medium, Hard, Master.
  - **Ranking Titles**: From SCRIPT_KIDDIE to THE_ARCHITECT.
  - **Anti-Smurfing**: Intelligent score calculation.
- **Advanced Tools**:
  - **Pencil Mode**: For candidate notes.
  - **Undo/Redo Stack**: Fearless experimentation.
  - **Archives**: Save unfinished games automatically; Favorite your best runs.
- **Native Integration**:
  - **Game Center**: Seamless login and user profile.
  - **iCloud Sync**: (Optional) Cross-device save data synchronization.
  - **Haptics**: Satisfying mechanical feedback.

### **🛠️ Architecture**

- **Language**: Swift 5
- **UI Framework**: SwiftUI
- **Data Flow**: ObservableObject + Combine
- **Persistence**: Codable -> JSON (Local/iCloud Documents)
- **Algorithm**: Backtracking solver & Human-like difficulty evaluator.

### Resources

- 📂 **GitHub Repository**:  
  https://github.com/kaiiiichen/SudoSodoku

---

### Status

Maintaining.
