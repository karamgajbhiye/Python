import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    #merge function from pandas to join the two tables
    result = pd.merge(left=person,right=address,how="left",on="personId")
    return result[["firstName","lastName","city","state"]]