import numpy as np 
import pandas as pd
df = pd.read_csv('asdfds.csv')
df_filtered = df[(df['age'] > 30) & (df['income'].notnull())]
df.groupby('Name').mean()
square_list = lambda nums: list(map(lambda x: x**2, nums))
