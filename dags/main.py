from modules.coingecko import obtener_datos_coingecko
from modules.redshift import cargar_datos_redshift
from modules.cleaning import remove_duplicates

def main():
    datos = obtener_datos_coingecko()
    if datos:
        datos_limpios = remove_duplicates(datos)
        cargar_datos_redshift(datos_limpios)
    else:
        print('No se obtuvieron datos de CoinGecko.')

if __name__ == "__main__":
    main()