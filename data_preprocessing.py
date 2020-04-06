import pandas as pd
def data_change(df2,year):
    def month(row):
        s= (row['Sampling Date'])
        z=int(0)  
        for z in range( len(s))        :
            if s[z]==" ":
                break;
        s= s[0:z]  
        s.strip()
        return s
       
    df2['Sampling Date'] = df2.apply(month, axis= 1)
    df2= df2.drop(df2.columns[[0,2,3,4,5]],1)
    df2['month']= df2['Sampling Date']
    df2= df2.drop('Sampling Date',1)        
    df2= df2.groupby(['month']).mean()
    df2['year']=year
    return df2
array_month=['January','February','March','April','May','June','July','August','September','October','November','December']
def data_change_2(df2,year):
    def month(row):
        s= (row['Sampling Date'])
        z=int(0)  
        for z in range( len(s))        :
            if s[z]=="-" or s[z]=='/':
                break;
        s= s[z+1:]  
        a=s[0]
        b=s[1]
        c =0 
        if not (b=='-' or b=='/'):
            c=int(a)*10+int(b)
        else:
            c=int(a)
        s= array_month[c-1]    
        s.strip()
        return s
       
    df2['month'] = df2.apply(month, axis= 1)
    df2= df2.drop(df2.columns[[0,1,2,3,4]],1)
    df2= df2.groupby(['month']).mean()
    df2['year']=year
    return df2
"""
df3= pd.read_excel("delhi air 2005.xls")
print(df3.tail())
print(list(df3.columns))
df3= data_change_2(df3, 2005)
"""

def append(df):
    df1= df[0]
    for i in range(1,len(df)):
        df1=df1.append(df[i])
    return df1    