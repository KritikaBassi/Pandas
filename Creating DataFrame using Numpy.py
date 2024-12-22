#Creating DataFrame using Numpy
import pandas as pd
import numpy as np
a=np.array([[1,2,3,4],[20,30,40,50]])#Two Rows
df=pd.DataFrame(a)
print(df)
print()

b=np.array([[1,20],[2,30],[3,40],[4,50]])#Two Columns
df1=pd.DataFrame(b)
print(df1)
print()

#Giving index and column names
c=np.array([[1,20],[2,30],[3,40],[4,50]])
df2=pd.DataFrame(c,index=[1,2,3,4],columns=['Roll No.','Marks'])
print(df2)
