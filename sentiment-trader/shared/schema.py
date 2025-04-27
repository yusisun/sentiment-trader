from pydantic import BaseModel

class SentimentData(BaseModel):
    symbol: str
    sentiment_score: float
    timestamp: str

class PriceData(BaseModel):
    symbol: str
    close: float
    volume: float
    timestamp: str