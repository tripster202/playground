import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for a given ticker symbol.
    """
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # data = yf.download(tickers, start=start_date, end=end_date, interval='1h', auto_adjust=True)
    print("Data fetched successfully!")
    return stock_data

def explore_dataframes(df):
    """
    Teach users about DataFrame operations using the stock data.
    """
    print("\n--- DataFrame Overview ---")
    print("First 5 rows of the DataFrame:")
    print(df.head())

    print("\nDataFrame Columns:")
    print(df.columns)

    print("\nBasic Statistics:")
    print(df.describe())

    print("\n--- DataFrame Manipulations ---")
    print("1. Adding a new column: Daily Return")
    df['Daily Return'] = df['Adj Close'].pct_change()
    print(df[['Adj Close', 'Daily Return']].head())

    print("\n2. Filtering rows: Days with positive returns")
    positive_returns = df[df['Daily Return'] > 0]
    print(positive_returns[['Adj Close', 'Daily Return']].head())

    print("\n3. Resampling: Monthly average closing price")
    monthly_avg = df['Adj Close'].resample('M').mean()
    print(monthly_avg.head())

    print("\n4. Handling missing data: Filling NaN values")
    df['Daily Return'].fillna(0, inplace=True)
    print(df[['Adj Close', 'Daily Return']].head())

def main():
    """
    Main function to run the program.
    """
    print("Welcome to the DataFrame tutorial using yfinance!")
    
    # Predefined values
    ticker = "AAPL"  # Example: Apple Inc.
    start_date = "2022-01-01"
    end_date = "2022-12-31"

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Convert the index to datetime if not already
    stock_data.index = pd.to_datetime(stock_data.index)

    # Teach DataFrame manipulations
    explore_dataframes(stock_data)

if __name__ == "__main__":
    main()