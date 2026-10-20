# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [83144,83145,82150,82038,82797,82763,82872,82367,82536,81981,80612,80862,80484,80242,80034,79063,79245,80227,80016,80507,81625,81233,81544,81578,82016,81401,81019,81186,81130,81118,81306,82066,81909,80392,80304,80291,80258,79729,79261,69466,69579,69456,68251,68415,66832,67911,67462,67144,66432,64380,64375,64606,63741,64647,64324,64216,63842,63877,64079,64008,65156,65945,65888,65157,65625,66144,67284,66653,66639,65924,66925,66956,67263,67108,66766,66729,66886,70927,70673,70049,50652,69334,69973,68400,68061,68578,68877,68879,69055,68662,68822,69329,72687,71999,71760,71163,71911,71896,32500,29218,71927,71297,71305,71044,71337,71883,71822,71536,71536,71622,71723,71880,71860,72100,72216,71887,72077,72940,72976,72966,72638,72948,73497,73004,73041,73173,73160,73187,73258,73375,73351,73173,73098,73161,73305,73474,73536,73457,73413,73412,72100,72333,72164,72272,72204,72285,72461,72421,71652,71521,72267,72157,72774,72425,72144,72060,72091,71858,90185,91338,91466,90900,91678,91404,91268,91244,90903,90779,90787,90721,90187,92429,90518,90619,91070,90328,89376,93286,92202,92581,92485,91947,91196,91259,89619,90086,92063,91355,90950,91327,90373,91498,91800,92531,91603,90910,90031,89351,89334,92097,94406,94315,95455,98972,99763,100286,99229,99622,99701,99805,99938,99738,99082,97430,98094,97267,96741,98081,98013,98194,97447,97983,97789,97969,97729,97911,98043,98405,97912,97120,97448,97154,98095,97021,97191,97616,97402,97263,98035,97210,98424,100121,100876,97552,98049,98085,98228,98388,98342,98488,98750,99086,99181,100188,99107,99272,99553,99072,99636,99061,99186,97674,96679,96704,96743,96096,92830,95088,95560,94866,94995,95295,95497,95531,95527,95559,96236,96597,95538,94422,96363,95972,95418,93095,93128,94558,94795,94727,94611,94508,93857,93852,93955,93340,93862,94112,94249,93603,94682,93898,94267,94288]
```

## 资产明细
- **BTC**: $62484.0
- **ETH**: $19218.0
- **SOL**: $12416.0
- **USDT**: $168.5

## 交易记录
- 2026-10-20T04:31:00.000000 - HOLD - No new trades executed. Defensive hold on BTC/ETH/SOL at oversold levels (RSI: BTC 37 / ETH 25 / SOL 26); kept resting above-market sell-trim orders BTC 0.12@82700, ETH 1.5@2460, SOL 2@109.5 & 2.36@110.2. No margin/liquidation risk.
- 2026-10-20T04:31:00.000000 - Portfolio weights: BTC 66.3% / ETH 20.4% / SOL 13.2% / USDT ~0.2% (~$94,288 total equity). SOL trim-on-strength only into 111-117 (currently below zone); add BTC only on reclaim >= 84K.
- 2026-10-19T23:41:00.000000 - Buy 13.9155 SOL-USDT limit @ $104.20 (~$1,450 USDT, ordId 4024870491446063105, clOrdId solAccum1042) - accumulate SOL on dip into EMA-99 support; state live
- 2026-10-19T23:41:00.000000 - HOLD BTC & ETH; kept resting TP sells BTC 0.12@82700, ETH 1.5@2460, SOL 2@109.5 & 2.36@110.2; SOL relative leader -> small dip accumulation
- 2026-10-19T19:48:28.904924 - Placed limit SELL 0.12 BTC-USDT @ 82700 (ordId 4024417940506423297) to trim overweight BTC into resistance; live
- 2026-10-19T19:48:28.904924 - Canceled resting BTC-USDT BUY 0.0135 @ 80400 (ordId 4019629418285117441) to cut concentration and free ~1085 USDT
- 2026-10-19T04:23:00.000000 - Placed SOL-USDT limit BUY 20 SOL @ 104.00 (ordId 4022546721368715265) - dip accumulation ahead of Oct-21 Alpenglow mainnet upgrade
- 2026-10-19T04:23:00.000000 - Canceled SOL-USDT SELL 2.0 @ 107.20 (ordId 4018702296846708737); re-placed limit SELL 2.0 SOL @ 109.50 (ordId 4022546716369104897) to give the upgrade room
- 2026-10-19T04:23:00.000000 - Kept resting orders: ETH-USDT SELL 1.5 @ 2460, BTC-USDT BUY 0.0135 @ 80400, SOL-USDT SELL 2.36 @ 110.20
- 2026-10-19T04:23:00.000000 - No fills this cycle; all maker limit orders resting; totalEq ~$94,682; USDT avail ~$533 (frozen $3,165 in open orders)
- 2026-10-18T22:26:00.000000 - Placed limit SELL 1.5 ETH-USDT @ 2460 (orderId 4021831078046609409) - defensive trim into bounce, lower cost-basis risk
- 2026-10-18T22:26:00.000000 - Kept existing orders: BTC buy 0.0135 @ 80400, BTC sell 0.03 @ 82600, SOL sells 2 @ 107.2 and 2.36 @ 110.2
- 2026-10-18T10:55:00.000000 - Place BUY 0.008 BTC @ 81,300 USDT limit (orderId 4020438141836472321) - resting dip-accumulation order
- 2026-10-18T04:12:00.000000 - Placed BTC-USDT buy limit 0.0135 @ 80400 (dip-buy at $79.8k-80.4k support, ordId 4019629418285117441, clOrdId dipBuyBtc80400, live/unfilled)
- 2026-10-18T04:12:00.000000 - Kept existing sell orders: BTC-USDT 0.03 @ 82600 (ordId 4018702290001604609), SOL-USDT 2 @ 107.2 (ordId 4018702296846708737), SOL-USDT 2.36 @ 110.2 (ordId 4013025081735786497)
- 2026-10-18T04:12:00.000000 - No fills/cancellations/market orders this cycle; HOLD core BTC/ETH/SOL; ~$1096 USDT reserve remaining
- 2026-10-17T20:33:00.000000 - Re-placed SOL sell 2 @107.2 (from 108.5)
- 2026-10-17T20:33:00.000000 - Re-placed BTC sell 0.03 @82600 (from 82800)
- 2026-10-17T20:33:00.000000 - Bought 0.035 BTC @81635.6 (BTC-USDT)
- 2026-10-17T20:33:00.000000 - Sold 1.2 ETH @2420.18 (ETH-USDT)
- 2026-10-17T20:33:00.000000 - Canceled ETH sell order 1.2 @2540
- 2026-10-17T20:33:00.000000 - Canceled SOL buy order 9 @102.6 (freed ~923 USDT)
- 2026-10-17T20:33:00.000000 - Canceled ETH buy order 0.4 @2360 (freed ~944 USDT)
- 2026-10-17T17:05:09.004922 - No fills this cycle; kept all 6 resting orders; Cycle tape BTC ~81264 / ETH ~2404 / SOL ~103.2; totalEq ~93339 USDT; free USDT ~270
- 2026-10-17T17:05:09.004922 - HOLD BTC (daily downtrend, short-term oversold; ~65% of equity overweight) - keep SELL 0.03 @ 82800; no adds
- 2026-10-17T17:05:09.004922 - HOLD ETH (downtrend basing above 2317; daily RSI ~22 deeply oversold) - keep BUY 0.4 @ 2360 dip and SELL 1.2 @ 2540 trim
- 2026-10-17T17:05:09.004922 - HOLD SOL (1D oversold, 4H coiling; Alpenglow upgrade Oct 21 catalyst) - keep BUY 9 @ 102.6 dip and SELL 2 @ 108.5 / 2.36 @ 110.2 trims
- 2026-10-17T12:12:00.000000 - No fills this cycle; kept 6 resting orders; Cycle tape BTC ~81560 / ETH ~2433 / SOL ~104.3; totalEq ~93955 USDT
- 2026-10-17T12:12:00.000000 - No new buys this cycle (free USDT only ~$270, account already over-long/BTC-concentrated into risk-off tape) - defensive hold
- 2026-10-17T12:12:00.000000 - HOLD SOL (daily oversold RSI 27, Oct 21 Alpenglow catalyst) - keep BUY 9 @102.6 dip bid and SELL 2.0 @108.5 / 2.36 @110.2 trims
- 2026-10-17T12:12:00.000000 - HOLD ETH (relative-strength leader: 4H bullish MACD cross, daily RSI 26 oversold) - keep BUY 0.4 @2360 dip bid and SELL 1.2 @2540 trim
- 2026-10-17T12:12:00.000000 - HOLD BTC (daily downtrend, 1D RSI 38, ~65% of equity overweight) - no adds; trim only on strength
- 2026-10-17T12:12:00.000000 - REPRICED: Canceled SELL 0.03 BTC-USDT @ 84,900 (botBtcTrimUp1016) and placed SELL 0.03 BTC-USDT @ 82,800 (botBtcTrim1017, ordId=4017696427048710145) - move de-risk trim below EMA99/resistance so it can fill on a bounce
- 2026-10-17T00:28:00.000000 - PLACED: Buy 9.0 SOL-USDT limit @102.6 (~$923.4 USDT, ordId=4016263684880347137, clOrdId=botSolDip1017) - accumulate into 100.5-102.6 ahead of Oct21 Alpenglow upgrade; invalidation <100
- 2026-10-17T00:28:00.000000 - HOLD BTC (daily downtrend, RSI 38.6) - keep SELL 0.03 @84900; add only near 80000
- 2026-10-17T00:28:00.000000 - HOLD ETH (oversold RSI 25.4, weakest structure) - keep SELL 1.2 @2540 and BUY 0.4 @2360; sell rallies 2470-2540
- 2026-10-17T00:28:00.000000 - HOLD SOL - keep SELL 2.0 @108.5 and 2.36 @110.2 trims (targets)
- 2026-10-17T00:28:00.000000 - Cycle tape (BTC ~81639 / ETH ~2423 / SOL ~104.4); totalEq ~93852 USDT; USDT avail ~270 after new SOL dip order
- 2026-10-16T20:53:41.870070 - FILLED: Buy 1.1 ETH-USDT limit @ 2415 (~$2656.5 USDT, ordId=4015855924275589121) - botEthDip1016b add on oversold dip (daily RSI ~25, near daily lower BB)
- 2026-10-16T20:53:41.870070 - HOLD BTC (daily downtrend, no chase) - keep SELL 0.03 @84900; hold USDT for dip-buys below 80k
- 2026-10-16T20:53:41.870070 - HOLD ETH - keep SELL 1.2 @2540 at resistance; adding done
- 2026-10-16T20:53:41.870070 - HOLD SOL (weakest of the three) - keep SELL 2.0 @108.5 and 2.36 @110.2 trims; no new adds before Oct21 Alpenglow upgrade
- 2026-10-16T20:53:41.870070 - Cycle tape (BTC ~81700 / ETH ~2415 / SOL ~104); totalEq ~93857 USDT; USDT avail ~1193 after ETH fill
- 2026-10-16T13:20:00.000000 - Place limit BUY 7.5 SOL-USDT @ 103.5 (botSolDip1016, ~$776 USDT) - dip-accumulation add into 102-104 support; do not chase above 108
- 2026-10-16T13:20:00.000000 - FILLED since prior cycle: Buy 2.04 ETH @ 2450 (botEthBuy1016) and Buy 56.5 SOL @ 106.2 (botSolBuy1016) - ETH 5.40 -> 7.43, SOL 17.31 -> 73.81
- 2026-10-16T13:20:00.000000 - HOLD BTC (over-concentrated ~64% of equity, daily downtrend, macro-capped) - keep core; SELL 0.03 @84900 resting; hold dry USDT for dip-buys below 80k
- 2026-10-16T13:20:00.000000 - HOLD ETH (daily oversold, intraday overbought) - keep SELL 1.2 @2540 at resistance; add only on dip 2400-2430
- 2026-10-16T13:20:00.000000 - SOL best structure of the three (4H MACD bull cross, Alpenglow mainnet-beta Oct 21) - small add only; keep SELL 2 @108.5 and 2.36 @110.2
- 2026-10-16T13:20:00.000000 - Kept resting: BUY 0.01 BTC @81000, BUY 0.4 ETH @2395, BUY 0.25 ETH @2395, BUY 0.4 ETH @2360, SELL 0.03 BTC @84900, SELL 1.2 ETH @2540, SELL 2 SOL @108.5, SELL 2.36 SOL @110.2
- 2026-10-16T13:20:00.000000 - Defensive-hold tape (daily downtrend, oversold bounce underway; BTC 82050 / ETH 2465 / SOL 105.6); BTC/ETH HOLD core, small SOL dip-add; new risk this cycle ~$776; totalEq ~94508 USDT
- 2026-10-16T07:00:00.000000 - Buy 2.04 ETH @ 2450 (~$4,998 USDT) - botEthBuy1016 (FILLED; ETH 5.40 -> 7.43)
- 2026-10-16T07:00:00.000000 - Place limit BUY 56.5 SOL @ 106.2 (~$6,000 USDT) - botSolBuy1016 (LIVE, inside 105.0-106.4 entry zone)
- 2026-10-16T07:00:00.000000 - HOLD BTC (downtrend, macro-capped by PPI 6.3% + ETF outflows ~$261M); keep dry USDT for dip-buys < $80k
- 2026-10-16T07:00:00.000000 - Kept resting: BUY 0.01 BTC @81000, SELL 0.03 BTC @84900, BUY 0.25 ETH @2395, BUY 0.4 ETH @2395, BUY 0.4 ETH @2360, SELL 1.2 ETH @2540, SELL 2 SOL @108.5, SELL 2.36 SOL @110.2
- 2026-10-16T07:00:00.000000 - Tape: majors correcting, alt momentum alive; SOL strongest RS (Alpenglow upgrade Oct 21) + ETH outperformer (whale rotation BTC->ETH, spot inflows) -> scale in; BTC HOLD. USDT dry ~$4.6k; totalEq ~94611 USDT
- 2026-10-16T00:18:00.000000 - Cancel stale limit SELL 0.03 BTC-USDT @84200 (botBtcTrim1015) - lifted exit into 84900-86100 resistance zone
- 2026-10-16T00:18:00.000000 - Place limit SELL 0.03 BTC-USDT @84900 (botBtcTrimUp1016) - trim over-concentrated (~64% of equity) BTC into 84900 resistance
- 2026-10-16T00:18:00.000000 - Place limit BUY 0.25 ETH-USDT @2395 (botEthDipAdd1016) - add ~$599 to preferred oversold name at 2395 support rung
- 2026-10-16T00:18:00.000000 - Keep resting BUY 0.01 BTC-USDT @81000, BUY 0.4 ETH-USDT @2395, BUY 0.4 ETH-USDT @2360, SELL 1.2 ETH-USDT @2540, SELL 2.0 SOL-USDT @108.5, SELL 2.36 SOL-USDT @110.2 - HOLD core
- 2026-10-16T00:18:00.000000 - No fills this cycle. Constructive-but-cautious tape (hot CPI 3.7%/PPI 6.3%, spot-ETF outflows, corporate/treasury bid BTC & ETH); RS BTC>ETH>SOL; BTC strongest -> HOLD + lift trim 0.03 to 84900; ETH daily RSI 26 deeply oversold (best risk/reward) -> add 0.25@2395 atop 0.4@2395 & 0.4@2360 + trim 1.2@2540; SOL weakest but fully frozen (avail 0.0047, 17.347 blocked) -> trim 2.0@108.5 & 2.36@110.2 unchanged; USDT buffer ~$18.9k; totalEq ~94727 USDT
- 2026-10-15T21:30:00.000000 - Cancel stale limit SELL 4.36 SOL-USDT @110.5 (botSolTrimAvail1015) - re-priced down into 108.5-110.2 resistance
- 2026-10-15T21:30:00.000000 - Place limit SELL 2.0 SOL-USDT @108.5 (botSolTrimA1015) - trim weakest name into 108-110 resistance
- 2026-10-15T21:30:00.000000 - Place limit SELL 2.36 SOL-USDT @110.2 (botSolTrimB1015) - trim weakest name near 110.5 top of range
- 2026-10-15T21:30:00.000000 - Place limit BUY 0.4 ETH-USDT @2360 (botEthDip1015b) - second dip-buy rung at 2340-2360 support
- 2026-10-15T21:30:00.000000 - Keep resting BUY 0.01 BTC-USDT @81000, SELL 0.03 BTC-USDT @84200, BUY 0.4 ETH-USDT @2395, SELL 1.2 ETH-USDT @2540 - HOLD core
- 2026-10-15T21:30:00.000000 - No fills this cycle. Cautious oversold-bounce tape (hot CPI 3.7%/PPI 6.3%, spot-ETF outflows BTC $261M / ETH $129M / SOL 8-day streak); BTC strongest -> HOLD + trim 0.03@84200; ETH daily RSI 28 oversold -> dip-buys 0.4@2395 & 0.4@2360 + trim 1.2@2540; SOL weakest (below EMA99, daily RSI 27.7) -> trim 2.0@108.5 & 2.36@110.2; USDT buffer ~$18.9k; totalEq ~94795 USDT
- 2026-10-15T16:50:00.000000 - Place limit BUY 0.01 BTC-USDT @81000 (botBtcDip1015) - dip-buy at 80200 support; add strongest name
- 2026-10-15T16:50:00.000000 - Place limit SELL 0.03 BTC-USDT @84200 (botBtcTrim1015) - trim over-concentrated (~64% of equity) BTC into 83900-84400 resistance
- 2026-10-15T16:50:00.000000 - Place limit BUY 0.4 ETH-USDT @2395 (botEthDip1015) - dip-buy above 2360-2340 support; ETH 1D RSI 25 oversold
- 2026-10-15T16:50:00.000000 - Place limit SELL 1.2 ETH-USDT @2540 (botEthTrim1015) - trim into 2540 resistance
- 2026-10-15T16:50:00.000000 - Place limit SELL 4.36 SOL-USDT @110.5 (botSolTrimAvail1015) - trim weakest name into 110-112 resistance; 8 SOL blocked by 12.987 stuck frozen (not cancelable)
- 2026-10-15T16:50:00.000000 - Neutral/risk-off tape (hot CPI 3.7%/PPI 6.3%, broad spot-ETF outflows, taker flow net sell, crowded OKX longs BTC 4.1/ETH 5.3/SOL 12.8); SOL weakest -> trim 4.36@110.5; ETH dip-buy 0.4@2395 / trim 1.2@2540; BTC HOLD + dip 0.01@81000 / trim 0.03@84200; USDT buffer ~$18.9k; totalEq ~94558 USDT
- 2026-10-15T11:20:00.000000 - Cancel stale limit SELL 10 SOL-USDT @106.5 (botSolTrim1015) - re-priced down into reduce zone
- 2026-10-15T11:20:00.000000 - Cancel stale limit SELL 2.2 ETH-USDT @2412 (botEthTrim1015) - nudged up to resistance
- 2026-10-15T11:20:00.000000 - Place limit SELL 8 SOL-USDT @104.8 (botSolTrimA1015) - SOL reduce ladder
- 2026-10-15T11:20:00.000000 - Place limit SELL 8 SOL-USDT @104.4 (botSolTrimB1015) - SOL reduce ladder
- 2026-10-15T11:20:00.000000 - Place limit SELL 2.2 ETH-USDT @2420 (botEthTrim1015b) - trim into 2420-2500 resistance
- 2026-10-15T11:20:00.000000 - HOLD 0.7392 BTC (untouched) - neutral/bearish, no sale; optional dip-bid skipped
- 2026-10-15T11:20:00.000000 - Defensive risk-off tape (hot CPI 3.7%, ETF outflows, deleveraging); SOL weakest -> reduce 16 SOL into 104.4-104.8; ETH trim 2.2 @2420; BTC HOLD; USDT buffer ~11.9k (~12.8% of equity); totalEq ~93128 USDT
- 2026-10-15T04:20:00.000000 - HOLD 0.7392 BTC (untouched, near 80.8k support), no new buys this cycle
- 2026-10-15T04:20:00.000000 - Placed limit SELL 10 SOL-USDT @106.5 (botSolTrim1015) - trim ~30% of SOL into resistance 105-108
- 2026-10-15T04:20:00.000000 - Placed limit SELL 2.2 ETH-USDT @2412 (botEthTrim1015) - trim ~29% of ETH into resistance 2400-2440
- 2026-10-15T04:20:00.000000 - Cancel stale limit SELL 3 SOL-USDT @108.8 (botSolTrim1014) - ~6% above market, was freezing inventory
- 2026-10-15T04:20:00.000000 - Cancel stale limit SELL 2.5 ETH-USDT @2509 (botEthTrim1014) - ~6% above market, was freezing inventory
- 2026-10-14T13:40:00.000000 - Cancel BTC-USDT buy 0.01 @79500 (botBtcDip1012b) - below 80.9k support, dead
- 2026-10-14T13:40:00.000000 - Cancel ETH-USDT buy 0.5 @2395 (botEthDip1012) - off-market, replacing
- 2026-10-14T13:40:00.000000 - Cancel SOL-USDT sell 3 @110.5 (botSolTrim1013) - far above market, dead
- 2026-10-14T13:40:00.000000 - Cancel SOL-USDT sell 5 @116.5 (botSolTp1011) - far above market, dead
- 2026-10-14T13:40:00.000000 - Place SELL 2.5 ETH-USDT @2509 (botEthTrim1014) - trim weakest name into 2509-2517 resistance band
- 2026-10-14T13:40:00.000000 - Place BUY 0.8 ETH-USDT @2415 (botEthDip1014) - raise dip-buy toward support
- 2026-10-14T13:40:00.000000 - Place SELL 3 SOL-USDT @108.8 (botSolTrim1014) - trim into resistance
- 2026-10-14T13:40:00.000000 - Place BUY 0.01 BTC-USDT @80900 (botBtcDip1014n) - dip ladder at 80.9k support
- 2026-10-14T13:40:00.000000 - Keep resting BUY 0.01 BTC-USDT @80500 (botBtcDip1012) - dip ladder top-up
- 2026-10-14T13:40:00.000000 - Defensive risk-off tape (hot CPI 3.7%, all majors oversold at lower Bollinger bands); ETH SELL(62) weakest -> partial exit 2.5 @2509; BTC/SOL HOLD; USDT buffer ~11.9k (~12% of equity); totalEq ~95418 USDT
- 2026-10-13T21:15:00.000000 - Cancel BTC-USDT sell 0.03 @85800 (botBtcTp1011)
- 2026-10-13T21:15:00.000000 - Place BTC-USDT sell 0.05 @84300 (botBtcTp1013, order 4007188937131438081) - de-risk, raise USDT
- 2026-10-13T21:15:00.000000 - Cancel ETH-USDT sell 0.5 @2585 (botEthTp1012)
- 2026-10-13T21:15:00.000000 - Place ETH-USDT sell 0.5 @2540 (botEthTp1013, order 4007188943573889025) - lower trim to 99-EMA resistance
- 2026-10-13T21:15:00.000000 - Cancel SOL-USDT sell 4 @111.5 (botSolTrim1012)
- 2026-10-13T21:15:00.000000 - Place SOL-USDT sell 3 @110.5 (botSolTrim1013, order 4007188950016339969) - trim into resistance
- 2026-10-13T21:15:00.000000 - Market neutral-bearish (CPI-week caution, RSI ~37-40 all majors); BTC over-concentrated at 67% of equity - de-risked the tape, freed sell orders toward 15-20% USDT
- 2026-10-13T21:15:00.000000 - No new buys added; kept BTC dip-buys 0.01@80500/79500, ETH dip-buy 0.5@2395
- 2026-10-13T06:40:00.000000 - No coin trading into its resistance/trim zone; nothing to sell into strength. HOLD all. totalEq ~96,363 USDT; ~5,532 USDT dry powder retained
- 2026-10-12T23:10:00.000000 - Placed 6 resting limit orders: BUY 0.01 BTC-USDT @ 80500 (botBtcDip1012), BUY 0.01 BTC-USDT @ 79500 (botBtcDip1012b), BUY 0.5 ETH-USDT @ 2395 (botEthDip1012), SELL 0.5 ETH-USDT @ 2585 (botEthTp1012), SELL 0.02 BTC-USDT @ 84000 (botBtcTp1012), SELL 4 SOL-USDT @ 111.5 (botSolTrim1012)
- 2026-10-12T23:10:00.000000 - Kept resting take-profits SELL 5 SOL-USDT @ 116.5 (botSolTp1011) and SELL 0.03 BTC-USDT @ 85800 (botBtcTp1011); no cancellations
- 2026-10-12T23:10:00.000000 - Noted prior-cycle fills: BUY 0.5 ETH-USDT @ 2460 + 0.4 ETH-USDT @ 2510 (dip-ladder adds), BUY 0.04 BTC-USDT @ 81900/82700/83000, BUY 8.5 SOL-USDT @ 108, SELL 0.5 ETH-USDT @ 2585 (TP)
- 2026-10-12T23:10:00.000000 - Defensive de-levered tape (OKX loan ratios ~2.6-4.2, spot-ETF outflows); BTC HOLD (RS 58), ETH HOLD/accumulate (62, daily RSI ~30), SOL trim 4@111.5 (70, weakest - lost 99-EMA 111.15); ~5532 USDT dry powder retained
- 2026-10-12T23:10:00.000000 - No fills this cycle; account ~91% invested, totalEq ~94422 USDT
- 2026-10-12T05:34:57.000000 - Place limit BUY 0.01 BTC @ 83000 (order 4002407848793878529, top-up strongest-RS BTC dip ladder to ~3% size)
- 2026-10-12T05:34:57.000000 - Place limit BUY 0.40 ETH @ 2485 (order 4002407853558607873, build underweight ETH on dip within 2480-2520 entry zone)
- 2026-10-12T05:34:57.000000 - KEEP 9 resting orders - BTC dip ladder 83000/82700/81900, ETH dip ladder 2510/2485/2460; TP sells BTC 0.03@85800, ETH 0.5@2585, SOL 5@116.5
- 2026-10-12T05:34:57.000000 - HOLD BTC/ETH/SOL core - no SOL adds (weakest RS); no cancellations; no fills this cycle
- 2026-10-11T18:47:45.000000 - Place limit BUY 0.4 ETH @ 2510 (order 4001107803599548417, scale-in dip-buy; deepest-oversold major)
- 2026-10-11T18:47:45.000000 - Keep resting BUY 0.6 ETH @ 2460 (order 4000353679685726209, pre-existing dip-buy)
- 2026-10-11T18:47:45.000000 - HOLD BTC/ETH/SOL core - no SOL adds (weakest RS, below 20-SMA ~116.9, negative daily MACD); no cancellations
- 2026-10-11T12:40:00.000000 - Place limit BUY 0.02 BTC @ 81900 (order 4000353673612374017, resting dip-buy)
- 2026-10-11T12:40:00.000000 - Place limit BUY 0.6 ETH @ 2460 (order 4000353679685726209, resting dip-buy)
- 2026-10-11T12:40:00.000000 - Place limit SELL 4.38 SOL @ 111.8 on SOL-USDT (order 4000353685859741697, ~15% trim, resting)
- 2026-10-11T12:40:00.000000 - Keep resting TP SELL 0.05 BTC @ 84000 (order 3994603626224431105) and SELL 1.5 ETH @ 2549 (order 3994603619949752321)
- 2026-10-11T12:40:00.000000 - HOLD BTC/ETH/SOL core - no new SOL adds (weakest, below EMA99, negative daily MACD); no cancellations
- 2026-10-11T05:23:48.000000 - Sell 16.24 SOL @ avg 109.72 on SOL-USDT (market), received ~1781.9 USDT, fee 1.78 USDT [order 3999481216605106177]
- 2026-10-11T05:23:48.000000 - HOLD BTC (neutral, range 82200-83700, conf 55); HOLD ETH (neutral, conf 55)
- 2026-10-10T23:26:00.000000 - Cancelled 4 stale resting dip-buys (BTC 0.007@81900, SOL 3@106, ETH 0.24@2465, ETH 0.26@2465); freed ~2123.8 USDT
- 2026-10-10T23:26:00.000000 - Placed limit BUY 0.20 ETH-USDT @ 2500 (order 3998768379305930753, ~500 USDT, ~10% of avail USDT, resting unfilled)
- 2026-10-10T23:26:00.000000 - Kept reduce-only take-profit sells: BTC 0.05@84000, ETH 1.5@2549; no adds to BTC/SOL; flat/no shorts
- 2026-10-10T18:30:00.000000 - HOLD - no new orders this cycle; kept 6 resting limits (BTC buy 0.007@81900, BTC sell 0.05@84000, ETH buy 0.5@2465, ETH sell 1.5@2549, SOL buy 3@106); account ~95% invested, ~2815 USDT dry powder
- 2026-10-10T12:25:12.000000 - Place limit BUY 0.26 ETH @ $2,465 (order 3997422013258412033, resting ETH dip-buy; combined pending ETH dip-buy now 0.5 ETH; BTC/SOL HOLD, no fills)
- 2026-10-10T00:00:38.000000 - Place limit BUY 0.007 BTC @ $81,900 (order 3995931476030402561, resting unfilled dip-buy)
- 2026-10-10T00:00:38.000000 - Place limit BUY 0.24 ETH @ $2,465 (order 3995931480493142017, resting unfilled dip-buy)
- 2026-10-10T00:00:38.000000 - Place limit BUY 3 SOL @ $106.0 (order 3995931484855218177, resting unfilled dip-buy)
- 2026-10-09T19:26:10.987713 - Sell 24 SOL @ avg $109.29 on SOL-USDT (market), received ~2622.96 USDT
- 2026-10-09T13:01:19.838220 - Sell limit 0.05 BTC @ 84000 USDT (resting, unfilled)
- 2026-10-09T13:01:19.838216 - Sell limit 1.5 ETH @ 2549 USDT (resting, unfilled)
- 2026-10-09T05:45:04.031332 - Buy 13.5 SOL @ 110.58, spent ~1492.83 USDT
- 2026-10-08T17:21:48.979950 - Place limit SELL 1.5 ETH @ $2,600.0 (order 3992228753720225793)
- 2026-10-08T17:21:48.979947 - Place limit SELL 25 SOL @ $114.0 (order 3992228749190377473)
- 2026-10-08T00:19:49.237529 - Buy 0.0239853 BTC @ avg 83384.4, spent 2000 USDT (BTC-USDT market)
- 2026-10-08T00:19:49.237526 - Buy 1.164435 ETH @ avg 2576.36, spent 3000 USDT (ETH-USDT market)
- 2026-10-07T13:15:12.299690 - Buy 1.171531 ETH, spent 3000 USDT (avg 2560.75)

## MCP工具
- [mcp-aktools](https://github.com/aahl/mcp-aktools): 用于查询价格走势及行情
- [mcp-okx](https://github.com/aahl/mcp-okx): 用于获取欧易账户信息和下单
- [mcp-notify](https://github.com/aahl/mcp-notify): 用于推送分析结果到指定渠道(可选)
- [mcp-hooks](https://github.com/aahl/ai-trading/tree/main/mcp-hooks.py): 用于保存交易结果和更新Readme

## 相关链接
- https://t.me/s/mcpBtc
- [自动交易工作流配置文件](https://github.com/aahl/ai-trading/blob/main/.github/workflows/claude.yaml)
- [自动交易工作流运行记录](https://github.com/aahl/ai-trading/actions/workflows/claude.yaml)
- [智谱免费模型可用于 Claude Code](https://www.bigmodel.cn/invite?icode=EwilDKx13%2FhyODIyL%2BKabHHEaazDlIZGj9HxftzTbt4%3D)
- [GLM Coding Plan·限时优惠](https://www.bigmodel.cn/claude-code?ic=WTOWFVEJXH)
- [欧易模拟盘API接口申请](https://www.okx.com/zh-hans/help/how-can-i-do-spot-trading-with-the-jupyter-notebook)
