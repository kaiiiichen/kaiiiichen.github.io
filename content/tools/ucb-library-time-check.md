---
title: "UC Berkeley Library Time Check"
date: 2026-02-01
tags: ["tools", "UC Berkeley", "library"]
summary: "Show the latest opening status of all UC Berkeley Libraries."
---
- We update using GitHub Actions to automatically run actions on the page and print the result here.
- Remember that you can study overnight in some libraries.
- For overnight information, visit [https://www.lib.berkeley.edu/hours](https://www.lib.berkeley.edu/hours) and pay attention that they are displayed in the form like '8 a.m. - 6 a.m.', which means it opens till 6 a.m. next morning.
- These kinds of information are listed in the details of a library's opening hours details and you need to click on the library to see them, which also makes Python Web Scraper a bit complex to do (so this feature is not integrated here :D).

<!-- BEGIN_UCB_LIB_TIME_OUTPUT -->

```text
============================================================
UC Berkeley Library Open Status
Last Update: 2026-02-02 09:26:39 PST
Data Source: https://www.lib.berkeley.edu/hours
============================================================

Now Open (13)：
🟢 Art History/Classics Library — 9 a.m.-8 p.m.
🟢 Berkeley Law Library — 8 a.m.-9 p.m.
🟢 Bioscience, Natural Resources & Public Health Library — 9 a.m.-9 p.m.
🟢 Business Library — 7 a.m.-10 p.m.
🟢 Chemistry, Astronomy & Physics Library — 9 a.m.-10 p.m.
🟢 Doe Library — 8 a.m.-6 a.m.
🟢 East Asian Library — 9 a.m.-10 p.m.
🟢 Engineering & Mathematical Sciences Library — 9 a.m.-11 p.m.
🟢 Environmental Design Library — 9 a.m.-10 p.m.
🟢 Graduate Services (study only) — 8 a.m.-10 p.m.
🟢 Institute of Governmental Studies Library — 9 a.m.-5 p.m.
🟢 Main (Gardner) Stacks — 9 a.m.-2 a.m.
🟢 Music Library — 9 a.m.-8 p.m.

Now Closed (9)：
🔴 Bancroft Library
🔴 Ethnic Studies Library
🔴 Institute of Transportation Studies Library
🔴 Moffitt Library (temporarily closed)
🔴 Morrison Library
🔴 Newspapers & Microforms Library
🔴 Social Research Library
🔴 South/Southeast Asia Library (study only)
🔴 Systemwide Library Facility-North

Status Unknown (5)：
⚪ Print + scan
⚪ Berkeley Art Museum and Pacific Film Archive
⚪ Environmental Design Archives
⚪ Graduate Theological Union Library
⚪ Lawrence Berkeley National Laboratory Library

============================================================
```

<!-- END_UCB_LIB_TIME_OUTPUT -->
