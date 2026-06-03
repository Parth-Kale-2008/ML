import pandas as pd
import numpy as np
data = {
    'age':[21,None,45,63,62],
    'salary':[45000,28000,None,50000,20000]
}

df = pd.DataFrame(data)

df['age'].fillna(df['age'].mean(),inplace =True)
df['salary'].fillna(df['salary'].median(),inplace =True)

print(df)