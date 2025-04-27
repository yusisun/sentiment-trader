# Sentiment Trading Pipeline

This project builds a full-stack, end-to-end crypto trading system that uses social media sentiment (Twitter/Reddit) and technical indicators to generate live trading signals and execute trades automatically.

## 🛠 Project Structure

```
sentiment-trader/
├── docker-compose.yml          # Define multi-service architecture
├── .env                         # API keys and environment variables
├── backend/                     # MemeBERT inference server (FastAPI)
├── collector/                   # Reddit and Twitter real-time scrapers
├── signals/                     # Feature engineering + ML model inference
├── executor/                    # Trading bot executing on CEXs (Binance, Bybit)
├── shared/                      # Common config, utils, schemas
├── database/                    # PostgreSQL schema and database utils
├── backtest/                    # Backtest runner, metrics, plots
├── dashboard/                   # Streamlit app to monitor signals and performance
├── tests/                       # Unit tests for modules
```

## ⚡ Quick Start

1. **Clone the Repo**

```bash
git clone https://github.com/yusisun/sentiment-trader.git
cd sentiment-trader
```

2. **Fill Your Secrets**

Create `.env` file:
```env
BINANCE_API_KEY=your_binance_key
BINANCE_API_SECRET=your_binance_secret
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_SECRET=your_reddit_secret
TWITTER_BEARER=your_twitter_bearer_token
DB_HOST=localhost
DB_NAME=sentiment
DB_USER=postgres
DB_PASS=your_db_password
```

3. **Launch Docker Containers**

```bash
docker-compose up --build
```

Services launched:
- Reddit/Twitter collectors
- MemeBERT inference API
- Feature generator + predictor
- Trade execution bot
- PostgreSQL database

## 📡 Live Data Collection (collector/)
- `reddit_scraper.py`: Pulls latest posts mentioning top 10 memecoins from Reddit subreddits like r/cryptocurrency, r/dogecoin.
- `twitter_scraper.py`: Pulls tweets mentioning $COIN or #COIN using Tweepy (Twitter API v2).
- **Stored fields**: text, created_at, retweets, likes.
- **Output**: Saves structured `.csv` files every 15 minutes.

## 🧠 Sentiment Analysis (backend/)
- `app.py`: FastAPI app that loads a MemeBERT model.
- When collector scrapes new data, the backend scores each text as positive/neutral/negative sentiment.
- Output is a **sentiment score** (-1 to +1) per post/tweet.

## 📈 Feature Engineering + Prediction (signals/)
- `features.py`: Merges technical indicators (RSI, MACD, OBV) with sentiment averages.
- `predictor.py`: Loads trained XGBoost or LSTM model to predict next move:
  - **BUY** → if expected price increase
  - **SELL** → if expected price decrease

## 🛒 Trade Execution (executor/)
- `trader.py`: Connects to Binance (or any CEX) using ccxt.
- `strategy.py`: Defines trading rule: Buy if prediction is BUY, Sell if SELL.
- Executes real trades (or can simulate in paper trading mode).

## 🛢️ Data Storage (database/)
- PostgreSQL container stores:
  - Raw Reddit/Twitter text and sentiment
  - Signals generated
  - Executed trades (including PnL)

## 📊 Backtesting Framework (backtest/)
- `backtest_runner.py`: Replays historical price and sentiment data.
- `metrics.py`: Computes Sharpe ratio, Max drawdown, Win rate.
- `plots.py`: Graphs cumulative PnL curve.

## 📺 Real-Time Monitoring (dashboard/)
- Streamlit dashboard visualizes:
  - Current open positions
  - Last sentiment scores
  - Trade history and live PnL performance

## ✅ Unit Testing (tests/)
- Placeholder tests (`test_collector.py`, etc.) ready to expand.
- Run with `pytest` to ensure pipeline stability.

---

# ⚡ How It Flows End-to-End

1. **Collectors** pull tweets/posts every 15 min.
2. **Backend** (FastAPI) scores sentiment via MemeBERT.
3. **Signals** combine features (sentiment + TA) → predict BUY/SELL.
4. **Executor** places live trades on Binance (or paper trades).
5. **Database** logs everything.
6. **Dashboard** shows live system status and performance.

---

# 🚀 How to Run This Project

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/sentiment-trader.git
cd sentiment-trader
```

### 2. Setup Secrets (.env)
Provide API keys for:
- Binance
- Reddit
- Twitter
- PostgreSQL credentials

### 3. Launch All Services
```bash
docker-compose up --build
```

### 4. Access:
- API Docs: `http://localhost:8000/docs`
- Dashboard: `http://localhost:8501`

---

# 🔥 Future Extensions
- Dynamic trade sizing by confidence score
- Integrate Google Trends & Discord mentions
- Deploy to AWS / GCP for production uptime


**Built for serious alpha hunting. 🧠🚀**

