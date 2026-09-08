# ETH.D

Copy this page into local OneNote. ETH.D only. One script.

Laptop awake. BTC.D auto 10:25. ETH.D auto **10:30**. No Z. No QMI join. CoinGecko public, no API key. Same endpoint as BTC.D. Timer is this Mac only — not in the GitHub repo.

## One script

`CRYPTO/scripts/get_eth_d.py`

**Auto** (timer, or pull when you feel like it):

```bash
cd /Users/griff1/Quant-Blocks/CRYPTO
python3 scripts/get_eth_d.py
```

There is no `--z` flag.

Writes `onchain/eth_d.csv`. Columns: `date, value, unit, source`.

`value` = Ethereum’s share of total crypto market cap, in percent.

Source: CoinGecko `GET /api/v3/global` → `market_cap_percentage.eth`. Same date is not written twice.
