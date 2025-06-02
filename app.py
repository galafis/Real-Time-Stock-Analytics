#!/usr/bin/env python3
"""
Real-Time Stock Analytics Dashboard
Interactive dashboard for real-time stock analysis with technical indicators.
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class StockAnalyzer:
    """Real-time stock analysis with technical indicators."""
    
    def __init__(self):
        self.data = None
        self.symbol = None
    
    def fetch_data(self, symbol, period='1y'):
        """Fetch stock data from Yahoo Finance."""
        try:
            self.symbol = symbol.upper()
            ticker = yf.Ticker(self.symbol)
            self.data = ticker.history(period=period)
            return True
        except Exception as e:
            st.error(f"Error fetching data for {symbol}: {str(e)}")
            return False
    
    def calculate_technical_indicators(self):
        """Calculate technical indicators."""
        if self.data is None or self.data.empty:
            return
        
        # Moving Averages
        self.data['MA20'] = self.data['Close'].rolling(window=20).mean()
        self.data['MA50'] = self.data['Close'].rolling(window=50).mean()
        
        # RSI
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        exp1 = self.data['Close'].ewm(span=12).mean()
        exp2 = self.data['Close'].ewm(span=26).mean()
        self.data['MACD'] = exp1 - exp2
        self.data['MACD_Signal'] = self.data['MACD'].ewm(span=9).mean()
        
        # Bollinger Bands
        self.data['BB_Middle'] = self.data['Close'].rolling(window=20).mean()
        bb_std = self.data['Close'].rolling(window=20).std()
        self.data['BB_Upper'] = self.data['BB_Middle'] + (bb_std * 2)
        self.data['BB_Lower'] = self.data['BB_Middle'] - (bb_std * 2)
    
    def create_price_chart(self):
        """Create interactive price chart with technical indicators."""
        fig = go.Figure()
        
        # Candlestick chart
        fig.add_trace(go.Candlestick(
            x=self.data.index,
            open=self.data['Open'],
            high=self.data['High'],
            low=self.data['Low'],
            close=self.data['Close'],
            name=self.symbol
        ))
        
        # Moving averages
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['MA20'],
            mode='lines',
            name='MA20',
            line=dict(color='orange', width=1)
        ))
        
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['MA50'],
            mode='lines',
            name='MA50',
            line=dict(color='blue', width=1)
        ))
        
        # Bollinger Bands
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['BB_Upper'],
            mode='lines',
            name='BB Upper',
            line=dict(color='gray', width=1, dash='dash'),
            showlegend=False
        ))
        
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['BB_Lower'],
            mode='lines',
            name='BB Lower',
            line=dict(color='gray', width=1, dash='dash'),
            fill='tonexty',
            fillcolor='rgba(128,128,128,0.1)',
            showlegend=False
        ))
        
        fig.update_layout(
            title=f'{self.symbol} Stock Price with Technical Indicators',
            yaxis_title='Price ($)',
            xaxis_title='Date',
            template='plotly_white',
            height=600
        )
        
        return fig
    
    def create_indicators_chart(self):
        """Create technical indicators chart."""
        fig = go.Figure()
        
        # RSI
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['RSI'],
            mode='lines',
            name='RSI',
            line=dict(color='purple')
        ))
        
        # RSI levels
        fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought (70)")
        fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold (30)")
        
        fig.update_layout(
            title='RSI (Relative Strength Index)',
            yaxis_title='RSI',
            xaxis_title='Date',
            template='plotly_white',
            height=300
        )
        
        return fig
    
    def create_macd_chart(self):
        """Create MACD chart."""
        fig = go.Figure()
        
        # MACD line
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['MACD'],
            mode='lines',
            name='MACD',
            line=dict(color='blue')
        ))
        
        # Signal line
        fig.add_trace(go.Scatter(
            x=self.data.index,
            y=self.data['MACD_Signal'],
            mode='lines',
            name='Signal',
            line=dict(color='red')
        ))
        
        # Histogram
        histogram = self.data['MACD'] - self.data['MACD_Signal']
        colors = ['green' if x >= 0 else 'red' for x in histogram]
        
        fig.add_trace(go.Bar(
            x=self.data.index,
            y=histogram,
            name='Histogram',
            marker_color=colors,
            opacity=0.6
        ))
        
        fig.update_layout(
            title='MACD (Moving Average Convergence Divergence)',
            yaxis_title='MACD',
            xaxis_title='Date',
            template='plotly_white',
            height=300
        )
        
        return fig
    
    def get_stock_info(self):
        """Get basic stock information."""
        try:
            ticker = yf.Ticker(self.symbol)
            info = ticker.info
            return {
                'Company': info.get('longName', 'N/A'),
                'Sector': info.get('sector', 'N/A'),
                'Market Cap': f"${info.get('marketCap', 0):,.0f}" if info.get('marketCap') else 'N/A',
                'P/E Ratio': f"{info.get('trailingPE', 0):.2f}" if info.get('trailingPE') else 'N/A',
                'Dividend Yield': f"{info.get('dividendYield', 0)*100:.2f}%" if info.get('dividendYield') else 'N/A'
            }
        except:
            return {}

def main():
    """Main Streamlit application."""
    st.set_page_config(
        page_title="Real-Time Stock Analytics",
        page_icon="📈",
        layout="wide"
    )
    
    st.title("📈 Real-Time Stock Analytics Dashboard")
    st.markdown("Interactive dashboard for stock analysis with technical indicators")
    
    # Sidebar
    st.sidebar.header("Stock Selection")
    
    # Popular stocks
    popular_stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'META', 'NFLX']
    
    # Stock input
    col1, col2 = st.sidebar.columns([2, 1])
    with col1:
        symbol = st.text_input("Enter Stock Symbol:", value="AAPL").upper()
    with col2:
        if st.button("📊 Analyze"):
            st.session_state.analyze_clicked = True
    
    # Quick select buttons
    st.sidebar.markdown("**Quick Select:**")
    cols = st.sidebar.columns(2)
    for i, stock in enumerate(popular_stocks):
        col = cols[i % 2]
        if col.button(stock, key=f"quick_{stock}"):
            symbol = stock
            st.session_state.analyze_clicked = True
    
    # Time period selection
    period = st.sidebar.selectbox(
        "Time Period:",
        ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y'],
        index=5
    )
    
    # Initialize analyzer
    analyzer = StockAnalyzer()
    
    # Analyze stock
    if st.session_state.get('analyze_clicked', False) or symbol:
        with st.spinner(f'Fetching data for {symbol}...'):
            if analyzer.fetch_data(symbol, period):
                analyzer.calculate_technical_indicators()
                
                # Stock info
                stock_info = analyzer.get_stock_info()
                if stock_info:
                    st.subheader(f"{stock_info.get('Company', symbol)} ({symbol})")
                    
                    # Display key metrics
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col1:
                        current_price = analyzer.data['Close'].iloc[-1]
                        st.metric("Current Price", f"${current_price:.2f}")
                    with col2:
                        price_change = analyzer.data['Close'].iloc[-1] - analyzer.data['Close'].iloc[-2]
                        change_pct = (price_change / analyzer.data['Close'].iloc[-2]) * 100
                        st.metric("Daily Change", f"${price_change:.2f}", f"{change_pct:.2f}%")
                    with col3:
                        st.metric("Market Cap", stock_info.get('Market Cap', 'N/A'))
                    with col4:
                        st.metric("P/E Ratio", stock_info.get('P/E Ratio', 'N/A'))
                    with col5:
                        st.metric("Dividend Yield", stock_info.get('Dividend Yield', 'N/A'))
                
                # Charts
                st.subheader("📊 Price Chart with Technical Indicators")
                price_chart = analyzer.create_price_chart()
                st.plotly_chart(price_chart, use_container_width=True)
                
                # Technical indicators
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📈 RSI Indicator")
                    rsi_chart = analyzer.create_indicators_chart()
                    st.plotly_chart(rsi_chart, use_container_width=True)
                
                with col2:
                    st.subheader("📉 MACD Indicator")
                    macd_chart = analyzer.create_macd_chart()
                    st.plotly_chart(macd_chart, use_container_width=True)
                
                # Data table
                st.subheader("📋 Recent Data")
                recent_data = analyzer.data.tail(10)[['Open', 'High', 'Low', 'Close', 'Volume', 'MA20', 'MA50', 'RSI']]
                st.dataframe(recent_data.round(2), use_container_width=True)
                
                # Reset the analyze button state
                st.session_state.analyze_clicked = False
    
    # Footer
    st.markdown("---")
    st.markdown("**Disclaimer:** This is for educational purposes only. Not financial advice.")

if __name__ == "__main__":
    main()

