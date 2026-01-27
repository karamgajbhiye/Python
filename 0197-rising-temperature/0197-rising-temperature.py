import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    #sorted
    df=weather.sort_values(by='recordDate')
    #Calculate the difference in temperature from the previous day
    temp_increase = df['temperature'].diff() > 0
    #Calculate the difference in days between each record
    consecutive_days = df['recordDate'].diff().dt.days == 1
    
    return df[temp_increase & consecutive_days][['id']]

    