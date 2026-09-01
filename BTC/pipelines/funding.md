# Binance BTCUSDT perp funding

Get → save, append-only. Copy this page into local OneNote.

```bash
python3 scripts/get_funding.py
```

Writes `trading/funding.csv`. Same date is not written twice.

Columns: `date, funding_rate, funding_pct, z, source`.

Positive `funding_pct` = longs pay shorts. Negative = shorts pay longs.

Auto (no args) uses today’s QMI row for Z. Manual: `python3 scripts/get_funding.py --z -0.84`. If corridor has not written **today**, both stop.

Timer on this Mac: 10:15 (`com.quantblocks.funding.plist`).
