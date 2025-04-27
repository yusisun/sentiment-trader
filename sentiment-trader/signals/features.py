import pandas as pd
import talib
def generate_features(price_df, sentiment_df):
    price_df['RSI'] = talib.RSI(price_df['close'], timeperiod=14)
    price_df['MACD'], _, _ = talib.MACD(price_df['close'])
    price_df['OBV'] = talib.OBV(price_df['close'], price_df['volume'])
    features = price_df[['RSI', 'MACD', 'OBV']].copy()
    features['sentiment'] = sentiment_df['sentiment_score']
    return features.fillna(0)