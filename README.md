# Quant Blocks

Independent research repository for **Bitcoin tape**, **crypto market-structure series**, and **commodities**. Companion to Quantitative Macro Intelligence.

This repository is **not** Chaos Corridor.

Chaos Corridor (Bitcoin power-law engine, Z-score, composite risk) lives here and stays there:

**https://github.com/Schmidt-34/Quantitative-Macro-Intelligence**

Do not put corridor scripts, corridor data, or PL model work in this repo. Tape getters here **join** the QMI daily row on `date`. They do not re-fit the corridor.

| Block | What it is |
|---|---|
| [`BTC/`](BTC/) | Bitcoin that is not the live corridor: extra on-chain, BTC tape, research, articles, pipelines, models |
| [`CRYPTO/`](CRYPTO/) | On-chain + trading for everything digital that is not Bitcoin |
| [`COMMODITIES/`](COMMODITIES/) | Physical book: energy, metals, critical materials |

Each block has the same work layers: data/onchain, trading, research, articles, pipelines, scripts, models.

---

## Live getters

Four append-only public-API getters. Tool ≠ model. Fitted work stays in `models/` until a series has enough rows.

| Series | Block | Script | Writes |
|---|---|---|---|
| BTC.D | CRYPTO | [`CRYPTO/scripts/get_btc_d.py`](CRYPTO/scripts/get_btc_d.py) | `CRYPTO/onchain/btc_d.csv` |
| Binance BTCUSDT perp OI | BTC | [`BTC/scripts/get_oi.py`](BTC/scripts/get_oi.py) | `BTC/trading/oi.csv` |
| Binance BTCUSDT perp funding | BTC | [`BTC/scripts/get_funding.py`](BTC/scripts/get_funding.py) | `BTC/trading/funding.csv` |
| Binance BTCUSDT perp basis | BTC | [`BTC/scripts/get_basis.py`](BTC/scripts/get_basis.py) | `BTC/trading/basis.csv` |

CSVs are gitignored — regenerate locally. Same date is not written twice.

OI, funding, and basis join today’s QMI corridor row for Z. Run Chaos Corridor first (or pass `--z` from the chart). Point `QMI_METRICS` at the corridor CSV if it is not at `~/Quantitative-Macro-Intelligence/04-Quant-Models/chaos-corridor/data/chaos_corridor_metrics.csv`.

### Quick start

```bash
cd CRYPTO && python3 scripts/get_btc_d.py
cd BTC && python3 scripts/get_oi.py
cd BTC && python3 scripts/get_funding.py
cd BTC && python3 scripts/get_basis.py
```

Manual Z (chart): `python3 scripts/get_oi.py --z -0.84` (same flag on funding and basis).

Schedule is optional and local. This repo does not ship timers.

---

## Author

**Tomas Owain Griffiths**  
BSc Hons – Computer Science / Economics / Finance (Quantitative Focus)  
The Open University (2025 – Present)  
Former British Army Sniper Section Commander  

LinkedIn / Contact: griff687@hotmail.com

---

*All content is for research and educational purposes. Not financial advice.*
