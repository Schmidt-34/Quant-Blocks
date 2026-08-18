# BTC — stand-up order

Full catalog (every series from every feed): [`CATALOG.md`](CATALOG.md).

One line per BTC slot (Mon 16:30, Tue 10:30). Tick when the **file exists**. Stop.

Do **not** rebuild CheckOnChain, Glassnode, OnChainMind, or CoinGlass. Take **one series** from them. Price, addresses, hashrate stay in QMI.

---

## ACTION (every BTC slot)

1. Open this list.
2. Do the next unchecked **BUILD** line.
3. Write today’s Z next to the number (from the PL log).
4. One sentence in `research/`.
5. Stop.

If the pull fails: pipeline only. No sentence required.

---

## BUILD (free first → paywall last)

Homes done. One getter + one CSV per slot. Source is what you use until you pay.

Spot and perps are **different books**. The alpha is the gap: who is selling on spot vs who is selling on futures, on which venue.

### Free — Binance public (no API key)

- [ ] 1. `trading/oi.csv` — Binance perp OI
- [ ] 2. `trading/funding.csv` — Binance funding
- [ ] 3. `trading/basis.csv` — Binance perp vs index
- [ ] 4. `trading/cvd_perp.csv` — Binance **futures** taker buy/sell (cumulate)
- [ ] 5. `trading/cvd_spot.csv` — Binance **spot** taker buy/sell (cumulate)
- [ ] 6. `trading/cvd_gap.csv` — perp CVD minus spot CVD (you compute from 4 and 5)

### Free — public table / free on-chain API

- [ ] 7. `onchain/etf_netflow.csv` — Farside
- [ ] 8. `onchain/puell.csv` — BGeometrics free or DIY
- [ ] 9. `onchain/mvrv.csv` — BGeometrics free
- [ ] 10. `onchain/sopr.csv` — BGeometrics free
- [ ] 11. `onchain/nupl.csv` — BGeometrics free

### Paid — multi-venue tape (Velo / CoinGlass)

Same series as 1–6, but **per exchange**, then aggregated. This is the Velo chart: Binance / Coinbase / Bybit / OKX, spot vs perps.

- [ ] 12. `trading/cvd_by_venue.csv` — spot CVD and perp CVD by venue (Velo API). Until paid: watch Velo / MMT.
- [ ] 13. `trading/oi_by_venue.csv` — OI by venue (Velo)
- [ ] 14. `trading/funding_by_venue.csv` — funding by venue (Velo)
- [ ] 15. `trading/premium.csv` — perp minus spot, aggregated (Velo)
- [ ] 16. `trading/liquidations.csv` — CoinGlass long/short USD. Until then: type from the page.

Heatmaps, DOM, VRVP, VPOC (OpenMarket / MMT): **watch**. Do not rebuild. Store a daily note if a level mattered.

### Paid — on-chain

- [ ] 17. `onchain/sth_mvrv.csv` — Glassnode
- [ ] 18. `onchain/exchange_netflow.csv` — Glassnode / CryptoQuant

### Join and later

- [ ] Every BTC slot after OI exists: dated sentence in `research/` — series vs Z
- [ ] `articles/` — one saved claim, marked tested / not
- [ ] `models/` — OI vs Z overlay **only after 12 OI rows**. Never a second corridor.

---

## LEARN (tick when you can say it in one sentence from your numbers)

- [ ] Flow (this block) vs structure (PL / Z)
- [ ] Open interest = leverage left open
- [ ] Funding = who is paying to stay crowded
- [ ] Liquidation map = where leverage dies (watch on CoinGlass; store the daily USD totals)
- [ ] MVRV = price vs on-chain cost basis (cousin of Z, not a copy of Z)
- [ ] SOPR = coins moved today were in profit or loss
- [ ] Exchange netflow vs ETF netflow = coins to venues vs traditional bid
- [ ] Puell = miner income stress, not hashrate

---

## FOLLOW (do not scrape the whole product)

| Source | What you take | Where it goes |
|---|---|---|
| [CoinGlass liquidation map](https://www.coinglass.com/pro/futures/LiquidationMap) | OI, funding, daily liqs, basis. Watch the map; store numbers. | `trading/` |
| [CheckOnChain](https://charts.checkonchain.com/) | One chart family → one CSV. Skip Power Law (that is QMI). | `onchain/` |
| [Glassnode Studio](https://studio.glassnode.com) | Same families, cleaner catalog: MVRV, SOPR, exchange, ETF. | `onchain/` |
| [OnChainMind](https://onchainmind.io/) | Their research claim, dated. Test later on your CSV. | `articles/` then `research/` |
| [MacroMicro WEFC](https://en.macromicro.me/blog/wefc-taco-tuesday-every-day-wall-street-bets-on-trump-s-tariff-retreats) | Macro/policy claim (tariff, dollar, risk). Not a BTC series. | `articles/` — one line vs Z if it actually moved BTC |

Stablecoins, ETH, alts → CRYPTO. Gold, oil, gas → COMMODITIES.

---

## Not in this block

- Chaos Corridor runner, β, R², bands, addresses, hashrate
- Rebuilding those five websites
- A second power-law
