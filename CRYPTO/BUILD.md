# CRYPTO — stand-up order

Full catalog (every series from every feed): [`CATALOG.md`](CATALOG.md).

One line per CRYPTO slot (Tue 14:30, Wed 10:30). Tick when the **file exists**. Stop.

Do **not** rebuild CoinGlass, Glassnode, DefiLlama, or Velo. Take **one series** from them. Bitcoin-as-network stays in BTC / QMI.

---

## ACTION (every CRYPTO slot)

1. Open this list.
2. Do the next unchecked **BUILD** line.
3. Append today’s BTC.D (`python3 scripts/get_btc_d.py`) until you leave that list.
4. One sentence in `research/`.
5. Stop.

If the pull fails: pipeline only. No sentence required.  
Z from the PL log is optional — only if the join is real.

---

## BUILD (free first → paywall last)

Homes done. BTC.D standing. One getter + one CSV per slot. Source is what you use until you pay.

ETH tape is **not** BTC tape. Do not copy `BTC/trading/oi.csv` into this block.

### Free — CoinGecko global (no API key)

Same endpoint as BTC.D. One new file per slot.

- [x] 1. `onchain/btc_d.csv` — Bitcoin share of crypto mcap
- [ ] 2. `onchain/eth_d.csv` — ETH share (`market_cap_percentage.eth`)
- [ ] 3. `onchain/total_mcap.csv` — total crypto mcap USD



### Free — Binance public (no API key)

ETHUSDT. Spot and perps are **different books**.

- [ ] 4. `trading/eth_oi.csv` — Binance ETH perp OI
- [ ] 5. `trading/eth_funding.csv` — Binance ETH funding
- [ ] 6. `trading/eth_basis.csv` — ETH perp vs index
- [ ] 7. `trading/eth_cvd_perp.csv` — ETH futures taker buy/sell (cumulate)
- [ ] 8. `trading/eth_cvd_spot.csv` — ETH spot taker buy/sell (cumulate)
- [ ] 9. `trading/eth_cvd_gap.csv` — perp CVD minus spot CVD (you compute from 7 and 8)



### Free — stables (DefiLlama)

- [ ] 10. `onchain/usdt.csv` — USDT circulating
- [ ] 11. `onchain/usdc.csv` — USDC circulating
- [ ] 12. `onchain/stables.csv` — USDT+USDC (you compute from 10 and 11)



### Paid — multi-venue tape (Velo / CoinGlass)

Same series as 4–6, per exchange, then aggregated.

- [ ] 13. `trading/eth_oi_by_venue.csv` — ETH OI by venue (Velo)
- [ ] 14. `trading/eth_funding_by_venue.csv` — ETH funding by venue (Velo)
- [ ] 15. `trading/eth_liquidations.csv` — CoinGlass ETH long/short USD. Until then: type from the page.
- [ ] 16. `trading/alt_season.csv` — CoinGlass altcoin season index. Watch until paid.



### Paid — ETH on-chain / ETF

- [ ] 17. `onchain/eth_exchange_netflow.csv` — Glassnode
- [ ] 18. `onchain/eth_gas.csv` — Glassnode base fee / gas used
- [ ] 19. `onchain/eth_staking.csv` — Glassnode staked ETH
- [ ] 20. `onchain/eth_etf_netflow.csv` — CoinGlass / Glassnode. Freeze one source.



### Join and later

- [ ] Every CRYPTO slot after BTC.D exists: dated sentence in `research/`
- [ ] `articles/` — one Townhall or feed claim, marked tested / not
- [ ] `models/` — BTC.D vs Z or ETH funding extreme **only after 12 rows** of that series. Never a corridor for ETH.

---



## LEARN (tick when you can say it in one sentence from your numbers)

- [ ] BTC.D = Bitcoin’s share of crypto. The rest is this block.
- [ ] ETH.D vs BTC.D = rotation, not a new physics.
- [ ] Stables supply = dry powder. Not a price.
- [ ] ETH funding = who is paying to stay crowded in ETH.
- [ ] ETH OI = leverage left open in ETH. Not BTC OI.
- [ ] Spot vs perp CVD on ETH = who is selling spot vs who is selling futures.
- [ ] Optional Z join: cheap BTC + rising BTC.D = alts dying into a BTC bid. Cheap BTC + falling BTC.D = risk-on alts while the corridor says cheap.
- [ ] TVL / staking = ETH as a platform. Later. Not this list.

---



## FOLLOW (do not scrape the whole product)


| Source | What you take | Where it goes |
|---|---|---|
| [CoinGecko global](https://api.coingecko.com/api/v3/global) | BTC.D, ETH.D, total mcap | `onchain/` |
| Binance public | ETH OI, funding, CVD, basis | `trading/` |
| [DefiLlama stables](https://stablecoins.llama.fi) | USDT, USDC, then the sum | `onchain/` |
| [CoinGlass](https://www.coinglass.com) | ETH liq map, ETH ETF, alt season. Watch the map; store numbers. | `trading/` |
| [Glassnode Studio](https://studio.glassnode.com) | ETH gas, staking, exchange, MVRV — one family → one CSV | `onchain/` |
| Crypto Townhall (Mon 14:30) | One claim, dated, sourced | `articles/` then `research/` if you test it |


Bitcoin tape / SOPR / MVRV / ETF / miners → BTC. Gold, oil, gas → COMMODITIES.

---



## Not in this block

- Chaos Corridor runner, β, R², bands, addresses, hashrate
- BTC OI, BTC funding, BTC SOPR, BTC ETF
- A second power-law, including an ETH “corridor”
- Rebuilding CoinGlass / Glassnode / DefiLlama / Velo
