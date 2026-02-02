---
title: "UC Berkeley Library Time Check"
date: 2026-02-01
tags: ["tools", "UC Berkeley", "library"]
summary: "显示 ucb_lib_time 脚本的最新运行结果（自动更新）"
---

这个页面**只展示脚本的最新运行结果**（类似 terminal 输出）。

- 数据源：`https://www.lib.berkeley.edu/hours`
- 更新方式：GitHub Actions 定时运行原始抓取逻辑，把结果写回本页面

<!-- BEGIN_UCB_LIB_TIME_OUTPUT -->

```text
============================================================
UC Berkeley 图书馆开放状态
更新时间: 2026-02-01 23:31:20 PST
数据源: https://www.lib.berkeley.edu/hours
============================================================

当前开放的图书馆 (2个)：
🟢 Doe Library — 1 p.m.-6 a.m.
🟢 Main (Gardner) Stacks — 1 p.m.-2 a.m.

已关闭的图书馆 (23个)：
🔴 Art History/Classics Library
🔴 Bancroft Library
🔴 Berkeley Art Museum and Pacific Film Archive
🔴 Berkeley Law Library
🔴 Bioscience, Natural Resources & Public Health Library
🔴 Business Library
🔴 Chemistry, Astronomy & Physics Library
🔴 East Asian Library
🔴 Engineering & Mathematical Sciences Library
🔴 Environmental Design Archives
🔴 Environmental Design Library
🔴 Ethnic Studies Library
🔴 Graduate Services (study only)
🔴 Graduate Theological Union Library
🔴 Institute of Governmental Studies Library
... 还有 8 个图书馆已关闭

状态未知 (2个)：
⚪ Print + scan
⚪ Lawrence Berkeley National Laboratory Library

============================================================
```

<!-- END_UCB_LIB_TIME_OUTPUT -->
