from coinbase.rest import RESTClient
import time

client = RESTClient(key_file="cdp_api_key.json")

def get_candles(product_id, start=None, end=None, granularity='FIVE_MINUTE'):
    
    # Valid granularity values for Coinbase Advanced Trade API:
    # 'ONE_MINUTE', 'FIVE_MINUTE', 'FIFTEEN_MINUTE', 'THIRTY_MINUTE',
    # 'ONE_HOUR', 'TWO_HOUR', 'SIX_HOUR', 'ONE_DAY', 'ONE_WEEK', 'ONE_MONTH'

    if(not start and not end):
        end = int(time.time())
        start = end - (10*60)

    return client.get_candles(
        product_id=product_id,
        start=start,
        end=end,
        granularity=granularity
    )

if __name__ == "__main__":
    print(get_candles('BTC-USD'))
    # {'candles': [{'start': '1748221800', 'low': '109421.06', 'high': '109467.28', 'open': '109442.79', 'close': '109438.28', 'volume': '2.35288209'}, {'start': '1748221500', 'low': '109369.06', 'high': '109613.58', 'open': '109613.58', 'close': '109434.61', 'volume': '27.92043725'}]}