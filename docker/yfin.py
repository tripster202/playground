import yfinance as yf

# Define the ticker symbol
ticker_symbol = "MSFT"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch basic info about the stock
info = ticker.info

# Fetch historical data for the last 5 days
history = ticker.history(period="5d")

# Print the results
print(f"Stock Info for {ticker_symbol}:")
print(f"Company Name: {info['longName']}")
print(f"Current Price: {info['regularMarketPrice']}")
print("\nHistorical Data (Last 5 Days):")
print(history[['Open', 'High', 'Low', 'Close', 'Volume']])