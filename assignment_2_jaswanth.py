# -*- coding: utf-8 -*-
"""Assignment_2_Jaswanth.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q8odyF83586d3-lQxgRbAVCFovY24PAa
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

"""**Load The Data**"""

df = pd.read_csv('/content/House Price India.csv')

df.head()

df.shape

"""**Checking Null Values**"""

df.isnull().any()

df.isnull().sum()

"""**Descriptive statistics on the dataset.**"""

df.info()

df.describe()

"""**Univariate Analysis**"""

df.plot()

sns.distplot(df['number of floors'])

sns.displot(df['number of floors'])

df['number of floors'].value_counts()

plt.pie(df['number of floors'].value_counts(),[0,0.2,0.2,0.2,0.2,0.2],labels=['1','2','1.5','3','2.5','3.5'],autopct="%1.1f%%")
plt.title("Number Of Floors")
plt.show()

sns.barplot(x=df['number of floors'].value_counts().index,y=df['number of floors'].value_counts())

plt.boxplot(df['number of floors'])

"""**Bivariate Analysis**"""

sns.jointplot(x = 'number of floors',y = 'condition of the house',data = df)

sns.lineplot(x=df['number of floors'],y=df['condition of the house'])

sns.scatterplot(x=df['number of floors'],y=df['condition of the house'])

sns.barplot(x=df['number of floors'],y=df['condition of the house'])

"""**Multivariate Analysis**"""

sns.pairplot(df)

sns.heatmap(df.corr())