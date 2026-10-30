# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [81186,81130,81118,81306,82066,81909,80392,80304,80291,80258,79729,79261,69466,69579,69456,68251,68415,66832,67911,67462,67144,66432,64380,64375,64606,63741,64647,64324,64216,63842,63877,64079,64008,65156,65945,65888,65157,65625,66144,67284,66653,66639,65924,66925,66956,67263,67108,66766,66729,66886,70927,70673,70049,50652,69334,69973,68400,68061,68578,68877,68879,69055,68662,68822,69329,72687,71999,71760,71163,71911,71896,32500,29218,71927,71297,71305,71044,71337,71883,71822,71536,71536,71622,71723,71880,71860,72100,72216,71887,72077,72940,72976,72966,72638,72948,73497,73004,73041,73173,73160,73187,73258,73375,73351,73173,73098,73161,73305,73474,73536,73457,73413,73412,72100,72333,72164,72272,72204,72285,72461,72421,71652,71521,72267,72157,72774,72425,72144,72060,72091,71858,90185,91338,91466,90900,91678,91404,91268,91244,90903,90779,90787,90721,90187,92429,90518,90619,91070,90328,89376,93286,92202,92581,92485,91947,91196,91259,89619,90086,92063,91355,90950,91327,90373,91498,91800,92531,91603,90910,90031,89351,89334,92097,94406,94315,95455,98972,99763,100286,99229,99622,99701,99805,99938,99738,99082,97430,98094,97267,96741,98081,98013,98194,97447,97983,97789,97969,97729,97911,98043,98405,97912,97120,97448,97154,98095,97021,97191,97616,97402,97263,98035,97210,98424,100121,100876,97552,98049,98085,98228,98388,98342,98488,98750,99086,99181,100188,99107,99272,99553,99072,99636,99061,99186,97674,96679,96704,96743,96096,92830,95088,95560,94866,94995,95295,95497,95531,95527,95559,96236,96597,95538,94422,96363,95972,95418,93095,93128,94558,94795,94727,94611,94508,93857,93852,93955,93340,93862,94112,94249,93603,94682,93898,94267,94288,93490,95337,95601,95226,95879,97301,96573,95113,93569,93681,92773,92453,90953,91954,92130,92637,92209,91536,91462,92532,92562,92875,92086,92488,88547]
```

## 资产明细
- **BTC**: $56364.8
- **USDT**: $12593.5
- **ETH**: $11821.3
- **SOL**: $7767.0

## 交易记录
- 2026-10-30T19:15:00.000000 - ACTION: Defensive maker-only session amid risk-off selloff. Cancelled 11 stale far-above-market orders (BTC sells 82,150/82,400/83,500/84,500; ETH sell 2,410; SOL sells 100.5/105/108; plus off-market bids BTC 74,000, ETH 2,150, SOL 91). Kept 3 sensible orders. Placed 2 new post-only accumulate bids: BTC buy 0.02 @ 76,300 (ordId 4056231667559837697) and ETH buy 0.3 @ 2,220 (ordId 4056231672358121473). No fills.
- 2026-10-30T19:15:00.000000 - MARKET VIEW: RISK-OFF, trending down, high volatility (exchange security breach ~970k SOL outflow, >100k liquidations, ETH ETF outflows). BTC ~$76,620 (RSI 22.7 deeply oversold, below all EMAs, MACD hist still neg); ETH ~$2,234 (RSI 48, MACD turned positive, on BOLL mid - relative-strength leader); SOL ~$94.41 (RSI 24.8, weakest, breach epicenter, below all EMAs). Relative strength ETH>BTC>SOL. HOLD core, accumulate BTC 76.0-76.4k / ETH 2,207-2,233, avoid new SOL buys.
- 2026-10-30T19:15:00.000000 - RESULT: totalEq ~$88,547; USDT avail ~$8,901 (~$3,712 frozen in maker bids); core BTC/ETH/SOL fully held, no market sells into the dump. Live book: BTC buys 76,000/76,300, ETH buy 2,220, BTC sell 80,000, ETH sell 2,334. (Simulated account.)
- 2026-10-29T19:20:00.000000 - ACTION: Placed 1 post-only BTC order - BUY 0.02 @ 80,300 (ordId 4053378261677780993, dip-accumulation inside analyzer buy zone 79,800-80,300, BTC strongest with fresh MACD bullish cross). No cancels, no fills. Existing grid (BTC buys 79,000/79,500, sells 82,150/82,400/83,500/84,500; ETH buy 2,290/sell 2,410; SOL buy 99.2/sells 105/108) kept.
- 2026-10-29T19:20:00.000000 - MARKET VIEW: Choppy, risk-off tilt (Fed on hold but some hawkish votes). BTC ~$80,900 sideways mild-bullish (RSI 59, fresh MACD bull cross, above BOLL mid); ETH ~$2,335 neutral-soft (ETF outflows); SOL ~$100.3 weakest downtrend (ETF redemptions, whale dump). Relative strength BTC>ETH>SOL. HOLD all three; BTC best R/R, avoid new SOL longs. TotalEq ~$92.5k.
- 2026-10-29T05:39:23.747708 - ACTION: Placed 2 post-only BTC orders - BUY 0.02 @ 79,500 (ordId 4051692318537297921, dip-accumulation in 79,400-79,600 zone, BTC strongest + MACD bottoming) and SELL 0.03 @ 81,300 (ordId 4051692324677758977, trim into resistance below 20MA ~80,820). No cancels; all 8 prior resting orders kept. No fills.
- 2026-10-29T05:39:23.747708 - MARKET VIEW: Neutral-to-risk-off. BTC ~$80,300 (RSI ~47, MACD histogram bottoming, relatively strongest); ETH ~$2,328 (range-bound, below EMA-99 2,346); SOL ~$100.6 (weakest, persistent ETF outflows, rejected 103.9). Relative strength BTC>ETH>SOL. Maker-only, keep USDT dry powder.
- 2026-10-29T05:39:23.747708 - ORDER MAINTENANCE: No cancels - verified all 8 resting orders aligned with spot (BTC sells 82,150/82,400/83,500/84,500; SOL sells 105/108; SOL buy 99.2; ETH sell 2,410). Added 2 post-only BTC orders (see ACTION). 10 live orders, no fills.
- 2026-10-29T05:39:23.747708 - RESULT: totalEq ~$92,086; USDT avail ~$16,829 (~$3,872 frozen in resting orders); core BTC/ETH/SOL held, no market sells. (Simulated account.)
- 2026-10-28T19:34:52.000000 - RESULT: totalEq ~$92,875; free USDT ~$16,208 (~$5,667 frozen in 12 resting maker orders); core BTC/ETH/SOL held, no market sells. (Simulated account.)
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
