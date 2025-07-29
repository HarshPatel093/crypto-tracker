import streamlit as st
import requests
import pandas as pd
import time

# Page setup
st.set_page_config(page_title="Crypto Tracker", layout="wide")

# Sidebar: User settings
with st.sidebar:
    st.header("⚙️ Settings")

    # Cryptocurrency options
    coin_options = {
        "Bitcoin": "bitcoin",
        "Ethereum": "ethereum",
        "Litecoin": "litecoin"
    }
    coin_name = st.selectbox("Select cryptocurrency", list(coin_options.keys()))
    coin_id = coin_options[coin_name]

    # Currency options
    vs_currency = st.selectbox(
        "Compare against (currency)",
        options=["usd", "aud", "eur", "inr"],
        format_func=lambda x: x.upper()
    )

    # Days slider
    days = st.slider("📅 Select number of days to show", min_value=1, max_value=60, value=30)

# Prevent API spamming
time.sleep(1)

# Get current price
def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    try:
        res = requests.get(url, params={"ids": coin_id, "vs_currencies": vs_currency})
        res.raise_for_status()
        return res.json().get(coin_id, {}).get(vs_currency, None)
    except Exception:
        st.error(f"❌ Failed to fetch price for {coin_name} in {vs_currency.upper()}.")
        return None

# Get historical price data
def get_historical_data(days):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    try:
        res = requests.get(url, params={"vs_currency": vs_currency, "days": days, "interval": "daily"})
        res.raise_for_status()
        data = res.json()
        prices = data.get("prices", [])
        if not prices:
            return pd.DataFrame()
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df[["date", "price"]].set_index("date")
        return df
    except Exception:
        st.warning("⚠️ No historical data available. CoinGecko API might be rate limiting or unavailable.")
        return pd.DataFrame()

# Main content
st.title(f"📊 {coin_name} Price Tracker")

# Show current price
price = get_price()
if price is not None:
    st.subheader(f"💰 Current {coin_name} Price: {price:.2f} {vs_currency.upper()}")

# Show historical chart
df = get_historical_data(days)
st.markdown(f"### 📘 {coin_name} Price Over Last {days} Days")
if df.empty:
    st.warning("⚠️ No historical data available.")
else:
    st.line_chart(df)
