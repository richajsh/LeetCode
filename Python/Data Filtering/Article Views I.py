import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df= views.where(views.author_id==views.viewer_id)
    df= df[['author_id']].sort_values(by="author_id").drop_duplicates().rename({"author_id":"id"}, axis=1).dropna()
    return df