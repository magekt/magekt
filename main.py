import requests
import hmac
import hashlib
import time
import os
import pandas as pd
import ta
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("WAZIRX_API_KEY")
SECRET_KEY = os.getenv("WAZIRX_SECRET_KEY")
BASE_URL = "https://api.wazirx.com"
PRIVATE_URL = "https://api.wazirx.com/sapi/v1"

TRADING_PAIRS = ["btcusdt", "shibusdt"]
MIN_PROFIT_MARGIN = 0.5  # 0.5% minimum expected gain per trade

HEADERS = {
    "X-Api-Key": API_KEY
}

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = datetime.now().strftime("logs/%Y-%m-%d.log")
    with open(filename, "a") as f:
        f.write(f"[{now}] {msg}\n")
    print(f"[{now}] {msg}")

def get_timestamp():
    return int(time.time() * 1000)

def sign_payload(payload):
    query = "&".join([f"{key}={value}" for key, value in payload.items()])
    signature = hmac.new(SECRET_KEY.encode(), query.encode(), hashlib.sha256).hexdigest()
    return query + f"&signature={signature}"

def get_klines(symbol, interval='1h', limit=50):
    url = f"{BASE_URL}/api/v2/klines"
    params = {"market": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['close'] = df['close'].astype(float)
    return df

def analyze(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    latest = df.iloc[-1]
    if latest['rsi'] < 30 and latest['macd'] > latest['macd_signal']:
        return "buy"
    elif latest['rsi'] > 70 and latest['macd'] < latest['macd_signal']:
        return "sell"
    else:
        return "hold"

def get_balances():
    timestamp = get_timestamp()
    payload = {"timestamp": timestamp}
    query = sign_payload(payload)
    url = f"{PRIVATE_URL}/funds?{query}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def place_order(symbol, side, quantity):
    timestamp = get_timestamp()
    payload = {
        "symbol": symbol,
        "side": side,
        "type": "market",
        "quantity": quantity,
        "timestamp": timestamp
    }
    query = sign_payload(payload)
    url = f"{PRIVATE_URL}/order/place?{query}"
    response = requests.post(url, headers=HEADERS)
    log(f"Placed {side} order on {symbol}: {response.text}")
    return response.json()

def sell_minor_holdings():
    balances = get_balances()
    ignore = ["usdt", "inr"]
    for coin, details in balances.items():
        if coin not in ignore and float(details['free']) > 0:
            symbol = f"{coin}usdt"
            quantity = float(details['free'])
            try:
                place_order(symbol, "sell", quantity)
                log(f"Auto-sold {quantity} {coin} to USDT.")
            except Exception as e:
                log(f"Failed to sell {coin}: {str(e)}")

def trade():
    for pair in TRADING_PAIRS:
        df = get_klines(pair)
        signal = analyze(df)
        log(f"Analysis for {pair}: {signal}")
        if signal == "buy":
            # Simulate order size as 50% of USDT balance
            balances = get_balances()
            usdt_bal = float(balances.get("usdt", {}).get("free", 0))
            if usdt_bal > 1:
                price = df['close'].iloc[-1]
                qty = round(usdt_bal * 0.5 / price, 4)
                place_order(pair, "buy", qty)

if __name__ == "__main__":
    log("--- Starting Daily Routine ---")
    sell_minor_holdings()
    trade()
    log("--- Done for Today ---")
