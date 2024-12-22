#Notebook work III
import pandas as pd
import numpy as np
print('From list')
l1=['Anastasia',12.5,1,'yes']
l2=['Dima',9.0,3,'no']
l3=['Katherine',16.5,2,'yes']
l4=['James',np.NaN,3,'no']
l5=['Emily',9.0,2,'no']
df=pd.DataFrame([l1,l2,l3,l4,l5],columns=['Name','Score','Attempts','Qualify'])
print(df)
print()
print('From dictionary')
d={'Name':['Anastasia','Dima','Katherine','James','Emily'],'Score':[12.5,9.0,16.5,np.NaN,9.0],'Attempts':[1,3,2,3,2],'Qualify':['yes','no','yes','no','no']}
df1=pd.DataFrame(d)
print(df1)
print()
print('From Series')
n=pd.Series(['Anastasia','Dima','Katherine','James','Emily'])
s=pd.Series([12.5,9.0,16.5,np.NaN,9.0])
a=pd.Series([1,3,2,3,2])
q=pd.Series(['yes','no','yes','no','no'])
df2=pd.DataFrame({'Name':n,'Score':s,'Attempts':a,'Qualify':q})
print(df2)
print()
print('From list of dictionary')
l=[{'Name':'Anastasia','Score':12.5,'Attempts':1,'Qualify':'yes'},{'Name':'Dima','Score':9.0,'Attempts':3,'Qualify':'no'},{'Name':'Katherine','Score':16.5,'Attempts':2,'Qualify':'yes'},{'Name':'James','Score':np.NaN,'Attempts':3,'Qualify':'no'},{'Name':'Emily','Score':9.0,'Attempts':2,'Qualify':'no'}]
df3=pd.DataFrame(l)
print(df3)
                  
            
