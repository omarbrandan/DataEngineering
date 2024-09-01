from dotenv import load_dotenv
from datetime import datetime, timedelta
import os


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

def get_defaultairflow_args():
    return {
        "owner": "omar",
        "depends_on_past": False,
        "start_date": datetime(2024, 8, 28),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }