import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## load and read the data
a = pd.read_csv('Documents/salary.csv')
a.head()
a.describe()
a.shape