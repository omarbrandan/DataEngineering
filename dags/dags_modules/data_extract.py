import logging
from dags_utils import fetch_data_from_api

def extract_data():
    api_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': False
    }

    logging.info(f"Fetching data from API: {api_url} with params: {params}")

    try:
        data = fetch_data_from_api(api_url, params)
        logging.info("Data fetched successfully")
        return data
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        raise