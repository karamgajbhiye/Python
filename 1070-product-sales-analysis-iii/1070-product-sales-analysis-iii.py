import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    
    # Add a column with the first (earliest) year each product was sold
    sales['first_year'] = sales.groupby('product_id')['year'].transform('min')
    
    # Filter rows to keep only sales from the product's first year
    sales = sales[sales['first_year'] == sales['year']]
    
    # Return only the required columns
    return sales[['product_id', 'first_year', 'quantity', 'price']]
