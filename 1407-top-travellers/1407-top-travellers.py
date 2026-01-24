import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # 1. Aggregate total distance per user_id
    rides_sum = (
        rides.groupby('user_id', as_index=False)['distance']
        .sum()
        .rename(columns={'distance': 'travelled_distance'})
    )

    # 2. Left join users with aggregated rides
    result = pd.merge(
        users,
        rides_sum,
        how='left',
        left_on='id',
        right_on='user_id'
    )

    # 3. Replace NaN with 0 for users with no rides
    result['travelled_distance'] = result['travelled_distance'].fillna(0)

    # 4. Sort as required
    result = result.sort_values(
        by=['travelled_distance', 'name'],
        ascending=[False, True]
    )

    return result[['name', 'travelled_distance']]
