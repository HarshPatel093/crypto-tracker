import requests
import pandas as pd

COINGECKO_URL = "https://api.coingecko.com/api/v3"

def get_current_price(coin_id, vs_currency="usd"):
    try:
        response = requests.get(
            f"{COINGECKO_URL}/simple/price",
            params={"ids": coin_id, "vs_currencies": vs_currency},
            timeout=10
        )
        response.raise_for_status()
        return response.json().get(coin_id, {}).get(vs_currency)
    except Exception as e:
        print(f"Price fetch error: {e}")
        return None

def get_historical_data(coin_id, vs_currency="usd", days=30):
    url = f"{COINGECKO_URL}/coins/{coin_id}/market_chart"
    try:
        response = requests.get(url, params={"vs_currency": vs_currency, "days": days}, timeout=10)
        data = response.json()
        prices = data.get("prices", [])
        if not prices:
            return pd.DataFrame()
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df[["date", "price"]]
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return pd.DataFrame()
