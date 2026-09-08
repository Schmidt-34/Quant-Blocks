# Binance BTCUSDT perp CVD

Copy this page into local OneNote. Perp CVD only. One script.

Laptop awake. Corridor auto 10:00. OI auto 10:10. CVD perp auto **10:12**. Needs today’s QMI row (Z). Perps only. Timer is this Mac only — not in the GitHub repo.

This is **futures** taker buy minus taker sell, then cumulated. Spot CVD is `get_cvd_spot.py`.

## One script

`BTC/scripts/get_cvd_perp.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_cvd_perp.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_cvd_perp.py --z -0.81
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/cvd_perp.csv`. Columns: `date, buy_vol, sell_vol, delta, cvd, z, source`.

From Binance USD-M daily kline: taker buy BTC vs the rest of volume (taker sell). `delta` = buy − sell. Positive = net aggressive buying on perps. `cvd` = running sum of `delta` from the start of this file.

Change the `--z` number each time, or omit `--z` and let the script take Z from QMI.
