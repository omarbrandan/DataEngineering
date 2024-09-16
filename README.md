# DataEngineering

Primera Preentrega: extraer datos de una API pública y crear la tabla en Redshift para posterior carga de datos.

Segunda Preentrega: adaptar los datos leídos de la API y cargar en la tabla creada en Redshift (el archivo .sql de la preentrega 1, preentrega1.sql, es el mismo para la preentrega 2).

Tercera Preentrega: correr el proyecto en un container de Docker, embebido en un DAG de Airflow dentro del container.

Entrega Final: 3° Preentrega con la tarea de envío de correo y automatización con Taskfile.

    Pasos para correr el proyecto de manera automática con Taskfile.yml:
        sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
        ./bin/task pre_project
        ./bin/task start_project
        ./bin/task down_project
        ./bin/task cleanup

Recordar cargar las credenciales en el archivo .env que se va a crear en los pasos detallados anteriormente.