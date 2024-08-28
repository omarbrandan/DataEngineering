# Usa la imagen base de Apache Airflow con Python
FROM apache/airflow:2.6.3-python3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY dags/ /opt/airflow/dags/
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

# Define las variables de entorno
ENV $(cat /app/.env | xargs)

# Configura el comando de entrada para iniciar Airflow
ENTRYPOINT ["airflow", "scheduler"]
CMD ["airflow", "webserver"]