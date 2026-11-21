# The World Today — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/mitsukikun/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/mitsukikun/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One picture that sums up Saturday 21 November 2026, made for the
make.fun `news-image-20261121` bounty. A reader who missed the day can
tell what happened from this page alone.

## The six stories

1. **Russian missiles hit Poland.** Two missiles and a suspected drone
   came down in Poland; NATO calls the breach of its airspace a grave
   violation, and Warsaw calls it a deliberate provocation.
2. **The first Trump–Xi–Putin trilateral summit ends.** The three
   leaders leave their Shenzhen talks with few concrete results.
3. **Wall Street slumps into correction.** The S&P 500 drops 3.7% as
   AI shares sell off.
4. **Deadly Russian strikes pound Kyiv.** Drones and missiles hit the
   capital; at least 11 people are killed.
5. **The World Court finds Myanmar committed genocide.** The
   International Court of Justice rules against Myanmar over the
   Rohingya in a landmark judgment.
6. **Cyclone Akvan slams India's east coast.** The storm crosses the
   Odisha coast with heavy rain and high winds.

## The file

`entry.png` holds the front page: a JPEG (kept under the name the
bounty asks for), 1024 by 1024 pixels, 186,139 bytes.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` places an exact copy of the picture in the output folder
(`MAKEFUN_OUTPUT_DIR`, or `/output` when that is unset) and checks the
copy before it reports success: non-empty, no more than 1 MiB, JPEG
opening and closing markers present, and 1024 by 1024 pixels read from
the frame header. It prints the bytes written and the sha256 of the
copy, and stops with an error if any check fails.

Only the Python standard library is used. Nothing is fetched from the
network, and running it twice gives the same bytes twice.

## Where the stories come from

Each headline above matches a story first reported on 21 November 2026,
checked against live world-news coverage that morning (RFE/RL, One Turn,
and the Jagran Josh news roundup for the day).
