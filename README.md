# Streamlit Cryptocurrency Dashboard

This app uses the [CoinGecko API](https://www.coingecko.com) to display cryptocurrency market data in a Streamlit dashboard.

## Features

- Fetches top cryptocurrencies by market cap using the CoinGecko API.
- Displays data in a table with rank, name, current price (USD), and 24h price change.
- Easily extensible for additional metrics or charts.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/stevenmarten/streamlit_crypto_app.git
   cd streamlit_crypto_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your CoinGecko API key as an environment variable. You can get an API key by creating an account on CoinGecko (the API key used in this repository is stored as a secret for deployment). Export your key as `COINGECKO_API_KEY`:
   ```bash
   export COINGECKO_API_KEY=<your_api_key_here>
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The app will start locally and open in your browser at `http://localhost:8501/`.

## Deploying to Streamlit Cloud

To deploy this app to Streamlit Cloud:

1. Go to [Streamlit Cloud](https://share.streamlit.io/).
2. Create a new app and connect it to this repository (`stevenmarten/streamlit_crypto_app`).
3. Provide the branch (`main`) and main file (`app.py`).
4. Add your CoinGecko API key in the app's secrets (`COINGECKO_API_KEY`).
5. Deploy and share the public URL.

## License

This project is for demonstration purposes.
