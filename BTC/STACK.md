# BTC stack — architecture

Full series list: [`CATALOG.md`](CATALOG.md).  
Stand-up order: [`BUILD.md`](BUILD.md).

Z is risk and already lives in Chaos Corridor. This block **imports today’s Z**. It does not compute it.

Three products:

1. **Data book** — dated CSVs you own
2. **Dashboard** — those CSVs next to Z
3. **Trading / investing** — tape for timing, on-chain for regime, Z for cheap/dear

```
Velo / CoinGlass / Glassnode / CheckOnChain / OnChainMind / MacroMicro / QMI(Z)
        ↓
  scripts/get_*.py
        ↓
  append-only CSV in trading/ or onchain/
        ↓
  join on date + Z
        ↓
  dashboard · research · trade log · later a model
```

One source per series. Who owns which book is in CATALOG.md.
