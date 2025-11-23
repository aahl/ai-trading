#!/usr/bin/env python3
"""
加密货币交易AI代理
- 交易对: BTC-USDT, ETH-USDT, SOL-USDT, ETH-BTC, SOL-BTC, SOL-ETH
- 分析交易对市场行情 (Subagent: crypto-market-analyzer)
- 根据行情完成交易动作 (Subagent: okx-trading-executor)
- 保存交易结果 (Tool: save_trading_result)
- 将分析、持仓、交易结果以 markdown 格式发送到 Telegram
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
        logger.info("📊 开始市场行情分析...")

        market_analysis = {
            "timestamp": datetime.now().isoformat(),
            "pairs_analysis": {},
            "summary": {},
            "recommendations": []
        }

        try:
            # 对每个交易对进行详细的市场分析
            for pair in self.SUPPORTED_PAIRS:
                logger.info(f"🔍 分析交易对: {pair}")

                try:
                    # 使用crypto-market-analyzer进行深入分析
                    result = Task(
                        description=f"市场分析 {pair}",
                        prompt=f"""请对交易对 {pair} 进行全面的市场行情分析：

**分析要求**：
1. 当前价格和价格趋势分析（包括短期、中期、长期趋势）
2. 技术指标分析：
   - RSI（相对强弱指数）- 判断超买超卖
   - MACD（指数平滑移动平均线）- 判断趋势变化
   - 移动平均线（MA5、MA10、MA20、MA50）- 支撑阻力位
   - 布林带（Bollinger Bands）- 波动性和价格通道
   - KDJ随机指标 - 短期交易信号

3. 交易量分析：
   - 当前交易量水平
   - 交易量变化趋势
   - 量价关系分析

4. 市场情绪分析：
   - 多空情绪占比
   - 资金流向
   - 市场热度指标

5. 支撑阻力位：
   - 关键支撑位
   - 关键阻力位
   - 突破位分析

6. 交易建议：
   - 明确的交易方向：买入(BUY)、卖出(SELL)、持有(HOLD)
   - 置信度评分（0-1之间的数值）
   - 详细的分析依据和理由
   - 建议的风险控制措施

**输出格式要求**：
- 提供结构化的分析结果
- 包含具体的数值和指标
- 给出明确的交易建议和置信度

请使用 crypto-market-analyzer 代理进行专业分析。""",
                        subagent_type="crypto-market-analyzer"
                    )

                    if result:
                        market_analysis["pairs_analysis"][pair] = {
                            "analysis": result,
                            "timestamp": datetime.now().isoformat()
                        }
                        logger.info(f"✅ {pair} 分析完成")
                    else:
                        logger.warning(f"⚠️ {pair} 分析结果为空")
                        market_analysis["pairs_analysis"][pair] = {
                            "error": "No analysis result",
                            "timestamp": datetime.now().isoformat()
                        }

                except Exception as e:
                    logger.error(f"❌ 分析 {pair} 时出错: {e}")
                    market_analysis["pairs_analysis"][pair] = {
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    }

            # 生成分析摘要
            market_analysis["summary"] = self._generate_analysis_summary(market_analysis)

        except Exception as e:
            logger.error(f"❌ 市场分析过程出错: {e}")

        return market_analysis

    def _generate_analysis_summary(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """生成分析摘要"""
        try:
            summary = {
                "total_pairs": len(self.SUPPORTED_PAIRS),
                "analyzed_pairs": 0,
                "buy_signals": 0,
                "sell_signals": 0,
                "hold_signals": 0,
                "high_confidence_trades": [],
                "market_conditions": "Normal"
            }

            for pair, pair_data in analysis["pairs_analysis"].items():
                if "error" not in pair_data:
                    summary["analyzed_pairs"] += 1

                    # 解析交易建议
                    analysis_text = pair_data.get("analysis", "")
                    if isinstance(analysis_text, str):
                        text_lower = analysis_text.lower()

                        # 统计交易信号
                        if any(word in text_lower for word in ["buy", "买入", "long", "做多", "bullish"]):
                            summary["buy_signals"] += 1
                        elif any(word in text_lower for word in ["sell", "卖出", "short", "做空", "bearish"]):
                            summary["sell_signals"] += 1
                        else:
                            summary["hold_signals"] += 1

                        # 识别高置信度交易
                        confidence_keywords = ["high confidence", "high_confidence", "高置信度", "强信号", "strong signal"]
                        if any(keyword in text_lower for keyword in confidence_keywords):
                            summary["high_confidence_trades"].append(pair)

            # 判断市场状态
            total_signals = summary["buy_signals"] + summary["sell_signals"] + summary["hold_signals"]
            if total_signals > 0:
                buy_ratio = summary["buy_signals"] / total_signals
                sell_ratio = summary["sell_signals"] / total_signals

                if buy_ratio > 0.6:
                    summary["market_conditions"] = "Bullish"
                elif sell_ratio > 0.6:
                    summary["market_conditions"] = "Bearish"
                elif buy_ratio > 0.4 and sell_ratio > 0.4:
                    summary["market_conditions"] = "Volatile"
                else:
                    summary["market_conditions"] = "Consolidating"

            return summary

        except Exception as e:
            logger.error(f"❌ 生成分析摘要时出错: {e}")
            return {}

    def execute_trades(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        根据市场分析执行交易
        使用 okx-trading-executor 代理进行交易执行
        """
        logger.info("💼 开始执行交易...")

        executed_trades = []
        high_confidence_trades = []

        # 识别高置信度交易机会
        for pair, pair_data in analysis["pairs_analysis"].items():
            if "error" in pair_data:
                continue

            try:
                analysis_text = pair_data.get("analysis", "")

                # 检查是否有买入/卖出信号和高置信度
                if isinstance(analysis_text, str):
                    text_lower = analysis_text.lower()

                    # 识别交易信号
                    has_buy_signal = any(word in text_lower for word in ["buy", "买入", "long", "做多", "bullish"])
                    has_sell_signal = any(word in text_lower for word in ["sell", "卖出", "short", "做空", "bearish"])

                    # 识别置信度指标
                    confidence_keywords = [
                        "high confidence", "high_confidence", "高置信度", "强信号", "strong signal",
                        "confidence", "置信度", "confident", "确信"
                    ]
                    has_high_confidence = any(keyword in text_lower for keyword in confidence_keywords)

                    # 识别具体置信度数值
                    confidence_score = 0.5  # 默认置信度
                    import re
                    confidence_patterns = [
                        r'confidence[:\s]*([\d.]+)', r'置信度[:\s]*([\d.]+)',
                        r'confidence[:\s]*(\d+)%', r'置信度[:\s]*(\d+)%'
                    ]
                    for pattern in confidence_patterns:
                        match = re.search(pattern, text_lower)
                        if match:
                            try:
                                score = float(match.group(1))
                                if score > 1 and score <= 100:  # 百分比格式
                                    confidence_score = score / 100
                                else:
                                    confidence_score = min(score, 1.0)  # 直接使用0-1格式
                                break
                            except ValueError:
                                continue

                    # 只执行高置信度的交易
                    if ((has_buy_signal or has_sell_signal) and confidence_score > 0.7):
                        action = "buy" if has_buy_signal else "sell"
                        high_confidence_trades.append({
                            "pair": pair,
                            "action": action,
                            "confidence": confidence_score,
                            "analysis": analysis_text[:200] + "..." if len(analysis_text) > 200 else analysis_text,
                            "timestamp": datetime.now().isoformat()
                        })
                        logger.info(f"🎯 发现高置信度交易机会: {pair} {action} (置信度: {confidence_score:.2f})")

            except Exception as e:
                logger.error(f"❌ 处理 {pair} 交易建议时出错: {e}")

        # 执行高置信度交易
        for trade in high_confidence_trades:
            try:
                logger.info(f"🚀 执行交易: {trade['pair']} {trade['action']} (置信度: {trade['confidence']:.2f})")

                result = Task(
                    description=f"执行交易 {trade['pair']}",
                    prompt=f"""
基于以下市场分析，执行交易操作：

**交易详情**:
- 交易对: {trade['pair']}
- 交易方向: {trade['action']}
- 置信度: {trade['confidence']:.2f}
- 分析依据: {trade['analysis']}

**执行要求**:
1. **模拟环境**: 这是模拟交易环境，请只进行小额测试交易
2. **风险控制**: 根据置信度设置合理的交易量和止盈止损
   - 置信度 0.7-0.8: 小额测试交易（0.01-0.1个标准手）
   - 置信度 0.8-0.9: 中等交易量（0.1-0.5个标准手）
   - 置信度 0.9以上: 较大交易量（0.5-1个标准手）
3. **账户管理**: 考虑当前账户余额和风险控制
4. **止损设置**: 设置合理的止损点位（建议2-5%）
5. **止盈设置**: 设置合理的止盈点位（建议5-10%）
6. **交易记录**: 交易成功后记录交易详情到系统

**执行优先级**:
- 高置信度交易优先执行
- 流动性好的交易对优先
- 避免过度交易，单次交易风险控制在总资金的1-2%

请使用 okx-trading-executor 代理进行交易执行，确保执行模拟交易而非实盘交易。
""",
                    subagent_type="okx-trading-executor"
                )

                executed_trade = {
                    "pair": trade['pair'],
                    "action": trade['action'],
                    "confidence": trade['confidence'],
                    "analysis": trade['analysis'],
                    "result": result,
                    "timestamp": datetime.now().isoformat()
                }

                executed_trades.append(executed_trade)
                self.trades.append(f"{trade['action'].upper()} {trade['pair']} (置信度: {trade['confidence']:.2f})")

                logger.info(f"✅ 交易执行完成: {trade['pair']} {trade['action']} (置信度: {trade['confidence']:.2f})")

            except Exception as e:
                logger.error(f"❌ 执行 {trade['pair']} 交易时出错: {e}")
                executed_trades.append({
                    "pair": trade['pair'],
                    "action": trade['action'],
                    "confidence": trade['confidence'],
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })

        logger.info(f"📊 交易执行完成，共执行 {len(executed_trades)} 笔交易")
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

    def send_telegram_report(self, analysis: Dict[str, Any], image_url: str = None) -> bool:
        """
        发送Telegram报告
        以"📈 #AI模拟盘 自动交易报告"为标题
        """
        logger.info("📱 发送Telegram交易报告...")

        try:
            # 检查Telegram工具是否可用
            self.telegram_tools_available = self._check_telegram_tools()

            if not self.telegram_tools_available:
                logger.warning("⚠️ Telegram工具不可用，跳过报告发送")
                return False

            # 生成报告内容
            report_content = self.generate_telegram_report(analysis)

            # 设置Telegram markdown格式
            mcp__notify__tg_markdown_rule()

            if image_url:
                # 发送图片消息，使用mermaid图表
                mcp__notify__tg_send_photo(
                    photo=image_url,
                    caption=report_content,
                    parse_mode="MarkdownV2"
                )
                logger.info("✅ 已发送Telegram图片报告")
                return True
            else:
                # 发送文本消息
                mcp__notify__tg_send_message(
                    text=report_content,
                    parse_mode="MarkdownV2"
                )
                logger.info("✅ 已发送Telegram文本报告")
                return True

        except Exception as e:
            logger.error(f"❌ 发送Telegram报告时出错: {e}")
            # 回退到简单文本消息
            try:
                fallback_message = "📈 #AI模拟盘 自动交易报告\n\n⚠️ 报告生成时出现错误，请稍后重试。"
                mcp__notify__tg_send_message(text=fallback_message)
                logger.info("✅ 已发送Telegram回退消息")
                return True
            except Exception as fallback_error:
                logger.error(f"❌ 发送Telegram回退消息也失败: {fallback_error}")
                return False

    def generate_telegram_report(self, analysis: Dict[str, Any]) -> str:
        """
        生成Telegram格式的报告内容，以"📈 #AI模拟盘 自动交易报告"为标题
        """
        try:
            report_lines = [
                "📈 *#AI模拟盘 自动交易报告*",
                "",
                f"📅 ***分析时间***: {analysis.get('timestamp', datetime.now().isoformat())}",
                ""
            ]

            # 添加分析摘要
            summary = analysis.get("summary", {})
            if summary:
                report_lines.extend([
                    "📊 ***分析摘要***:",
                    f"   🎯 分析交易对: {summary.get('analyzed_pairs', 0)}/{summary.get('total_pairs', 0)}",
                    f"   🟢 买入信号: {summary.get('buy_signals', 0)}",
                    f"   🔴 卖出信号: {summary.get('sell_signals', 0)}",
                    f"   ⚪ 持有信号: {summary.get('hold_signals', 0)}",
                    f"   🌍 市场状态: {summary.get('market_conditions', 'Normal')}",
                    ""
                ])

            # 添加各交易对详细分析
            report_lines.extend(["🔍 ***交易对分析***:", ""])

            for pair, pair_data in analysis["pairs_analysis"].items():
                if "error" in pair_data:
                    report_lines.append(f"*{pair}*: ❌ 分析失败")
                    report_lines.append(f"   错误: {pair_data['error']}")
                else:
                    analysis_text = pair_data.get("analysis", "")
                    if isinstance(analysis_text, str):
                        # 提取关键信息
                        text_lower = analysis_text.lower()

                        # 判断交易建议
                        if any(word in text_lower for word in ["buy", "买入", "long", "做多", "bullish"]):
                            action_emoji = "🟢"
                            action_text = "买入"
                        elif any(word in text_lower for word in ["sell", "卖出", "short", "做空", "bearish"]):
                            action_emoji = "🔴"
                            action_text = "卖出"
                        else:
                            action_emoji = "⚪"
                            action_text = "持有"

                        # 判断置信度
                        confidence_text = ""
                        if any(word in text_lower for word in ["high confidence", "high_confidence", "高置信度", "强信号", "strong signal"]):
                            confidence_text = "🔥 高置信度"
                        elif any(word in text_lower for word in ["medium confidence", "中等置信度"]):
                            confidence_text = "⚡ 中等置信度"
                        else:
                            confidence_text = "📊 一般置信度"

                        report_lines.append(f"*{pair}*: {action_emoji} {action_text}")
                        report_lines.append(f"   {confidence_text}")

                        # 添加简要分析
                        if len(analysis_text) > 50:
                            brief_analysis = analysis_text[:100] + "..." if len(analysis_text) > 100 else analysis_text
                            report_lines.append(f"   分析: {brief_analysis}")

                report_lines.append("")

            # 添加账户信息
            try:
                account_info = self.get_account_info()
                if account_info["success"]:
                    total_balance = account_info["total_balance"]
                    assets = account_info["assets"]

                    report_lines.extend([
                        "💰 ***当前账户状态***:",
                        f"   总余额: ${total_balance:,.2f}",
                    ])

                    if assets:
                        report_lines.append("   资产分布:")
                        for currency, amount in assets.items():
                            report_lines.append(f"     {currency}: {amount}")
                    report_lines.append("")
            except Exception as e:
                logger.warning(f"获取账户信息失败: {e}")

            # 添加交易记录
            if self.trades:
                report_lines.extend([
                    "💼 ***最近交易记录***:",
                ])
                for i, trade in enumerate(self.trades[-5:]):
                    report_lines.append(f"{i+1}. {trade}")
                report_lines.append("")

            # 添加风险提示和说明
            report_lines.extend([
                "*💡 说明*: 这是模拟交易环境，所有交易均为测试性质。",
                "*⚠️ 风险提示*: 加密货币交易存在高风险，请谨慎投资。",
                "*🔒 安全提示*: 本系统使用模拟环境进行交易测试。",
                "",
                "*🤖 AI交易代理* - 自动化加密货币交易系统"
            ])

            return "\n".join(report_lines)

        except Exception as e:
            logger.error(f"❌ 生成Telegram报告时出错: {e}")
            return "📈 #AI模拟盘 自动交易报告\n\n⚠️ 报告生成时出现错误，请稍后重试。"

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

    parser = argparse.ArgumentParser(description="AI加密货币交易代理")
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
        logger.info("🚀 启动AI交易模式...")
        if args.cycles > 1:
            result = agent.run_multi_cycle_analysis(cycles=args.cycles)
        else:
            result = agent.run_trading_cycle()

    if result.get("success"):
        logger.info("✅ AI交易代理执行完成")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result
    else:
        logger.error(f"❌ AI交易代理执行失败: {result.get('error', '未知错误')}")
        print(f"错误: {result.get('error', '未知错误')}")
        return result

def run_single_cycle():
    """
    运行单个交易周期（用于快速测试和演示）
    """
    try:
        agent = CryptoTradingAgent()
        logger.info("🚀 开始AI交易周期...")

        result = agent.run_trading_cycle()

        if result["success"]:
            logger.info("✅ AI交易周期执行成功")
            return result
        else:
            logger.error(f"❌ AI交易周期执行失败: {result['error']}")
            return result

    except Exception as e:
        logger.error(f"💥 执行AI交易周期时发生异常: {e}")
        return {"success": False, "error": str(e)}


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