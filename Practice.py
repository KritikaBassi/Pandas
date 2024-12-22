import pandas as pd
d1={'Name':['ANKIT','AMIT','AISHWARYA','PRIYANKA','PRIYA','SREYA'],'Age':[21,19,20,18,17,21],
    'Stream':['MATH','COMMERCE','SCIENCE','MATH','MATH','SCIENCE'],'Percentage':[88,92,95,70,65,78]}
Report=pd.DataFrame(d1)
print(Report)
print()
'''
#(i)Display the details of students whose percentage is greater than 80
print(Report[Report.Percentage>80])
print()
#Or
print(Report[Report['Percentage']>80])
print()
#(ii) Display Science stream students
print(Report[Report['Stream']=='SCIENCE'])
print()
#(iii)Display the details of students who age is between 15 and 20
print(Report[(Report['Age']>15) & (Report['Age']<20)])
print()
#(iv)Display the details of students who are either in Science or Commerce stream
print(Report[(Report.Stream=='SCIENCE') | (Report.Stream=='COMMERCE')])
print()
#(v)Display the details of students whose percentage is not equal to 95
print(Report[Report['Percentage']!=95])
print()
#(vi)Display student name and percentage
print(Report.iloc[:,::3])
print()
#OR
print(Report[["Name",'Percentage']])
print()
#(vii)Display the details of students who are in Math stream and percentage greater than 80
print(Report[(Report['Stream']=='MATH') & (Report['Percentage']>80)])
print()
#(viii)Increase the percentage of Math stream students by 2
#*** Need to understand
Report.loc[Report.Stream=='MATH','Percentage']+=2
print(Report)
print()
#(ix)Display Name and Age of Math students
print(Report[['Name','Age']][Report['Stream']=='MATH'])
print()
#(x)Delete the columns ‘Age’ & ‘Stream'
print(Report.drop(['Age','Stream'],axis=1))
print()
#(xi)Delete the details of ‘Priyanka’
print(Report.drop(3,axis=0))
print()
#(xii)Insert a new column ‘Grade’
Report['Grade']=['A1','A2','B1','A2','A1','B1']
print(Report)
print()
#(xiii) Insert a new column ‘Gender’ after ‘Age’
Report.insert(2,'Gender',['M','M','F','F','F','F'])
print(Report)
print()
#(xiv) Insert a new row
Report.loc[6]=['SHYAM',19,'COMMERCE',85]
print(Report)
print()
#OR
new={'Name':'SHYAM','Age':19,'Stream':'COMMERCE','Percentage':85}
s=pd.Series(new,name=6)
Report=Report.append(s)
print(Report)
'''
#(xv)Change the index to 111,222,333,444,555,666
Report.index=[111,222,333,444,555,666]
print(Report)
