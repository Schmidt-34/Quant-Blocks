# Binance ETHUSDT perp funding

Copy this page into local OneNote. ETH funding only. One script.

Laptop awake. ETH OI auto 10:40. ETH funding auto **10:45**. Needs today’s QMI row (Z). ETH perps, not BTC funding. Timer is this Mac only — not in the GitHub repo.

## One script

`CRYPTO/scripts/get_eth_funding.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_eth_funding.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_eth_funding.py --z -0.84
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/eth_funding.csv`. Positive `funding_pct` = longs pay shorts. Change the `--z` number each time, or omit `--z`.
