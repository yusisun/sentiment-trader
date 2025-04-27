import tweepy
import pandas as pd
import os, time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TWITTER_BEARER = os.getenv("TWITTER_BEARER")

client = tweepy.Client(bearer_token=TWITTER_BEARER, wait_on_rate_limit=True)

memecoins = ["DOGE", "SHIBA", "PEPE", "WIF", "BONK", "FLOKI", "TURBO", "LADYS", "HOSKY", "PIT"]

query_base = " OR ".join([f"${coin} OR #{coin}" for coin in memecoins])


def collect_tweets():
    tweets = client.search_recent_tweets(query=query_base, max_results=100, tweet_fields=["created_at", "public_metrics"])
    data = []
    for tweet in tweets.data:
        data.append({
            "text": tweet.text,
            "created_at": tweet.created_at,
            "retweets": tweet.public_metrics["retweet_count"],
            "likes": tweet.public_metrics["like_count"]
        })
    df = pd.DataFrame(data)
    df.to_csv(f"shared/twitter_{datetime.utcnow().strftime('%Y%m%d_%H%M')}.csv", index=False)

if __name__ == "__main__":
    while True:
        collect_tweets()
        time.sleep(900)  # every 15 minutes