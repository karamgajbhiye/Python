import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    #Aggregate total amount per day
    daily_amount = customer.groupby('visited_on',as_index=False).agg(amount=('amount','sum'))
    #Sort by date
    daily_amount = daily_amount.sort_values('visited_on')
    #7-day rolling sum
    daily_amount['7d_amount'] = daily_amount['amount'].rolling(window=7).sum()
    #7-day rolling average
    daily_amount['average_amount'] = daily_amount['amount'].rolling(window=7).mean().round(2)
    #Remove rows before day 7
    result = daily_amount[daily_amount["7d_amount"].notna()]

    return (
        result[['visited_on', '7d_amount', 'average_amount']]
        .rename(columns={'7d_amount': 'amount'})
    )