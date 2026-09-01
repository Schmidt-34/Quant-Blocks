# Binance BTCUSDT perp funding

Copy this page into local OneNote. Funding only. One script.

Laptop awake. Corridor auto 10:00. OI auto 10:10. Funding auto **10:15**. Needs today’s QMI row (Z). Perps only. Timer is this Mac only — not in the GitHub repo.

## One script

`BTC/scripts/get_funding.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_funding.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_funding.py --z -0.84
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/funding.csv`. Positive `funding_pct` = longs pay shorts. Change the `--z` number each time, or omit `--z`.
