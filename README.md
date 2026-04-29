# 📈 AI模拟盘 自动交易报告

本项目利用 Github Action 定时运行 Claude Code，并结合MCP工具，实现在欧易模拟盘环境下自动交易。

```mermaid
xychart
    title "模拟盘余额"
    line [84177,83775,83762,83785,83738,84160,84639,84939,86370,85548,86046,86599,85942,86161,86622,86664,87115,87369,86666,86685,86384,86152,86243,86969,86548,87164,86885,86566,86809,86427,86348,86417,86273,84538,83299,83369,83430,83490,83404,83270,83362,83056,82605,82459,82614,81734,81788,81551,82598,82702,82320,82580,82878,82426,83139,82778,82686,82056,82166,81963,82110,82951,82983,82984,83038,82838,82915,82998,83235,82642,82682,82858,82746,81396,81512,81362,81277,80600,80461,80699,80673,80616,80288,80038,79836,79142,79722,82837,82533,83480,82366,83032,82960,82654,82330,82883,82934,82901,82188,81728,81005,81298,82110,82135,82449,83264,83203,83440,83439,83440,83440,83446,83447,83448,83447,83448,83449,83369,83369,83369,83313,83256,82872,82873,82801,82844,82785,82791,82791,82793,82794,76339,76145,75714,76110,76096,76397,76594,76585,76310,76607,77160,77170,77160,77456,76541,76774,76927,82520,82744,82337,81639,82040,81307,81314,81887,83490,83414,83984,83396,83594,83261,83287,83253,83470,83327,83465,83987,85348,84930,84786,82355,82433,82438,82167,81795,81466,81105,81315,81756,82064,81426,81398,81481,81210,82242,82099,83658,84359,86925,86892,86814,86980,86203,85802,86003,85811,86028,85657,85721,85896,85880,86300,86299,87378,86965,87214,87115,87118,86780,86238,84966,85623,86555,86562,86129,85722,85387,86569,86070,88870,89278,88477,88720,88781,88668,88467,88372,87493,87018,86917,87102,86870,86613,86644,86758,86317,85242,85334,86149,86106,84968,84671,84302,83410,84816,85001,85127,85693,85891,85384,87001,87811,87945,88007,88734,88528,88495,88705,88189,88248,86662,87234,86279,86251,86314,86177,86364,86503,86886,86114,86731,86310,86176,86240,86017,86136,85685,85938,85749,85111,85044,85164,85016,85008,84824,84354,84287,84572,84745,84500,85234,85096,85095,84970,83180,83338,83157,84070,84309]
```

## 资产明细
- **BTC**: $50394.0
- **ETH**: $26912.4
- **SOL**: $5459.4
- **USDT**: $1542.9

## 交易记录
- 2026-04-28T21:17:35.488914 - Buy 0.436488 ETH with 1000 USDT on ETH-USDT at avg price 2291.01, fee 0.000436488 ETH, order id 3520148463366447104
- 2026-04-28T17:56:51.091554 - 2026-04-28 | OKX SIM | Intended: SELL SOL-BTC market 15 SOL | Result: SOL-BTC unavailable (51021 This crypto isn't listed yet) | Executed fallback: SELL SOL-USDT market 15 SOL | Filled 15 SOL @ 83.61 USDT | Fee 1.25415 USDT | ordId 3519743567907528704 | tradeId 114122854 | clOrdId sim0428solusdt01 | Thesis: SOL weaker than BTC; modest de-risking via executable spot pair.
- 2026-04-26T13:28:33.849854 - Executed a conservative simulated OKX spot market sell order for 15 SOL on SOL-USDT at an average fill price of 86.04 USDT, order ID 3513405243680886784, client order ID sim0426solusdt01, fully filled.
- 2026-04-26T09:13:21.725080 - Buy 3.9081 SOL on SOL-ETH with 0.2 ETH at avg price 0.0511754118369545 ETH/SOL, fee 0.0039081 SOL, order id 3512892531020402688
- 2026-04-26T06:18:32.960551 - Hold positions; no new trade executed. Existing exposure already concentrated in BTC, ETH, and SOL, while USDT balance is too low for meaningful spot deployment.
- 2026-04-25T22:55:03.948131 - Bought 0.00553295 BTC on BTC-USDT at 77535.4 USDT, paying 0.00000553295 BTC fee.
- 2026-04-25T22:55:03.948130 - Sold 5 SOL on SOL-USDT at 86.08 USDT, paying 0.4304 USDT fee.
- 2026-04-25T22:55:03.948127 - Attempted to sell 10 SOL on SOL-ETH, but the order was canceled by slippage protection.
- 2026-04-25T20:53:11.085830 - Sell 1.5 ETH for BTC via ETH-BTC at avg 0.0314381108533327 BTC, received about 0.04715716628 BTC before 0.00004715716628 BTC fee; order 3511402680215408640
- 2026-04-25T19:09:45.160291 - No trade executed. Attempted buy SOL-BTC spot market using ~0.08 BTC but instrument was unavailable/not listed in this environment. Fallback attempted buy SOL-ETH spot market using 1.5 ETH, but order was canceled due to price limit/slippage exceeding 5%.

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
