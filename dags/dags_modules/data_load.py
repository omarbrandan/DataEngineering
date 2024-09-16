from modules.redshift import cargar_datos_redshift
from modules.cleaning import remove_duplicates

def preparar_y_cargar_datos(data):
    datos_procesados = procesar_datos(data)
    alert_content = ""
    for moneda in datos_procesados:
        if moneda.get('current_price') > 3000:
            alert_content += f"Moneda: {moneda.get('name')}, Precio actual: {moneda.get('current_price')}<br>"
    cargar_datos_redshift(datos_procesados)
    return alert_content

def procesar_datos(data):
    data_sin_duplicados = remove_duplicates(data)
    return data_sin_duplicados

def verificar_alertas(datos):
    alertas = []
    for moneda in datos:
        if moneda.get('current_price') > 3000:
            alertas.append(f"Moneda {moneda.get('name')} ({moneda.get('symbol')}) tiene un precio actual de {moneda.get('current_price')}.")
    return "<br>".join(alertas) if alertas else None