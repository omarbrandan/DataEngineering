FROM apache/airflow:2.7.1-python3.8

# Establece el directorio de trabajo
WORKDIR /opt/airflow

# Copia los archivos necesarios al contenedor
COPY dags/ /opt/airflow/dags/
COPY modules/ /opt/airflow/dags/dags_modules/
COPY requirements.txt /opt/airflow/requirements.txt

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install -r /opt/airflow/requirements.txt