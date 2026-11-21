# Front Page — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/mitsukikun/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/mitsukikun/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A single front page that sums up 21 November 2026's world news in one image,
for the make.fun `news-image-20261121` bounty.

## What the page carries

Six verified stories from 21 November 2026, laid out as a newspaper front page:

- **Russian missiles hit Poland** — the lead story: two missiles and a suspected drone came down in Poland; NATO calls the airspace breach a grave violation, Warsaw calls it a deliberate provocation.
- **Trump, Xi and Putin end their first trilateral summit** — the leaders leave the Shenzhen talks with few concrete results.
- **Wall Street slumps into correction** — the S&P 500 falls 3.7% as AI shares sell off.
- **Deadly Russian strikes pound Kyiv** — at least 11 killed as drones and missiles hit the capital.
- **The World Court rules Myanmar committed genocide against the Rohingya** — the International Court of Justice delivers its landmark judgment.
- **Cyclone Akvan slams India's east coast** — the storm crosses the Odisha coast with heavy rain and high winds.

The image is a 1024x1024 front page, delivered as `entry.png`.
It is a JPEG (named `entry.png`, as the bounty requires) of 186,139 bytes.

## Sources

Stories verified against live world-news coverage of 21 November 2026
(RFE/RL, One Turn, Jagran Josh school-assembly roundup) on the morning
of the day itself; each headline above matches a story first reported
on 21 November 2026.

## How to run

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` into the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`) and verifies the copy: JPEG magic
bytes at both ends, size at most 1 MiB, and dimensions exactly 1024x1024 read
from the JPEG start-of-frame marker. It then prints the bytes written and the
sha256 of the output, and exits non-zero with a clear error if any check fails.

No dependencies beyond the Python standard library, no network access, and the
output is deterministic.
