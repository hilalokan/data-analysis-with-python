'''
A jointplot comprises of 2 histograms of the given variables and 1 scatterplot representing their correlation, by default.

By modifying the parameters, one can also use KDE plot instead of a scatterplot as well.
'''

#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size
sns.set(rc={'figure.figsize':(13,10)})

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

sns.jointplot(x = "price", y="carat", data=df_diamonds)

