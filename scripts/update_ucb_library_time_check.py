#!/usr/bin/env python3
"""
Update `content/tools/ucb-library-time-check.md` with latest output.

This script fetches https://www.lib.berkeley.edu/hours and parses library open/closed
status similar to the original `ucb_lib_time/berkeley_library_status.py`, then writes
the formatted output into the markdown file between markers:

  <!-- BEGIN_UCB_LIB_TIME_OUTPUT -->
  <!-- END_UCB_LIB_TIME_OUTPUT -->
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import pytz
import requests
from bs4 import BeautifulSoup


UCB_HOURS_URL = "https://www.lib.berkeley.edu/hours"
PACIFIC_TZ = pytz.timezone("America/Los_Angeles")

MARKER_BEGIN = "<!-- BEGIN_UCB_LIB_TIME_OUTPUT -->"
MARKER_END = "<!-- END_UCB_LIB_TIME_OUTPUT -->"

MD_PATH = "content/tools/ucb-library-time-check.md"


@dataclass(frozen=True)
class Library:
    name: str
    status: str  # Open / Closed / Unknown
    hours: Optional[str]
    url: str


def fetch_html(url: str) -> str:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }
    )
    resp = session.get(url, timeout=20)
    resp.raise_for_status()
    return resp.text


def parse_libraries(html: str) -> List[Library]:
    soup = BeautifulSoup(html, "html.parser")
    libraries: List[Library] = []
    seen = set()

    # Mirror original approach: scan all <li>, find <a href="/visit/...">
    for item in soup.find_all("li"):
        name_link = item.find("a", href=re.compile(r"/visit/"))
        if not name_link:
            continue

        name = name_link.get_text(strip=True)
        if (
            not name
            or "View" in name
            or "Map" in name
            or name in seen
        ):
            continue

        seen.add(name)

        item_text = item.get_text(separator=" ", strip=True)
        status = "Unknown"
        hours: Optional[str] = None

        if re.search(r"\bClosed\b", item_text, re.I):
            status = "Closed"
        else:
            hours_pattern = re.compile(
                r"(\d{1,2}\s+(?:a\.m\.|p\.m\.)\s*-\s*\d{1,2}\s+(?:a\.m\.|p\.m\.))",
                re.I,
            )
            m = re.search(hours_pattern, item_text)
            if m:
                hours = m.group(1)
                status = "Open"
            else:
                # more flexible dash chars
                if re.search(r"\d+\s*(?:a\.m\.|p\.m\.)", item_text, re.I):
                    status = "Open"
                    flexible = re.compile(
                        r"(\d{1,2}\s*(?:a\.m\.|p\.m\.)\s*[-–—]\s*\d{1,2}\s*(?:a\.m\.|p\.m\.))",
                        re.I,
                    )
                    fm = re.search(flexible, item_text)
                    if fm:
                        hours = fm.group(1)

        href = name_link.get("href", "") or ""
        if href and not href.startswith("http"):
            href = f"https://www.lib.berkeley.edu{href}"

        libraries.append(Library(name=name, status=status, hours=hours, url=href))

    return libraries


def format_output(libraries: List[Library]) -> str:
    now = datetime.now(PACIFIC_TZ)
    open_libs = [l for l in libraries if l.status == "Open"]
    closed_libs = [l for l in libraries if l.status == "Closed"]
    unknown_libs = [l for l in libraries if l.status == "Unknown"]

    lines: List[str] = []
    lines.append("=" * 60)
    lines.append("UC Berkeley Library Open Status")
    lines.append(f"Last Update: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    lines.append(f"Data Source: {UCB_HOURS_URL}")
    lines.append("=" * 60)
    lines.append("")

    lines.append(f"Now Open ({len(open_libs)})：")
    if open_libs:
        for l in open_libs:
            hrs = f" — {l.hours}" if l.hours else ""
            lines.append(f"🟢 {l.name}{hrs}")
    else:
        lines.append("(None)")

    lines.append("")
    lines.append(f"Now Closed ({len(closed_libs)})：")
    if closed_libs:
        # show first 15 to keep page compact
        for l in closed_libs[:15]:
            lines.append(f"🔴 {l.name}")
        if len(closed_libs) > 15:
            lines.append(f"... and other {len(closed_libs) - 15} libraries are closed.")
    else:
        lines.append("(None)")

    if unknown_libs:
        lines.append("")
        lines.append(f"Status Unknown ({len(unknown_libs)})：")
        for l in unknown_libs[:10]:
            lines.append(f"⚪ {l.name}")
        if len(unknown_libs) > 10:
            lines.append(f"... and other {len(unknown_libs) - 10} libraries' status are unknown.")

    lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines) + "\n"


def replace_between_markers(md: str, replacement_block: str) -> str:
    if MARKER_BEGIN not in md or MARKER_END not in md:
        raise RuntimeError("Markers not found in markdown file.")

    before, rest = md.split(MARKER_BEGIN, 1)
    _, after = rest.split(MARKER_END, 1)

    # Always wrap in a fenced code block
    new_mid = (
        f"{MARKER_BEGIN}\n\n"
        "```text\n"
        f"{replacement_block}"
        "```\n\n"
        f"{MARKER_END}"
    )

    return before + new_mid + after


def main() -> None:
    try:
        html = fetch_html(UCB_HOURS_URL)
        libraries = parse_libraries(html)
        if not libraries:
            raise RuntimeError("Parsed 0 libraries (page structure may have changed).")
        output = format_output(libraries)
    except Exception as e:
        now = datetime.now(PACIFIC_TZ)
        output = (
            "=" * 60
            + "\n"
            + "UC Berkeley Library Open Status\n"
            + f"Last Update: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
            + f"Data Source: {UCB_HOURS_URL}\n"
            + "=" * 60
            + "\n\n"
            + "❌ We're sorry. This update failed.\n"
            + f"Error: {e}\n"
            + "\n"
        )

    with open(MD_PATH, "r", encoding="utf-8") as f:
        md = f.read()

    new_md = replace_between_markers(md, output)

    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write(new_md)


if __name__ == "__main__":
    main()

