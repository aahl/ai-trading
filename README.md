# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [80242,80034,79063,79245,80226,80016,80507,81625,81233,81544,81578,82016,81401,81019,81186,81130,81118,81306,82066,81909,80392,80304,80291,80258,79729,79261,69466,69579,69456,68251,68415,66832,67911,67462,67144,66432,64380,64375,64606,63740,64647,64324,64216,63842,63877,64078,64008,65156,65945,65888,65157,65625,66144,67284,66653,66639,65924,66925,66956,67263,67108,66766,66729,66886,70927,70673,70049,50652,69334,69973,68400,68061,68578,68876,68879,69055,68662,68822,69329,72687,71999,71760,71162,71911,71896,32500,29218,71927,71297,71305,71044,71337,71883,71822,71536,71536,71622,71723,71880,71860,72100,72216,71887,72077,72940,72976,72966,72638,72948,73497,73004,73041,73173,73160,73186,73258,73375,73351,73173,73098,73161,73305,73474,73536,73457,73413,73412,72100,72333,72164,72272,72204,72285,72461,72421,71652,71521,72267,72157,72774,72424,72144,72060,72091,71858,90185,91338,91466,90900,91678,91404,91268,91244,90903,90779,90787,90721,90187,92429,90518,90619,91070,90328,89376,93286,92202,92581,92485,91947,91196,91259,89619,90086,92063,91355,90950,91327,90373,91498,91800,92531,91603,90910,90031,89351,89334,92097,94406,94315,95455,98972,99763,100286,99229,99622,99701,99805,99938,99738,99082,97430,98094,97267,96741,98081,98013,98194,97447,97983,97789,97969,97729,97911,98043,98405,97912,97120,97448,97154,98095,97021,97190,97616,97402,97263,98035,97210,98424,100120,100876,97552,98049,98085,98228,98388,98342,98488,98750,99086,99181,100188,99107,99272,99553,99072,99636,99061,99186,97674,96679,96704,96743,96096,92830,95088,95560,94866,94995,95295,95497,95531,95527,95559,96236,96597,95538,94422,96363,95972,95418,93094,93128,94558,94795,94727,94611,94508,93857,93852,93954,93340,93862,94112,94249,93603,94682,93898,94267,94288,93490,95337,95601,95226,95879,97301,96573,95113,93569,93681,92773]
```

## 资产明细
- **BTC**: $56765.5
- **ETH**: $12440.0
- **SOL**: $16243.6
- **USDT**: $7323.8

## 交易记录
- 2026-10-23T23:04:54.917402 - Placed limit SELL 1 ETH-USDT @ 2430 (ordId 4036406007320555521, live) and SELL 1 ETH-USDT @ 2470 (ordId 4036406014098550785, live) - staggered trims of weakest name ABOVE spot (~2368), fills only on a bounce; no market dump at oversold lows
- 2026-10-23T23:04:54.917402 - Kept take-profit ladder: BTC 0.05 @ 82800 (4033317888488648705), SOL 2.36 @ 106.6 (4033317902648619009), SOL 2.0 @ 105.8 (4033317895568633857) - all live. No new buys, no cancellations, no fills
- 2026-10-23T23:04:54.917402 - HOLD / cautious-bearish - BTC/ETH/SOL RSI 12-15 (extreme oversold), all below key EMAs with negative MACD + ETF outflows; relative strength BTC>SOL>ETH; avoided chasing shorts at the bottom, kept ~7.9pct USDT dry powder; totalEq ~92773
- 2026-10-23T18:19:42.000000 - Sold 2.0 ETH-USDT market @ avg $2,380.08, received ~$4,755 USDT (order 4035831891022589953, filled) - trimmed weakest name (weakest technicals, heavy long unwind, soft catalysts) to rebuild cash buffer; kept core 5.2487 ETH
- 2026-10-23T18:19:42.000000 - Cancelled live ETH-USDT limit SELL 2.0 ETH @ $2,435 (ordId 4033317909762158593) - low fill odds above spot; de-risked via market instead
- 2026-10-23T18:19:42.000000 - Kept take-profit ladder: BTC 0.05 @ $82,800, SOL 2.36 @ $106.6, SOL 2.0 @ $105.8 (all live). HOLD / no new buys - book was ~97pct crypto / 2.7pct cash into a broad daily downtrend; USDT buffer lifted to ~7.8pct; totalEq ~93681
- 2026-10-22T21:34:40.046207 - HOLD / no new buys - RISK-OFF tape; all majors oversold and downtrending (BTC -4.2pct / ETH -4.6pct / SOL -4.5pct); kept ~2577 USDT (~2.8pct) dry powder; only limit maker sells above spot; totalEq ~93569
- 2026-10-22T21:34:40.046207 - Placed limit SELL 2 SOL-USDT @ 105.80 (ordId 4033317895568633857, live) and SELL 2.36 SOL-USDT @ 106.60 (ordId 4033317902648619009, live) - trims re-listed inside SOL reduce zone
- 2026-10-22T21:34:40.046207 - Placed limit SELL 2 ETH-USDT @ 2435 (ordId 4033317909762158593, live) - reduce weakest name into 2430-2460 supply band
- 2026-10-22T21:34:40.046207 - Placed limit SELL 0.05 BTC-USDT @ 82800 (ordId 4033317888488648705, live) - trim overweight BTC (~61pct of book) into 1D-mid resistance
- 2026-10-22T21:34:40.046207 - Cancelled 3 stale far-above-market sells: BTC 0.05 @ 85100 (ordId 4030625117973786625), SOL 2 @ 109.50 (ordId 4022546716369104897), SOL 2.36 @ 110.20 (ordId 4013025081735786497) - unfillable in a falling tape
- 2026-10-22T04:21:46.000000 - Buy 1.3497 ETH-USDT market @ 2445.03 USDT, spent 3300 USDT (mean-reversion long; deepest oversold + net taker buying/inflows; order 4031246007774228481, filled)
- 2026-10-22T04:21:46.000000 - Sell 17 SOL-USDT market @ 105.52 USDT, received 1793.84 USDT (trim on SELL signal - real distribution/ETF outflows into breakdown; order 4031246014552223745, filled)
- 2026-10-21T23:13:00.000000 - Sell 0.05 BTC limit @ $85,100 - trim into strength/resistance (order 4030625117973786625, resting live, ~1% above mkt $84,270); reduced outsized/overbought BTC (~56% of book). Kept BTC dip-buys 0.027@83350 & 0.033@81800, ETH buy 0.75@2468, SOL trims 2@109.5 & 2.36@110.2. Total equity ~$96,573.
- 2026-10-21T18:33:00.000000 - Placed limit BUY 0.75 ETH-USDT @ $2,468 (~$1,851) - preferred long buy-the-dip ladder at BOLL-mid retest; ETH best relative strength; did not chase overbought $2,516 high
- 2026-10-21T18:33:00.000000 - Placed limit BUY 0.027 BTC-USDT @ $83,350 (~$2,250) - buy-the-dip ladder above existing $81,800 rung; did not chase overbought $84.7k high (1H RSI ~91)

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
