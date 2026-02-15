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
Last Update: 2026-02-15 12:59:51 PST
Data Source: https://www.lib.berkeley.edu/hours
============================================================

Now Open (3)：
🟢 Berkeley Law Library — 10 a.m.-6 p.m.
🟢 Business Library — 7 a.m.-10 p.m.
🟢 East Asian Library — 12 p.m.-8 p.m.

Now Closed (22)：
🔴 Art History/Classics Library
🔴 Bancroft Library
🔴 Berkeley Art Museum and Pacific Film Archive
🔴 Bioscience, Natural Resources & Public Health Library
🔴 Chemistry, Astronomy & Physics Library
🔴 Doe Library
🔴 Engineering & Mathematical Sciences Library
🔴 Environmental Design Archives
🔴 Environmental Design Library
🔴 Ethnic Studies Library
🔴 Graduate Services (study only)
🔴 Graduate Theological Union Library
🔴 Institute of Governmental Studies Library
🔴 Institute of Transportation Studies Library
🔴 Main (Gardner) Stacks
... and other 7 libraries are closed.

Status Unknown (2)：
⚪ Print + scan
⚪ Lawrence Berkeley National Laboratory Library

============================================================
```

<!-- END_UCB_LIB_TIME_OUTPUT -->
