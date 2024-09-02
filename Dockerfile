FROM apache/airflow:2.7.1-python3.8

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

RUN mkdir -p /opt/airflow/dags /opt/airflow/modules /opt/airflow/dags/dags_modules

USER root

# Instalar las dependencias necesarias para compilar psycopg2
RUN apt-get update \
    && apt-get install -y \
       postgresql \
       libpq-dev

USER airflow

COPY dags/ /opt/airflow/dags/

RUN pip install --upgrade pip
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install -r /opt/airflow/requirements.txt

WORKDIR /opt/airflow
