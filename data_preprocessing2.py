# -*- coding: utf-8 -*-
import pandas as pd

#separating data based on year and month
def data_change(df1):
    def month(row):
        s= (row['datetime_utc'])
        s=s[4:6]
        s.strip()
        return s
    def year(row):
        s=(row['datetime_utc'])
        s=s[0:4]
        s.strip()
        return s
    def Year(row):
        s=(row['datetime_utc'])
        s=s[0:4]
        s.strip()
        return s
    df1['month']= df1.apply(month, axis=1)      
    df1['year']= df1.apply(year, axis=1)
    df1['Year']=df1.apply(Year, axis=1)
    df1=df1.drop('datetime_utc',1)
    return df1

#grouping temp based on year and month
def data_change2(df1):
    df1= df1.groupby(['year','month'])[' _tempm'].mean()
    return df1

#translating month number into month name
def data_change3(df1):
    def month(row):
        arr_month=['January','February','March','April','May','June','July','August','September','October','November','December']
        s=(row['month'])
        s=int(s)
        return arr_month[s-1]
    df1['month']=df1.apply(month , axis=1)
    return df1
        
