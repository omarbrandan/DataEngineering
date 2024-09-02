from utils import fetch_data_from_api

def extract_data():
    api_url = "https://api.coingecko.com/api/v3/coins/markets"
    data = fetch_data_from_api(api_url)
    return data