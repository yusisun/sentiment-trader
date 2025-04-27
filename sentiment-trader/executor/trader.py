import ccxt
import os
from dotenv import load_dotenv
from strategy import decide_trade

load_dotenv()

exchange = ccxt.binance({
    'apiKey': os.getenv("BINANCE_API_KEY"),
    'secret': os.getenv("BINANCE_API_SECRET"),
})

symbol = "DOGE/USDT"

def execute_trade(signal):
    if signal == "BUY":
        exchange.create_market_buy_order(symbol, 100)
    elif signal == "SELL":
        exchange.create_market_sell_order(symbol, 100)

if __name__ == "__main__":
    decision = decide_trade()
    execute_trade(decision)