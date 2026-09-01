# BTC.D

Copy this page into local OneNote. BTC.D only. One script.

Laptop awake. Corridor auto 10:00. OI 10:10. Funding 10:15. Basis 10:20. BTC.D auto **10:25**. No Z. No QMI join. CoinGecko public, no API key. Does not touch Binance or Chaos Corridor. Timer is this Mac only — not in the GitHub repo.

## One script

`CRYPTO/scripts/get_btc_d.py`

**Auto** (timer, or pull when you feel like it):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_btc_d.py
```

There is no `--z` flag.

Writes `onchain/btc_d.csv`. Columns: `date, value, unit, source`.

`value` = Bitcoin’s share of total crypto market cap, in percent.

Source: CoinGecko `GET /api/v3/global` → `market_cap_percentage.btc`. Same date is not written twice.
