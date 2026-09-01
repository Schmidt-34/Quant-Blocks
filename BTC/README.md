# BTC

Bitcoin lab. Not Chaos Corridor.

Corridor / PL engine: https://github.com/Schmidt-34/Quantitative-Macro-Intelligence

Current tape: Binance BTCUSDT perp **OI**, **funding**, **basis**. Append with the getters in `scripts/`. Next BUILD line is perp CVD.

| Layer | For |
|---|---|
| `onchain/` | Extra Bitcoin series the live corridor does not own |
| `trading/` | BTC tape (OI, CVD, OBV, funding, basis) and trade log |
| `research/` | Dated notes (GitHub). Daily habit is the Word BTC LOG |
| `articles/` | Third-party, dated, sourced |
| `pipelines/` | How BTC series get in |
| `scripts/` | Helpers |
| `models/` | New fitted work later — never a copy of the corridor |

Full map: [`CATALOG.md`](CATALOG.md). Architecture: [`STACK.md`](STACK.md). Stand-up order: [`BUILD.md`](BUILD.md).
