from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from dags_modules.data_extract import extract_data
from dags_modules.data_transform import transform_data
from dags_modules.data_load import preparar_y_cargar_datos
from dags_modules.mail_sender import send_email
from dags_modules.dags_utils import get_defaultairflow_args
from dotenv import load_dotenv
import os
from airflow.models import Variable

load_dotenv()

def prepare_and_send_email(**kwargs):
    alert_content = kwargs['ti'].xcom_pull(task_ids='prepare_and_load_task')
    if not alert_content:
        return
    send_email_context = {
        'var': {
            'value': {
                'subject_mail': Variable.get("subject_mail"),
                'email': Variable.get("email"),
                'email_password': Variable.get("email_password"),
                'to_address': Variable.get("to_address")
            }
        },
        'alert_content': alert_content
    }
    send_email(**send_email_context)

with DAG(
    dag_id='ETL_to_Redshift',
    default_args=get_defaultairflow_args(),
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
        op_args=[extract_data_task.output],
        dag=dag,
    )

    prepare_and_load_task = PythonOperator(
    task_id='prepare_and_load_task',
    python_callable=preparar_y_cargar_datos,
    op_args=[transform_data_task.output],
    dag=dag,
    )

    prepare_and_send_email_task = PythonOperator(
    task_id='prepare_and_send_email_task',
    python_callable=prepare_and_send_email,
    provide_context=True,
    dag=dag,
)

    extract_data_task >> transform_data_task >> prepare_and_load_task >> prepare_and_send_email_task