---
title: "Linux Daily-Driver & Systems Engineering Workstation"
date: 2025-12-03
draft: false
tags: ["roadmap", "linux", "fedora", "systems", "software engineering", "thinkpad"]
summary: "To build a reliable Fedora-first daily-driver workstation for programming and systems learning, with a reproducible toolchain, documented workflows, and a low-friction Windows fallback."
---

**Last Updated**

2025.12.23

---

**Core Objective:** To make Fedora on my ThinkPad a reliable daily-driver programming workstation, and use it as a hands-on lab to learn computer systems fundamentals—Linux workflows, OS concepts, system architecture, debugging/performance tooling, and reproducible development environments—while keeping Windows as a clean fallback for a small set of apps/games.

---

## 1. Problem Statement & Philosophy

I want a Linux-first setup that is **boringly reliable** day-to-day, but also **deeply hackable** when I’m learning systems: everything from filesystems and processes to performance profiling and low-level debugging.

The core tension is simple:

1. **Daily-driver stability:** Updates should not break my workflow; sleep/wake and Wi‑Fi should be predictable; tools should be easy to maintain.
2. **Systems learning:** I need a real environment where I can observe, measure, and experiment with how software interacts with the OS and hardware.

### 1.1 Why Fedora as the Primary OS

Fedora gives me a modern Linux stack (newer kernels, toolchains, and desktop components) without turning my machine into a perpetual science fair. It’s a good compromise between “fresh” and “stable” for learning systems while still shipping real work.

### 1.2 Philosophy: Reproducibility Over Heroics

Instead of relying on “I remember how I set this up,” I want:

- **Configuration as code:** dotfiles, scripts, and a documented setup process.
- **Isolation when experimenting:** containers/virtualization to keep the base system clean.
- **Learning by measurement:** performance tools and debugging workflows that turn vague feelings into evidence.

---

## 2. Technical Stack

* **Hardware & Boot:**
    * ThinkPad workstation setup.
    * UEFI dual-boot: Fedora (primary) + Windows (fallback).
* **Linux Platform:**
    * Fedora Workstation (GNOME) as the daily OS.
    * Btrfs by default (snapshots/rollback-friendly), with a simple, understandable partition plan.
* **Development Toolchain (General):**
    * Git + SSH, modern terminal workflow.
    * Editors/IDEs: VS Code and/or Neovim.
    * Build systems: CMake + Ninja, Make (as needed).
* **Languages (Systems + SWE):**
    * C/C++ toolchains: GCC/Clang.
    * Python (venv/uv), plus a clean dependency strategy.
    * Rust and Go for systems-side experimentation.
* **Systems & Debugging Toolkit:**
    * strace/ltrace for syscall/library tracing.
    * gdb/lldb for debugging.
    * perf + flamegraphs for profiling.
    * valgrind (selectively) for memory diagnostics.
    * ELF tooling: readelf/objdump/nm.
* **Dev Environments & Isolation:**
    * Podman (rootless) for containers.
    * toolbx / distrobox (optional) for quick disposable dev shells.
* **Architecture/OS Experiments:**
    * QEMU/KVM + virt-manager for controlled labs.
* **Cross-Device Workflow (Mac ↔ Linux):**
    * Syncthing for file sync (projects/notes/data).
    * Optional shared clipboard/input tooling when both machines are on the same LAN.

---

## 3. Development Roadmap

### Phase 1: Daily-Driver Baseline (Stability First)
*Goal: A Fedora environment I can rely on every day without thinking about it.*

- [✅] **Boot & Reliability:**
    - Make Fedora the default boot target; keep Windows clean and minimal.
    - Validate sleep/wake behavior and fix any recurring issues.
- [ ] **Core Developer Setup:**
    - Install a minimal, consistent toolchain (git, compilers, editor, build tools).
    - Establish a standard project directory layout (e.g., `~/dev`, `~/notes`, `~/data`).
- [ ] **Storage & Backups:**
    - Decide what is stored on Fedora vs. shared storage.
    - Set up a backup routine (local + off-device) that is actually used.

### Phase 2: Environment as Code (Reproducibility)
*Goal: A new machine can be “ready to code” quickly, predictably, and repeatably.*

- [ ] **Dotfiles Repository:**
    - Version shell/editor/git configs; document decisions.
    - Add a minimal bootstrap script (install essentials + link configs).
- [ ] **Language Environment Hygiene:**
    - Standardize Python environments (venv/uv) and Node/Rust/Go installs.
    - Avoid global dependency spaghetti.
- [ ] **Developer Ergonomics:**
    - Terminal workflow (tmux, shortcuts, search tools).
    - Consistent fonts/input method setup for bilingual work (if needed).

### Phase 3: Systems Learning Through Micro-Projects (Evidence > Opinions)
*Goal: Learn core OS and architecture concepts by building and measuring real artifacts.*

- [ ] **Processes & Syscalls:**
    - Write small C programs; observe behavior with `strace`.
    - Explore signals, pipes, file descriptors, and process trees.
- [ ] **Memory & Performance:**
    - Build minimal benchmarks; profile with `perf`.
    - Investigate caching, page faults, allocation behavior, and I/O patterns.
- [ ] **Filesystems & I/O:**
    - Study mount points, permissions, and practical storage debugging.
    - Measure read/write patterns and latency trade-offs.
- [ ] **Networking Basics (Practical):**
    - DNS, routing, ports, and sockets through small experiments.
    - Learn to debug “it doesn’t connect” systematically.

### Phase 4: Advanced Topics & Long-Term Maintainability
*Goal: Turn the workstation into a long-lived “systems lab” that stays clean.*

- [ ] **Virtualization/Emulation Labs:**
    - QEMU experiments: minimal Linux boot, init systems, kernel parameters.
- [ ] **Observability Playbooks:**
    - Create a personal debugging handbook: “slow”, “hot”, “leaky”, “broken network”.
- [ ] **Optional Hardening:**
    - A simple security baseline (updates, sensible defaults, minimal exposure).
    - A rollback plan (snapshots + rescue boot strategy).

---

## 4. Future Outlook

- **A personal systems notebook:** concise writeups, pitfalls, and debugging recipes that compound over time.
- **Reusable project templates:** starter repos for C/C++/Rust/Python with clean builds and tests.
- **Frictionless cross-device workflow:** predictable sync, backups, and a low-maintenance setup that keeps working even when I’m busy.

---

**Status**

Ongoing.
