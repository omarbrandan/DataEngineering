import requests
import json

def obtener_datos_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        print(f"Error al hacer la solicitud: {response.status_code}")
        return None

def main():
    datos = obtener_datos_coingecko()
    if datos:
        # Convertir JSON a diccionario de Python
        datos_dict = json.loads(json.dumps(datos))

        # Ejemplo de manipulación de datos: imprimir los nombres y precios de las criptomonedas
        for moneda in datos_dict:
            nombre = moneda.get('name')
            precio = moneda.get('current_price')
            print(f"Nombre: {nombre}, Precio: ${precio}")

if __name__ == "__main__":
    main()
