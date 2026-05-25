#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                               ║
║     ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗  ██╗ █████╗     ██╗   ██╗██╗████████╗██████╗  ║
║     ████╗ ████║██╔══██╗██╔══██╗██║  ██║██╔══██╗██║  ██║██╔══██╗    ██║   ██║██║╚══██╔══╝██╔══██╗ ║
║     ██╔████╔██║███████║██████╔╝███████║███████║███████║███████║    ██║   ██║██║   ██║   ██████╔╝ ║
║     ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔══██║██╔══██║██╔══██║██╔══██║    ██║   ██║██║   ██║   ██╔══██╗ ║
║     ██║ ╚═╝ ██║██║  ██║██║     ██║  ██║██║  ██║██║  ██║██║  ██║    ╚██████╔╝██║   ██║   ██║  ██║ ║
║     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ║
║                                                                                               ║
║                         U L T R A   B O T   v 6 . 0                                            ║
║                      Premium Trading Intelligence System                                       ║
║                         Light Green & Silver Edition                                           ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import signal
import sqlite3
import random
import math
import threading
from datetime import datetime, timedelta
from collections import deque, defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum
import argparse

# ============================================
# ULTRA PREMIUM COLOR SCHEME - LIGHT GREEN & SILVER
# ============================================

class UltraTheme:
    """Maphaha Ultra Bot Premium Color Scheme"""
    
    # Primary Colors - Light Green & Silver
    LIGHT_GREEN = '\033[38;2;144;238;144m'
    GREEN_LIME = '\033[38;2;50;205;50m'
    GREEN_MINT = '\033[38;2;152;251;152m'
    GREEN_PALE = '\033[38;2;175;238;175m'
    GREEN_SPRING = '\033[38;2;0;255;127m'
    
    # Silver & Metallic
    SILVER = '\033[38;2;192;192;192m'
    SILVER_LIGHT = '\033[38;2;211;211;211m'
    SILVER_METALLIC = '\033[38;2;165;165;165m'
    PLATINUM = '\033[38;2;229;228;226m'
    CHROME = '\033[38;2;220;220;245m'
    
    # Background Colors - Light Theme
    BG_MAIN = '\033[48;2;248;255;248m'
    BG_PANEL = '\033[48;2;255;255;255m'
    BG_HEADER = '\033[48;2;240;255;240m'
    BG_GREEN_SOFT = '\033[48;2;235;255;235m'
    
    # Accent Colors
    ACCENT_GREEN = '\033[38;2;0;200;100m'
    ACCENT_GREEN_DARK = '\033[38;2;0;150;75m'
    ACCENT_RED = '\033[38;2;220;80;80m'
    ACCENT_GOLD = '\033[38;2;218;165;32m'
    ACCENT_BLUE = '\033[38;2;70;130;200m'
    
    # Text Colors
    TEXT_PRIMARY = '\033[38;2;30;40;30m'
    TEXT_SECONDARY = '\033[38;2;80;90;80m'
    TEXT_MUTED = '\033[38;2;140;145;140m'
    TEXT_BRIGHT = '\033[38;2;255;255;255m'
    
    # Effects
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    
    # Box Drawing - Premium
    BOX_TL = "╔"
    BOX_TR = "╗"
    BOX_BL = "╚"
    BOX_BR = "╝"
    BOX_H = "═"
    BOX_V = "║"
    BOX_T = "╠"
    BOX_BT = "╣"
    BOX_CROSS = "╬"
    
    # Icons
    ICON_BULL = "🐂"
    ICON_BEAR = "🐻"
    ICON_LIGHTNING = "⚡"
    ICON_STAR = "⭐"
    ICON_CHART = "📊"
    ICON_CROWN = "👑"
    ICON_ROCKET = "🚀"
    ICON_DIAMOND = "💎"

# ============================================
# ULTRA CONFIGURATION
# ============================================

VERSION = "6.0.0"
BUILD = "Ultra Platinum Edition"
COMPANY = "Maphaha Ultra Systems"

class UltraConfig:
    """Ultra Bot Configuration"""
    # Trading Settings
    INITIAL_CAPITAL = 50000.0
    BASE_LOT_SIZE = 1.0
    MAX_POSITIONS = 15
    RISK_PER_TRADE = 0.025
    MAX_DAILY_TRADES = 50
    MAX_DAILY_LOSS = 2000.0
    
    # Strategy Parameters
    SIGNAL_THRESHOLD_ULTRA = 85
    SIGNAL_THRESHOLD_STRONG = 70
    SIGNAL_THRESHOLD_MODERATE = 50
    
    STOP_LOSS_PTS = 500
    TAKE_PROFIT_PTS = 1500
    
    # AI Parameters
    AI_LEARNING_RATE = 0.01
    AI_HISTORY_BARS = 2000
    NEURAL_NODES = 128
    
    # System Settings
    UPDATE_INTERVAL = 1
    HISTORY_BARS = 2000
    ENABLE_AI_PREDICTIONS = True
    ENABLE_SOUND = False
    ENABLE_ANIMATIONS = True
    ENABLE_ULTRA_MODE = True
    
    # File Paths
    DB_PATH = os.path.expanduser("~/maphaha_ultra.db")
    LOG_PATH = os.path.expanduser("~/maphaha_ultra_logs")
    MODEL_PATH = os.path.expanduser("~/maphaha_ai_model.json")

# ============================================
# ENUMS & DATA CLASSES
# ============================================

class UltraSignal(Enum):
    ULTRA_BUY = "ULTRA BUY 💎"
    STRONG_BUY = "STRONG BUY ⭐"
    BUY = "BUY 🐂"
    NEUTRAL = "NEUTRAL ⚪"
    SELL = "SELL 🐻"
    STRONG_SELL = "STRONG SELL 🔴"
    ULTRA_SELL = "ULTRA SELL 💀"

class TradeMomentum(Enum):
    EXPLOSIVE = "EXPLOSIVE 🚀"
    STRONG = "STRONG 💪"
    MODERATE = "MODERATE 📈"
    WEAK = "WEAK 📉"
    SIDEWAYS = "SIDEWAYS ↔️"

@dataclass
class UltraPosition:
    """Enhanced trading position"""
    id: int
    symbol: str
    signal: UltraSignal
    entry_price: float
    volume: float
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    take_profit_3: float
    open_time: datetime
    close_price: Optional[float] = None
    close_time: Optional[datetime] = None
    profit: float = 0.0
    profit_pips: float = 0.0
    status: str = "OPEN"
    notes: str = ""

@dataclass
class UltraSignalData:
    """Ultra trading signal"""
    symbol: str
    signal: UltraSignal
    momentum: TradeMomentum
    confidence: float
    entry_price: float
    target_price: float
    stop_price: float
    timestamp: datetime
    indicators: Dict[str, Any]
    ai_prediction: float
    reasoning: List[str]

# ============================================
# ULTRA AI ENGINE
# ============================================

class UltraAIEngine:
    """Advanced AI prediction engine"""
    
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.prices = deque(maxlen=UltraConfig.AI_HISTORY_BARS)
        self.patterns = []
        self.accuracy = 0.85
        self.predictions = []
        
    def learn_pattern(self, pattern: List[float], outcome: float):
        """Learn from market patterns"""
        self.patterns.append({
            'pattern': pattern,
            'outcome': outcome,
            'timestamp': datetime.now()
        })
        
        # Keep only recent patterns
        if len(self.patterns) > 10000:
            self.patterns = self.patterns[-10000:]
    
    def predict_next(self, recent_prices: List[float]) -> Dict:
        """Predict next price movement"""
        if len(recent_prices) < 50:
            return {'direction': 0, 'confidence': 0, 'target': recent_prices[-1] if recent_prices else 0}
        
        # Calculate multiple technical factors
        current = recent_prices[-1]
        sma20 = sum(recent_prices[-20:]) / 20
        sma50 = sum(recent_prices[-50:]) / 50
        
        # Trend strength
        trend = (sma20 - sma50) / sma50 * 100
        
        # Momentum
        momentum = (recent_prices[-1] - recent_prices[-10]) / recent_prices[-10] * 100
        
        # Volatility
        volatility = sum(abs(recent_prices[i] - recent_prices[i-1]) 
                       for i in range(-20, 0)) / 20
        
        # AI Prediction
        ai_score = 0
        if trend > 0.5 and momentum > 0:
            ai_score += 40
        elif trend < -0.5 and momentum < 0:
            ai_score -= 40
        
        # Pattern matching
        for pattern in self.patterns[-100:]:  # Check recent patterns
            if len(pattern['pattern']) <= len(recent_prices):
                similarity = self._calculate_similarity(recent_prices[-len(pattern['pattern']):], 
                                                       pattern['pattern'])
                if similarity > 0.9:
                    ai_score += pattern['outcome'] * 20
        
        # Normalize
        confidence = min(95, abs(ai_score) + 20)
        
        direction = 1 if ai_score > 0 else -1 if ai_score < 0 else 0
        
        predicted_change = (ai_score / 100) * volatility * current
        target = current + predicted_change
        
        return {
            'direction': direction,
            'confidence': confidence,
            'target': target,
            'ai_score': ai_score,
            'trend': trend,
            'momentum': momentum,
            'volatility': volatility
        }
    
    def _calculate_similarity(self, seq1: List[float], seq2: List[float]) -> float:
        """Calculate pattern similarity"""
        if len(seq1) != len(seq2):
            return 0
        
        # Normalize sequences
        norm1 = [(x - min(seq1)) / (max(seq1) - min(seq1) + 0.0001) for x in seq1]
        norm2 = [(x - min(seq2)) / (max(seq2) - min(seq2) + 0.0001) for x in seq2]
        
        # Calculate correlation
        similarity = sum(1 - abs(a - b) for a, b in zip(norm1, norm2)) / len(seq1)
        return similarity

# ============================================
# ULTRA INDICATORS SUITE
# ============================================

class UltraIndicators:
    """Advanced technical indicators"""
    
    @staticmethod
    def ema(prices: List[float], period: int) -> float:
        if len(prices) < period:
            return prices[-1] if prices else 0
        multiplier = 2 / (period + 1)
        ema = sum(prices[:period]) / period
        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema
        return ema
    
    @staticmethod
    def rsi(prices: List[float], period: int = 14) -> float:
        if len(prices) < period + 1:
            return 50
        
        gains = losses = 0
        for i in range(-period, 0):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                gains += diff
            else:
                losses += abs(diff)
        
        if losses == 0:
            return 100
        if gains == 0:
            return 0
        
        rs = gains / losses
        return 100 - (100 / (1 + rs))
    
    @staticmethod
    def macd(prices: List[float]) -> Tuple[float, float, float]:
        if len(prices) < 26:
            return 0, 0, 0
        
        ema12 = UltraIndicators.ema(prices, 12)
        ema26 = UltraIndicators.ema(prices, 26)
        macd = ema12 - ema26
        signal = UltraIndicators.ema([macd], 9) if len(prices) > 9 else macd
        histogram = macd - signal
        return macd, signal, histogram
    
    @staticmethod
    def bollinger(prices: List[float], period: int = 20) -> Tuple[float, float, float, float]:
        if len(prices) < period:
            return 0, 0, 0, 0
        
        recent = prices[-period:]
        sma = sum(recent) / period
        variance = sum((p - sma) ** 2 for p in recent) / period
        std = math.sqrt(variance)
        
        return sma + (2 * std), sma + std, sma, sma - (2 * std)
    
    @staticmethod
    def ichimoku(prices: List[float], highs: List[float], lows: List[float]) -> Dict:
        """Ichimoku Cloud indicator"""
        if len(prices) < 52:
            return {}
        
        # Tenkan-sen (Conversion Line)
        period9_high = max(highs[-9:])
        period9_low = min(lows[-9:])
        tenkan = (period9_high + period9_low) / 2
        
        # Kijun-sen (Base Line)
        period26_high = max(highs[-26:])
        period26_low = min(lows[-26:])
        kijun = (period26_high + period26_low) / 2
        
        # Senkou Span A
        senkou_a = (tenkan + kijun) / 2
        
        # Senkou Span B
        period52_high = max(highs[-52:])
        period52_low = min(lows[-52:])
        senkou_b = (period52_high + period52_low) / 2
        
        return {
            'tenkan': tenkan,
            'kijun': kijun,
            'senkou_a': senkou_a,
            'senkou_b': senkou_b,
            'cloud_top': max(senkou_a, senkou_b),
            'cloud_bottom': min(senkou_a, senkou_b)
        }
    
    @staticmethod
    def fibonacci(prices: List[float]) -> Dict:
        """Fibonacci retracement levels"""
        if len(prices) < 50:
            return {}
        
        high = max(prices[-50:])
        low = min(prices[-50:])
        diff = high - low
        
        return {
            'level_0': low,
            'level_236': low + diff * 0.236,
            'level_382': low + diff * 0.382,
            'level_500': low + diff * 0.500,
            'level_618': low + diff * 0.618,
            'level_786': low + diff * 0.786,
            'level_100': high
        }
    
    @staticmethod
    def vwap(prices: List[float], volumes: List[int]) -> float:
        """Volume Weighted Average Price"""
        if not volumes or sum(volumes) == 0:
            return prices[-1] if prices else 0
        
        total_value = sum(p * v for p, v in zip(prices, volumes))
        total_volume = sum(volumes)
        return total_value / total_volume if total_volume > 0 else prices[-1]

# ============================================
# ULTRA SIGNAL GENERATOR
# ============================================

class UltraSignalGenerator:
    """Ultra-advanced signal generation engine"""
    
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.prices = deque(maxlen=UltraConfig.HISTORY_BARS)
        self.highs = deque(maxlen=UltraConfig.HISTORY_BARS)
        self.lows = deque(maxlen=UltraConfig.HISTORY_BARS)
        self.volumes = deque(maxlen=UltraConfig.HISTORY_BARS)
        
        # AI Engine
        self.ai = UltraAIEngine(symbol)
        
        # History trackers
        self.signal_history = []
        self.performance = []
        
    def add_data(self, price: float, high: float = None, low: float = None, volume: int = 0):
        self.prices.append(price)
        self.highs.append(high or price)
        self.lows.append(low or price)
        self.volumes.append(volume)
        
        # Train AI
        if len(self.prices) > 100:
            self.ai.learn_pattern(list(self.prices)[-50:], 1 if price > self.prices[-2] else -1)
    
    def generate_ultra_signal(self) -> UltraSignalData:
        """Generate ultra-precise trading signal"""
        if len(self.prices) < 100:
            return UltraSignalData(
                symbol=self.symbol,
                signal=UltraSignal.NEUTRAL,
                momentum=TradeMomentum.SIDEWAYS,
                confidence=0,
                entry_price=self.prices[-1] if self.prices else 0,
                target_price=0,
                stop_price=0,
                timestamp=datetime.now(),
                indicators={},
                ai_prediction=0,
                reasoning=["Analyzing market data..."]
            )
        
        # Calculate all indicators
        prices_list = list(self.prices)
        highs_list = list(self.highs)
        lows_list = list(self.lows)
        volumes_list = list(self.volumes)
        
        rsi = UltraIndicators.rsi(prices_list)
        macd, macd_signal, macd_hist = UltraIndicators.macd(prices_list)
        upper, middle_upper, middle, lower = UltraIndicators.bollinger(prices_list)
        ichimoku = UltraIndicators.ichimoku(prices_list, highs_list, lows_list)
        fibonacci = UltraIndicators.fibonacci(prices_list)
        vwap = UltraIndicators.vwap(prices_list, volumes_list) if volumes_list else prices_list[-1]
        
        # AI Prediction
        ai_pred = self.ai.predict_next(prices_list)
        
        # Technical scoring (0-200 scale)
        buy_score = 0
        sell_score = 0
        reasons = []
        
        # RSI (30 points)
        if rsi < 25:
            buy_score += 30
            reasons.append(f"RSI Extreme Oversold ({rsi:.1f})")
        elif rsi < 35:
            buy_score += 20
            reasons.append(f"RSI Oversold ({rsi:.1f})")
        elif rsi > 75:
            sell_score += 30
            reasons.append(f"RSI Extreme Overbought ({rsi:.1f})")
        elif rsi > 65:
            sell_score += 20
            reasons.append(f"RSI Overbought ({rsi:.1f})")
        
        # MACD (25 points)
        if macd > macd_signal and macd_hist > 0:
            buy_score += 25
            reasons.append("MACD Bullish Momentum")
        elif macd < macd_signal and macd_hist < 0:
            sell_score += 25
            reasons.append("MACD Bearish Momentum")
        
        # Bollinger Bands (20 points)
        current = prices_list[-1]
        if current <= lower:
            buy_score += 20
            reasons.append("Price at Lower BB")
        elif current >= upper:
            sell_score += 20
            reasons.append("Price at Upper BB")
        
        # Ichimoku Cloud (25 points)
        if ichimoku:
            if current > ichimoku.get('cloud_top', 0):
                buy_score += 15
                reasons.append("Above Ichimoku Cloud")
            elif current < ichimoku.get('cloud_bottom', 0):
                sell_score += 15
                reasons.append("Below Ichimoku Cloud")
            
            if ichimoku.get('tenkan', 0) > ichimoku.get('kijun', 0):
                buy_score += 10
                reasons.append("Tenkan above Kijun")
            else:
                sell_score += 10
                reasons.append("Tenkan below Kijun")
        
        # Fibonacci (15 points)
        if fibonacci:
            if current <= fibonacci.get('level_382', 0):
                buy_score += 15
                reasons.append("Fibonacci Support Level")
            elif current >= fibonacci.get('level_618', 0):
                sell_score += 15
                reasons.append("Fibonacci Resistance Level")
        
        # VWAP (10 points)
        if current > vwap:
            buy_score += 10
            reasons.append("Price above VWAP")
        else:
            sell_score += 10
            reasons.append("Price below VWAP")
        
        # AI Prediction (25 points)
        if ai_pred['direction'] > 0:
            buy_score += ai_pred['confidence'] * 0.25
            reasons.append(f"AI predicts bullish ({ai_pred['confidence']:.0f}% confidence)")
        elif ai_pred['direction'] < 0:
            sell_score += ai_pred['confidence'] * 0.25
            reasons.append(f"AI predicts bearish ({ai_pred['confidence']:.0f}% confidence)")
        
        # Momentum calculation
        net_score = buy_score - sell_score
        total_score = buy_score + sell_score
        
        # Determine signal type
        if net_score > 70:
            signal = UltraSignal.ULTRA_BUY
            momentum = TradeMomentum.EXPLOSIVE
            confidence = min(99, net_score)
        elif net_score > 50:
            signal = UltraSignal.STRONG_BUY
            momentum = TradeMomentum.STRONG
            confidence = min(95, net_score)
        elif net_score > 30:
            signal = UltraSignal.BUY
            momentum = TradeMomentum.MODERATE
            confidence = min(85, net_score)
        elif net_score < -70:
            signal = UltraSignal.ULTRA_SELL
            momentum = TradeMomentum.EXPLOSIVE
            confidence = min(99, abs(net_score))
        elif net_score < -50:
            signal = UltraSignal.STRONG_SELL
            momentum = TradeMomentum.STRONG
            confidence = min(95, abs(net_score))
        elif net_score < -30:
            signal = UltraSignal.SELL
            momentum = TradeMomentum.MODERATE
            confidence = min(85, abs(net_score))
        else:
            signal = UltraSignal.NEUTRAL
            momentum = TradeMomentum.SIDEWAYS
            confidence = 50
        
        # Apply thresholds
        if confidence < UltraConfig.SIGNAL_THRESHOLD_MODERATE:
            signal = UltraSignal.NEUTRAL
        
        # Calculate targets
        atr = UltraIndicators.ema([abs(prices_list[i] - prices_list[i-1]) 
                                  for i in range(-14, 0)], 14)
        
        if signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY]:
            target = current + (atr * 3)
            stop = current - (atr * 1.5)
        elif signal in [UltraSignal.ULTRA_SELL, UltraSignal.STRONG_SELL, UltraSignal.SELL]:
            target = current - (atr * 3)
            stop = current + (atr * 1.5)
        else:
            target = current
            stop = current
        
        return UltraSignalData(
            symbol=self.symbol,
            signal=signal,
            momentum=momentum,
            confidence=confidence,
            entry_price=current,
            target_price=target,
            stop_price=stop,
            timestamp=datetime.now(),
            indicators={
                'RSI': round(rsi, 2),
                'MACD': round(macd, 5),
                'MACD_Signal': round(macd_signal, 5),
                'BB_Upper': round(upper, 5),
                'BB_Middle': round(middle, 5),
                'BB_Lower': round(lower, 5),
                'Ichimoku': ichimoku,
                'Fibonacci': fibonacci,
                'VWAP': round(vwap, 5),
                'ATR': round(atr, 5),
                'AI_Prediction': ai_pred,
                'Buy_Score': round(buy_score, 1),
                'Sell_Score': round(sell_score, 1),
                'Net_Score': round(net_score, 1)
            },
            ai_prediction=ai_pred['confidence'],
            reasoning=reasons[:5]
        )

# ============================================
# ULTRA TRADING ENGINE
# ============================================

class UltraTradingEngine:
    """Ultra-advanced trading execution engine"""
    
    def __init__(self):
        self.positions: List[UltraPosition] = []
        self.closed_positions: List[UltraPosition] = []
        self.position_counter = 0
        self.capital = UltraConfig.INITIAL_CAPITAL
        self.initial_capital = UltraConfig.INITIAL_CAPITAL
        self.daily_trades = 0
        self.daily_loss = 0
        self.last_reset = datetime.now().date()
        
    def reset_daily(self):
        today = datetime.now().date()
        if today != self.last_reset:
            self.daily_trades = 0
            self.daily_loss = 0
            self.last_reset = today
    
    def execute_signal(self, signal: UltraSignalData) -> Optional[UltraPosition]:
        """Execute ultra signal"""
        self.reset_daily()
        
        if signal.signal == UltraSignal.NEUTRAL:
            return None
        
        # Check daily limits
        if self.daily_trades >= UltraConfig.MAX_DAILY_TRADES:
            return None
        
        if self.daily_loss >= UltraConfig.MAX_DAILY_LOSS:
            return None
        
        # Check existing positions
        same_direction = any(p.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY] and
                           signal.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY]
                           for p in self.positions if p.status == "OPEN")
        
        if same_direction:
            return None
        
        # Calculate position size based on confidence
        volume_multiplier = 1.0
        if signal.signal == UltraSignal.ULTRA_BUY or signal.signal == UltraSignal.ULTRA_SELL:
            volume_multiplier = 2.0
        elif signal.signal == UltraSignal.STRONG_BUY or signal.signal == UltraSignal.STRONG_SELL:
            volume_multiplier = 1.5
        
        volume = UltraConfig.BASE_LOT_SIZE * volume_multiplier * (signal.confidence / 100)
        volume = max(min(volume, UltraConfig.BASE_LOT_SIZE * 3), UltraConfig.BASE_LOT_SIZE * 0.3)
        
        # Calculate multiple TP levels
        atr = signal.indicators.get('ATR', 0.001)
        tp_distance = UltraConfig.TAKE_PROFIT_PTS * 0.0001
        
        if signal.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY]:
            stop_loss = signal.entry_price - (tp_distance * 0.5 + atr)
            tp1 = signal.entry_price + (tp_distance * 1.0)
            tp2 = signal.entry_price + (tp_distance * 1.5)
            tp3 = signal.entry_price + (tp_distance * 2.5)
        else:
            stop_loss = signal.entry_price + (tp_distance * 0.5 + atr)
            tp1 = signal.entry_price - (tp_distance * 1.0)
            tp2 = signal.entry_price - (tp_distance * 1.5)
            tp3 = signal.entry_price - (tp_distance * 2.5)
        
        self.position_counter += 1
        position = UltraPosition(
            id=self.position_counter,
            symbol=signal.symbol,
            signal=signal.signal,
            entry_price=signal.entry_price,
            volume=volume,
            stop_loss=stop_loss,
            take_profit_1=tp1,
            take_profit_2=tp2,
            take_profit_3=tp3,
            open_time=datetime.now(),
            notes=" | ".join(signal.reasoning[:3])
        )
        
        self.positions.append(position)
        self.daily_trades += 1
        
        return position
    
    def update_positions(self, current_price: float) -> List[UltraPosition]:
        """Update and check positions"""
        closed = []
        
        for pos in self.positions[:]:
            if pos.status != "OPEN":
                continue
            
            if pos.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY]:
                # Long position
                if current_price <= pos.stop_loss:
                    self.close_position(pos, current_price, "Stop Loss")
                    closed.append(pos)
                elif current_price >= pos.take_profit_3:
                    self.close_position(pos, current_price, "Take Profit (TP3)")
                    closed.append(pos)
                elif current_price >= pos.take_profit_2:
                    # Partial profit - but simplified for demo
                    pass
            else:
                # Short position
                if current_price >= pos.stop_loss:
                    self.close_position(pos, current_price, "Stop Loss")
                    closed.append(pos)
                elif current_price <= pos.take_profit_3:
                    self.close_position(pos, current_price, "Take Profit (TP3)")
                    closed.append(pos)
        
        return closed
    
    def close_position(self, position: UltraPosition, price: float, reason: str):
        """Close a position"""
        if position.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY]:
            profit = (price - position.entry_price) * position.volume
            pips = (price - position.entry_price) * 10000
        else:
            profit = (position.entry_price - price) * position.volume
            pips = (position.entry_price - price) * 10000
        
        position.close_price = price
        position.close_time = datetime.now()
        position.profit = profit
        position.profit_pips = pips
        position.status = "CLOSED"
        
        if profit < 0:
            self.daily_loss += abs(profit)
        
        self.capital += profit
        self.closed_positions.append(position)
        self.positions.remove(position)
    
    def get_stats(self) -> Dict:
        """Get comprehensive statistics"""
        total_trades = len(self.closed_positions)
        winning = sum(1 for p in self.closed_positions if p.profit > 0)
        total_profit = sum(p.profit for p in self.closed_positions)
        
        return {
            'total_trades': total_trades,
            'winning_trades': winning,
            'losing_trades': total_trades - winning,
            'win_rate': (winning / total_trades * 100) if total_trades > 0 else 0,
            'total_profit': total_profit,
            'current_capital': self.capital,
            'return_pct': ((self.capital - self.initial_capital) / self.initial_capital) * 100,
            'open_positions': len([p for p in self.positions if p.status == "OPEN"]),
            'avg_profit': total_profit / total_trades if total_trades > 0 else 0,
            'best_trade': max([p.profit for p in self.closed_positions]) if self.closed_positions else 0,
            'worst_trade': min([p.profit for p in self.closed_positions]) if self.closed_positions else 0,
            'daily_trades': self.daily_trades
        }

# ============================================
# ULTRA MARKET SIMULATOR
# ============================================

class UltraMarketSimulator:
    """Ultra-realistic market simulation"""
    
    def __init__(self):
        self.symbols = {}
        self._init_ultra_symbols()
    
    def _init_ultra_symbols(self):
        """Initialize ultra symbol data"""
        symbols_config = {
            "EURUSD": {"price": 1.09250, "volatility": 0.008, "trend": 0.0001, "spread": 0.0001},
            "GBPUSD": {"price": 1.27850, "volatility": 0.010, "trend": 0.00015, "spread": 0.00012},
            "USDJPY": {"price": 149.850, "volatility": 0.007, "trend": -0.0002, "spread": 0.015},
            "XAUUSD": {"price": 2380.50, "volatility": 0.015, "trend": 0.002, "spread": 0.30},
            "BTCUSD": {"price": 68500, "volatility": 0.040, "trend": 0.003, "spread": 50},
            "ETHUSD": {"price": 3650, "volatility": 0.045, "trend": 0.002, "spread": 5},
            "US30": {"price": 39200, "volatility": 0.012, "trend": 0.001, "spread": 5},
            "US500": {"price": 5250, "volatility": 0.013, "trend": 0.0015, "spread": 0.5},
            "GER30": {"price": 18500, "volatility": 0.011, "trend": 0.001, "spread": 4},
            "UK100": {"price": 8200, "volatility": 0.009, "trend": 0.0008, "spread": 3},
            "AUDUSD": {"price": 0.6650, "volatility": 0.009, "trend": 0.0001, "spread": 0.0001},
            "NZDUSD": {"price": 0.6150, "volatility": 0.009, "trend": 0.00005, "spread": 0.00012},
            "USDCAD": {"price": 1.3650, "volatility": 0.008, "trend": 0.0002, "spread": 0.0001},
            "USDCHF": {"price": 0.8950, "volatility": 0.007, "trend": -0.0001, "spread": 0.0001},
            "XAGUSD": {"price": 28.50, "volatility": 0.018, "trend": 0.001, "spread": 0.05}
        }
        
        for symbol, config in symbols_config.items():
            self.symbols[symbol] = {
                'price': config['price'],
                'volatility': config['volatility'],
                'trend': config['trend'],
                'spread': config['spread'],
                'history': deque(maxlen=UltraConfig.HISTORY_BARS),
                'highs': deque(maxlen=UltraConfig.HISTORY_BARS),
                'lows': deque(maxlen=UltraConfig.HISTORY_BARS),
                'volumes': deque(maxlen=UltraConfig.HISTORY_BARS)
            }
            
            # Initialize history
            for _ in range(UltraConfig.HISTORY_BARS):
                self.symbols[symbol]['history'].append(config['price'])
                self.symbols[symbol]['highs'].append(config['price'] * 1.001)
                self.symbols[symbol]['lows'].append(config['price'] * 0.999)
                self.symbols[symbol]['volumes'].append(random.randint(1000, 100000))
    
    def get_price(self, symbol: str) -> float:
        return self.symbols[symbol]['price']
    
    def get_high_low(self, symbol: str) -> Tuple[float, float]:
        data = self.symbols[symbol]
        return data['highs'][-1], data['lows'][-1]
    
    def get_volume(self, symbol: str) -> int:
        return self.symbols[symbol]['volumes'][-1]
    
    def update_price(self, symbol: str) -> float:
        data = self.symbols[symbol]
        old = data['price']
        
        # Advanced price movement simulation
        trend = data['trend'] * old * 0.15
        volatility = data['volatility'] * old * random.gauss(0, 0.4)
        
        # Momentum component
        momentum = 0
        if len(data['history']) > 20:
            recent_momentum = (data['history'][-1] - data['history'][-20]) / 20
            momentum = recent_momentum * 0.3
        
        # Mean reversion
        sma50 = sum(list(data['history'])[-50:]) / 50
        reversion = (sma50 - old) * 0.01
        
        change = trend + volatility + momentum + reversion
        
        # Random spikes (news events)
        if random.random() < 0.02:
            change *= random.uniform(2, 4)
            if random.random() < 0.5:
                change = abs(change)
            else:
                change = -abs(change)
        
        new_price = max(old + change, 0.0001)
        data['price'] = new_price
        data['history'].append(new_price)
        
        # Generate OHLC
        range_val = new_price * data['volatility'] * 0.6
        data['highs'].append(new_price + abs(random.gauss(0, range_val)))
        data['lows'].append(new_price - abs(random.gauss(0, range_val)))
        data['volumes'].append(random.randint(5000, 500000))
        
        return new_price

# ============================================
# ULTRA UI RENDERER - LIGHT GREEN & SILVER
# ============================================

class UltraUI:
    """Premium Ultra Bot UI Renderer"""
    
    def __init__(self):
        self.theme = UltraTheme()
        self.animation = True
        self.last_frame = 0
        
    def clear(self):
        os.system('clear')
    
    def draw_premium_box(self, title: str, width: int = 80, color: str = None):
        """Draw premium styled box"""
        if color is None:
            color = self.theme.SILVER
        
        print(f"{color}{self.theme.BOX_TL}{self.theme.BOX_H * (width-2)}{self.theme.BOX_TR}{self.theme.RESET}")
        if title:
            padding = (width - len(title) - 4) // 2
            print(f"{color}{self.theme.BOX_V}{' ' * padding}{self.theme.LIGHT_GREEN}{self.theme.BOLD}{title}{self.theme.RESET}{color}{' ' * (width - len(title) - 4 - padding)}{self.theme.BOX_V}{self.theme.RESET}")
            print(f"{color}{self.theme.BOX_T}{self.theme.BOX_H * (width-2)}{self.theme.BOX_BT}{self.theme.RESET}")
    
    def draw_gradient_bar(self, percentage: float, width: int = 40):
        """Draw premium gradient progress bar"""
        filled = int((percentage / 100) * width)
        
        # Gradient colors from light green to silver
        bar = ""
        for i in range(width):
            if i < filled:
                if i < width * 0.25:
                    bar += f"{self.theme.GREEN_PALE}█"
                elif i < width * 0.5:
                    bar += f"{self.theme.LIGHT_GREEN}█"
                elif i < width * 0.75:
                    bar += f"{self.theme.GREEN_SPRING}█"
                else:
                    bar += f"{self.theme.ACCENT_GREEN}█"
            else:
                bar += f"{self.theme.SILVER_LIGHT}░"
        
        return f"{bar}{self.theme.RESET}"
    
    def render_ultra_logo(self):
        """Render ultra premium logo"""
        self.clear()
        print(f"{self.theme.LIGHT_GREEN}{self.theme.BOLD}")
        print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                                                          ║")
        print("║     ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗  ██╗ █████╗     ██╗   ██╗██╗████████╗██████╗  █████╗ ║")
        print("║     ████╗ ████║██╔══██╗██╔══██╗██║  ██║██╔══██╗██║  ██║██╔══██╗    ██║   ██║██║╚══██╔══╝██╔══██╗██╔══██╗║")
        print("║     ██╔████╔██║███████║██████╔╝███████║███████║███████║███████║    ██║   ██║██║   ██║   ██████╔╝███████║║")
        print("║     ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔══██║██╔══██║██╔══██║██╔══██║    ██║   ██║██║   ██║   ██╔══██╗██╔══██║║")
        print("║     ██║ ╚═╝ ██║██║  ██║██║     ██║  ██║██║  ██║██║  ██║██║  ██║    ╚██████╔╝██║   ██║   ██║  ██║██║  ██║║")
        print("║     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝║")
        print("║                                                                                                          ║")
        print(f"║{self.theme.SILVER}{self.theme.ICON_CROWN}{' '*10}ULTRA BOT v{VERSION} - PREMIUM TRADING INTELLIGENCE{self.theme.ICON_DIAMOND}{' '*10}{self.theme.LIGHT_GREEN}║")
        print(f"║{self.theme.SILVER_LIGHT}{BUILD:^74}{self.theme.LIGHT_GREEN}║")
        print("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
        print(f"{self.theme.RESET}")
    
    def render_ultra_dashboard(self, symbol: str, price: float, signal: UltraSignalData,
                              engine: UltraTradingEngine, generator: UltraSignalGenerator):
        """Render ultra premium dashboard"""
        self.clear()
        
        # Header
        print(f"{self.theme.BG_HEADER}{self.theme.TEXT_PRIMARY}{self.theme.BOLD}")
        print("═" * 100)
        print(f"{self.theme.ICON_ROCKET} MAPHAHA ULTRA BOT - LIVE TRADING DASHBOARD {self.theme.ICON_ROCKET} | {symbol} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("═" * 100)
        print(f"{self.theme.RESET}")
        
        # Price Panel
        print(f"\n{self.theme.BG_PANEL}{self.theme.SILVER}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}MARKET PRICE{self.theme.RESET}{self.theme.SILVER}{' ' * 83}{self.theme.BOX_V}")
        
        # Determine price color
        price_color = self.theme.ACCENT_GREEN if signal.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY] else \
                     self.theme.ACCENT_RED if signal.signal in [UltraSignal.ULTRA_SELL, UltraSignal.STRONG_SELL, UltraSignal.SELL] else \
                     self.theme.TEXT_PRIMARY
        
        print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}Symbol:{self.theme.RESET} {self.theme.BOLD}{symbol}{self.theme.RESET}  "
              f"{self.theme.TEXT_SECONDARY}Bid:{self.theme.RESET} {price_color}{self.theme.BOLD}${price:.5f}{self.theme.RESET}  "
              f"{self.theme.TEXT_SECONDARY}Ask:{self.theme.RESET} ${price + 0.0001:.5f}  "
              f"{self.theme.TEXT_SECONDARY}Spread:{self.theme.RESET} 0.0001  "
              f"{self.theme.TEXT_SECONDARY}Volume:{self.theme.RESET} {generator.volumes[-1] if generator.volumes else 0:,}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Signal Panel
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}SIGNAL ANALYSIS{self.theme.RESET}{self.theme.SILVER}{' ' * 81}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}{self.theme.RESET}")
        
        # Signal display with premium styling
        if signal.signal == UltraSignal.ULTRA_BUY:
            signal_icon = "💎🚀"
            signal_color = self.theme.ACCENT_GREEN
            bg_color = self.theme.BG_GREEN_SOFT
        elif signal.signal == UltraSignal.STRONG_BUY:
            signal_icon = "⭐🐂"
            signal_color = self.theme.LIGHT_GREEN
            bg_color = self.theme.BG_GREEN_SOFT
        elif signal.signal == UltraSignal.BUY:
            signal_icon = "🐂"
            signal_color = self.theme.GREEN_MINT
            bg_color = self.theme.BG_GREEN_SOFT
        elif signal.signal == UltraSignal.ULTRA_SELL:
            signal_icon = "💀⚠️"
            signal_color = self.theme.ACCENT_RED
            bg_color = self.theme.BG_PANEL
        elif signal.signal == UltraSignal.STRONG_SELL:
            signal_icon = "🔴🐻"
            signal_color = self.theme.ACCENT_RED
            bg_color = self.theme.BG_PANEL
        elif signal.signal == UltraSignal.SELL:
            signal_icon = "🐻"
            signal_color = self.theme.ACCENT_RED
            bg_color = self.theme.BG_PANEL
        else:
            signal_icon = "⚪"
            signal_color = self.theme.TEXT_MUTED
            bg_color = self.theme.BG_PANEL
        
        print(f"{bg_color}{self.theme.BOX_V}  {signal_icon} {signal_color}{self.theme.BOLD}{signal.signal.value:^20}{self.theme.RESET}{bg_color}  "
              f"{self.theme.TEXT_SECONDARY}Momentum:{self.theme.RESET} {signal.momentum.value}  "
              f"{self.theme.TEXT_SECONDARY}Confidence:{self.theme.RESET} {signal_color}{signal.confidence:.0f}%{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Confidence bar
        bar = self.draw_gradient_bar(signal.confidence, 50)
        print(f"{bg_color}{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}Confidence:{self.theme.RESET} {bar} {signal.confidence:.0f}%{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Reasoning
        if signal.reasoning:
            reasons_text = " | ".join(signal.reasoning[:3])
            print(f"{bg_color}{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}Analysis:{self.theme.RESET} {reasons_text[:80]}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Technical Indicators Panel
        print(f"{self.theme.BG_PANEL}{self.theme.SILVER}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}TECHNICAL INDICATORS{self.theme.RESET}{self.theme.SILVER}{' ' * 75}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}{self.theme.RESET}")
        
        ind = signal.indicators
        print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}RSI:{self.theme.RESET} {ind.get('RSI', 50):>6.1f}  "
              f"{self.theme.TEXT_SECONDARY}MACD:{self.theme.RESET} {ind.get('MACD', 0):>8.5f}  "
              f"{self.theme.TEXT_SECONDARY}Signal:{self.theme.RESET} {ind.get('MACD_Signal', 0):>8.5f}  "
              f"{self.theme.TEXT_SECONDARY}Hist:{self.theme.RESET} {ind.get('MACD', 0) - ind.get('MACD_Signal', 0):>8.5f}{self.theme.SILVER}{self.theme.BOX_V}")
        
        print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}BB Upper:{self.theme.RESET} {ind.get('BB_Upper', 0):>8.5f}  "
              f"{self.theme.TEXT_SECONDARY}Middle:{self.theme.RESET} {ind.get('BB_Middle', 0):>8.5f}  "
              f"{self.theme.TEXT_SECONDARY}Lower:{self.theme.RESET} {ind.get('BB_Lower', 0):>8.5f}{self.theme.SILVER}{self.theme.BOX_V}")
        
        print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}VWAP:{self.theme.RESET} {ind.get('VWAP', 0):>8.5f}  "
              f"{self.theme.TEXT_SECONDARY}ATR:{self.theme.RESET} {ind.get('ATR', 0):>8.5f}  "
              f"{self.theme.TEXT_SECONDARY}AI Pred:{self.theme.RESET} {ind.get('AI_Prediction', {}).get('confidence', 0):>6.1f}%{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Score bars
        buy_score = ind.get('Buy_Score', 0)
        sell_score = ind.get('Sell_Score', 0)
        
        buy_bar = self.draw_gradient_bar(buy_score, 30)
        sell_bar = self.draw_gradient_bar(sell_score, 30)
        
        print(f"{self.theme.BOX_V}  {self.theme.ACCENT_GREEN}Bullish Score:{self.theme.RESET} {buy_bar} {buy_score:.0f}{self.theme.SILVER}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.ACCENT_RED}Bearish Score:{self.theme.RESET} {sell_bar} {sell_score:.0f}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Performance Panel
        stats = engine.get_stats()
        print(f"{self.theme.BG_PANEL}{self.theme.SILVER}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}PERFORMANCE METRICS{self.theme.RESET}{self.theme.SILVER}{' ' * 76}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}{self.theme.RESET}")
        
        win_color = self.theme.ACCENT_GREEN if stats['win_rate'] >= 50 else self.theme.ACCENT_RED
        profit_color = self.theme.ACCENT_GREEN if stats['total_profit'] >= 0 else self.theme.ACCENT_RED
        return_color = self.theme.ACCENT_GREEN if stats['return_pct'] >= 0 else self.theme.ACCENT_RED
        
        print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}Trades:{self.theme.RESET} {stats['total_trades']:>4}  "
              f"{self.theme.TEXT_SECONDARY}Win Rate:{self.theme.RESET} {win_color}{stats['win_rate']:>5.1f}%{self.theme.RESET}  "
              f"{self.theme.TEXT_SECONDARY}Profit:{self.theme.RESET} {profit_color}${stats['total_profit']:>10.2f}{self.theme.RESET}  "
              f"{self.theme.TEXT_SECONDARY}Return:{self.theme.RESET} {return_color}{stats['return_pct']:>+6.1f}%{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
        
        print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}Capital:{self.theme.RESET} ${stats['current_capital']:>10.2f}  "
              f"{self.theme.TEXT_SECONDARY}Open:{self.theme.RESET} {stats['open_positions']}  "
              f"{self.theme.TEXT_SECONDARY}Daily Trades:{self.theme.RESET} {stats['daily_trades']}/{UltraConfig.MAX_DAILY_TRADES}  "
              f"{self.theme.TEXT_SECONDARY}Best/Worst:{self.theme.RESET} ${stats['best_trade']:+.0f}/${stats['worst_trade']:+.0f}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Open Positions Panel
        if engine.positions:
            print(f"{self.theme.BG_PANEL}{self.theme.SILVER}")
            print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.ACCENT_GOLD}OPEN POSITIONS{self.theme.RESET}{self.theme.SILVER}{' ' * 82}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}{self.theme.RESET}")
            
            for pos in engine.positions[:5]:  # Show max 5
                if pos.signal in [UltraSignal.ULTRA_BUY, UltraSignal.STRONG_BUY, UltraSignal.BUY]:
                    pos_color = self.theme.ACCENT_GREEN
                    unrealized = (price - pos.entry_price) * pos.volume
                else:
                    pos_color = self.theme.ACCENT_RED
                    unrealized = (pos.entry_price - price) * pos.volume
                
                unreal_color = self.theme.ACCENT_GREEN if unrealized >= 0 else self.theme.ACCENT_RED
                
                print(f"{self.theme.BOX_V}  {pos_color}{pos.signal.value[:12]}{self.theme.RESET} "
                      f"Entry: ${pos.entry_price:.5f}  "
                      f"SL: ${pos.stop_loss:.5f}  "
                      f"TP1: ${pos.take_profit_1:.5f}  "
                      f"P&L: {unreal_color}${unrealized:+.2f}{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # AI Prediction Panel
        ai_pred = ind.get('AI_Prediction', {})
        if ai_pred:
            print(f"{self.theme.BG_PANEL}{self.theme.SILVER}")
            print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}🤖 AI PREDICTION ENGINE{self.theme.RESET}{self.theme.SILVER}{' ' * 77}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}{self.theme.RESET}")
            
            direction_icon = "🟢" if ai_pred.get('direction', 0) > 0 else "🔴" if ai_pred.get('direction', 0) < 0 else "⚪"
            direction_text = "BULLISH" if ai_pred.get('direction', 0) > 0 else "BEARISH" if ai_pred.get('direction', 0) < 0 else "NEUTRAL"
            dir_color = self.theme.ACCENT_GREEN if ai_pred.get('direction', 0) > 0 else self.theme.ACCENT_RED
            
            print(f"{self.theme.BOX_V}  {direction_icon} {dir_color}{self.theme.BOLD}AI Direction:{self.theme.RESET} {dir_color}{direction_text}{self.theme.RESET}  "
                  f"{self.theme.TEXT_SECONDARY}Confidence:{self.theme.RESET} {ai_pred.get('confidence', 0):.0f}%  "
                  f"{self.theme.TEXT_SECONDARY}Target:{self.theme.RESET} ${ai_pred.get('target', 0):.5f}{self.theme.SILVER}{self.theme.BOX_V}")
            
            print(f"{self.theme.BOX_V}  {self.theme.TEXT_SECONDARY}Trend:{self.theme.RESET} {ai_pred.get('trend', 0):+.2f}%  "
                  f"{self.theme.TEXT_SECONDARY}Momentum:{self.theme.RESET} {ai_pred.get('momentum', 0):+.2f}%  "
                  f"{self.theme.TEXT_SECONDARY}Volatility:{self.theme.RESET} {ai_pred.get('volatility', 0):.4f}{self.theme.SILVER}{self.theme.BOX_V}")
        
        # Bottom status bar
        print(f"{self.theme.BG_HEADER}{self.theme.TEXT_SECONDARY}")
        print("═" * 100)
        print(f"{self.theme.ICON_LIGHTNING} [Ctrl+C] Menu  |  [Q] Quit  |  [S] Statistics  |  [R] Reset  |  [H] Help {self.theme.ICON_STAR}")
        print("═" * 100)
        print(f"{self.theme.RESET}")
    
    def render_ultra_menu(self):
        """Render ultra premium menu"""
        self.render_ultra_logo()
        
        print(f"\n{self.theme.BG_PANEL}{self.theme.SILVER}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}{self.theme.ICON_DIAMOND} ULTRA TRADING SYMBOLS {self.theme.ICON_DIAMOND}{self.theme.RESET}{self.theme.SILVER}{' ' * 70}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        
        # Symbols organized by category
        symbols = [
            ("1", "EURUSD", "Euro/USD", "FOREX", "🔵"),
            ("2", "GBPUSD", "British Pound", "FOREX", "🔵"),
            ("3", "USDJPY", "USD/JPY", "FOREX", "🔵"),
            ("4", "AUDUSD", "Aussie", "FOREX", "🔵"),
            ("5", "USDCAD", "Loonie", "FOREX", "🔵"),
            ("6", "XAUUSD", "Gold", "COMMODITY", "🟡"),
            ("7", "XAGUSD", "Silver", "COMMODITY", "⚪"),
            ("8", "BTCUSD", "Bitcoin", "CRYPTO", "🟠"),
            ("9", "ETHUSD", "Ethereum", "CRYPTO", "🔷"),
            ("10", "US30", "Dow Jones", "INDEX", "📈"),
            ("11", "US500", "S&P 500", "INDEX", "📊"),
            ("12", "GER30", "German DAX", "INDEX", "🇩🇪"),
            ("13", "UK100", "UK FTSE", "INDEX", "🇬🇧"),
            ("14", "NZDUSD", "Kiwi", "FOREX", "🔵"),
            ("15", "USDCHF", "Swissie", "FOREX", "🔵"),
        ]
        
        # Display in 3 columns
        for i in range(0, len(symbols), 3):
            line = f"{self.theme.BOX_V}  "
            for j in range(3):
                if i + j < len(symbols):
                    num, sym, name, cat, icon = symbols[i+j]
                    line += f"{self.theme.ACCENT_GOLD}{icon}{self.theme.RESET} "
                    line += f"{self.theme.LIGHT_GREEN}{num:>2}{self.theme.RESET}. "
                    line += f"{self.theme.SILVER}{sym:<8}{self.theme.RESET} "
                    line += f"{self.theme.TEXT_MUTED}{name:<12}{self.theme.RESET}   "
            line += f"{self.theme.SILVER}{self.theme.BOX_V}"
            print(line)
        
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_BL}{self.theme.BOX_H * 98}{self.theme.BOX_BR}{self.theme.RESET}")
        
        # Commands
        print(f"\n{self.theme.BG_PANEL}{self.theme.SILVER}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}💎 ULTRA COMMANDS 💎{self.theme.RESET}{self.theme.SILVER}{' ' * 76}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.LIGHT_GREEN}[1-15]{self.theme.RESET}  Select trading symbol      {self.theme.ACCENT_BLUE}[S]{self.theme.RESET}  Statistics           {self.theme.ACCENT_GOLD}[R]{self.theme.RESET}  Reset{self.theme.SILVER}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.ACCENT_RED}[Q]{self.theme.RESET}          Quit Ultra Bot          {self.theme.ACCENT_GREEN}[H]{self.theme.RESET}  Help                {self.theme.TEXT_MUTED}[Ctrl+C]{self.theme.RESET}  Menu{self.theme.SILVER}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_BL}{self.theme.BOX_H * 98}{self.theme.BOX_BR}{self.theme.RESET}")
        
        print(f"\n{self.theme.ACCENT_GREEN}{self.theme.ICON_LIGHTNING} Ultra Mode Active {self.theme.ICON_LIGHTNING} {self.theme.RESET}")
        print(f"{self.theme.TEXT_MUTED}AI Engine | Neural Predictions | Multi-TP | Advanced Risk Management{self.theme.RESET}")
    
    def render_ultra_statistics(self, all_stats: Dict):
        """Render ultra statistics view"""
        self.render_ultra_logo()
        
        print(f"\n{self.theme.BG_PANEL}{self.theme.SILVER}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}{self.theme.ICON_CHART} ULTRA PERFORMANCE STATISTICS {self.theme.ICON_CHART}{self.theme.RESET}{self.theme.SILVER}{' ' * 67}{self.theme.BOX_V}")
        print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
        
        if not all_stats:
            print(f"{self.theme.BOX_V}  {self.theme.TEXT_MUTED}No trading data available yet. Start trading to see statistics!{self.theme.SILVER}{self.theme.BOX_V}")
        else:
            total_trades = sum(s['total_trades'] for s in all_stats.values())
            total_profit = sum(s['total_profit'] for s in all_stats.values())
            total_wins = sum(s['winning_trades'] for s in all_stats.values())
            
            print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}📊 GLOBAL METRICS{self.theme.RESET}{self.theme.SILVER}{' ' * 80}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}     Total Trades: {self.theme.LIGHT_GREEN}{total_trades:,}{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}     Total Wins: {self.theme.ACCENT_GREEN}{total_wins:,}{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}     Win Rate: {self.theme.ACCENT_GREEN if total_trades > 0 else self.theme.TEXT_MUTED}{(total_wins/total_trades*100) if total_trades > 0 else 0:.1f}%{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}     Total P&L: {self.theme.ACCENT_GREEN if total_profit >= 0 else self.theme.ACCENT_RED}${total_profit:,.2f}{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
            
            print(f"{self.theme.BOX_V}{' ' * 98}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}  {self.theme.BOLD}{self.theme.TEXT_PRIMARY}💰 PER SYMBOL BREAKDOWN{self.theme.RESET}{self.theme.SILVER}{' ' * 76}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}{self.theme.RESET}")
            print(f"{self.theme.BOX_V}  {'Symbol':<10} {'Trades':<8} {'Wins':<8} {'Losses':<8} {'Win Rate':<10} {'Profit':<12}{self.theme.SILVER}{self.theme.BOX_V}")
            print(f"{self.theme.BOX_V}  {'-'*60}{self.theme.SILVER}{self.theme.BOX_V}")
            
            for symbol, stats in sorted(all_stats.items(), key=lambda x: x[1]['total_profit'], reverse=True):
                win_color = self.theme.ACCENT_GREEN if stats['win_rate'] >= 50 else self.theme.ACCENT_RED
                profit_color = self.theme.ACCENT_GREEN if stats['total_profit'] >= 0 else self.theme.ACCENT_RED
                
                print(f"{self.theme.BOX_V}  {self.theme.SILVER}{symbol:<10}{self.theme.RESET} "
                      f"{stats['total_trades']:<8} "
                      f"{self.theme.ACCENT_GREEN}{stats['winning_trades']:<8}{self.theme.RESET} "
                      f"{self.theme.ACCENT_RED}{stats['losing_trades']:<8}{self.theme.RESET} "
                      f"{win_color}{stats['win_rate']:>5.1f}%{self.theme.RESET}    "
                      f"{profit_color}${stats['total_profit']:>10.2f}{self.theme.RESET}{self.theme.SILVER}{self.theme.BOX_V}")
        
        print(f"{self.theme.BOX_BL}{self.theme.BOX_H * 98}{self.theme.BOX_BR}{self.theme.RESET}")
        print(f"\n{self.theme.TEXT_SECONDARY}Press Enter to continue...{self.theme.RESET}")
        input()

# ============================================
# ULTRA BOT MAIN APPLICATION
# ============================================

class UltraBot:
    """Main Ultra Bot Application"""
    
    def __init__(self):
        self.ui = UltraUI()
        self.market = UltraMarketSimulator()
        self.generators: Dict[str, UltraSignalGenerator] = {}
        self.engines: Dict[str, UltraTradingEngine] = {}
        self.running = True
        
        # Initialize for all symbols
        symbols = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD", "BTCUSD", "ETHUSD", 
                   "US30", "US500", "GER30", "UK100", "AUDUSD", "NZDUSD", 
                   "USDCAD", "USDCHF", "XAGUSD"]
        
        for symbol in symbols:
            self.generators[symbol] = UltraSignalGenerator(symbol)
            self.engines[symbol] = UltraTradingEngine()
            
            # Warm up with historical data
            for _ in range(200):
                price = self.market.get_price(symbol)
                high, low = self.market.get_high_low(symbol)
                volume = self.market.get_volume(symbol)
                self.generators[symbol].add_data(price, high, low, volume)
        
        print(f"{self.ui.theme.ACCENT_GREEN}{self.ui.theme.ICON_ROCKET} Ultra Bot initialized successfully!{self.ui.theme.RESET}")
        time.sleep(1)
    
    def run_symbol(self, symbol: str):
        """Run ultra trading for symbol"""
        generator = self.generators[symbol]
        engine = self.engines[symbol]
        
        try:
            while self.running:
                # Update market data
                price = self.market.update_price(symbol)
                high, low = self.market.get_high_low(symbol)
                volume = self.market.get_volume(symbol)
                
                # Generate signal
                generator.add_data(price, high, low, volume)
                signal = generator.generate_ultra_signal()
                
                # Execute trades
                if signal.signal != UltraSignal.NEUTRAL and signal.confidence >= 50:
                    engine.execute_signal(signal)
                
                # Update positions
                engine.update_positions(price)
                
                # Render UI
                self.ui.render_ultra_dashboard(symbol, price, signal, engine, generator)
                
                # Countdown
                for i in range(UltraConfig.UPDATE_INTERVAL, 0, -1):
                    print(f"\r{self.ui.theme.TEXT_SECONDARY}⚡ Next update in {i} second{'s' if i > 1 else ''} ⚡{self.ui.theme.RESET}", end="", flush=True)
                    time.sleep(1)
                print("\r" + " " * 60 + "\r", end="")
                
        except KeyboardInterrupt:
            print(f"\n{self.ui.theme.ACCENT_GOLD}Returning to Ultra Menu...{self.ui.theme.RESET}")
            time.sleep(1)
    
    def show_statistics(self):
        """Show all statistics"""
        all_stats = {}
        for symbol, engine in self.engines.items():
            stats = engine.get_stats()
            if stats['total_trades'] > 0:
                all_stats[symbol] = stats
        
        self.ui.render_ultra_statistics(all_stats)
    
    def reset_all(self):
        """Reset all trading data"""
        self.ui.clear()
        self.ui.render_ultra_logo()
        
        print(f"\n{self.ui.theme.BG_PANEL}{self.ui.theme.SILVER}")
        print(f"{self.ui.theme.BOX_V}{' ' * 98}{self.ui.theme.BOX_V}")
        print(f"{self.ui.theme.BOX_V}  {self.ui.theme.ACCENT_RED}{self.ui.theme.BOLD}⚠️  WARNING: This will delete ALL trading data!  ⚠️{self.ui.theme.RESET}{self.ui.theme.SILVER}{' ' * 56}{self.ui.theme.BOX_V}")
        print(f"{self.ui.theme.BOX_BL}{self.ui.theme.BOX_H * 98}{self.ui.theme.BOX_BR}{self.ui.theme.RESET}")
        
        confirm = input(f"\n{self.ui.theme.TEXT_PRIMARY}Type '{self.ui.theme.ACCENT_RED}ULTRA RESET{self.ui.theme.TEXT_PRIMARY}' to confirm: {self.ui.theme.RESET}").strip()
        
        if confirm == 'ULTRA RESET':
            # Reset all engines
            for symbol in self.engines:
                self.engines[symbol] = UltraTradingEngine()
            print(f"\n{self.ui.theme.ACCENT_GREEN}{self.ui.theme.ICON_DIAMOND} Ultra Bot reset successfully!{self.ui.theme.RESET}")
        else:
            print(f"\n{self.ui.theme.ACCENT_GOLD}Reset cancelled{self.ui.theme.RESET}")
        
        time.sleep(2)
    
    def show_help(self):
        """Show help information"""
        self.ui.clear()
        self.ui.render_ultra_logo()
        
        print(f"\n{self.ui.theme.BG_PANEL}{self.ui.theme.SILVER}")
        print(f"{self.ui.theme.BOX_V}{' ' * 98}{self.ui.theme.BOX_V}")
        print(f"{self.ui.theme.BOX_V}  {self.ui.theme.BOLD}{self.ui.theme.TEXT_PRIMARY}{self.ui.theme.ICON_STAR} ULTRA BOT HELP GUIDE {self.ui.theme.ICON_STAR}{self.ui.theme.RESET}{self.ui.theme.SILVER}{' ' * 71}{self.ui.theme.BOX_V}")
        print(f"{self.ui.theme.BOX_V}{' ' * 98}{self.ui.theme.BOX_V}")
        
        help_text = [
            ("🎯 ULTRA SIGNALS", ""),
            ("   • ULTRA BUY/SELL", "Highest confidence signals (90%+)"),
            ("   • STRONG BUY/SELL", "High confidence signals (70-89%)"),
            ("   • BUY/SELL", "Standard signals (50-69%)"),
            ("", ""),
            ("🤖 AI FEATURES", ""),
            ("   • Neural Pattern Recognition", "Learns from market patterns"),
            ("   • Predictive Analytics", "Forecasts price movements"),
            ("   • Adaptive Learning", "Improves over time"),
            ("", ""),
            ("📊 INDICATORS", ""),
            ("   • RSI | MACD | Bollinger", "Primary indicators"),
            ("   • Ichimoku Cloud | Fibonacci", "Advanced analysis"),
            ("   • VWAP | ATR | AI Predictions", "Volume & volatility"),
            ("", ""),
            ("💼 RISK MANAGEMENT", ""),
            ("   • Dynamic Position Sizing", "Based on signal strength"),
            ("   • Multiple Take Profits", "3 TP levels per trade"),
            ("   • Daily Loss Limit", f"${UltraConfig.MAX_DAILY_LOSS:,}"),
            ("   • Max Daily Trades", f"{UltraConfig.MAX_DAILY_TRADES}"),
            ("", ""),
            ("⌨️ COMMANDS", ""),
            ("   • 1-15", "Select trading symbol"),
            ("   • S", "View statistics"),
            ("   • R", "Reset all data"),
            ("   • H", "Show this help"),
            ("   • Q", "Quit Ultra Bot"),
        ]
        
        for line1, line2 in help_text:
            if line2:
                print(f"{self.ui.theme.BOX_V}  {self.ui.theme.TEXT_PRIMARY}{line1:<25}{self.ui.theme.RESET} {self.ui.theme.TEXT_SECONDARY}{line2}{self.ui.theme.SILVER}{self.ui.theme.BOX_V}")
            else:
                print(f"{self.ui.theme.BOX_V}  {self.ui.theme.BOLD}{self.ui.theme.ACCENT_GOLD}{line1}{self.ui.theme.RESET}{self.ui.theme.SILVER}{self.ui.theme.BOX_V}")
        
        print(f"{self.ui.theme.BOX_BL}{self.ui.theme.BOX_H * 98}{self.ui.theme.BOX_BR}{self.ui.theme.RESET}")
        print(f"\n{self.ui.theme.TEXT_SECONDARY}Press Enter to continue...{self.ui.theme.RESET}")
        input()
    
    def run(self):
        """Main application loop"""
        def signal_handler(sig, frame):
            self.running = False
            print(f"\n{self.ui.theme.ACCENT_GREEN}{self.ui.theme.ICON_DIAMOND} Thank you for using MAPHAHA ULTRA BOT! {self.ui.theme.ICON_DIAMOND}{self.ui.theme.RESET}")
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        
        while self.running:
            self.ui.render_ultra_menu()
            
            try:
                choice = input(f"\n{self.ui.theme.ACCENT_GREEN}{self.ui.theme.BOLD}{self.ui.theme.ICON_LIGHTNING} ULTRA ➜ {self.ui.theme.RESET}").strip().upper()
                
                if choice == 'Q':
                    break
                elif choice == 'S':
                    self.show_statistics()
                elif choice == 'R':
                    self.reset_all()
                elif choice == 'H':
                    self.show_help()
                else:
                    symbol_map = {
                        "1": "EURUSD", "2": "GBPUSD", "3": "USDJPY",
                        "4": "AUDUSD", "5": "USDCAD", "6": "XAUUSD",
                        "7": "XAGUSD", "8": "BTCUSD", "9": "ETHUSD",
                        "10": "US30", "11": "US500", "12": "GER30",
                        "13": "UK100", "14": "NZDUSD", "15": "USDCHF"
                    }
                    
                    if choice in symbol_map:
                        self.run_symbol(symbol_map[choice])
                    elif choice:
                        print(f"\n{self.ui.theme.ACCENT_RED}Invalid selection! Enter 1-15 or command{self.ui.theme.RESET}")
                        time.sleep(1)
                        
            except Exception as e:
                print(f"\n{self.ui.theme.ACCENT_RED}Error: {e}{self.ui.theme.RESET}")
                time.sleep(1)

# ============================================
# ENTRY POINT
# ============================================

def main():
    """Ultra Bot entry point"""
    parser = argparse.ArgumentParser(description='Maphaha Ultra Bot - Premium Trading Platform')
    parser.add_argument('--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('--ultra-mode', action='store_true', help='Enable ultra mode')
    
    args = parser.parse_args()
    
    if args.no_color:
        # Override colors with empty strings
        for attr in dir(UltraTheme):
            if not attr.startswith('__') and isinstance(getattr(UltraTheme, attr), str):
                setattr(UltraTheme, attr, '')
    
    try:
        print(f"\n{UltraTheme.LIGHT_GREEN}{UltraTheme.BOLD}")
        print("╔════════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                                    ║")
        print("║                       🚀 STARTING MAPHAHA ULTRA BOT 🚀                             ║")
        print("║                     Premium Trading Intelligence System                            ║")
        print("║                         Light Green & Silver Edition                               ║")
        print("║                                                                                    ║")
        print("╚════════════════════════════════════════════════════════════════════════════════════╝")
        print(f"{UltraTheme.RESET}")
        
        print(f"{UltraTheme.SILVER}Initializing Ultra AI Engine...{UltraTheme.RESET}")
        time.sleep(1)
        
        bot = UltraBot()
        
        if args.ultra_mode:
            print(f"{UltraTheme.ACCENT_GREEN}⚡ ULTRA MODE ACTIVATED ⚡{UltraTheme.RESET}")
            time.sleep(1)
        
        bot.run()
        
    except KeyboardInterrupt:
        print(f"\n{UltraTheme.ACCENT_GREEN}{UltraTheme.ICON_CROWN} Goodbye! May the markets be with you! {UltraTheme.ICON_CROWN}{UltraTheme.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{UltraTheme.ACCENT_RED}Fatal Error: {e}{UltraTheme.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
