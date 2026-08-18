# BTC catalog — full sweep

Z, spot-for-the-corridor, addresses > 0, and hashrate stay in QMI. This file is **everything else** a BTC quant would take from the feeds you already sit on.

Feeds swept:

- [Velo](https://velo.xyz/chart) — futures / spot / options / CME TradFi, API columns
- [CoinGlass](https://www.coinglass.com/pro/futures/LiquidationMap) — maps, L/S, Hyperliquid, ETF, indexes
- [Glassnode Studio](https://studio.glassnode.com) — on-chain + professional derivatives
- [CheckOnChain](https://charts.checkonchain.com/) — same on-chain families + their models
- [OnChainMind](https://onchainmind.io/) — proprietary overlays + research
- [MacroMicro](https://en.macromicro.me/crypto) — macro + some crypto series + WEFC

**Rule:** one source of truth per series. Variants (1h vs 1d, mean vs median, by-exchange) are columns, not extra products. LTH vs STH vs all **are** different series.

---

## Who you pull from (do not duplicate)

| Book | Primary | Backup / picture-only |
|---|---|---|
| High-res tape (OI, funding, liqs USD, CVD, premium, orderbook depth) | **Velo** | CoinGlass |
| Liquidation **map / heatmap**, long/short ratios, Hyperliquid whales | **CoinGlass** | Velo has counts/USD, not the map |
| On-chain P/L, supply, entities, lightning, mempool, miner (not hashrate) | **Glassnode** | CheckOnChain for charts; CoinGlass indexes are copies |
| CheckOnChain-only models (AVIV, True Market Mean, cointime) | **CheckOnChain** | — |
| OCM custom (MVRV momentum, σ bands, NVU, MPI, STH cost bands) | **OnChainMind** | do not rebuild |
| CME BTC futures/options, GBTC premium | **Velo TradFi** | Glassnode CME OI/volume |
| US spot ETF flows / AUM / premium | **CoinGlass or Glassnode** — pick one, freeze it | MacroMicro as a check |
| Macro (DXY, M2, Fed, claims) | **MacroMicro** | Glassnode macro endpoints if easier to pipe |
| Corridor Z / price-for-PL / addresses>0 / hashrate | **QMI** | never from these sites |

ETH, stables-as-object, alts → CRYPTO. Gold/oil/gas as the object → COMMODITIES. BTC vs DXY/M2/gold **as a join** can live here as overlay series.

---

## A. Spot

| Series | Primary | Folder | Notes |
|---|---|---|---|
| BTC spot OHLC | Velo spot or QMI close | `trading/spot.csv` | Need it next to perps. Do not refit power law. |
| Spot volume | Velo | `trading/spot_volume.csv` | |
| Spot trade count | Velo | `trading/spot_trades.csv` | |
| Spot CVD (agg) | Velo | `trading/spot_cvd.csv` | |
| Spot taker buy/sell | CoinGlass | `trading/spot_taker.csv` | |
| Spot orderbook bid/ask ±range | CoinGlass / Velo | `trading/spot_ob.csv` | |
| Spot orderbook heatmap | CoinGlass | watch + optional snapshots | |
| Spot large limit orders | CoinGlass | `trading/spot_iceberg.csv` | |
| Spot footprint (90d) | CoinGlass | later | |
| Coinbase premium | CoinGlass | `trading/coinbase_prem.csv` | US vs offshore |
| Market cap | Glassnode | `onchain/mcap.csv` | |
| Drawdown from ATH | Glassnode / CheckOnChain | `trading/dd_ath.csv` | |
| Realized vol 1w / 1m / 3m / 1y | Glassnode | `trading/rvol.csv` | |
| BTC.D (dominance) | CoinGlass index | CRYPTO or here as overlay | market-wide — default CRYPTO |

---

## B. Futures tape (Velo + CoinGlass)

### Levels and flow

| Series | Primary | Folder |
|---|---|---|
| Aggregated OI (USD + coin) | Velo | `trading/oi.csv` |
| OI OHLC / bar-to-bar % | Velo | same file or `trading/oi_ohlc.csv` |
| OI by venue | Velo / CoinGlass | `trading/oi_venue.csv` |
| OI stablecoin-margined vs coin-margined | CoinGlass / Glassnode | `trading/oi_margin.csv` |
| OI perpetual vs dated | Glassnode | `trading/oi_perp.csv` |
| CME BTC futures OI + volume | Velo TradFi / Glassnode | `trading/oi_cme.csv` |
| Estimated leverage ratio (OI / exchange balance) | Glassnode | `trading/elr.csv` |
| OI / mcap, OI / volume | Glassnode / CoinGlass | `trading/oi_ratios.csv` |
| Funding rate (pred + settled) | Velo | `trading/funding.csv` |
| Funding 1h / 8h / 24h / annualised | Velo | columns |
| OI-weighted funding | Velo / CoinGlass | `trading/funding_oiw.csv` |
| Volume-weighted funding | CoinGlass | `trading/funding_vw.csv` |
| Funding $ spend (rate × OI) | Velo | `trading/funding_spend.csv` |
| Funding arb / APR across venues | CoinGlass | `trading/funding_arb.csv` |
| Perp premium | Velo | `trading/premium.csv` |
| 3m annualised basis | Velo / Glassnode | `trading/basis_3m.csv` |
| Term structure (calendar) | Glassnode / CoinGlass | `trading/term.csv` |
| Near–far month spread APY | MacroMicro | same family |
| Liquidations USD long / short | Velo / CoinGlass | `trading/liquidations.csv` |
| Liquidation **count** | Velo | `trading/liq_count.csv` |
| Liquidation map | CoinGlass | watch; optional `trading/liq_map.csv` |
| Liquidation heatmap models 1/2/3 | CoinGlass | snapshots, not a daily CSV first |
| Liquidation max pain | CoinGlass | `trading/liq_maxpain.csv` |
| Liq / OI, liq / mcap | Glassnode | `trading/liq_ratios.csv` |
| Futures volume + buy/sell | Velo / Glassnode | `trading/fut_volume.csv` |
| Futures CVD | Velo / CoinGlass | `trading/fut_cvd.csv` |
| Futures vs spot volume ratio | CoinGlass | `trading/fut_spot_vol.csv` |
| Taker buy/sell (perp) | CoinGlass | `trading/fut_taker.csv` |
| Net position | CoinGlass | `trading/net_pos.csv` |
| Footprint | CoinGlass | later |
| VWAP / OIWAP | Velo chart | optional |

### Positioning (CoinGlass — Velo does not replace this)

| Series | Primary | Folder |
|---|---|---|
| Global account long/short | CoinGlass | `trading/ls_accounts.csv` |
| Top trader **account** L/S | CoinGlass | `trading/ls_top_acct.csv` |
| Top trader **position** L/S | CoinGlass | `trading/ls_top_pos.csv` |
| Bitfinex margin L/S | CoinGlass | `trading/ls_bitfinex.csv` |
| Whale index | CoinGlass | `trading/whale_idx.csv` |
| CDRI (CoinGlass derivatives risk 0–100) | CoinGlass | `trading/cdri.csv` |
| CGDI | CoinGlass | `trading/cgdi.csv` |
| Position openings / closures | Glassnode | `trading/pos_open_close.csv` |

### Order book

| Series | Primary | Folder |
|---|---|---|
| Futures orderbook depth history | Velo | `trading/ob_depth.csv` |
| Bid/ask ±range history | CoinGlass | `trading/ob_range.csv` |
| Orderbook heatmap | CoinGlass | watch + snapshots |
| Large limit orders | CoinGlass | `trading/ob_large.csv` |

### Hyperliquid (CoinGlass)

| Series | Primary | Folder |
|---|---|---|
| HL whale alerts / positions | CoinGlass | `trading/hl_whales.csv` |
| HL account L/S | CoinGlass | `trading/hl_ls.csv` |
| HL wallet PnL / position distribution | CoinGlass | later |
| Borrow / lend (Velo HL) | Velo | optional, DeFi-ish |

---

## C. Options (Velo + Glassnode + CoinGlass)

| Series | Primary | Folder |
|---|---|---|
| Options OI (agg) | Velo / Glassnode | `trading/opt_oi.csv` |
| Options volume | Velo / Glassnode | `trading/opt_vol.csv` |
| Options OI by strike | Glassnode / CoinGlass | `trading/opt_oi_strike.csv` |
| Put/call OI ratio | Glassnode | `trading/opt_pc_oi.csv` |
| Put/call volume ratio | Glassnode | `trading/opt_pc_vol.csv` |
| Max pain | CoinGlass | `trading/opt_maxpain.csv` |
| DVOL | Velo / Glassnode | `trading/dvol.csv` |
| ATM IV 1w / 1m / 3m / 6m | Velo / Glassnode | `trading/iv_atm.csv` |
| IV term structure | Velo / Glassnode | `trading/iv_term.csv` |
| 25Δ skew 1w / 1m / 3m / 6m | Velo / Glassnode | `trading/skew_25d.csv` |
| Volatility smile | Glassnode | snapshots |
| Options vega / delta / gamma / notional / premium | Velo | `trading/opt_greeks.csv` |
| Options / futures OI ratio | CoinGlass | `trading/opt_fut_oi.csv` |
| CME options OI + volume | Velo TradFi / Glassnode | `trading/opt_cme.csv` |
| IBIT options (CheckOnChain) | CheckOnChain | later |

---

## D. ETF / institutions / treasuries

| Series | Primary | Folder |
|---|---|---|
| US spot BTC ETF netflow | CoinGlass **or** Glassnode — pick one | `onchain/etf_netflow.csv` |
| ETF AUM / holdings / balances | same | `onchain/etf_aum.csv` |
| ETF premium / discount | CoinGlass | `onchain/etf_prem.csv` |
| ETF volume | Glassnode | `onchain/etf_vol.csv` |
| HK BTC ETF flow | CoinGlass | `onchain/etf_hk.csv` |
| GBTC / Grayscale premium | Velo TradFi / CoinGlass | `onchain/gbtc_prem.csv` |
| Purpose ETF (Canada) | Glassnode | optional |
| Corporate treasury BTC | Glassnode treasuries / CheckOnChain / MacroMicro | `onchain/treasury_cos.csv` |
| Government BTC (US, El Salvador, Bhutan, DE) | Glassnode | `onchain/treasury_gov.csv` |
| MSTR / DAT mNAV, BTC yield (CheckOnChain) | CheckOnChain | later — equity overlay |
| CME large spec / smart money (MacroMicro) | MacroMicro | `trading/cme_cot.csv` |

---

## E. On-chain profit / loss (Glassnode; CheckOnChain charts)

Unrealised ≠ SOPR. SOPR = they moved. Unrealised = still sitting.

| Series | Primary | Folder |
|---|---|---|
| Realized cap | Glassnode | `onchain/realized_cap.csv` |
| Realized price | Glassnode | `onchain/realized_price.csv` |
| MVRV | Glassnode | `onchain/mvrv.csv` |
| MVRV-Z (Glassnode) | Glassnode | `onchain/mvrv_z.csv` — **not** corridor `z` |
| LTH-MVRV / STH-MVRV | Glassnode | `onchain/mvrv_cohort.csv` |
| Delta cap | Glassnode | `onchain/delta_cap.csv` |
| Investor cap | Glassnode | `onchain/investor_cap.csv` |
| Balanced price | Glassnode | `onchain/balanced_px.csv` |
| SOPR / aSOPR | Glassnode | `onchain/sopr.csv` |
| LTH-SOPR / STH-SOPR | Glassnode | `onchain/sopr_cohort.csv` |
| NUPL / LTH-NUPL / STH-NUPL | Glassnode | `onchain/nupl.csv` |
| Relative unrealised profit | Glassnode | `onchain/u_profit.csv` |
| Relative **unrealised loss** | Glassnode | `onchain/u_loss.csv` |
| Supply in profit / loss / % | Glassnode | `onchain/supply_pl.csv` |
| UTXOs in profit / loss / % | Glassnode | `onchain/utxo_pl.csv` |
| Addresses in profit / % | Glassnode | `onchain/addr_pl.csv` |
| Realized profit / loss / net / P/L ratio | Glassnode | `onchain/realized_pl.csv` |
| RPV ratio | Glassnode | `onchain/rpv.csv` |
| URPD / cost-basis heatmap | Glassnode | `onchain/urpd.csv` |
| SOPD | Glassnode | `onchain/sopd.csv` |
| Seller exhaustion | Glassnode / CheckOnChain | `onchain/seller_exh.csv` |
| CVDD | Glassnode | `onchain/cvdd.csv` |
| Reserve risk | Glassnode | `onchain/reserve_risk.csv` |
| RHODL | Glassnode / CheckOnChain | `onchain/rhodl.csv` |
| Accumulation trend score | Glassnode | `onchain/ats.csv` |
| True Market Mean / AVIV (cointime) | **CheckOnChain** | `onchain/aviv.csv` |
| Yearly cohort cost basis | CheckOnChain | `onchain/yearly_cb.csv` |
| STH cost basis / STH cost bands | CheckOnChain / OnChainMind | `onchain/sth_cb.csv` |

---

## F. Lifespan / HODL / spent age

| Series | Primary | Folder |
|---|---|---|
| HODL waves | Glassnode | `onchain/hodl_waves.csv` |
| Realized-cap HODL waves | Glassnode | `onchain/rcap_hodl.csv` |
| LTH / STH supply + net change | Glassnode | `onchain/lth_sth.csv` |
| Supply last active 1y+ / 2y+ / 5y+ / 10y+ | Glassnode | `onchain/old_supply.csv` |
| CDD / CDD-90 / binary CDD / CYD / adj | Glassnode | `onchain/cdd.csv` |
| Dormancy / adj dormancy / dormancy flow | Glassnode | `onchain/dormancy.csv` |
| Liveliness | Glassnode | `onchain/liveliness.csv` |
| ASOL / MSOL | Glassnode | `onchain/asol.csv` |
| Spent output age bands (SOAB) | Glassnode | `onchain/soab.csv` |
| Spent volume age bands (SVAB) | Glassnode | `onchain/svab.csv` |
| Hodler net position change / lost coins | Glassnode | `onchain/hodler_npc.csv` |
| Probably / provably lost supply | Glassnode | `onchain/lost.csv` |

Age-band splits (1d–1w, 1y–2y, …) are **columns** of SOAB/SVAB/HODL, not 20 pipelines.

---

## G. Flows — exchanges, whales, entities

| Series | Primary | Folder |
|---|---|---|
| Exchange balance (BTC + %) | Glassnode | `onchain/ex_balance.csv` |
| Exchange inflow / outflow / netflow | Glassnode | `onchain/ex_netflow.csv` |
| Exchange withdrawals count | Glassnode | `onchain/ex_wd.csv` |
| Miner balance + miner net position | Glassnode | `onchain/miner_bal.csv` |
| Whale count (≥1k BTC entities) | Glassnode | `onchain/whales.csv` |
| Entity supply distribution | Glassnode | `onchain/entity_dist.csv` |
| Address supply dist / wallet waves | Glassnode / CheckOnChain | `onchain/wallet_waves.csv` |
| Address cohorts 0.01 / 1 / 100 / 1k / 10k | Glassnode | `onchain/addr_cohorts.csv` |
| USD-balance cohorts ($1k–$1M) | Glassnode | `onchain/addr_usd.csv` |
| Whale transfers | CoinGlass | `onchain/whale_tx.csv` |
| Exchange PoR / assets transparency | CoinGlass | later |
| WBTC balance | Glassnode | `onchain/wbtc.csv` |
| Mt. Gox remaining | Glassnode | `onchain/mtgox.csv` |

**Skip here:** total / new / active addresses as the *adoption series* — QMI already owns addresses > 0. Cohort and profit-address series above are extra.

---

## H. Network / mempool / lightning (not QMI hashrate)

| Series | Primary | Folder |
|---|---|---|
| Tx count / rate, transfer count / rate | Glassnode | `onchain/tx.csv` |
| Transfer volume USD (mean / median / total) | Glassnode | `onchain/xfer_vol.csv` |
| Change-adjusted volume | Glassnode | `onchain/xfer_adj.csv` |
| Fees mean / median / total, FRM | Glassnode | `onchain/fees.csv` |
| Block interval, size, blocks mined, UTXO count | Glassnode | `onchain/blocks.csv` |
| SegWit / Taproot adoption, script types | Glassnode | `onchain/scripts.csv` |
| Mempool tx count / size / fees by fee band | Glassnode | `onchain/mempool.csv` |
| Lightning: capacity, channels, nodes, fees, gini | Glassnode | `onchain/ln.csv` |
| NVT / NVTS / velocity | Glassnode | `onchain/nvt.csv` |
| SSR + SSR oscillator | Glassnode | `onchain/ssr.csv` — stables vs BTC; series can live here |
| Issuance, inflation rate, circulating / adjusted supply | Glassnode | `onchain/issuance.csv` |
| Activity / holder retention, holder accumulation ratio | Glassnode | `onchain/retention.csv` |

---

## I. Miners (hashrate stays in QMI)

| Series | Primary | Folder |
|---|---|---|
| Difficulty | Glassnode | `onchain/difficulty.csv` |
| Difficulty ribbon / compression | Glassnode | `onchain/diff_ribbon.csv` |
| Hash ribbon | Glassnode | chart; hashrate still QMI |
| Thermocap, mcap/thermocap | Glassnode / CheckOnChain | `onchain/thermocap.csv` |
| Miner revenue total / fees / subsidy | Glassnode | `onchain/miner_rev.csv` |
| Puell | Glassnode | `onchain/puell.csv` |
| Hashprice | CheckOnChain | `onchain/hashprice.csv` |
| Mining pulse / profitable days | CheckOnChain | later |
| Miner Position Index (MPI) | OnChainMind | `onchain/mpi.csv` |
| Miner total flows | OnChainMind | `onchain/miner_flows.csv` |

---

## J. Cycle / valuation models on the feeds (do not replace QMI)

Pull as **comparators**, labelled. Never overwrite corridor β / Z.

| Series | Primary | Folder |
|---|---|---|
| Glassnode Power-Law | Glassnode | skip or `onchain/gn_pl.csv` as **their** fit |
| Stock-to-flow / deflection | Glassnode / CoinGlass | `onchain/s2f.csv` — dead model, optional |
| Pi Cycle Top | Glassnode / CoinGlass / CheckOnChain | `onchain/pi_cycle.csv` |
| Mayer Multiple | CheckOnChain | `onchain/mayer.csv` |
| Rainbow / 200w MA heatmap / 2y MA multiplier | CoinGlass / CheckOnChain | `onchain/rainbow.csv` |
| AHR999, golden ratio, bubble index | CoinGlass | later |
| Fear & Greed | CoinGlass / Glassnode | `trading/fng.csv` |
| NVU (users not volume) | OnChainMind | `onchain/nvu.csv` |
| RVT | OnChainMind | `onchain/rvt.csv` |
| MVRV momentum / 2y delta / σ bands | OnChainMind | `onchain/mvrv_mom.csv` |
| σ trading channel | OnChainMind | later |
| STH NUPL / STH MVRV momentum / STH cost bands | OnChainMind | `onchain/sth_ocm.csv` |
| CheckOnChain cycle tops/bottoms, euphoria zone, magic lines, NVT price | CheckOnChain | follow; store one if you use it weekly |

---

## K. Macro overlay (MacroMicro + Glassnode macro + CheckOnChain TradFi)

Object is **BTC vs the print**, not a commodities book.

| Series | Primary | Folder |
|---|---|---|
| DXY | MacroMicro | `onchain/dxy.csv` |
| US M2 / global M2 vs BTC | MacroMicro / CoinGlass / CheckOnChain | `onchain/m2.csv` |
| Fed / ECB balance sheet, policy rate | MacroMicro / Glassnode | `onchain/cb.csv` |
| US 10y, inflation, CPI, consumer confidence, LEI | MacroMicro / Glassnode | `onchain/us_macro.csv` |
| BTC correlation vs SPX / DXY / gold / 10y | CoinGlass / CheckOnChain | `onchain/corr.csv` |
| Economic calendar | CoinGlass | `articles/` or a calendar file |
| WEFC / TACO / tariff notes | MacroMicro | `articles/` — claim, tested vs Z or not |
| Gold / WTI as **join only** | MacroMicro — or COMMODITIES block | do not duplicate the physical book |

---

## L. Infra (engineering)

| Piece | Where |
|---|---|
| Getter | `scripts/get_<series>.py` — Velo API, CoinGlass API, Glassnode API |
| Pipeline note | `pipelines/<series>.md` — source frozen, units, resolution, append rule |
| Store | `trading/*.csv`, `onchain/*.csv` — `date, values…, z, source` |
| Join | `z` copied from that day’s PL log |
| Dashboard | reads CSVs. Screens: risk strip (Z) · tape · options · ETF · holder P/L · flows · miners · mempool · your book |
| Trade log | `trading/log.csv` |
| Research | `research/YYYY-MM-DD.md` |
| Articles | `articles/` — OCM / WEFC / CheckOnChain claim + tested/not |
| Models | `models/` after history. Overlays on Z. Never a second corridor. |

**Dashboard screens (full):**

1. Risk — imported Z  
2. Tape — OI, funding, liqs, map, L/S, CVD, basis, ELR, CDRI  
3. Options — DVOL, skew, PC, max pain, OI by strike  
4. ETF / CME / Coinbase premium  
5. Holder P/L — MVRV, SOPR, NUPL, unrealised loss, URPD, STH  
6. Flows — exchange, whales, miner balance  
7. Miners — Puell, revenue, difficulty (hashrate from QMI)  
8. Network — mempool, fees, LN  
9. Macro overlay — DXY, M2, 10y  
10. Positions — your log vs all of the above  

---

## Not in this block

- QMI runner, β, R², ±1.5σ, addresses>0, hashrate  
- ETH gas, DeFi TVL, bridges, ETH2 staking, NFT gas  
- USDT/USDC **as the book** (SSR vs BTC is the exception)  
- Altcoin season, SOL/XRP ETFs  
- Rebuilding Velo / CoinGlass / Glassnode / CheckOnChain / OCM / MacroMicro  

---

Stand-up order (what you actually build next) stays in [`BUILD.md`](BUILD.md). This file is the map of **everything available**.
