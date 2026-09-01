# BTC.D

Get → save, append-only. Copy this page into local OneNote.

```bash
python3 scripts/get_btc_d.py
```

Writes `onchain/btc_d.csv`. Same date is not written twice.

Source: CoinGecko `GET /api/v3/global` → `market_cap_percentage.btc`.
