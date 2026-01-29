import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = (
        (triangle['x'] + triangle['y'] > triangle['z'] ) &
        (triangle['x'] + triangle['z'] > triangle['y'] ) &
        (triangle['y'] + triangle['z'] > triangle['x'] )
    )
    triangle['triangle'] = triangle['triangle'].map({True: 'Yes', False: 'No'})
    return triangle