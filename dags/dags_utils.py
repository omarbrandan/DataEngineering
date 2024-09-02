from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests
import psycopg2
from psycopg2.extras import execute_values

load_dotenv()

def get_schema()->str:
    return os.getenv("REDSHIFT_SCHEMA")  

def get_credentials() -> dict:
    return {
        "dbname": os.getenv("REDSHIFT_DBNAME"),
        "user": os.getenv("REDSHIFT_USER"),
        "password": os.getenv("REDSHIFT_PASSWORD"),
        "host": os.getenv("REDSHIFT_HOST"),
        "port": os.getenv("REDSHIFT_PORT"),
    }
    
def fetch_data_from_api(api_url: str, params: dict = None) -> dict:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()