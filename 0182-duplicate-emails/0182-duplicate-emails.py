import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by email
    df = person.groupby('email')['id'].count().reset_index()
    # Filter only duplicates
    df = df[df['id']>1][['email']]
    return df
    