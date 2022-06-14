#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size 
sns.set(rc={'figure.figsize':(13,10)}) 

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

'''
sns.histplot(df_diamonds["price"],
             kde=True) #kde=Kernel Density Estimation #bins="auto"
'''


#sns.histplot(df_diamonds["price"], bins=100, kde=True)

#sns.histplot(df_diamonds["price"]) #the line is not visible, kde is set to False by default


sns.kdeplot(df_diamonds["price"]) #displays only the line depicting the density