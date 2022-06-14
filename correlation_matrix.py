#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size -> 
sns.set(rc={'figure.figsize':(13,10)}) 

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

plt.title("Correlation Matrix")

sns.heatmap(df_diamonds.corr(), annot= True) #heatmap() from sns library is used to plot the correlation matrix
