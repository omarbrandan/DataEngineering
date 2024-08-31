FROM apache/airflow:2.7.1-python3.8

# Establece el directorio de trabajo
WORKDIR /opt/airflow

# Copia los archivos necesarios al contenedor
COPY dags/ /opt/airflow/dags/
COPY modules/ /opt/airflow/modules/
COPY requirements.txt /opt/airflow/requirements.txt

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install -r /opt/airflow/requirements.txt

# Inicializa la base de datos y corre el webserver y scheduler
CMD ["bash", "-c", "airflow db init && airflow scheduler & airflow webserver"]