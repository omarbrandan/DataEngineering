FROM apache/airflow:2.7.1-python3.8

WORKDIR /opt/airflow

COPY dags/ /opt/airflow/dags/
COPY dags_modules/ /opt/airflow/dags/dags_modules/

RUN pip install --upgrade pip
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install -r /opt/airflow/requirements.txt
