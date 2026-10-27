# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [81625,81233,81544,81578,82016,81401,81019,81186,81130,81118,81306,82066,81909,80392,80304,80291,80258,79729,79261,69466,69579,69456,68251,68415,66832,67911,67462,67144,66432,64380,64375,64606,63740,64647,64324,64216,63842,63877,64078,64008,65156,65945,65888,65157,65625,66144,67284,66653,66639,65924,66925,66956,67263,67108,66766,66729,66886,70927,70673,70049,50652,69334,69973,68400,68061,68578,68876,68879,69055,68662,68822,69329,72687,71999,71760,71162,71911,71896,32500,29218,71927,71297,71305,71044,71337,71883,71822,71536,71536,71622,71723,71880,71860,72100,72216,71887,72077,72940,72976,72966,72638,72948,73497,73004,73041,73173,73160,73186,73258,73375,73351,73173,73098,73161,73305,73474,73536,73457,73413,73412,72100,72333,72164,72272,72204,72285,72461,72421,71652,71521,72267,72157,72774,72424,72144,72060,72091,71858,90185,91338,91466,90900,91678,91404,91268,91244,90903,90779,90787,90721,90187,92429,90518,90619,91070,90328,89376,93286,92202,92581,92485,91947,91196,91259,89619,90086,92063,91355,90950,91327,90373,91498,91800,92531,91603,90910,90031,89351,89334,92097,94406,94315,95455,98972,99763,100286,99229,99622,99701,99805,99938,99738,99082,97430,98094,97267,96741,98081,98013,98194,97447,97983,97789,97969,97729,97911,98043,98405,97912,97120,97448,97154,98095,97021,97190,97616,97402,97263,98035,97210,98424,100120,100876,97552,98049,98085,98228,98388,98342,98488,98750,99086,99181,100188,99107,99272,99553,99072,99636,99061,99186,97674,96679,96704,96743,96096,92830,95088,95560,94866,94995,95295,95497,95531,95527,95559,96236,96597,95538,94422,96363,95972,95418,93094,93128,94558,94795,94727,94611,94508,93857,93852,93954,93340,93862,94112,94249,93603,94682,93898,94267,94288,93490,95337,95601,95226,95879,97301,96573,95113,93569,93681,92773,92453,90952,91954,92130,92637,92209,91536,91462]
```

## 资产明细
- **BTC**: $56785.0
- **ETH**: $10970.2
- **SOL**: $6455.4
- **USDT**: $17251.7

## 交易记录
- 2026-10-27T12:00:00.000000 - MARKET VIEW: Risk-off broad downtrend. All majors below 25/99 EMA; daily RSI ~33-37. FOMC/rate decision this week = event risk. Relative strength BTC>SOL>ETH. Defensive posture: protect accumulated gains, no market-chasing, hold USDT dry powder.
- 2026-10-27T12:00:00.000000 - ORDER MAINTENANCE: Cancelled 5 stale/misaligned orders - BTC BUY 0.0189@76,400 & 0.01@76,800 (far below flush zone); BTC SELL 0.05@81,200 (below $82k trim ladder); SOL BUY 4@98 (at stop level); SOL SELL 2.18@104 (below $105/$108 TP ladder).
- 2026-10-27T12:00:00.000000 - NEW ORDERS (post-only maker): BUY BTC 0.025@78,300 (~$1,958, ordId 4046671084116258817); BUY SOL 23@99.2 (~$2,282, ordId 4046671089988284417); SELL BTC 0.05@84,500 (~$4,225, ordId 4046671096296517633); SELL SOL 2.18@108 (ordId 4046671102269206529). New buy deployment ~$4,239 total (<5% each).
- 2026-10-27T12:00:00.000000 - KEPT ORDERS: BTC BUY 0.005@78,200; BTC SELL 0.05@82,150 & 0.05@82,400; ETH SELL 1@2,390 & 1@2,410; SOL SELL 2.18@105. No fills this session; 10 live orders resting.
- 2026-10-27T12:00:00.000000 - RESULT: totalEq ~$91,462; free USDT ~$12,653 (frozen ~$4,630 in resting dip-bids). Core BTC/ETH/SOL held, no market sells. (Simulated account.)
- 2026-10-26T04:22:00.000000 - DEFENSIVE HOLD / maker-only maintenance - all majors in confirmed DAILY DOWNTRENDS, oversold on 1H/4H but no reversal confirmation; risk-off regime (FOMC/PCE/midterms + Mideast). Held core BTC/ETH/SOL, no market sells, no fills. Relative strength BTC>SOL>ETH. Free USDT ~$14.29k (~15.6% of book) dry powder; totalEq ~$91,536
- 2026-10-26T04:22:00.000000 - Defensive order tweaks: cancelled BTC BUY 0.005 @ 79,000 (4042137507697537025, too close to $79.9k spot in downtrend) and re-placed post-only BTC BUY 0.005 @ 78,200 (4042849628374708225); added small SOL BUY 4 @ 98.0 (4042849632938110977) at support; kept all trim ladders (BTC 81,200/82,150/82,400, ETH 2,390/2,410, SOL 104/105), BTC flush bids 76,400/76,800, SOL BUY 8 @ 99.5; no ETH adds (weakest)
- 2026-10-25T22:35:00.000000 - HOLD / selective-accumulate - daily downtrend with early 4H/1H oversold stabilization in a macro-event week; relative strength SOL>BTC>ETH; kept core BTC/ETH/SOL, no chasing; USDT reserve ~21% (~$19.65k); totalEq ~$92,209
- 2026-10-25T22:35:00.000000 - Cancelled 3 stale orders: ETH add-bid 0.45 @ 2,300 (strategy = do not add ETH), SOL SELL 2.36 @ 106.6 & 2.0 @ 105.8 (trims too far above 104-105 zone)
- 2026-10-25T22:35:00.000000 - Placed post-only (maker) scale-in bids: BTC 0.005 @ 79,800 / 79,400 / 79,000 and SOL 8 @ 100.5 / 8 @ 99.5 (~$2.8k new bid liquidity); no fills
- 2026-10-25T22:35:00.000000 - Rebuilt SOL trim ladder - post-only SELL 2.18 @ 104 and 2.18 @ 105 (ordId 4042137521488408577 / 4042137526286692353)
- 2026-10-25T22:35:00.000000 - Kept: deep BTC flush bids 0.0189 @ 76,400 & 0.01 @ 76,800; BTC trim SELL 0.05 @ 81,200 / 82,150 / 82,400; ETH trim SELL 1.0 @ 2,390 & 1.0 @ 2,410
- 2026-10-25T04:20:00.000000 - Cancelled 2 stale bottom bids: SOL BUY 23 @ 101 (4039231248518361089) and BTC BUY 0.0189 @ 79,500 (4039231255195693057) - both too close to spot after the oversold bounce; no fills
- 2026-10-25T04:20:00.000000 - Re-placed maker-only (post_only) bids deeper at support: SOL BUY 23 @ 100.0 (4039941115981869057) and BTC BUY 0.0189 @ 79,300 (4039941120612380673); kept ETH BUY 0.45 @ 2,300 (4039231262175014913) - only accumulate deeper, no chasing
- 2026-10-25T04:20:00.000000 - HOLD / de-risk - relief bounce within a daily downtrend; relative strength ETH>BTC>SOL, 1H overbought into supply; kept all 6 trim sells (BTC 0.05@81,200 & 0.05@82,150; ETH 1.0@2,390 & 1.0@2,410; SOL 2.0@105.8 & 2.36@106.6), no market orders, no fills; BTC still ~61pct of book, USDT dry powder ~$9.65k (~10.4pct); totalEq ~$92,637
- 2026-10-24T22:28:00.000000 - Placed post-only BUYs at deep support: SOL 23 @ 101.0 (~$2,323, ordId 4039231248518361089), BTC 0.0189 @ 79,500 (~$1,503, ordId 4039231255195693057), ETH 0.45 @ 2,300 (~$1,035, ordId 4039231262175014913) - accumulation only at support, no chasing spot; all live, no fills
- 2026-10-24T22:28:00.000000 - Re-priced trim ladder: cancelled stale BTC SELL 0.05 @ 82,800 (4033317888488648705) + ETH SELL 1.0 @ 2,430 (4036406007320555521) & 1.0 @ 2,470 (4036406014098550785), replaced with BTC SELL 0.05 @ 81,200 (4039231269020119041), ETH SELL 1.0 @ 2,390 (4039231276368539649) & 1.0 @ 2,410 (4039231282609664001); kept BTC 0.05 @ 82,150 (4037825836267089921) + SOL TP 2.0 @ 105.8 (4033317895568633857) & 2.36 @ 106.6 (4033317902648619009)

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
