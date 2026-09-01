# Binance BTCUSDT perp basis (mark vs index)

Get → save, append-only. Copy this page into local OneNote.

```bash
python3 scripts/get_basis.py
```

Writes `trading/basis.csv`. Same date is not written twice.

Columns: `date, mark, index, basis_usd, basis_pct, z, source`.

Positive `basis_pct` = perp rich vs index. Negative = perp cheap vs index.

Auto (no args) uses today’s QMI row for Z. Manual: `python3 scripts/get_basis.py --z -0.84`. If corridor has not written **today**, both stop.

Timer on this Mac: 10:20 (`com.quantblocks.basis.plist`).
