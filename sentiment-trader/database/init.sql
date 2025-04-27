CREATE TABLE sentiment_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    sentiment_score FLOAT,
    timestamp TIMESTAMP
);

CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    side VARCHAR(10),
    executed_price FLOAT,
    volume FLOAT,
    timestamp TIMESTAMP
);
