import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId')
    df_no_orders = df[df['customerId'].isna()]
    result = df_no_orders[['name']].rename(columns={'name': 'Customers'}).reset_index(drop=True)
    
    return result
