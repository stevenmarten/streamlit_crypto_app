import streamlit as st
import requests

st.set_page_config(page_title="Cryptocurrency Dashboard", layout="centered")

API_KEY = "CG-3AgFsvJvoNWhuAxhDXSHdZtR"

def get_market_data(vs_currency="usd", per_page=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": 1,
        "sparkline": "false",
        "x_cg_pro_api_key": API_KEY
    }
    response = requests.get(url, params=params, timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return []

def main():
    st.title("Cryptocurrency Market Dashboard")
    st.write("This Streamlit app retrieves market data from the CoinGecko API and displays the top cryptocurrencies by market cap.")

    currency = st.selectbox("Select currency:", ["usd", "eur", "gbp"])
    num_coins = st.slider("Number of coins to display:", min_value=1, max_value=50, value=10)

    data = get_market_data(vs_currency=currency, per_page=num_coins)

    if data:
        st.subheader(f"Top {num_coins} Cryptocurrencies by Market Cap (priced in {currency.upper()})")
        for coin in data:
            name = coin.get("name")
            symbol = coin.get("symbol", "").upper()
            price = coin.get("current_price")
            market_cap = coin.get("market_cap")
            st.write(f"**{name} ({symbol})** — Price: {currency.upper()} {price:,.2f}  |  Market Cap: {currency.upper()} {market_cap:,.2f}")
    else:
        st.warning("No data available. Please try again later.")

if __name__ == "__main__":
    main()
