# -*- coding: utf-8 -*-
import pandas as pd
import data_preprocessing2 as pre


df1=pd.read_csv('delhi_weather_since_1997.csv', header=0)
df1=df1.drop(df1.columns[[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19]],1)

#pre processing
df1= pre.data_change(df1)
df1=pre.data_change3(df1)
df1=pre.data_change2(df1)


#transferring data to excel
df1.to_excel("delhi weather since 1997.xlsx")

