import praw
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os, time

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_USER_AGENT = "MemeSentimentBot"

memecoins = ["DOGE", "SHIBA", "PEPE", "WIF", "BONK", "FLOKI", "TURBO", "LADYS", "HOSKY", "PIT"]
subreddits = ["CryptoCurrency", "solana", "dogecoin", "memecoins"]

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def collect_reddit_posts():
    all_data = []
    for coin in memecoins:
        for sub in subreddits:
            for post in reddit.subreddit(sub).search(coin, sort="new", time_filter="hour"):
                if post.score > 5:
                    all_data.append({
                        "coin": coin,
                        "title": post.title,
                        "text": post.selftext,
                        "created_utc": datetime.utcfromtimestamp(post.created_utc),
                        "score": post.score,
                        "subreddit": sub
                    })
    df = pd.DataFrame(all_data)
    df.to_csv(f"shared/reddit_{datetime.utcnow().strftime('%Y%m%d_%H%M')}.csv", index=False)

if __name__ == "__main__":
    while True:
        collect_reddit_posts()
        time.sleep(900)  # every 15 minutes
