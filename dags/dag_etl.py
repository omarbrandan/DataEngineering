from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dags_modules.data_extract import extract_data
from dags_modules.data_transform import transform_data
from dags_modules.data_load import preparar_y_cargar_datos
from dotenv import load_dotenv
import os

load_dotenv()

default_args = {
    'owner': 'omar',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    dag_id='ETL_to_Redshift',
    default_args=default_args,
    description='DAG para ETL de criptomonedas a Redshift',
    schedule_interval='@daily',
    start_date=datetime(2024, 8, 28),
    catchup=False,
) as dag:

    extract_data_task = PythonOperator(
        task_id='extract_data_task',
        python_callable=extract_data,
        dag=dag,
    )

    transform_data_task = PythonOperator(
        task_id='transform_data_task',
        python_callable=transform_data,
        op_args=[extract_data()],
        dag=dag,
    )

    prepare_and_load_task = PythonOperator(
    task_id='prepare_and_load_task',
    python_callable=preparar_y_cargar_datos,
    op_args=[transform_data(extract_data())],
    dag=dag,
)

    extract_data_task >> transform_data_task >> prepare_and_load_task