#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size 
sns.set(rc={'figure.figsize':(13,10)})

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

cols = ["x", "y", "z"]

for col in cols:
    plt.figure(figsize=(10,10))
    sns.scatterplot(x=col, y="price", data=df_diamonds)
    plt.show()