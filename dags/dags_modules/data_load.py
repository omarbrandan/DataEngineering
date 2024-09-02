from modules.redshift import cargar_datos_redshift
from modules.cleaning import remove_duplicates

def preparar_y_cargar_datos(data):
    datos_procesados = procesar_datos(data)
    cargar_datos_redshift(datos_procesados)

def procesar_datos(data):
    data_sin_duplicados = remove_duplicates(data)
    return data_sin_duplicados