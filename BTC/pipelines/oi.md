# Binance BTCUSDT perp OI

Copy this page into local OneNote. OI only. One script.

Laptop awake. Corridor auto 10:00. OI auto **10:10**. Needs today’s QMI row (Z). Perps only. Timer is this Mac only — not in the GitHub repo.

## One script

`BTC/scripts/get_oi.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_oi.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_oi.py --z -0.84
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/oi.csv`. `oi_usd` = OI × mark. Change the `--z` number each time, or omit `--z` and let the script take Z from QMI.
