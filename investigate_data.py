#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size -> 
sns.set(rc={'figure.figsize':(13,10)})

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")
print(df_diamonds.head()) #by default, displays the first 5 rows of a dataset

print(df_diamonds.info()) #info method prints the information of dtype and columns,non-null values and memory usage of DataFrame

print(df_diamonds.columns) #prints the name of the columns

print(df_diamonds["cut"].unique())

print(df_diamonds["cut"].value_counts()) #returns the frequency of a value in a series object

print(df_diamonds["cut"]) #prints the information stored in a column