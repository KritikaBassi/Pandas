#Creating DataFrame using Series
import pandas as pd

n1=pd.Series(['Shreya','Rakshit','Srijan'])
a1=pd.Series([20,22,18])
df1=pd.DataFrame({'Name':n1,'Age':a1})
print(df1)
print()

#To give index to the dataframe
n2=pd.Series(['Shreya','Rakshit','Srijan'],index=['R1','R2','R3'])
a2=pd.Series([20,22,18],index=['R1','R2','R3'])
df2=pd.DataFrame({'Name':n2,'Age':a2},index=['R1','R2','R3'])
print(df2)
