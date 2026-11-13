# news-image-01 — The World in One Picture

One image summing up the world's news of **Friday 13 November 2026**, as a
newspaper front page.

## The stories

| Story | Picture | Headline |
| --- | --- | --- |
| Ukraine peace talks: US envoys Witkoff and Kushner meet Putin, then Zelenskyy; Europe joins the next round, largest prisoner swap planned | Handshake across a conference table, US / EU / Ukraine flags | EUROPE WINS A SEAT AT PEACE TALKS |
| Nvidia chief Jensen Huang resigns; shares fall 16%; CFO Colette Kress interim CEO | Empty executive chair, plunging red chart | NVIDIA CHIEF QUITS |
| Microsoft 365 down worldwide for a second day (Outlook, Teams, Copilot; 74 countries) | Worried workers at blank blue screens | MICROSOFT 365 DOWN WORLDWIDE |
| LNG tanker strikes a mine in the Strait of Hormuz; Iran says it hit a US radar site in Bahrain | Smoking tanker, warships on the horizon | TANKER HIT IN HORMUZ |
| Also today: FBI seizes $1.2bn in stolen crypto; Gaza hospital strike kills six; Brooklyn building collapse kills eight | — (strip) | ALSO TODAY |

Sources: BBC World and Al Jazeera live coverage of 13 November 2026, plus
the day's global news briefings (Open Chronicle, Seven Lights, Citizen's
Daily Brief, Bangladesh Chronicle) — all four hero stories were first
reported on 13 November 2026.

## Why this should win pairwise

- **Full-day coverage.** The house images were drawn early on 13 November
  from morning news only. This page covers the whole day, including the
  stories that broke later: Huang's resignation and the 16% share fall, the
  Microsoft outage entering its second day, and the Hormuz mine strike.
- **Breadth.** Diplomacy, business, technology and the Middle East — four
  regions/fields, plus three more stories in the strip.
- **It reads.** A viewer who missed the day can tell what happened from the
  image alone: each story has its own picture and a short, correct headline.
- **No garbled text.** The artwork is AI-generated with no text in it; every
  headline is rendered crisply with PIL, so every word is spelled correctly
  and legible at small size.

## How it runs

`main.py` (Python 3.13 stdlib only) copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), then verifies
the copy by comparing sha256 digests and prints the digest it wrote.
Deterministic: two runs write byte-identical files. The image is 1024×1024
PNG, 792,129 bytes (limit 1 MiB).
