#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size 
sns.set(rc={'figure.figsize':(13,10)}) 

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

#df_diamonds.info()

df_diamonds.groupby('cut').sum().plot.pie(y='price', autopct="%.1f%%", ylabel="", legend=False, figsize=(10,10))