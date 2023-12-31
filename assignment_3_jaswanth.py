# -*- coding: utf-8 -*-
"""Assignment_3_Jaswanth.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VJ7dgDJUikaum1QNkXlXGdUPBwH3nmkT

## Loading The Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/penguins_size.csv')

df.head()

df.shape

"""## Checking NULL Values"""

df.isnull().any()

df.isnull().sum()

"""## Dealing With NULL Values"""

df.culmen_length_mm.median()

df.culmen_depth_mm.median()

df.flipper_length_mm.median()

df.body_mass_g.median()

df.sex.mode()

##Dealing with NULL values

## Below features are type of float therefore we will deal the NULL values with median
df['culmen_length_mm'].fillna(df['culmen_length_mm'].median(),inplace=True)
df['culmen_depth_mm'].fillna(df['culmen_depth_mm'].median(),inplace=True)
df['flipper_length_mm'].fillna(df['flipper_length_mm'].median(),inplace=True)
df['body_mass_g'].fillna(df['body_mass_g'].median(),inplace=True)

## Below one is object type therefore we will deal the NULL values with mode
df['sex'].fillna('MALE',inplace=True)

df.head()

df.isnull().any()

df.isnull().sum()

"""## Descriptive Analysis"""

df.info()

df.describe()

"""#### Univariate, Bi-Variate, and Multi-Variate Analysis

## 1.Univariate
"""

sns.distplot(df.culmen_length_mm)

sns.distplot(df.culmen_depth_mm)

sns.distplot(df.flipper_length_mm)

sns.distplot(df.body_mass_g)

plt.boxplot(df.culmen_length_mm)

plt.boxplot(df.culmen_depth_mm)

plt.boxplot(df.flipper_length_mm)

plt.boxplot(df.body_mass_g)

"""## 2. Bi-Variate Analysis"""

sns.lineplot(x=df.culmen_length_mm,y=df.culmen_depth_mm)

sns.scatterplot(x=df.culmen_length_mm,y=df.culmen_depth_mm)

sns.barplot(x=df.culmen_length_mm,y=df.culmen_depth_mm)

"""## 3. Multi-Variate Analysis"""

sns.pairplot(df)

"""## Co-Relation"""

sns.heatmap(df.corr(),annot=True)

df.corr().flipper_length_mm.sort_values(ascending=False)

"""## Performing Encoding"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df.info()

df.head()

df.species = le.fit_transform(df.species)
df.island = le.fit_transform(df.island)
df.sex = le.fit_transform(df.sex)

df.head()

"""## Splitting Data into Independent And Dependent Datas"""

y = df.species
X = df.drop(columns=['species'],axis=1)

y.head()

X.head()

"""## Scaling Data"""

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()

X_scaled = pd.DataFrame(scale.fit_transform(X),columns=X.columns)

X_scaled.head()

"""## Splitting The Data Into Training And Testing"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.3,random_state=2)

"""#### Checking The Shape Of Splitted Training And Testing Dataset"""

X_train.shape

X_test.shape

y_train.shape

y_test.shape