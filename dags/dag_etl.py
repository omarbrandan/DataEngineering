from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dags_modules.data_extract import extract_data
from dags_modules.data_transform import transform_data
from dags_modules.data_load import load_data
from utils import get_defaultairflow_args
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración del DAG
dag = DAG(
    'ETL_to_Redshift',
    description='DAG para realizar ETL de criptomonedas y cargar en Redshift',
    schedule_interval='@daily',
    start_date=datetime(2024, 8, 28),
    catchup=False,
    default_args=get_defaultairflow_args()
)

# Definir las tareas usando PythonOperator
extract_task = PythonOperator(
    task_id='extract_data_task',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data,
    op_args=[extract_task.output],
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    op_args=[transform_task.output],
    dag=dag
)

# Definir las dependencias entre las tareas
extract_task >> transform_task >> load_task