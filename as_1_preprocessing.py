import pandas as pd
import numpy as np

data = {
    'student_id': [101, 102, 103, 104, 105, 102, 106, 107, 108, 101],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob', 'Frank', 'Grace', 'Heidi', 'Alice'],
    'math_mark': [85, 70, 88, None, 95, 70, 60, 82, np.nan, 85],
    'science_mark': [92, np.nan, 88, 75, 95, np.nan, 65, 82, 90, 92]
}

df = pd.DataFrame(data)
print(df)
df.to_csv('students_marks.csv', index=False)
# Calculate the mean only for numeric columns
df.fillna(df.mean(numeric_only=True), inplace=True)
print("--------------without missing values-----------")
print(df)
df.drop_duplicates(inplace=True)
print("--------------after removing duplicates-----------")
print(df)
#df.to_csv("student_marks_cleaned.csv", index=False)