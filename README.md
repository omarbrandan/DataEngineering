# DataEngineering

Primera Preentrega: extraer datos de una API pública y crear la tabla en Redshift para posterior carga de datos.

Segunda Preentrega: adaptar los datos leídos de la API y cargar en la tabla creada en Redshift (el archivo .sql de la preentrega 1, preentrega1.sql, es el mismo para la preentrega 2).

Tercera Preentrega: correr el proyecto en un container de Docker, embebido en un DAG de Airflow dentro del container.

--- (.env será agregado a gitignore en la entrega final) ---

Taskfile.yml:
    sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
    ./bin/task pre_project
    ./bin/task start_project
    ./bin/task down_project
    ./bin/task cleanup