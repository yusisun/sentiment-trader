import pandas as pd

def run_backtest(signal_generator, price_data, sentiment_data):
    signals = []
    for i in range(len(price_data)):
        signal = signal_generator(price_data.iloc[:i+1], sentiment_data.iloc[:i+1])
        signals.append(signal)
    return signals