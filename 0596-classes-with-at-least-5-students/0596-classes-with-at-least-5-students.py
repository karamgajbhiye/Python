import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    #count students per class
    class_count = courses.groupby('class')['student'].count()
    
    # find all the classes that have at least five students
    class_count = class_count[class_count >= 5]
    
    # # Convert Series to DataFrame
    class_count = class_count.reset_index()
    
    # return only class column
    return class_count[['class']]
