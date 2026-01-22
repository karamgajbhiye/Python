import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    t1 = pd.merge(company,orders,how='left',left_on='com_id', right_on='com_id')
    red_ids = t1[t1['name'] == 'RED']['sales_id'].unique()

    #filter red_ids from sales
    result = sales_person[sales_person['sales_id'].isin(red_ids)==False][['name']]
    #print(result['name'])
    return result