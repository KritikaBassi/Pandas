#Operations on DataFrame
import pandas as pd
d1={'Rollno.':[1,2,3,4],'Name':['ASHA','NISHA','RAGHAV','SURESH'],'Marks 1':[30,29,25,21],'Marks 2':[28,27,26,24]}
df=pd.DataFrame(d1)
print(df)
print()
'''
#Selecting column from dataframe

print(df['Name'])
print()
print(df.Name)
print()
print(df[['Rollno.','Name']])
print()
print(df.iloc[:,0:3])#first is for rows and second one is for columns

#Adding column to dataframe
df['Marks 3']=[27,26,25,22]
print(df)
print()
df.insert(3,'New Marks',[100,200,300,400])
print(df)

#Sum of Columns
df['Total Marks']=df['Marks 1']+df['Marks 2']+df['Marks 3']+df['New Marks']
print(df)

#Modifing the values
df['Marks 1']=[11,11,11,11]
print(df)

#Renaming column
df.rename(columns={'Marks 1':'M1','Marks 2':'M2'},inplace=True)
print(df)

#Deleting column
del df['Marks 1']
print(df)
print()
df.pop('Marks 2')
print(df)
print()
#Axis has two values 0 and 1 where 0 (default) for row and 1 is for column
df.drop('Name',axis=1,inplace=True)
print(df)

#Adding Row in a DataFrame
df.loc[4]=[5,'SHINY',23,27]
print(df)
print()
df.loc[8]=[9,'ABC',99,99]
print(df)

#Displaying a row
print(df.loc[1])

#Changing the values in a row
df.loc[1]=[2,'DIYA',300,300]
print(df)

#Modify values in row / Show selected rows
print(df.loc[df['Name']=='NISHA'])
print()
print(df.loc[df['Marks 1']>25])
print()
print(df.loc[df['Marks 1']>25,['Name','Rollno.']])
print()
#SYNTAX:print(df.loc[condition,list of columns])
print(df.loc[(df['Marks 1']>25)&(df['Marks 1']<30)])
print()
#SYNTAX:print(df.loc[(condition1)&(condition2),[list of columns]])
#& is for AND , | is for OR
print(df.loc[(df['Marks 1']>20)&(df['Marks 1']<30),['Name','Rollno.']])
print()
#SYNTAX:print(df.loc[condition,column]=value
df.loc[df['Name']=='NISHA','Marks 1']=100
print(df)

#Deleting row in DataFrame
df.drop(0,inplace=True)
print(df)
print()
df.drop([1,3],inplace=True)
print(df)

#Sorting Data in DataFrame
#default is ascending order
print(df.sort_values('Marks 1'))#OR print(df.sort_values('Marks 1',ascending=True))
print(df.sort_values('Marks 1',ascending=False))
print(df.sort_values(['Marks 1','Marks 2']))#first column is only cosidered
#Error:print([df.sort_values('Marks 1')] & [df.sort_values('Marks 2',ascending=False)])

#Append rows in a DataFrame
df1=pd.DataFrame([[5,'SUNIL',21,25],[6,'SHIKHA',32,21]],index=[4,5],columns=['Rollno.','Name','Marks 1','Marks 2'])
df=df.append(df1)
print(df)

#Boolen Indexing
df.index=[True,False,True,True,False,True]
print(df)
print()
print(df.loc[True])
'''
#Iteration:functions used are iterrows(for rows) iteritems(for columns)
for(row,RowSeries) in df.iterrows():
    print('Row index:',row)
    print('Row Series')
    print(RowSeries)
print()
for(col,colSeries)in df.iteritems():
    print('Column Index:',col)
    print('Column Series:')
    print(colSeries)
df.index=[True,False,True,True]
print(df)
print()
