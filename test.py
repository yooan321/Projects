import numpy as np 
import pandas as pd
df = pd.read_csv('asdfds.csv')
df_filtered = df[(df['age'] > 30) & (df['income'].notnull())]
df.groupby('Name').mean()
square_list = lambda nums: list(map(lambda x: x**2, nums))
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
import seaborn as sns
tips = sns.load_dataset('tips')