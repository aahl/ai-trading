#!/usr/bin/env python3
"""
加密货币交易AI代理
- 交易对: BTC-USDT, ETH-USDT, SOL-USDT, ETH-BTC, SOL-BTC, SOL-ETH
- 市场分析与交易执行
- 结果保存与Telegram推送
"""

import asyncio
import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CryptoTradingAgent:
    """加密货币交易AI代理"""

    # 支持的交易对
    SUPPORTED_PAIRS = [
        "BTC-USDT", "ETH-USDT", "SOL-USDT",
        "ETH-BTC", "SOL-BTC", "SOL-ETH"
    ]

    def __init__(self):
        self.trades = []
        self.positions = {}

    def analyze_market(self) -> Dict[str, Any]:
        """
        分析市场行情
        使用 crypto-market-analyzer 代理进行市场分析
        """
        logger.info("开始市场分析...")

        # 分析主要交易对的市场情况
        market_analysis = {
            "timestamp": datetime.now().isoformat(),
            "pairs_analysis": {},
            "recommendations": []
        }

        for pair in self.SUPPORTED_PAIRS:
            try:
                # 使用Task工具进行市场分析
                result = Task(
                    description=f"市场分析 {pair}",
                    prompt=f"分析交易对 {pair} 的市场行情，包括价格趋势、技术指标、交易量分析等。提供买入、卖出或持有的建议。",
                    subagent_type="crypto-market-analyzer"
                )

                market_analysis["pairs_analysis"][pair] = result

            except Exception as e:
                logger.error(f"分析 {pair} 时出错: {e}")
                market_analysis["pairs_analysis"][pair] = {
                    "error": str(e),
                    "pair": pair
                }

        return market_analysis

    def execute_trades(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        根据市场分析执行交易
        使用 okx-trading-executor 代理进行交易执行
        """
        logger.info("开始执行交易...")

        executed_trades = []

        for pair, pair_analysis in analysis["pairs_analysis"].items():
            if "error" in pair_analysis:
                continue

            try:
                # 提取交易建议
                recommendation = pair_analysis.get("recommendation", {})
                action = recommendation.get("action", "hold")

                if action != "hold":
                    # 使用Task工具执行交易
                    result = Task(
                        description=f"执行交易 {pair}",
                        prompt=f"""
                        基于以下市场分析，执行交易操作：

                        交易对: {pair}
                        建议: {action}
                        分析详情: {json.dumps(pair_analysis, ensure_ascii=False)}

                        请执行相应的买入或卖出操作。如果是模拟环境，请确保只进行小额测试交易。
                        """,
                        subagent_type="okx-trading-executor"
                    )

                    executed_trades.append({
                        "pair": pair,
                        "action": action,
                        "result": result,
                        "timestamp": datetime.now().isoformat()
                    })

                    logger.info(f"执行交易 {pair}: {action}")

            except Exception as e:
                logger.error(f"执行 {pair} 交易时出错: {e}")
                executed_trades.append({
                    "pair": pair,
                    "action": action,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })

        return executed_trades

    def save_trading_result(self, balance: float, assets: Dict[str, float] = None) -> str:
        """
        保存交易结果
        使用 mcp__hooks__save_trading_result 工具
        """
        logger.info(f"保存交易结果，总余额: ${balance:.2f}")

        if assets is None:
            assets = {}

        try:
            result = mcp__hooks__save_trading_result(
                balance=balance,
                assets=assets,
                trades=self.trades
            )

            if result and "mermaid_image" in result:
                return result["mermaid_image"]

            return None

        except Exception as e:
            logger.error(f"保存交易结果时出错: {e}")
            return None

    def send_telegram_report(self, analysis: Dict[str, Any], image_url: str = None):
        """
        发送Telegram报告
        使用 mcp__notify__tg_send_message 或 mcp__notify__tg_send_photo
        """
        logger.info("发送Telegram交易报告...")

        try:
            # 生成报告内容
            report_content = self.generate_report_content(analysis)

            if image_url:
                # 发送图片消息
                mcp__notify__tg_send_photo(
                    photo=image_url,
                    caption=report_content,
                    parse_mode="MarkdownV2"
                )
                logger.info("已发送Telegram图片报告")
            else:
                # 发送文本消息
                mcp__notify__tg_send_message(
                    text=report_content,
                    parse_mode="MarkdownV2"
                )
                logger.info("已发送Telegram文本报告")

        except Exception as e:
            logger.error(f"发送Telegram报告时出错: {e}")

    def generate_report_content(self, analysis: Dict[str, Any]) -> str:
        """
        生成报告内容
        """
        report_lines = [
            "📈 #AI模拟盘 自动交易报告",
            "",
            f"📅 **分析时间**: {analysis.get('timestamp', datetime.now().isoformat())}",
            "",
            "📊 **交易对分析**:",
        ]

        for pair, pair_analysis in analysis["pairs_analysis"].items():
            if "error" not in pair_analysis:
                recommendation = pair_analysis.get("recommendation", {})
                action = recommendation.get("action", "hold")

                # 根据建议添加emoji
                action_emoji = {
                    "buy": "🟢",
                    "sell": "🔴",
                    "hold": "⚪"
                }.get(action, "❓")

                report_lines.append(f"- {pair}: {action_emoji} {action.upper()}")

        report_lines.extend([
            "",
            "💡 **说明**: 这是模拟交易环境，所有交易均为测试性质。",
            "⚠️ **风险提示**: 加密货币交易存在高风险，请谨慎投资。"
        ])

        return "\n".join(report_lines)

    def run_trading_cycle(self):
        """
        执行一个完整的交易周期
        """
        logger.info("开始交易周期...")

        try:
            # 1. 市场分析
            market_analysis = self.analyze_market()

            # 2. 执行交易
            executed_trades = self.execute_trades(market_analysis)

            # 3. 保存交易结果
            # 获取账户余额
            try:
                account_balance = mcp__okx__account_balance(ccy="")
                total_balance = float(account_balance.get("totalEq", 0))
                image_url = self.save_trading_result(total_balance)
            except:
                total_balance = 0
                image_url = None

            # 4. 发送Telegram报告
            self.send_telegram_report(market_analysis, image_url)

            logger.info("交易周期完成")

            return {
                "success": True,
                "market_analysis": market_analysis,
                "executed_trades": executed_trades,
                "balance": total_balance,
                "image_url": image_url
            }

        except Exception as e:
            logger.error(f"交易周期执行失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }


def main():
    """
    主函数
    """
    agent = CryptoTradingAgent()

    logger.info("启动加密货币交易AI代理...")

    # 执行交易周期
    result = agent.run_trading_cycle()

    if result["success"]:
        logger.info("交易成功完成")
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        logger.error(f"交易失败: {result['error']}")
        print(f"错误: {result['error']}")


if __name__ == "__main__":
    main()