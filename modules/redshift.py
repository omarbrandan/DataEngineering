import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def cargar_datos_redshift(datos):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('REDSHIFT_DBNAME'),
            user=os.getenv('REDSHIFT_USER'),
            password=os.getenv('REDSHIFT_PASSWORD'),
            host=os.getenv('REDSHIFT_HOST'),
            port=os.getenv('REDSHIFT_PORT')
        )
        cursor = conn.cursor()

        # Crear la tabla temporal
        cursor.execute("""
        CREATE TEMP TABLE IF NOT EXISTS cryptocurrencies_temp (
            id VARCHAR(50),
            symbol VARCHAR(10),
            name VARCHAR(50),
            current_price DECIMAL(36, 18),
            market_cap BIGINT,
            market_cap_rank INT,
            total_volume BIGINT,
            high_24h DECIMAL(36, 18),
            low_24h DECIMAL(36, 18),
            price_change_24h DECIMAL(36, 18),
            price_change_percentage_24h DECIMAL(36, 18),
            circulating_supply DECIMAL(36, 18),
            total_supply DECIMAL(36, 18),
            max_supply DECIMAL(36, 18),
            ath DECIMAL(36, 18),
            ath_change_percentage DECIMAL(36, 18),
            ath_date TIMESTAMP,
            atl DECIMAL(36, 18),
            atl_change_percentage DECIMAL(36, 18),
            atl_date TIMESTAMP,
            ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Insertar datos en la tabla temporal
        for moneda in datos:
            cursor.execute("""
                INSERT INTO cryptocurrencies_temp (
                    id, symbol, name, current_price, market_cap, market_cap_rank,
                    total_volume, high_24h, low_24h, price_change_24h, price_change_percentage_24h,
                    circulating_supply, total_supply, max_supply, ath, ath_change_percentage,
                    ath_date, atl, atl_change_percentage, atl_date, ingestion_time
                ) VALUES (
                    %(id)s, %(symbol)s, %(name)s, %(current_price)s, %(market_cap)s, %(market_cap_rank)s,
                    %(total_volume)s, %(high_24h)s, %(low_24h)s, %(price_change_24h)s, %(price_change_percentage_24h)s,
                    %(circulating_supply)s, %(total_supply)s, %(max_supply)s, %(ath)s, %(ath_change_percentage)s,
                    %(ath_date)s, %(atl)s, %(atl_change_percentage)s, %(atl_date)s, %(ingestion_time)s
                )
            """, {
                'id': moneda.get('id'),
                'symbol': moneda.get('symbol'),
                'name': moneda.get('name'),
                'current_price': moneda.get('current_price'),
                'market_cap': moneda.get('market_cap'),
                'market_cap_rank': moneda.get('market_cap_rank'),
                'total_volume': moneda.get('total_volume'),
                'high_24h': moneda.get('high_24h'),
                'low_24h': moneda.get('low_24h'),
                'price_change_24h': moneda.get('price_change_24h'),
                'price_change_percentage_24h': moneda.get('price_change_percentage_24h'),
                'circulating_supply': moneda.get('circulating_supply'),
                'total_supply': moneda.get('total_supply'),
                'max_supply': moneda.get('max_supply'),
                'ath': moneda.get('ath'),
                'ath_change_percentage': moneda.get('ath_change_percentage'),
                'ath_date': moneda.get('ath_date'),
                'atl': moneda.get('atl'),
                'atl_change_percentage': moneda.get('atl_change_percentage'),
                'atl_date': moneda.get('atl_date'),
                'ingestion_time': datetime.now()
            })

        # Transferir datos de la tabla temporal a la tabla principal
        cursor.execute("""
            INSERT INTO cryptocurrencies (
                id, symbol, name, current_price, market_cap, market_cap_rank,
                total_volume, high_24h, low_24h, price_change_24h, price_change_percentage_24h,
                circulating_supply, total_supply, max_supply, ath, ath_change_percentage,
                ath_date, atl, atl_change_percentage, atl_date, ingestion_time
            )
            SELECT
                id, symbol, name, current_price, market_cap, market_cap_rank,
                total_volume, high_24h, low_24h, price_change_24h, price_change_percentage_24h,
                circulating_supply, total_supply, max_supply, ath, ath_change_percentage,
                ath_date, atl, atl_change_percentage, atl_date, ingestion_time
            FROM cryptocurrencies_temp
        """)

        # Confirmar y cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        with open('d:\Omar\Documents\CODERHOUSE\Data Engineering\log\error.log', 'a') as f:
            f.write(f"{datetime.now()}: Error al cargar datos en Redshift: {e}\n")
        print(f"Error: {e}")