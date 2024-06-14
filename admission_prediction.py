# -*- coding: utf-8 -*-
"""admission prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IHGiH29NApgsWkN2mY7oAs8IbTwJD03W
"""

import pandas as pd

adm = pd.read_csv('path to dataset.csv')

adm.head()

adm.info()

adm.describe()

adm.columns

y = adm['Chance of Admit ']

x=adm[['Serial No', 'GRE Score', 'TOEFL Score', 'University Rating', ' SOP',
       'LOR ', 'CGPA', 'Research']]
x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred

from sklearn.metrics import mean_absolute_percentage_error
mean_absolute_percentage_error(y_test,y_pred)

