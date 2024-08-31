from dotenv import load_dotenv
from datetime import datetime, timedelta
import os


load_dotenv()  # take environment variables from .env.


def get_schema()->str:
    return os.getenv("REDSHIFT_HOST")

def get_credentials() -> dict:

    url = "https://api.coingecko.com/api/v3/coins/markets"
    user = os.getenv("REDSHIFT_USER")
    pwd = os.getenv("REDSHIFT_PASSWORD")
    port = os.getenv("REDSHIFT_PORT")
    data_base = os.getenv("REDSHIFT_DBNAME")

    return {
        "dbname": data_base,
        "user": user,
        "password": pwd,
        "host": url,
        "port": port,
    }


def get_defaultairflow_args():
    return {
        "owner": "omar",
        "depends_on_past": False,
        "start_date": datetime(2024, 1, 1),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "catch"
        "retry_delay": timedelta(minutes=5),
    }