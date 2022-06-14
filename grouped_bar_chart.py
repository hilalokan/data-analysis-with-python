#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size 
sns.set(rc={'figure.figsize':(13,10)})

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

sns.barplot(x = "cut",
            y = "price",
            hue = "color", #hue opens a small table and enters the desired values ​​in it
            data = df_diamonds).set_title("Cut - Price - Color")
'''
sns.barplot(x="cut",
            y="price",
            hue="clarity",
            data = df_diamonds)
plt.title("Cut - Price - Clarity")

'''

