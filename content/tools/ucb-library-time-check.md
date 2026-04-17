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
Last Update: 2026-04-17 08:07:37 PDT
Data Source: https://www.lib.berkeley.edu/hours
============================================================

Now Open (4)：
🟢 Berkeley Law Library — 8 a.m.-6 p.m.
🟢 Business Library — 7 a.m.-10 p.m.
🟢 Doe Library — 8 a.m.-10 p.m.
🟢 Graduate Services (study only) — 8 a.m.-10 p.m.

Now Closed (18)：
🔴 Art History/Classics Library
🔴 Bancroft Library
🔴 Bioscience, Natural Resources & Public Health Library
🔴 Chemistry, Astronomy & Physics Library
🔴 East Asian Library
🔴 Engineering & Mathematical Sciences Library
🔴 Environmental Design Library
🔴 Ethnic Studies Library
🔴 Institute of Governmental Studies Library
🔴 Institute of Transportation Studies Library
🔴 Main (Gardner) Stacks
🔴 Moffitt Library (temporarily closed)
🔴 Morrison Library
🔴 Music Library
🔴 Newspapers & Microforms Library
... and other 3 libraries are closed.

Status Unknown (5)：
⚪ Print + scan
⚪ Berkeley Art Museum and Pacific Film Archive
⚪ Environmental Design Archives
⚪ Graduate Theological Union Library
⚪ Lawrence Berkeley National Laboratory Library

============================================================
```

<!-- END_UCB_LIB_TIME_OUTPUT -->
