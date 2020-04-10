import pandas as pd
import numpy as np
df1= pd.read_excel('delhi air 1996 to 2015.xls')
df2= pd.read_excel('delhi weather since 1997.xlsx') 

df3= pd.merge(df1, df2, how='inner', on=['month','year'])
df3.fillna(df3.mean(), inplace= True)

df3=df3.drop('PM 2.5', axis=1)

X= df3.iloc[ : ,1:5 ]
y=df3.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(X_train, y_train)
#rpedictionn
y_pred = regressor.predict(X_test)


#backward elimination
import statsmodels.api as sm
X=  np.append(arr = np.ones( (217,1)).astype(int  ) ,  values= X, axis = 1)

X_opt= X[:,[0,1,2,3,4]]

regressor_OLS= sm.OLS(endog= y, exog= X_opt).fit() 
regressor_OLS.summary()  
#remove one with highestt p value
X_opt= X[:,[0,1,2,3]]

regressor_OLS= sm.OLS(endog= y, exog= X_opt).fit() 
regressor_OLS.summary()  

#all p values  are <0.05, delete none
X= df3.iloc[ : ,1:4 ]
y=df3.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
regressor= LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

#### to tell r square-> 0.22, adjusteed r-sq-> 0.210
X=  np.append(arr = np.ones( (217,1)).astype(int  ) ,  values= X, axis = 1)
X_opt= X[:,[0,1,2,3]]
regressor_OLS= sm.OLS(endog= y, exog= X_opt).fit() 
regressor_OLS.summary()

### this result can be explained as th edata had more than 50% null values 