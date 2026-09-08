# Binance ETHUSDT perp OI

Copy this page into local OneNote. ETH OI only. One script.

Laptop awake. Total mcap auto 10:35. ETH OI auto **10:40**. Needs today’s QMI row (Z). ETH perps, not BTC OI. Timer is this Mac only — not in the GitHub repo.

## One script

`CRYPTO/scripts/get_eth_oi.py`

**Auto** (timer, or pull when you feel like it — no typing):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_eth_oi.py
```

**Manual** (you type Z from the chart):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_eth_oi.py --z -0.84
```

If corridor has not written **today**, both stop. Run corridor first. Same date is not written twice.

Writes `trading/eth_oi.csv`. `oi_usd` = ETH perp OI × mark. Change the `--z` number each time, or omit `--z`.
