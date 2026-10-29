# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [82016,81401,81019,81186,81130,81118,81306,82066,81909,80392,80304,80291,80258,79729,79261,69466,69579,69456,68251,68415,66832,67911,67462,67144,66432,64380,64375,64606,63741,64647,64324,64216,63842,63877,64079,64008,65156,65945,65888,65157,65625,66144,67284,66653,66639,65924,66925,66956,67263,67108,66766,66729,66886,70927,70673,70049,50652,69334,69973,68400,68061,68578,68877,68879,69055,68662,68822,69329,72687,71999,71760,71163,71911,71896,32500,29218,71927,71297,71305,71044,71337,71883,71822,71536,71536,71622,71723,71880,71860,72100,72216,71887,72077,72940,72976,72966,72638,72948,73497,73004,73041,73173,73160,73187,73258,73375,73351,73173,73098,73161,73305,73474,73536,73457,73413,73412,72100,72333,72164,72272,72204,72285,72461,72421,71652,71521,72267,72157,72774,72425,72144,72060,72091,71858,90185,91338,91466,90900,91678,91404,91268,91244,90903,90779,90787,90721,90187,92429,90518,90619,91070,90328,89376,93286,92202,92581,92485,91947,91196,91259,89619,90086,92063,91355,90950,91327,90373,91498,91800,92531,91603,90910,90031,89351,89334,92097,94406,94315,95455,98972,99763,100286,99229,99622,99701,99805,99938,99738,99082,97430,98094,97267,96741,98081,98013,98194,97447,97983,97789,97969,97729,97911,98043,98405,97912,97120,97448,97154,98095,97021,97191,97616,97402,97263,98035,97210,98424,100121,100876,97552,98049,98085,98228,98388,98342,98488,98750,99086,99181,100188,99107,99272,99553,99072,99636,99061,99186,97674,96679,96704,96743,96096,92830,95088,95560,94866,94995,95295,95497,95531,95527,95559,96236,96597,95538,94422,96363,95972,95418,93095,93128,94558,94795,94727,94611,94508,93857,93852,93955,93340,93862,94112,94249,93603,94682,93898,94267,94288,93490,95337,95601,95226,95879,97301,96573,95113,93569,93681,92773,92453,90953,91954,92130,92637,92209,91536,91462,92532,92562,92875,92086]
```

## 资产明细
- **BTC**: $54741.6
- **USDT**: $20673.0
- **ETH**: $10692.5
- **SOL**: $5978.8

## 交易记录
- 2026-10-29T05:39:23.747708 - ACTION: Placed 2 post-only BTC orders - BUY 0.02 @ 79,500 (ordId 4051692318537297921, dip-accumulation in 79,400-79,600 zone, BTC strongest + MACD bottoming) and SELL 0.03 @ 81,300 (ordId 4051692324677758977, trim into resistance below 20MA ~80,820). No cancels; all 8 prior resting orders kept. No fills.
- 2026-10-29T05:39:23.747708 - MARKET VIEW: Neutral-to-risk-off. BTC ~$80,300 (RSI ~47, MACD histogram bottoming, relatively strongest); ETH ~$2,328 (range-bound, below EMA-99 2,346); SOL ~$100.6 (weakest, persistent ETF outflows, rejected 103.9). Relative strength BTC>ETH>SOL. Maker-only, keep USDT dry powder.
- 2026-10-29T05:39:23.747708 - ORDER MAINTENANCE: No cancels - verified all 8 resting orders aligned with spot (BTC sells 82,150/82,400/83,500/84,500; SOL sells 105/108; SOL buy 99.2; ETH sell 2,410). Added 2 post-only BTC orders (see ACTION). 10 live orders, no fills.
- 2026-10-29T05:39:23.747708 - RESULT: totalEq ~$92,086; USDT avail ~$16,829 (~$3,872 frozen in resting orders); core BTC/ETH/SOL held, no market sells. (Simulated account.)
- 2026-10-28T19:34:52.000000 - RESULT: totalEq ~$92,875; free USDT ~$16,208 (~$5,667 frozen in 12 resting maker orders); core BTC/ETH/SOL held, no market sells. (Simulated account.)
- 2026-10-28T19:34:52.000000 - ORDER MAINTENANCE: Cancelled 2 stale deep BTC bids (0.025@78,300 ordId 4046671084116258817; 0.005@78,200 ordId 4042849628374708225). Placed 3 post-only makers: BUY BTC 0.02@80,300 (ordId 4050473638411382785); BUY ETH 0.4@2,300 (ordId 4050473644283408385); SELL BTC 0.05@83,500 (ordId 4050473650725859329). No fills; 12 live orders.
- 2026-10-28T19:34:52.000000 - MARKET VIEW: Post-FOMC (Oct 28) relief bounce; BTC ~$81.1k (daily RSI 44.5, reclaiming 20-SMA; best structure), ETH ~$2,359 (oversold recovery, capped $2,400), SOL ~$102.2 (momentum lagging). Relative strength BTC~ETH > SOL. Maker-only, trim into resistance, keep USDT dry powder.
- 2026-10-28T05:16:02.000000 - ACTION: Placed post-only SELL 3 SOL @ 102.35 (ordId 4048749422246899713) as a small trim into resistance; resting/unfilled. No BTC/ETH/SOL market buys. Full existing grid of resting orders kept intact. USDT avail ~11,616 (dry powder), totalEq ~92,561.
- 2026-10-28T05:16:02.000000 - MARKET VIEW: All three majors (BTC/ETH/SOL) at intraday highs & short-term overbought ahead of FOMC (Oct 28). BTC ~80,970 (RSI ~65, res 81.3k), ETH ~2,356 (above 99EMA, res 2,367-2,370), SOL ~102.0 (most overbought, RSI-6 ~80, res 102.3-102.4). Stance: hold + trim rips + buy dips, no chasing.
- 2026-10-27T22:06:05.000000 - RESULT: totalEq ~$92,532; free USDT ~$11,616 (frozen ~$5,667 in resting bids); core BTC/ETH/SOL held, no market sells. (Simulated account.)
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
