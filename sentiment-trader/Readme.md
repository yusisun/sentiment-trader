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

4. **Access Dashboard**

Visit `http://localhost:8501` for live monitoring!


## 📚 How it Works

- **Collectors** scrape posts/tweets mentioning top meme coins (DOGE, PEPE, etc.)
- **Backend** scores posts in real-time using MemeBERT model
- **Signals** combines sentiment + technical indicators to predict next move
- **Executor** places trades based on signals
- **Database** stores sentiment, features, trades
- **Dashboard** visualizes PnL, trades, and signals

## 🚀 Extend Ideas

- Fine-tune MemeBERT on crypto slang
- Add orderbook flow features (depth imbalance)
- Dynamic position sizing based on sentiment strength
- Add real-time Google Trends signal

---

Feel free to contribute, fork, or ask questions!

**Built for serious alpha hunting. 🧠🚀**
