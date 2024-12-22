#DataFrame Notebook work IV
import pandas as pd
l1=['Scott','Manager',90000,'2010-10-01','Accounts']
l2=['Tom','Clerk',34000,'2010-01-04','Admin']
l3=['Joy','Clerk',32000,'2009-03-01','Admin']
l4=['Sam','Salesman',40000,'2004-04-01','Sales']
l5=['Martin','Manager',85000,'2008-08-05','Sales']
l6=['Michel','Salesman',43000,'2008-08-06','Sales']
l7=['Francis','Clerk',30000,'2009-10-10','Accounts']

emp=pd.DataFrame([l1,l2,l3,l4,l5,l6,l7],index=[1001,1002,1003,1004,1005,1006,1007],columns=['Ename','Job','Salary','Dojoin','Department'])
print(emp)
'''
print()
emp.insert(2,'City',['Noida','Noida','Noida','Noida','Noida','Noida','Noida'])
print(emp)
print()
emp.loc[1008]=['Robin','Analyst','Delhi',9000,'2011-04-01','Admin']
print(emp)
print()
emp.loc[emp['Ename']=='Francis','Salary']=35000
print(emp)
print()
print(emp.loc[(emp['Department']=='Sales')|(emp['Department']=='Accounts')]) 
print()
print(emp.loc[(emp['Salary']>30000)&(emp['Salary']<50000),['Ename','Job','Salary']])
print()
del emp['Dojoin']
print(emp)
print()
print(emp[['Ename','Job','Salary']])
'''
