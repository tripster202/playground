# create a program that does the following:

# import price data for a list of tickers from yfinance over a given period

# print out the pandas df for the user to easily understand the data in the dataframe

# calculate the average price for the given period
# calculate the travel
# the travel is defined as the cumulative sum of absolute differences between data points, divided by the average value for the given period
# calculate the channel
# the channel is defined as 2x the standard deviation of the data points, divided by the average value for the given period

# sort the tickers by volatility with the highest volatility being first
# volatility is defined as travel/channel

# create detailed print statements for the user to understand the outputs

import yfinance as yf
import pandas as pd
import numpy as np

def fetch_price_data(tickers, start_date, end_date):
    """Fetch price data for a list of tickers from yfinance."""
    data = yf.download(tickers, start=start_date, end=end_date,interval='1h', auto_adjust=True)['Close']
    if isinstance(data, pd.Series):  # Handle single ticker case
        data = data.to_frame(name=tickers[0])
    return data

def calculate_travel(data):
    """Calculate the travel for each ticker."""
    # Travel measures the cumulative movement of prices relative to the average price.
    # It is calculated as the cumulative sum of absolute differences between consecutive prices,
    # divided by the average price over the period.
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
    # It is defined as 2 times the standard deviation of prices, divided by the average price.
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
    # Higher volatility indicates more significant price fluctuations relative to the range.
    volatility = {ticker: travel[ticker] / channel[ticker] for ticker in travel}
    return volatility

def main():
    # User inputs
    tickers = input("Enter a list of tickers separated by commas: ").split(',')
    tickers = [ticker.strip().upper() for ticker in tickers]
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Fetch price data
    print("\nFetching price data...")
    data = fetch_price_data(tickers, start_date, end_date)
    print("\nPrice Data:")
    print(data)

    # Calculate metrics
    print("\nCalculating metrics...")
    travel = calculate_travel(data)
    channel = calculate_channel(data)
    volatility = calculate_volatility(travel, channel)

    # Sort tickers by volatility
    sorted_volatility = sorted(volatility.items(), key=lambda x: x[1], reverse=True)

    # Display results
    print("\nResults:")
    for ticker, vol in sorted_volatility:
        print(f"Ticker: {ticker}")
        print(f"  Travel: {travel[ticker]:.4f}")
        print(f"  Channel: {channel[ticker]:.4f}")
        print(f"  Volatility (Travel/Channel): {vol:.4f}")
        print("-" * 30)

if __name__ == "__main__":
    main()