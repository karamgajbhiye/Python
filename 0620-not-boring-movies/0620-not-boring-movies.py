import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    odd_id = cinema[cinema['id']%2==1]
    rem_bor = odd_id[odd_id['description']!='boring']
    rating_order = rem_bor.sort_values(by=['rating'],ascending=False)
    return rating_order
    