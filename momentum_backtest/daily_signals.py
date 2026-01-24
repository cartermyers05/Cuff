#!/usr/bin/env python3
"""
DAILY TRADING SIGNAL GENERATOR
==============================
Run this at 9:00-9:30 AM to get your plays for the day.

Usage:
    python daily_signals.py
"""

import pandas as pd
import numpy as np
import requests
import io
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

# Your trading universe
SYMBOLS = ['NVDL', 'TSLT', 'AMDL', 'SOXL', 'TQQQ', 'MULL', 'CLSK']

# Optimized parameters from backtesting
PARAMS = {
    'rsi_entry_min': 30,
    'rsi_entry_max': 60,
    'rsi_exit_threshold': 70,
    'stop_loss': 0.03,        # 3% stop
    'take_profit': 0.07,      # 7% target
    'volume_threshold': 1.5,  # 1.5x volume
    'momentum_threshold': 0.03,  # 3% 3-day move
    'max_hold_days': 3,
}

# Position sizing
CAPITAL = 40000
POSITION_PCT = 0.30
MAX_POSITIONS = 2


def fetch_recent_data(symbol: str, days: int = 100) -> pd.DataFrame:
    """Fetch recent data from Stooq"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days*2)  # Buffer for weekends

    stooq_symbol = f"{symbol}.US"
    d1 = start_date.strftime('%Y%m%d')
    d2 = end_date.strftime('%Y%m%d')

    url = f'https://stooq.com/q/d/l/?s={stooq_symbol}&d1={d1}&d2={d2}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200 and 'Date' in resp.text:
            df = pd.read_csv(io.StringIO(resp.text))
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.set_index('Date').sort_index()
            return df
    except Exception as e:
        print(f"  Error fetching {symbol}: {e}")

    return pd.DataFrame()


def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate technical indicators"""
    # RSI(14)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Volume averages
    df['VMA20'] = df['Volume'].rolling(window=20).mean()
    df['Volume_Ratio'] = df['Volume'] / df['VMA20']

    # 50-day SMA
    df['SMA50'] = df['Close'].rolling(window=50).mean()

    # Momentum
    df['Momentum_3d'] = df['Close'].pct_change(3)
    df['Momentum_5d'] = df['Close'].pct_change(5)

    # Volatility (for position sizing)
    df['ATR'] = (df['High'] - df['Low']).rolling(14).mean()

    return df


def analyze_symbol(symbol: str) -> Dict:
    """Analyze a single symbol for trading signals"""
    df = fetch_recent_data(symbol)

    if df.empty or len(df) < 60:
        return {'symbol': symbol, 'signal': 'NO_DATA', 'score': 0}

    df = calculate_indicators(df)
    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else latest

    # Current metrics
    price = latest['Close']
    rsi = latest['RSI']
    volume_ratio = latest['Volume_Ratio']
    momentum_3d = latest['Momentum_3d']
    above_sma = price > latest['SMA50'] if not pd.isna(latest['SMA50']) else True

    # Check entry conditions
    rsi_ok = PARAMS['rsi_entry_min'] <= rsi <= PARAMS['rsi_entry_max']
    volume_ok = volume_ratio >= PARAMS['volume_threshold']
    momentum_ok = momentum_3d >= PARAMS['momentum_threshold']

    # Calculate signal strength (0-100)
    score = 0
    signals = []

    if rsi_ok:
        score += 25
        signals.append(f"RSI={rsi:.1f} (in range)")
    else:
        if rsi < PARAMS['rsi_entry_min']:
            signals.append(f"RSI={rsi:.1f} (oversold - wait)")
        else:
            signals.append(f"RSI={rsi:.1f} (overbought)")

    if volume_ok:
        score += 25
        signals.append(f"Volume={volume_ratio:.1f}x (HIGH)")
    else:
        signals.append(f"Volume={volume_ratio:.1f}x (low)")

    if momentum_ok:
        score += 25
        signals.append(f"Mom3d={momentum_3d*100:.1f}% (strong)")
    else:
        signals.append(f"Mom3d={momentum_3d*100:.1f}%")

    if above_sma:
        score += 15
        signals.append("Above SMA50")
    else:
        signals.append("Below SMA50 (caution)")

    # Bonus for momentum alignment
    if momentum_3d > 0.05:
        score += 10

    # Determine signal
    if score >= 65 and rsi_ok and volume_ok and momentum_ok:
        signal = 'BUY'
    elif rsi > PARAMS['rsi_exit_threshold']:
        signal = 'SELL/EXIT'
    elif score >= 50:
        signal = 'WATCH'
    else:
        signal = 'WAIT'

    # Position sizing
    position_value = CAPITAL * POSITION_PCT
    shares = int(position_value / price)
    stop_price = price * (1 - PARAMS['stop_loss'])
    target_price = price * (1 + PARAMS['take_profit'])

    return {
        'symbol': symbol,
        'signal': signal,
        'score': score,
        'price': price,
        'rsi': rsi,
        'volume_ratio': volume_ratio,
        'momentum_3d': momentum_3d * 100,
        'above_sma': above_sma,
        'signals': signals,
        'shares': shares,
        'position_value': shares * price,
        'stop_loss': stop_price,
        'take_profit': target_price,
        'risk_reward': PARAMS['take_profit'] / PARAMS['stop_loss'],
    }


def print_header():
    """Print fancy header"""
    print("\n" + "="*70)
    print("  💰 MOMENTUM TRADING SIGNALS - " + datetime.now().strftime('%Y-%m-%d %H:%M'))
    print("="*70)
    print(f"  Capital: ${CAPITAL:,} | Position Size: {POSITION_PCT*100:.0f}% | Max Positions: {MAX_POSITIONS}")
    print("="*70)


def print_signal(result: Dict, rank: int):
    """Print a single signal result"""
    symbol = result['symbol']
    signal = result['signal']
    score = result['score']

    # Emoji based on signal
    emoji = {'BUY': '🟢', 'SELL/EXIT': '🔴', 'WATCH': '🟡', 'WAIT': '⚪', 'NO_DATA': '❌'}

    print(f"\n{emoji.get(signal, '⚪')} #{rank} {symbol} - {signal} (Score: {score}/100)")
    print("-" * 50)

    if result.get('price'):
        print(f"  Price:     ${result['price']:.2f}")
        print(f"  RSI:       {result['rsi']:.1f}")
        print(f"  Volume:    {result['volume_ratio']:.1f}x avg")
        print(f"  Momentum:  {result['momentum_3d']:.1f}% (3-day)")
        print(f"  Trend:     {'✅ Above' if result['above_sma'] else '❌ Below'} SMA50")

        if signal == 'BUY':
            print(f"\n  📊 TRADE SETUP:")
            print(f"     Shares:      {result['shares']} (${result['position_value']:,.0f})")
            print(f"     Entry:       ${result['price']:.2f}")
            print(f"     Stop Loss:   ${result['stop_loss']:.2f} (-{PARAMS['stop_loss']*100:.0f}%)")
            print(f"     Target:      ${result['take_profit']:.2f} (+{PARAMS['take_profit']*100:.0f}%)")
            print(f"     Risk/Reward: {result['risk_reward']:.1f}x")


def print_polymarket_reminder():
    """Remind about Polymarket confirmation"""
    print("\n" + "="*70)
    print("  ⚠️  POLYMARKET CONFIRMATION REQUIRED")
    print("="*70)
    print("""
  Your 9.84x W/L ratio comes from Polymarket sentiment, NOT technicals.

  Before entering any BUY signal:
  1. Check Polymarket for relevant sentiment on the underlying
  2. Look for positive catalyst sentiment (earnings, news, macro)
  3. Confirm volume/momentum aligns with prediction market sentiment

  Pure technicals = 1.03x W/L ratio
  Your edge = Polymarket sentiment timing

  DON'T TRADE WITHOUT POLYMARKET CONFIRMATION!
""")


def main():
    """Main signal generation"""
    print_header()

    print("\n📡 Fetching latest market data...")

    results = []
    for symbol in SYMBOLS:
        print(f"  Analyzing {symbol}...", end=" ")
        result = analyze_symbol(symbol)
        results.append(result)
        print(f"Score: {result['score']}")

    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)

    # Print BUY signals first
    buy_signals = [r for r in results if r['signal'] == 'BUY']
    watch_signals = [r for r in results if r['signal'] == 'WATCH']
    other_signals = [r for r in results if r['signal'] not in ['BUY', 'WATCH']]

    if buy_signals:
        print("\n" + "🟢"*35)
        print("  TOP BUY SIGNALS")
        print("🟢"*35)
        for i, result in enumerate(buy_signals[:MAX_POSITIONS], 1):
            print_signal(result, i)
    else:
        print("\n⚪ No strong BUY signals today. Consider waiting.")

    if watch_signals:
        print("\n" + "-"*70)
        print("  🟡 WATCHLIST (Close to entry)")
        print("-"*70)
        for i, result in enumerate(watch_signals[:3], 1):
            print_signal(result, i)

    print_polymarket_reminder()

    # Summary
    print("\n" + "="*70)
    print("  QUICK SUMMARY")
    print("="*70)
    print(f"  {'Symbol':<8} {'Signal':<10} {'Score':<8} {'RSI':<8} {'Vol':<8} {'Mom3d':<8}")
    print("-"*70)
    for r in results:
        if r.get('price'):
            print(f"  {r['symbol']:<8} {r['signal']:<10} {r['score']:<8} {r['rsi']:<8.1f} {r['volume_ratio']:<8.1f}x {r['momentum_3d']:<8.1f}%")
        else:
            print(f"  {r['symbol']:<8} {r['signal']:<10} {'N/A':<8}")

    print("\n" + "="*70)
    print(f"  Run again: python daily_signals.py")
    print("="*70 + "\n")

    return results


if __name__ == '__main__':
    main()
