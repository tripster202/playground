import yfinance as yf
import pandas as pd
import numpy as np

def fetch_price_data(tickers, start_date, end_date):
    """Fetch price data for a list of tickers from yfinance."""
    data = yf.download(tickers, start=start_date, end=end_date, interval='1h', auto_adjust=True)
    if isinstance(data, pd.DataFrame):
        return data[['High', 'Low', 'Close']]  # Return only relevant columns
    else:  # Handle single ticker case
        return data[['High', 'Low', 'Close']].to_frame()

def calculate_hl2(data):
    """Calculate the HL2 (High-Low Average) for each data point."""
    # HL2 is the average of the High and Low prices for each data point.
    hl2 = (data['High'] + data['Low']) / 2
    return hl2

def calculate_travel(data):
    """Calculate the travel for each ticker."""
    # Travel measures the cumulative movement of prices relative to the average price.
    travel = {}
    for ticker in data.columns:
        prices = data[ticker].dropna()
        avg_price = prices.mean()
        cumulative_diff = np.sum(np.abs(np.diff(prices)))
        travel[ticker] = cumulative_diff / avg_price
    return travel

def calculate_channel(data):
    """Calculate the channel for each ticker."""
    # Channel quantifies the price range's variability relative to the average price.
    channel = {}
    for ticker in data.columns:
        prices = data[ticker].dropna()
        avg_price = prices.mean()
        std_dev = np.std(prices)
        channel[ticker] = (2 * std_dev) / avg_price
    return channel

def calculate_volatility(travel, channel):
    """Calculate volatility as travel/channel for each ticker."""
    # Volatility is a measure of relative price movement, defined as the ratio of travel to channel.
    volatility = {ticker: travel[ticker] / channel[ticker] for ticker in travel}
    return volatility

def main():
    # User inputs
    tickers = ['QQQ', 'TSLA', 'SPY']
    start_date = '2024-01-01'
    end_date = '2025-01-01'

    # Fetch price data
    print("\nFetching price data...")
    data = fetch_price_data(tickers, start_date, end_date)
    print("\nPrice Data:")
    print(data)

    # Calculate HL2
    print("\nCalculating HL2 (High-Low Average)...")
    hl2 = calculate_hl2(data)
    print("\nHL2 Data:")
    print(hl2)

    # Calculate metrics
    print("\nCalculating metrics...")
    travel = calculate_travel(hl2)  # Use Close prices for travel
    channel = calculate_channel(hl2)  # Use Close prices for channel
    volatility = calculate_volatility(travel, channel)

    # Sort tickers by volatility
    sorted_volatility = sorted(volatility.items(), key=lambda x: x[1], reverse=True)

    # Display results
    print("\nResults: (Sorted by Highest Volatility)")
    for ticker, vol in sorted_volatility:
        print(f"Ticker: {ticker}")
        print(f"  Travel: {travel[ticker]:.4f}")
        print(f"  Channel: {channel[ticker]:.4f}")
        print(f"  Volatility (Travel/Channel): {vol:.4f}")
        print("-" * 30)

if __name__ == "__main__":
    main()