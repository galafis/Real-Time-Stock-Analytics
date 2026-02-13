"""Tests for StockAnalyzer in app.py."""

import pandas as pd
import pytest

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import StockAnalyzer


class TestStockAnalyzerInit:
    """Test StockAnalyzer instantiation."""

    def test_initial_data_is_none(self):
        analyzer = StockAnalyzer()
        assert analyzer.data is None

    def test_initial_symbol_is_none(self):
        analyzer = StockAnalyzer()
        assert analyzer.symbol is None


class TestCalculateTechnicalIndicators:
    """Test calculate_technical_indicators adds expected columns."""

    @pytest.fixture()
    def analyzer_with_data(self):
        analyzer = StockAnalyzer()
        dates = pd.date_range("2023-01-01", periods=60, freq="B")
        analyzer.data = pd.DataFrame(
            {
                "Open": range(100, 160),
                "High": range(101, 161),
                "Low": range(99, 159),
                "Close": range(100, 160),
                "Volume": [1000] * 60,
            },
            index=dates,
        )
        analyzer.symbol = "TEST"
        return analyzer

    def test_adds_expected_columns(self, analyzer_with_data):
        analyzer_with_data.calculate_technical_indicators()
        for col in ["MA20", "MA50", "RSI", "MACD", "MACD_Signal", "BB_Upper", "BB_Middle", "BB_Lower"]:
            assert col in analyzer_with_data.data.columns, f"Missing column {col}"

    def test_rsi_within_bounds(self, analyzer_with_data):
        analyzer_with_data.calculate_technical_indicators()
        rsi = analyzer_with_data.data["RSI"].dropna()
        assert (rsi >= 0).all() and (rsi <= 100).all()


class TestRSIEdgeCases:
    """Test RSI division-by-zero guard."""

    def _make_analyzer(self, prices):
        analyzer = StockAnalyzer()
        dates = pd.date_range("2023-01-01", periods=len(prices), freq="B")
        analyzer.data = pd.DataFrame(
            {
                "Open": prices,
                "High": prices,
                "Low": prices,
                "Close": prices,
                "Volume": [1000] * len(prices),
            },
            index=dates,
        )
        analyzer.symbol = "TEST"
        return analyzer

    def test_all_gains_rsi_is_100(self):
        # Strictly increasing prices: loss is always 0, RSI should be 100
        prices = list(range(100, 120))
        analyzer = self._make_analyzer(prices)
        analyzer.calculate_technical_indicators()
        rsi = analyzer.data["RSI"].dropna()
        assert len(rsi) > 0
        assert (rsi == 100).all()

    def test_all_losses_rsi_is_zero(self):
        # Strictly decreasing prices: gain is always 0, RSI should be 0
        prices = list(range(200, 180, -1))
        analyzer = self._make_analyzer(prices)
        analyzer.calculate_technical_indicators()
        rsi = analyzer.data["RSI"].dropna()
        assert len(rsi) > 0
        assert (rsi == 0).all()
