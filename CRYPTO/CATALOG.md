# CRYPTO catalog — full sweep

Bitcoin-as-network, BTC tape, and corridor Z stay out. This file is **everything else** a crypto quant would take from the feeds you already sit on: ETH, alts, stables, market-wide.

Feeds swept:

- [CoinGecko](https://www.coingecko.com) — global mcap / dominance (free)
- [Binance](https://www.binance.com) — public ETH/alt spot + perp tape (free)
- [DefiLlama](https://defillama.com) — stables + TVL (free)
- [Velo](https://velo.xyz/chart) — high-res ETH/alt tape when paid
- [CoinGlass](https://www.coinglass.com) — ETH maps, L/S, ETH ETF, alt season
- [Glassnode Studio](https://studio.glassnode.com) — ETH on-chain

**Rule:** one source of truth per series. Variants (1h vs 1d, by-exchange) are columns, not extra products. ETH vs SOL vs “alts as a bag” **are** different series. Stand one asset at a time.

---

## Who you pull from (do not duplicate)

| Book | Primary | Backup / picture-only |
|---|---|---|
| Dominance / total mcap | **CoinGecko global** | CoinGlass indexes |
| Stables as the book (USDT, USDC) | **DefiLlama** | Glassnode stable supply |
| ETH tape (OI, funding, CVD, premium) until paid | **Binance public** | CoinGlass |
| High-res / multi-venue ETH tape | **Velo** | CoinGlass |
| ETH liq **map**, L/S, Hyperliquid, ETH ETF | **CoinGlass** | Velo has USD, not the map |
| ETH on-chain (gas, staking, exchange, MVRV, SOPR) | **Glassnode** | DefiLlama for TVL only |
| Townhall / research claims | **articles/** | test later on your CSV |
| Corridor Z / BTC network / BTC tape | **QMI / BTC block** | never from these as ETH |

SSR (stables vs **BTC**) can live in BTC. USDT/USDC **as objects** live here.

---

## A. Market-wide

| Series | Primary | Folder | Notes |
|---|---|---|---|
| BTC.D | CoinGecko global | `onchain/btc_d.csv` | Standing. Bitcoin share of crypto. |
| ETH.D | CoinGecko global | `onchain/eth_d.csv` | Same pull as BTC.D. |
| Others.D | You compute | `onchain/others_d.csv` | 100 − BTC.D − ETH.D. After both exist. |
| Total crypto mcap USD | CoinGecko global | `onchain/total_mcap.csv` | |
| TOTAL2 (ex BTC) | You compute | `onchain/total2.csv` | After total mcap + BTC.D. |
| TOTAL3 (ex BTC+ETH) | You compute | `onchain/total3.csv` | After ETH.D. Later. |
| Altcoin season index | CoinGlass | `trading/alt_season.csv` | Watch until paid. |
| ETH/BTC | CoinGecko or Binance | `trading/eth_btc.csv` | Ratio. Not a corridor. |
| Fear & Greed | CoinGlass | skip or BTC | Market-wide; don’t store twice. |

---

## B. Stables

| Series | Primary | Folder | Notes |
|---|---|---|---|
| USDT circulating | DefiLlama | `onchain/usdt.csv` | Dry powder. |
| USDC circulating | DefiLlama | `onchain/usdc.csv` | |
| USDT+USDC | You compute | `onchain/stables.csv` | The book. |
| DAI / others | DefiLlama | later | One extra stable only if you use it weekly. |
| Exchange stable balance | Glassnode / CryptoQuant | `onchain/stable_exch.csv` | Paid. Coins sitting on venues. |
| Stablecoin net issuance | DefiLlama | columns on 10–12 | Supply change, not price. |

---

## C. ETH tape (Binance → Velo)

Spot and perps are different books. The alpha is the gap.

| Series | Primary | Folder |
|---|---|---|
| ETH spot close / volume | Binance / CoinGecko | `trading/eth_spot.csv` |
| ETH perp OI (USD + coin) | Binance, then Velo | `trading/eth_oi.csv` |
| ETH OI by venue | Velo / CoinGlass | `trading/eth_oi_by_venue.csv` |
| ETH funding | Binance, then Velo | `trading/eth_funding.csv` |
| ETH funding by venue | Velo | `trading/eth_funding_by_venue.csv` |
| ETH perp vs index (basis) | Binance / Velo | `trading/eth_basis.csv` |
| ETH premium (perp minus spot) | Velo | `trading/eth_premium.csv` |
| ETH CVD perp | Binance taker buy/sell | `trading/eth_cvd_perp.csv` |
| ETH CVD spot | Binance spot taker | `trading/eth_cvd_spot.csv` |
| ETH CVD gap | You compute | `trading/eth_cvd_gap.csv` |
| ETH liquidations long/short USD | CoinGlass / Velo | `trading/eth_liquidations.csv` |
| ETH liq map | CoinGlass | watch + daily note |
| ETH long/short accounts | CoinGlass | `trading/eth_ls.csv` |
| ETH taker buy/sell | Binance / CoinGlass | columns on CVD files |

---

## D. ETH on-chain (Glassnode)

| Series | Primary | Folder | What it is |
|---|---|---|---|
| Gas used / base fee | Glassnode | `onchain/eth_gas.csv` | Blockspace demand |
| Fees USD | Glassnode | `onchain/eth_fees.csv` | |
| Staked ETH / staking rate | Glassnode | `onchain/eth_staking.csv` | ETH locked, not BTC security |
| Exchange netflow ETH | Glassnode | `onchain/eth_exchange_netflow.csv` | Coins to venues |
| Exchange balance ETH | Glassnode | `onchain/eth_exchange_balance.csv` | |
| ETH MVRV | Glassnode | `onchain/eth_mvrv.csv` | Price vs ETH cost basis. Not corridor Z. |
| ETH SOPR | Glassnode | `onchain/eth_sopr.csv` | ETH moved today: profit or loss |
| ETH supply / issuance | Glassnode | `onchain/eth_supply.csv` | Post-merge issuance |
| Active addresses ETH | Glassnode | later | Not QMI addresses>0 |

---

## E. ETH ETF / options (after tape exists)

| Series | Primary | Folder |
|---|---|---|
| ETH US spot ETF netflow | CoinGlass or Glassnode — freeze one | `onchain/eth_etf_netflow.csv` |
| ETH ETF AUM | same | `onchain/eth_etf_aum.csv` |
| ETH options OI | Velo / Deribit / CoinGlass | `trading/eth_opt_oi.csv` |
| ETH IV / DVOL | Velo | `trading/eth_iv.csv` |

---

## F. Alts — one major at a time (after ETH tape)

Do not stand SOL, XRP, and “alts” in the same week.

| Series | Primary | Folder | When |
|---|---|---|---|
| SOL OI / funding | Binance / Velo | `trading/sol_oi.csv` | After ETH OI+funding exist |
| SOL CVD | Binance | `trading/sol_cvd.csv` | |
| XRP / other major | same pattern | `trading/<asset>_*.csv` | Only if you actually tape it |
| Alt OI aggregated | CoinGlass | `trading/alt_oi.csv` | Bag, not a coin. Later. |
| Hyperliquid whales / L/S | CoinGlass | watch | Often alt-heavy. Store a number if it mattered. |

---

## G. DeFi / TVL / bridges (later)

| Series | Primary | Folder | Notes |
|---|---|---|---|
| TVL ETH chain | DefiLlama | `onchain/tvl_eth.csv` | Platform usage |
| TVL all chains | DefiLlama | `onchain/tvl.csv` | |
| Bridge flows | DefiLlama | later | Don’t start here |
| NFT gas | — | skip | Noise unless you trade it |

---

## H. Infra (engineering)

| Piece | Where |
|---|---|
| Getter | `scripts/get_<series>.py` — one job |
| Pipeline note | `pipelines/<series>.md` — source frozen, units, append rule |
| Store | `trading/*.csv`, `onchain/*.csv` — `date, value(s), unit, source` (+ `z` only if joined) |
| Join | optional `z` from that day’s PL log |
| Dashboard | reads CSVs. Screens below |
| Trade log | `trading/log.csv` |
| Research | `research/YYYY-MM-DD.md` |
| Articles | `articles/` — Townhall / feed claim + tested/not |
| Models | `models/` after 12 rows. Overlay. Never an ETH power-law |

**Dashboard screens (when CSVs exist):**

1. Rotation — BTC.D, ETH.D, others.D  
2. Liquidity — USDT, USDC, stables sum  
3. ETH tape — OI, funding, liquidations, basis, CVD gap  
4. ETH on-chain — gas, staking, exchange netflow  
5. ETH ETF  
6. Optional risk strip — imported Z  
7. Your positions vs the above  

---

## Not in this block

- QMI runner, β, R², ±1.5σ, addresses>0, hashrate  
- BTC OI / funding / SOPR / MVRV / ETF / miners / Puell  
- Gold / oil / gas as objects  
- Rebuilding CoinGecko / Binance / DefiLlama / Velo / CoinGlass / Glassnode  
- An ETH corridor, LPPL, or a second power-law  

---

Stand-up order (what you actually build next) stays in [`BUILD.md`](BUILD.md). This file is the map of **everything available**.
