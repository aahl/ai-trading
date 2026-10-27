# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [81543,81578,82016,81401,81018,81185,81130,81117,81306,82065,81908,80391,80304,80291,80257,79728,79261,69465,69578,69456,68251,68415,66832,67910,67461,67143,66432,64380,64374,64605,63740,64647,64323,64216,63841,63876,64078,64008,65156,65944,65887,65157,65625,66144,67284,66653,66639,65923,66924,66956,67263,67108,66765,66729,66886,70927,70673,70049,50652,69334,69973,68399,68061,68577,68876,68878,69055,68661,68822,69328,72687,71999,71760,71162,71911,71896,32500,29218,71927,71296,71304,71044,71337,71883,71821,71535,71535,71621,71723,71879,71860,72099,72216,71887,72076,72940,72975,72966,72638,72948,73497,73004,73041,73173,73160,73186,73257,73375,73350,73173,73098,73160,73305,73474,73535,73457,73413,73411,72099,72333,72163,72272,72203,72284,72460,72420,71652,71521,72267,72156,72774,72424,72143,72059,72090,71858,90185,91338,91465,90900,91678,91404,91268,91243,90903,90779,90787,90721,90187,92429,90517,90619,91070,90328,89376,93285,92201,92581,92485,91947,91196,91259,89619,90086,92062,91355,90950,91327,90373,91498,91800,92531,91603,90910,90030,89351,89334,92096,94406,94314,95455,98971,99762,100286,99229,99622,99701,99804,99937,99738,99081,97430,98093,97267,96741,98081,98013,98194,97446,97983,97789,97969,97728,97911,98043,98404,97911,97119,97448,97154,98095,97021,97190,97616,97401,97262,98035,97210,98423,100120,100876,97552,98049,98084,98228,98387,98342,98488,98749,99085,99180,100188,99106,99271,99553,99072,99635,99060,99185,97673,96678,96703,96742,96096,92830,95087,95560,94866,94995,95295,95497,95531,95526,95558,96236,96597,95538,94421,96362,95972,95418,93094,93127,94557,94794,94727,94611,94508,93856,93851,93954,93339,93861,94111,94248,93603,94682,93897,94267,94287,93490,95337,95601,95225,95878,97301,96573,95113,93568,93680,92772,92452,90952,91953,92130,92636,92208,91535,91462,92531]
```

## 资产明细
- **BTC**: $57576.9
- **USDT**: $17259.2
- **ETH**: $11148.8
- **SOL**: $6546.6

## 交易记录
- 2026-10-27T22:06:05.000000 - RESULT: totalEq ~$92,532; free USDT ~$11,616 (frozen ~$5,667 in resting bids); core BTC/ETH/SOL held, no market sells. (Simulated account.)
- 2026-10-27T22:06:05.000000 - ORDER MAINTENANCE: No cancels; kept all 10 resting orders (BTC buys 78,300/78,200; SOL buy 99.2; BTC sells 84,500/82,400/82,150; ETH sells 2,410/2,390; SOL sells 108/105). Added 3 post-only trims/adds into resistance: SELL BTC 0.05@81,300 (ordId 4047883653510344705); SELL SOL 2.18@102.8 (ordId 4047883853628977153); BUY ETH 0.45@2,305 (ordId 4047884064585691137). 13 live orders, no fills.
- 2026-10-27T22:06:05.000000 - MARKET VIEW: Defensive bounce into resistance ahead of FOMC (Oct 28). All majors recovering from oversold; 1H overbought; ETF flows mixed (BTC +$110M, ETH -$89M, SOL -$8M). Relative strength ETH>BTC>SOL. Maker-only, trim rips, keep dry powder.
- 2026-10-27T12:00:00.000000 - MARKET VIEW: Risk-off broad downtrend. All majors below 25/99 EMA; daily RSI ~33-37. FOMC/rate decision this week = event risk. Relative strength BTC>SOL>ETH. Defensive posture: protect accumulated gains, no market-chasing, hold USDT dry powder.
- 2026-10-27T12:00:00.000000 - ORDER MAINTENANCE: Cancelled 5 stale/misaligned orders - BTC BUY 0.0189@76,400 & 0.01@76,800 (far below flush zone); BTC SELL 0.05@81,200 (below $82k trim ladder); SOL BUY 4@98 (at stop level); SOL SELL 2.18@104 (below $105/$108 TP ladder).
- 2026-10-27T12:00:00.000000 - NEW ORDERS (post-only maker): BUY BTC 0.025@78,300 (~$1,958, ordId 4046671084116258817); BUY SOL 23@99.2 (~$2,282, ordId 4046671089988284417); SELL BTC 0.05@84,500 (~$4,225, ordId 4046671096296517633); SELL SOL 2.18@108 (ordId 4046671102269206529). New buy deployment ~$4,239 total (<5% each).
- 2026-10-27T12:00:00.000000 - KEPT ORDERS: BTC BUY 0.005@78,200; BTC SELL 0.05@82,150 & 0.05@82,400; ETH SELL 1@2,390 & 1@2,410; SOL SELL 2.18@105. No fills this session; 10 live orders resting.
- 2026-10-27T12:00:00.000000 - RESULT: totalEq ~$91,462; free USDT ~$12,653 (frozen ~$4,630 in resting dip-bids). Core BTC/ETH/SOL held, no market sells. (Simulated account.)
- 2026-10-26T04:22:00.000000 - DEFENSIVE HOLD / maker-only maintenance - all majors in confirmed DAILY DOWNTRENDS, oversold on 1H/4H but no reversal confirmation; risk-off regime (FOMC/PCE/midterms + Mideast). Held core BTC/ETH/SOL, no market sells, no fills. Relative strength BTC>SOL>ETH. Free USDT ~$14.29k (~15.6% of book) dry powder; totalEq ~$91,536
- 2026-10-26T04:22:00.000000 - Defensive order tweaks: cancelled BTC BUY 0.005 @ 79,000 (4042137507697537025, too close to $79.9k spot in downtrend) and re-placed post-only BTC BUY 0.005 @ 78,200 (4042849628374708225); added small SOL BUY 4 @ 98.0 (4042849632938110977) at support; kept all trim ladders (BTC 81,200/82,150/82,400, ETH 2,390/2,410, SOL 104/105), BTC flush bids 76,400/76,800, SOL BUY 8 @ 99.5; no ETH adds (weakest)
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
