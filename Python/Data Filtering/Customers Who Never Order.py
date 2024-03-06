import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result= customers.merge(orders.rename({'id': 'order_id'}, axis=1),
               left_on='id', right_on='customerId', how='left')
    result= result.rename({'name':'Customers'}, axis=1).loc[result['order_id'].isnull()]
    return result[['Customers']]