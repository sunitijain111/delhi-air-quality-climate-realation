import pandas as pd
import data_preprocessing as pre

i=0;
df=[]
s= "delhi air "
year= 1996
ext= ".xls"

while year<= 2002:
    if year==2010:
        year+=1
        continue
    df1= pd.read_excel(s+str(year)+ext)
    df1= pre.data_change(df1,year)
    df= df+[df1]
    year+=1

while year<= 2015:
    if year==2010:
        year+=1
        continue
    df1= pd.read_excel(s+str(year)+ext)
    df1= pre.data_change_2(df1,year)
    df= df+[df1]
    year+=1
    
df[6]=df[6].drop(df[6].index[0]) #extra row of annual

#appending data frames
df1= pre.append(df)
df1=df1.reset_index()

df1.to_excel("delhi air 1996 to 2015.xls")