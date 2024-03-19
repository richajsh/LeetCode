import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users= users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return users