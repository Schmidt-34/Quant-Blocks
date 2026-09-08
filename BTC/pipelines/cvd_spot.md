# Binance BTCUSDT spot CVD

Copy this page into local OneNote. Spot CVD only. One script.

Laptop awake. Perp CVD auto 10:12. Spot CVD auto **10:13**. Needs today’s QMI row (Z). **Spot book**, not perps. Timer is this Mac only — not in the GitHub repo.

## One script

`BTC/scripts/get_cvd_spot.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_cvd_spot.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/BTC
python3 scripts/get_cvd_spot.py --z -0.84
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/cvd_spot.csv`. Columns: `date, buy_vol, sell_vol, delta, cvd, z, source`.

From Binance **spot** daily kline: taker buy BTC vs the rest of volume. `delta` = buy − sell. Positive = net aggressive buying on spot. `cvd` = running sum of `delta` from the start of this file.

Change the `--z` number each time, or omit `--z`.
