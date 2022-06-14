#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import CategoricalDtype

#setting the plot size ->
sns.set(rc={'figure.figsize':(13,10)})

#Load Diamonds Dataset from seaborn library
df_diamonds = sns.load_dataset("diamonds")

'''
sns.kdeplot(df_diamonds["price"], shade = True) #With shade=True, one can fill the space staying under the line
'''

#investigate which value of a choosen categorical column affects by how the distribution

(sns
 .FacetGrid(df_diamonds,
            hue="cut", 
            height=5,
            xlim = (0, 10000))
.map(sns.kdeplot, "price", shade=True)
.add_legend())
plt.title('Cut - Price')
             