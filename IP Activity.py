import pandas as pd
import numpy as np
#print("Table:Employee")
print()
l1=['KAVYA','F','SALESMAN','2018-02-08',60000,'012','DELHI']
l2=['HIMANSHU','M','CLERK','2012-09-03',50000,'032','NOIDA']
l3=['ANVI','F','CLERK','2017-07-02',45000,'012','GURGAON']
l4=['RAHUL','M','MANAGER','2011-12-04',92000,'032','MEERUT']
l5=['MITANSHI','F','ANALYST','2013-05-16',75000,'077','NOIDA']
l6=['YASHASVI','F','SALESMAN','2015-04-21',50000,'032','DELHI']
l7=['DEEPAK','M','MANAGER','2011-12-01',88000,'012','MEERUT']
l8=['NITISH','M','SOFTWARE ENGINEER','2014-08-26',76000,'032','HAPUR']
l9=['POONAM','F','CLERK','2015-09-14',65000,'077','GURGAON']
l10=['AAYUSH','M','SOFTWARE ENGINEER','2013-08-10',50000,'012','HAPUR']

df=pd.DataFrame([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10],index=['I01','I02','I03','I04','I05','I06','I07','I08','I09','I10']
                ,columns=['EMPLOYEE NAME','SEX','JOB','DATE OF JOINING','SALARY','DEPT CODE','CITY'])
pd.set_option('display.width',None)
'''
print(df)
print()
print(df.axes)
print()
print(df.columns)
print()
print(df.index)
print()
print(df.ndim)
print()
print('Size')
print(df.size)
print()
print(df.shape)
print()
print(df.T)
print()
print('Count')
print(df.count(0))
print()
print(df.count(1))
print()
print(df.head())
print()
print(df.isna())
print()
print(df.columns[:1])
print()
df.drop(['I01','I02','I10'],inplace=True)
print(df)
df.loc['I11']=['KIARA','F','CLERK','2021-08-10',68000,'042']
print(df)
print()
print(df[:-8])
print()
print(df[1:4:4])
print()
print(df[0:1])
print()
print(df[-9:])
'''

print(df.set_index('EMPLOYEE NAME',inplace=True))

'''
print()
df.reset_index
print(df)

print(df.iloc[1:8:2])

print(df[:2:-1]) 
'''
