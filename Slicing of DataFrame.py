#Slicing of DataFrame
import pandas as pd
df=pd.DataFrame([[1,76],[2,57],[3,89]],index=[1,2,3],columns=['RollNo.','Marks'])
print(df)
print(df['Marks'])
print(df[['RollNo.','Marks']])
print(df.iloc[1])
print(df.iloc[[1,2]])
print(df.loc[[1,2]])
print(df.iloc[1:3,0:1])#first slicing is for rows and next is for columns
