from coingecko import obtener_datos_coingecko
from redshift import cargar_datos_redshift
from utils import log_error

def main():
    datos = obtener_datos_coingecko()
    if datos:
        cargar_datos_redshift(datos)
    else:
        log_error('No se obtuvieron datos de CoinGecko.')

if __name__ == "__main__":
    main()