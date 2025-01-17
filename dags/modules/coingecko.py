import requests
import json
from datetime import datetime

def obtener_datos_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 30,
        'page': 1,
        'sparkline': 'false'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        datos = response.json()
        return datos
    except requests.RequestException as e:
        with open('/opt/airflow/logs/error.log', 'a') as f:
            f.write(f"{datetime.now()}: Error al hacer la solicitud: {e}\n")
        return None
