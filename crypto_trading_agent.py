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

        # 使用Task工具进行批量市场分析，提高效率
        try:
            # 创建并发任务分析所有交易对
            analysis_tasks = []
            for pair in self.SUPPORTED_PAIRS:
                task = Task(
                    description=f"市场分析 {pair}",
                    prompt=f"""分析交易对 {pair} 的市场行情，包括：
1. 当前价格和价格趋势
2. 主要技术指标（RSI、MACD、移动平均线等）
3. 交易量和交易量变化
4. 市场情绪分析
5. 提供明确的买入、卖出或持有建议，并给出理由

请使用 crypto-market-analyzer 代理进行分析，重点关注 {pair} 的技术面和市场面分析。""",
                    subagent_type="crypto-market-analyzer",
                    model="sonnet"  # 使用更快的模型进行市场分析
                )
                analysis_tasks.append(task)

            # 批量执行分析任务
            results = analysis_tasks

            # 处理分析结果
            for i, result in enumerate(results):
                pair = self.SUPPORTED_PAIRS[i]
                try:
                    market_analysis["pairs_analysis"][pair] = result if result else {
                        "error": "No analysis result",
                        "pair": pair
                    }
                except Exception as e:
                    logger.error(f"处理 {pair} 分析结果时出错: {e}")
                    market_analysis["pairs_analysis"][pair] = {
                        "error": str(e),
                        "pair": pair
                    }

        except Exception as e:
            logger.error(f"市场分析过程中出错: {e}")
            # 回退到单对分析
            for pair in self.SUPPORTED_PAIRS:
                try:
                    result = Task(
                        description=f"市场分析 {pair}",
                        prompt=f"分析交易对 {pair} 的市场行情，包括价格趋势、技术指标、交易量分析等。提供买入、卖出或持有的建议。",
                        subagent_type="crypto-market-analyzer"
                    )
                    market_analysis["pairs_analysis"][pair] = result
                except Exception as pair_error:
                    logger.error(f"分析 {pair} 时出错: {pair_error}")
                    market_analysis["pairs_analysis"][pair] = {
                        "error": str(pair_error),
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
        trades_to_execute = []

        # 首先收集所有需要执行的交易
        for pair, pair_analysis in analysis["pairs_analysis"].items():
            if "error" in pair_analysis:
                continue

            try:
                # 提取交易建议
                recommendation = pair_analysis.get("recommendation", {})
                action = recommendation.get("action", "hold")
                confidence = recommendation.get("confidence", 0.5)  # 获取置信度

                # 只执行高置信度的交易（置信度 > 0.7）
                if action != "hold" and confidence > 0.7:
                    trades_to_execute.append({
                        "pair": pair,
                        "action": action,
                        "analysis": pair_analysis,
                        "confidence": confidence,
                        "timestamp": datetime.now().isoformat()
                    })
                    logger.info(f"计划执行交易 {pair}: {action} (置信度: {confidence:.2f})")

            except Exception as e:
                logger.error(f"处理 {pair} 交易建议时出错: {e}")

        # 批量执行交易
        for trade in trades_to_execute:
            try:
                result = Task(
                    description=f"执行交易 {trade['pair']}",
                    prompt=f"""
                    基于以下市场分析，执行交易操作：

                    交易对: {trade['pair']}
                    建议: {trade['action']}
                    置信度: {trade['confidence']:.2f}
                    分析详情: {json.dumps(trade['analysis'], ensure_ascii=False, indent=2)}

                    执行要求：
                    1. 这是模拟环境，请确保只进行小额测试交易
                    2. 根据置信度调整交易数量（高置信度可适当增加交易量）
                    3. 考虑当前账户余额和风险控制
                    4. 如果执行成功，记录交易详情到 self.trades 列表

                    请使用 okx-trading-executor 代理进行交易执行。
                    """,
                    subagent_type="okx-trading-executor",
                    model="haiku"  # 使用快速模型进行交易执行
                )

                # 记录成功的交易
                executed_trade = {
                    "pair": trade['pair'],
                    "action": trade['action'],
                    "confidence": trade['confidence'],
                    "result": result,
                    "timestamp": datetime.now().isoformat()
                }

                executed_trades.append(executed_trade)

                # 添加到交易记录
                self.trades.append(f"{trade['action'].upper()} {trade['pair']}")

                logger.info(f"执行交易 {trade['pair']}: {trade['action']} (置信度: {trade['confidence']:.2f})")

            except Exception as e:
                logger.error(f"执行 {trade['pair']} 交易时出错: {e}")
                executed_trades.append({
                    "pair": trade['pair'],
                    "action": trade['action'],
                    "confidence": trade['confidence'],
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })

        logger.info(f"交易执行完成，共执行 {len(executed_trades)} 笔交易")
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
            # 确保资产格式正确
            formatted_assets = {}
            for currency, value in assets.items():
                formatted_assets[currency] = round(float(value), 2)

            result = mcp__hooks__save_trading_result(
                balance=round(float(balance), 2),
                assets=formatted_assets,
                trades=self.trades if self.trades else []
            )

            if result and "mermaid_image" in result:
                logger.info("交易结果保存成功，生成图表")
                return result["mermaid_image"]

            logger.warning("交易结果保存成功，但未生成图表")
            return None

        except Exception as e:
            logger.error(f"保存交易结果时出错: {e}")
            return None

    def get_account_info(self) -> Dict[str, Any]:
        """
        获取账户信息
        """
        try:
            # 获取账户余额
            account_balance = mcp__okx__account_balance(ccy="")

            if account_balance:
                total_balance = float(account_balance.get("totalEq", 0))
                assets_data = account_balance.get("details", [])

                # 解析资产详情
                assets = {}
                for asset in assets_data:
                    ccy = asset.get("ccy", "")
                    avail = float(asset.get("availBal", 0))
                    if avail > 0:
                        assets[ccy] = avail

                return {
                    "total_balance": total_balance,
                    "assets": assets,
                    "success": True
                }
            else:
                return {
                    "total_balance": 0,
                    "assets": {},
                    "success": False,
                    "error": "无法获取账户信息"
                }
        except Exception as e:
            logger.error(f"获取账户信息时出错: {e}")
            return {
                "total_balance": 0,
                "assets": {},
                "success": False,
                "error": str(e)
            }

    def send_telegram_report(self, analysis: Dict[str, Any], image_url: str = None):
        """
        发送Telegram报告
        使用 mcp__notify__tg_send_message 或 mcp__notify__tg_send_photo
        """
        logger.info("发送Telegram交易报告...")

        try:
            # 生成报告内容
            report_content = self.generate_report_content(analysis)

            # 添加Telegram markdown格式支持
            mcp__notify__tg_markdown_rule()

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
            # 回退到简单文本消息
            try:
                fallback_message = "📈 #AI模拟盘 自动交易报告\n\n⚠️ 报告生成时出现错误，请稍后重试。"
                mcp__notify__tg_send_message(text=fallback_message)
                logger.info("已发送Telegram回退消息")
            except Exception as fallback_error:
                logger.error(f"发送Telegram回退消息也失败: {fallback_error}")

    def generate_report_content(self, analysis: Dict[str, Any]) -> str:
        """
        生成详细的报告内容，包含市场分析和交易建议
        """
        report_lines = [
            "📈 *#AI模拟盘 自动交易报告*",
            "",
            f"📅 ***分析时间***: {analysis.get('timestamp', datetime.now().isoformat())}",
            "",
            "📊 ***交易对分析***:",
        ]

        # 统计买入、卖出、持有数量
        buy_count = 0
        sell_count = 0
        hold_count = 0
        high_confidence_trades = []

        for pair, pair_analysis in analysis["pairs_analysis"].items():
            if "error" not in pair_analysis:
                recommendation = pair_analysis.get("recommendation", {})
                action = recommendation.get("action", "hold")
                confidence = recommendation.get("confidence", 0)

                # 统计交易建议
                if action == "buy":
                    buy_count += 1
                    if confidence > 0.8:
                        high_confidence_trades.append((pair, confidence, "买入"))
                elif action == "sell":
                    sell_count += 1
                    if confidence > 0.8:
                        high_confidence_trades.append((pair, confidence, "卖出"))
                else:
                    hold_count += 1

                # 根据建议添加emoji和详细信息
                action_emoji = {
                    "buy": "🟢",
                    "sell": "🔴",
                    "hold": "⚪"
                }.get(action, "❓")

                confidence_emoji = "🔥" if confidence > 0.8 else "⚡" if confidence > 0.6 else "📊"

                report_lines.append(f"*{pair}*: {action_emoji} {action.upper()} {confidence_emoji}")
                report_lines.append(f"   置信度: {confidence:.2f}")

                # 添加简要分析
                if "summary" in pair_analysis:
                    summary = pair_analysis["summary"][:100] + "..." if len(pair_analysis["summary"]) > 100 else pair_analysis["summary"]
                    report_lines.append(f"   分析: {summary}")
                report_lines.append("")

        # 添加统计信息
        report_lines.extend([
            "📈 ***交易统计***:",
            f"   🟢 买入建议: {buy_count}",
            f"   🔴 卖出建议: {sell_count}",
            f"   ⚪ 持有建议: {hold_count}",
        ])

        # 添加高置信度交易
        if high_confidence_trades:
            report_lines.extend([
                "",
                "🔥 ***高置信度交易建议***:",
            ])
            for pair, confidence, action in high_confidence_trades:
                report_lines.append(f"*{pair}*: {action} (置信度: {confidence:.2f})")

        # 添加交易记录
        if self.trades:
            report_lines.extend([
                "",
                "💼 ***最近交易记录***:",
            ])
            for i, trade in enumerate(self.trades[-5:]):  # 显示最近5笔交易
                report_lines.append(f"{i+1}. {trade}")

        # 添加账户信息
        try:
            account_info = self.get_account_info()
            if account_info["success"]:
                total_balance = account_info["total_balance"]
                assets = account_info["assets"]

                report_lines.extend([
                    "",
                    "💰 ***当前账户状态***:",
                    f"   总余额: ${total_balance:,.2f}",
                ])

                if assets:
                    report_lines.append("   资产分布:")
                    for currency, amount in assets.items():
                        report_lines.append(f"     {currency}: {amount}")
        except Exception as e:
            logger.warning(f"获取账户信息失败: {e}")

        report_lines.extend([
            "",
            "*💡 说明*: 这是模拟交易环境，所有交易均为测试性质。",
            "*⚠️ 风险提示*: 加密货币交易存在高风险，请谨慎投资。",
            "*🔒 安全提示*: 本系统使用模拟环境进行交易测试。"
        ])

        return "\n".join(report_lines)

    def run_trading_cycle(self):
        """
        执行一个完整的交易周期
        包含市场分析、交易执行、结果保存和报告生成
        """
        logger.info("🚀 开始交易周期...")

        try:
            # 1. 市场分析
            logger.info("📊 步骤 1/4: 开始市场分析...")
            market_analysis = self.analyze_market()

            # 2. 执行交易
            logger.info("💼 步骤 2/4: 开始执行交易...")
            executed_trades = self.execute_trades(market_analysis)

            # 3. 保存交易结果
            logger.info("💾 步骤 3/4: 保存交易结果...")
            account_info = self.get_account_info()

            if account_info["success"]:
                total_balance = account_info["total_balance"]
                assets = account_info["assets"]
                image_url = self.save_trading_result(total_balance, assets)
                logger.info(f"账户余额: ${total_balance:,.2f}")
            else:
                total_balance = 0
                assets = {}
                image_url = None
                logger.warning("无法获取账户信息，使用默认值")

            # 4. 发送Telegram报告
            logger.info("📱 步骤 4/4: 发送Telegram报告...")
            self.send_telegram_report(market_analysis, image_url)

            # 生成执行结果
            result = {
                "success": True,
                "market_analysis": market_analysis,
                "executed_trades": executed_trades,
                "balance": total_balance,
                "assets": assets,
                "image_url": image_url,
                "timestamp": datetime.now().isoformat()
            }

            logger.info("✅ 交易周期完成")

            # 记录执行摘要
            executed_count = len(executed_trades)
            if executed_count > 0:
                logger.info(f"📈 执行了 {executed_count} 笔交易")
            else:
                logger.info("📊 本次未执行任何交易，可能没有高置信度的交易建议")

            return result

        except Exception as e:
            logger.error(f"❌ 交易周期执行失败: {e}")
            # 发送错误报告
            try:
                error_message = f"🚨 *交易周期执行失败*\n\n错误信息: {str(e)}\n\n请稍后重试。"
                mcp__notify__tg_markdown_rule()
                mcp__notify__tg_send_message(text=error_message, parse_mode="MarkdownV2")
                logger.info("已发送错误报告")
            except Exception as notification_error:
                logger.error(f"发送错误报告失败: {notification_error}")

            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

    def run_multi_cycle_analysis(self, cycles: int = 3) -> Dict[str, Any]:
        """
        运行多个交易周期的综合分析
        """
        logger.info(f"🔬 开始运行 {cycles} 个交易周期的综合分析...")

        results = []
        successful_cycles = 0

        for i in range(cycles):
            logger.info(f"🔄 执行第 {i+1}/{cycles} 个交易周期...")

            try:
                result = self.run_trading_cycle()
                results.append(result)

                if result["success"]:
                    successful_cycles += 1
                else:
                    logger.warning(f"第 {i+1} 个周期执行失败: {result.get('error', '未知错误')}")

            except Exception as e:
                logger.error(f"第 {i+1} 个周期出现异常: {e}")
                results.append({
                    "success": False,
                    "error": str(e),
                    "cycle": i + 1
                })

        # 生成综合分析报告
        summary = self.generate_cycle_summary(results, successful_cycles, cycles)

        # 发送综合报告
        try:
            mcp__notify__tg_markdown_rule()
            mcp__notify__tg_send_message(text=summary, parse_mode="MarkdownV2")
            logger.info("已发送综合分析报告")
        except Exception as e:
            logger.error(f"发送综合报告失败: {e}")

        return {
            "summary": summary,
            "results": results,
            "successful_cycles": successful_cycles,
            "total_cycles": cycles,
            "success_rate": successful_cycles / cycles if cycles > 0 else 0
        }

    def generate_cycle_summary(self, results: List[Dict[str, Any]], successful_cycles: int, total_cycles: int) -> str:
        """
        生成多周期分析的摘要报告
        """
        total_balance = 0
        total_executed_trades = 0
        final_balance = 0

        for result in results:
            if result["success"]:
                total_balance += result.get("balance", 0)
                total_executed_trades += len(result.get("executed_trades", []))
                final_balance = result.get("balance", 0)  # 使用最后一次的结果

        avg_balance = total_balance / successful_cycles if successful_cycles > 0 else 0

        summary = f"""🔬 *多周期交易分析报告*

📊 *执行统计*:
   总周期数: {total_cycles}
   成功周期数: {successful_cycles}
   成功率: {(successful_cycles/total_cycles*100):.1f}%

💼 *交易执行*:
   总执行交易数: {total_executed_trades}
   平均每周期交易数: {(total_executed_trades/total_cycles):.1f}

💰 *账户表现*:
   平均账户余额: ${avg_balance:,.2f}
   最终账户余额: ${final_balance:,.2f}

⚠️ *重要提示*:
   - 本分析基于 {total_cycles} 个交易周期的综合结果
   - 模拟环境中的表现不代表实际投资回报
   - 请谨慎对待所有投资决策

🔒 *安全提醒*:
   - 加密货币投资具有高风险
   - 只投资您能承受损失的资金
   - 建议在实盘交易前充分了解风险"""

        return summary


def main():
    """
    主函数 - 启动加密货币交易AI代理
    """
    import argparse

    parser = argparse.ArgumentParser(description="加密货币交易AI代理")
    parser.add_argument("--cycles", type=int, default=1, help="执行多个交易周期")
    parser.add_argument("--multi-analysis", action="store_true", help="运行多周期综合分析")
    parser.add_argument("--test", action="store_true", help="测试模式，不执行实际交易")

    args = parser.parse_args()

    agent = CryptoTradingAgent()

    if args.multi_analysis:
        # 运行多周期综合分析
        logger.info("🔬 启动多周期综合分析模式...")
        result = agent.run_multi_cycle_analysis(cycles=args.cycles)
    elif args.test:
        # 测试模式
        logger.info("🧪 启动测试模式...")
        result = run_test_mode(agent)
    else:
        # 标准模式
        logger.info("🚀 启动标准交易模式...")
        if args.cycles > 1:
            result = agent.run_multi_cycle_analysis(cycles=args.cycles)
        else:
            result = agent.run_trading_cycle()

    if result.get("success"):
        logger.info("✅ 交易代理执行完成")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result
    else:
        logger.error(f"❌ 交易代理执行失败: {result.get('error', '未知错误')}")
        print(f"错误: {result.get('error', '未知错误')}")
        return result


def run_test_mode(agent: CryptoTradingAgent) -> Dict[str, Any]:
    """
    测试模式 - 验证系统各组件是否正常工作
    """
    logger.info("🧪 开始系统组件测试...")

    test_results = {
        "tests": {},
        "overall_success": True,
        "timestamp": datetime.now().isoformat()
    }

    # 测试1: 市场分析
    logger.info("📊 测试1: 市场分析功能...")
    try:
        analysis = agent.analyze_market()
        test_results["tests"]["market_analysis"] = {
            "success": True,
            "pairs_analyzed": len(analysis.get("pairs_analysis", {})),
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        test_results["tests"]["market_analysis"] = {
            "success": False,
            "error": str(e)
        }
        test_results["overall_success"] = False

    # 测试2: 账户信息
    logger.info("💼 测试2: 账户信息获取...")
    try:
        account_info = agent.get_account_info()
        test_results["tests"]["account_info"] = {
            "success": account_info["success"],
            "balance": account_info.get("total_balance", 0),
            "assets": len(account_info.get("assets", {})),
            "error": account_info.get("error") if not account_info["success"] else None
        }
    except Exception as e:
        test_results["tests"]["account_info"] = {
            "success": False,
            "error": str(e)
        }
        test_results["overall_success"] = False

    # 测试3: 保存功能
    logger.info("💾 测试3: 结果保存功能...")
    try:
        image_url = agent.save_trading_result(1000.0, {"BTC": 0.1, "USDT": 500})
        test_results["tests"]["save_result"] = {
            "success": True,
            "image_generated": image_url is not None,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        test_results["tests"]["save_result"] = {
            "success": False,
            "error": str(e)
        }
        test_results["overall_success"] = False

    # 测试4: Telegram通知
    logger.info("📱 测试4: Telegram通知功能...")
    try:
        test_analysis = {
            "timestamp": datetime.now().isoformat(),
            "pairs_analysis": {
                "BTC-USDT": {
                    "recommendation": {"action": "buy", "confidence": 0.8}
                }
            }
        }
        agent.send_telegram_report(test_analysis)
        test_results["tests"]["telegram_report"] = {
            "success": True,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        test_results["tests"]["telegram_report"] = {
            "success": False,
            "error": str(e)
        }
        test_results["overall_success"] = False

    # 生成测试报告
    logger.info("📋 生成测试报告...")
    try:
        test_report = generate_test_report(test_results)
        mcp__notify__tg_markdown_rule()
        mcp__notify__tg_send_message(text=test_report, parse_mode="MarkdownV2")
        logger.info("✅ 测试报告已发送")
    except Exception as e:
        logger.error(f"发送测试报告失败: {e}")

    return test_results


def generate_test_report(test_results: Dict[str, Any]) -> str:
    """
    生成测试报告
    """
    overall_success = test_results.get("overall_success", False)
    test_status = "✅ 通过" if overall_success else "❌ 失败"

    report = f"""🧪 *系统测试报告*

📊 *总体状态*: {test_status}

🔍 *测试详情*:
"""

    for test_name, test_result in test_results.get("tests", {}).items():
        status = "✅" if test_result.get("success", False) else "❌"
        report += f"   {status} {test_name.replace('_', ' ').title()}\n"

        if not test_result.get("success", False):
            error = test_result.get("error", "未知错误")
            report += f"      错误: {error}\n"
        else:
            if test_name == "market_analysis":
                pairs = test_result.get("pairs_analyzed", 0)
                report += f"      分析的交易对数量: {pairs}\n"
            elif test_name == "account_info":
                balance = test_result.get("balance", 0)
                assets = test_result.get("assets", 0)
                report += f"      账户余额: ${balance:,.2f}\n"
                report += f"      资产种类: {assets}\n"
            elif test_name == "save_result":
                generated = test_result.get("image_generated", False)
                report += f"      图表生成: {'是' if generated else '否'}\n"

    timestamp = test_results.get("timestamp", datetime.now().isoformat())
    report += f"\n📅 测试时间: {timestamp}\n"

    if overall_success:
        report += "\n🎉 所有测试通过，系统可以正常运行！"
    else:
        report += "\n⚠️ 部分测试失败，请检查相关组件配置。"

    return report


def run_single_cycle():
    """
    运行单个交易周期（用于测试和演示）
    """
    try:
        agent = CryptoTradingAgent()
        logger.info("🚀 开始AI交易周期...")

        result = agent.run_trading_cycle()

        if result["success"]:
            logger.info("✅ 交易周期执行成功")
            return result
        else:
            logger.error(f"❌ 交易周期执行失败: {result['error']}")
            return result

    except Exception as e:
        logger.error(f"💥 执行交易周期时发生异常: {e}")
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    main()