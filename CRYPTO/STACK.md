# CRYPTO stack — architecture

Full series list: [`CATALOG.md`](CATALOG.md).  
Stand-up order: [`BUILD.md`](BUILD.md).

Z is optional here. Import it from the PL log only when the join is real (alts as a satellite of Bitcoin risk). This block does **not** compute Z.

**BTC.D** is the market-wide regime you already own. Stables are dry powder. ETH tape is crowding. None of that is Bitcoin-as-network.

Three products:

1. **Data book** — dated CSVs you own
2. **Dashboard** — those CSVs; Z only if you joined it
3. **Trading / investing** — BTC.D for rotation, stables for liquidity, tape for ETH/alt timing

```
CoinGecko / Binance / DefiLlama / Velo / CoinGlass / Glassnode
        ↓
  scripts/get_*.py
        ↓
  append-only CSV in trading/ or onchain/
        ↓
  join on date  (+ Z if useful)
        ↓
  dashboard · research · trade log · later a model
```

One source per series. Who owns which book is in CATALOG.md.

Bitcoin OI, funding, SOPR, MVRV, ETF, miners → BTC. Corridor β / R² / Z / addresses / hashrate → QMI. Gold / oil / gas → COMMODITIES.
