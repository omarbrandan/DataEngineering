drop table if exists omaragustinbrandan_coderhouse.cryptocurrencies;

CREATE TABLE omaragustinbrandan_coderhouse.cryptocurrencies (
    id VARCHAR(50) PRIMARY KEY,
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
    atl_date TIMESTAMP
);

ALTER TABLE omaragustinbrandan_coderhouse.cryptocurrencies ADD COLUMN ingestion_time TIMESTAMP DEFAULT GETDATE();

SELECT * FROM omaragustinbrandan_coderhouse.cryptocurrencies;
