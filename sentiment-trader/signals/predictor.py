import joblib
import pandas as pd
from features import generate_features

model = joblib.load('model/xgb_model.pkl')

def predict_signal(price_df, sentiment_df):
    features = generate_features(price_df, sentiment_df)
    pred = model.predict(features.tail(1))
    return "BUY" if pred[0] == 1 else "SELL"

if __name__ == "__main__":
    print("Signal Generator Running...")