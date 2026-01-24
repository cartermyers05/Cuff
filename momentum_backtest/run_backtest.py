#!/usr/bin/env python3
"""
Quick runner script for the Momentum Trading Backtester

Usage:
    python run_backtest.py          # Run quick test
    python run_backtest.py --full   # Run full optimization

This script runs from the momentum_backtest directory.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from momentum_backtest.backtest import run_quick_test, run_full_optimization

if __name__ == '__main__':
    if '--full' in sys.argv:
        print("Starting full optimization - this will take several minutes...")
        results, top_results = run_full_optimization()
        print("\n" + "="*60)
        print("FULL OPTIMIZATION COMPLETE!")
        print("="*60)
        print("\nCheck the results/ directory for:")
        print("  - all_results.csv (all parameter combinations)")
        print("  - best_system_trades.csv (trade log)")
        print("  - OPTIMAL_SYSTEM.md (documentation)")
        print("  - equity_curves.png (visualization)")
        print("  - parameter_sensitivity.png (what matters most)")
        print("  - drawdown.png (risk analysis)")
        print("  - monthly_returns.png (performance over time)")
    else:
        print("Running quick test (small parameter grid)...")
        results = run_quick_test()
        print("\n" + "="*60)
        print("QUICK TEST COMPLETE!")
        print("="*60)
        print("\nTo run full optimization with all parameters:")
        print("  python run_backtest.py --full")
