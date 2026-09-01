# Binance BTCUSDT perp OI

Get → save, append-only. Copy this page into local OneNote.

```bash
python3 scripts/get_oi.py
```

Writes `trading/oi.csv`. Same date is not written twice.

Source: Binance USD-M `BTCUSDT` perp. No API key. `oi_usd` = open interest × mark.

Auto (no args) uses today’s QMI row for Z. Manual: `python3 scripts/get_oi.py --z -0.84`. If corridor has not written **today**, both stop.

Timer on this Mac: 10:10 (`com.quantblocks.oi.plist`). Corridor auto 10:00 in QMI.
