import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df= tweets[['tweet_id']].where(tweets['content'].str.len()>15).dropna()
    return df 