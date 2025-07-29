# 📈 Crypto Price Tracker

A simple and interactive web application built with [Streamlit](https://streamlit.io) to track the **live** and **historical** prices of popular cryptocurrencies like **Bitcoin**, **Ethereum**, and **Litecoin** in multiple currencies: **USD**, **AUD**, **EUR**, and **INR**.

---

## 🚀 Features

- 🔄 **Live Price** updates using the [CoinGecko API](https://www.coingecko.com/en/api)
- 📊 **Historical Price Graph** for the last 1 to 60 days
- ⚙️ Customizable options via sidebar:
  - Cryptocurrency: Bitcoin, Ethereum, Litecoin
  - Currency: USD, AUD, EUR, INR
  - Days: 1–60
- 🌙 Clean and responsive layout using Streamlit

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/crypto-tracker.git
cd crypto-tracker
pip install -r requirements.txt
streamlit run app.py

🌐 Live Demo
👉 Deployed on Streamlit Cloud:
https://crypto-tracker-ftxatknpgy83lbjcxmqhkn.streamlit.app/

🗂️ Project Structure
crypto-tracker/
├── app.py               # Main Streamlit app
├── crypto_api.py
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation

🙌 Acknowledgements
CoinGecko API for free crypto market data
Streamlit for making app development super easy