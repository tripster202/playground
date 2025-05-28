import candles
import pandas as pd
from statsmodels.tsa.seasonal import STL
from datetime import datetime
import pytz

def fetch_candle_data(symbol='BTC-USD', hours=48):
    """Fetch candle data and return as DataFrame."""
    data = candles.get_candles_fifteen(symbol=symbol, input_hours=hours)
    df = pd.DataFrame(
        [(int(candle['start']), float(candle['volume'])) for candle in data['candles']],
        columns=['timestamp', 'volume']
    ).set_index('timestamp')
    return df

def find_iqr_outliers(df):
    """Identify outliers in volume using the IQR method."""
    Q1 = df['volume'].quantile(0.25)
    Q3 = df['volume'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    return df[df['volume'] > upper_bound]

def find_zscore_outliers(df, threshold=3):
    """Identify outliers in volume using the Z-score method."""
    mean = df['volume'].mean()
    std = df['volume'].std()
    df = df.copy()
    z_score = (df['volume'] - mean) / std
    return df[z_score > threshold]
    # df['z_score'] = (df['volume'] - mean) / std
    # return df[df['z_score'] > threshold]

def find_stl_outliers(df, period=4, threshold=3):
    """Identify outliers in volume using STL decomposition."""
    df = df.copy()
    stl = STL(df['volume'], period=period)
    result = stl.fit()
    residuals = result.resid
    z_scores = (residuals - residuals.mean()) / residuals.std()
    return df[z_scores > threshold]

def unix_to_mst(unix_ts):
    """Convert unix timestamp to human-readable MST (Denver) time."""
    mst = pytz.timezone('America/Denver')
    dt = datetime.fromtimestamp(int(unix_ts), tz=pytz.UTC).astimezone(mst)
    return dt.strftime('%d %b %y %H:%M:%S')

def index_to_mst(df):
    """
    Takes a DataFrame with a unix timestamp index and returns a new DataFrame
    with the index converted to human-readable MST (Denver) time.
    """
    df = df.copy()
    df['mst_time'] = df.index.to_series().apply(unix_to_mst)
    df.set_index('mst_time', inplace=True)
    return df

if __name__ == "__main__":
    df = fetch_candle_data(symbol='BTC-USD', hours=48)
    print(f"DataFrame length: {len(df)}")

    iqr_outliers = find_iqr_outliers(df)
    print(f"\nIQR Outliers (MST):\n{index_to_mst(iqr_outliers)}")

    zscore_outliers = find_zscore_outliers(df)
    print(f"\nZ-score Outliers (MST):\n{index_to_mst(zscore_outliers)}")

    stl_outliers = find_stl_outliers(df)
    print(f"\nSTL Outliers (MST):\n{index_to_mst(stl_outliers)}")