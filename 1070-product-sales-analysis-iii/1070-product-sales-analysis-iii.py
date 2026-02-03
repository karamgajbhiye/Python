import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales['first_year'] = sales.groupby('product_id')['year'].transform('min')
    sales = sales[sales['first_year'] == sales['year']]
    return sales[['product_id','first_year','quantity','price']]