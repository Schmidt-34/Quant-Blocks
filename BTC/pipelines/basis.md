# Binance BTCUSDT perp basis (mark vs index)

Copy this page into local OneNote. Basis only. One script.

Laptop awake. Corridor auto 10:00. OI auto 10:10. Funding auto 10:15. Basis auto **10:20**. Needs today’s QMI row (Z). Perps only. Timer is this Mac only — not in the GitHub repo.

## One script

`BTC/scripts/get_basis.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_basis.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_basis.py --z -0.84
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/basis.csv`. Positive `basis_pct` = perp rich vs index. Change the `--z` number each time, or omit `--z`.
