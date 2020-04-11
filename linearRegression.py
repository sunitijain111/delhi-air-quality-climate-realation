# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#reading dataset
df1= pd.read_excel('delhi air 1996 to 2015.xls')
df2= pd.read_excel('delhi weather since 1997.xlsx') 
df3= pd.merge(df1, df2, how='inner', on=['month','year'])
df3.fillna(df3.mean(), inplace= True)
df3=df3.drop('PM 2.5', axis=1)


#plot the data
df3.plot(x='NO2', y='temp', style='o')  
plt.title('NO2 vs temp')  
plt.xlabel('NO2 LEVEL')  
plt.ylabel('temperature')  
plt.show()

#storing mintemp and maxtemp on x and y axis resp
X = df3['NO2'].values.reshape(-1,1)
y = df3['temp'].values.reshape(-1,1)

#slpitting data into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#training algo 
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

#predicting on test set
y_pred = regressor.predict(X_test)

#displaying actual and predicted values
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df

#plotting straight line
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

#evaluating error
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))