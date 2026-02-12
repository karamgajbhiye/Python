import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    sales=sales.groupby('product_id')['sale_date'].agg(['min','max']).reset_index()

    sales=sales[(sales['min']>='2019-01-01') & (sales['max']<="2019-03-31")]

    result = pd.merge(sales,product,how='inner',on='product_id')

    result = result[['product_id','product_name']]
    
    return result