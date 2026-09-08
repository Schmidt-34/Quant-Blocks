# Total crypto mcap

Copy this page into local OneNote. Total mcap only. One script.

Laptop awake. ETH.D auto 10:30. Total mcap auto **10:35**. No Z. No QMI join. CoinGecko public, no API key. Same endpoint as BTC.D. Timer is this Mac only — not in the GitHub repo.

## One script

`CRYPTO/scripts/get_total_mcap.py`

**Auto** (timer, or pull when you feel like it):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_total_mcap.py
```

There is no `--z` flag.

Writes `onchain/total_mcap.csv`. Columns: `date, value, unit, source`.

`value` = total crypto market cap in USD.

Source: CoinGecko `GET /api/v3/global` → `total_market_cap.usd`. Same date is not written twice.
