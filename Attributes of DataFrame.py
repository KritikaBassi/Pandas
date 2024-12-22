#Attributes of DataFrame
import pandas as pd
d1={'Rollno.':[1,2,3,4],'Name':['ASHA','NISHA','RAGHAV','SURESH'],'Marks 1':[30,29,25,21],'Marks 2':[28,27,26,24]}
df=pd.DataFrame(d1)
print(df)
print()

#Index
print('Index:')
print(df.index)
print()
df.index=['a','b','c','d']
print(df)
print()
#Boolen index
df.index=[True,False,True,True]
print(df)
print()

#Column Names
print('Column Names:')
print(df.columns)
print()

#Axis:To display names of columns and rows
print('Axis:')
print(df.axes)
print()

#Datatype of each Column
print('Datatype:')
print(df.dtypes)
print()

#Size:To display number of elements
print('Size:')
print(df.size)
print()

#Shape
print('Shape:')
print(df.shape)
print()

#Dimention
print('Dimention:')
print(df.ndim)
print()

#To check for any empty value
print(df.empty)
print()

#To check each value whether it is empty or not
print(df.isna())
print()

#Traspose:To change the rows to columns and columns to rows
print('Transpose:')
print(df.T)
print()

#Count
print('Count:')
print(df.count())#default is 0
print()
print(df.count(1))#1 represents the columns
print()
print(df.count(0))#0 represents the rows


