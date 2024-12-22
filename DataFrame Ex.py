import pandas as pd
l1=[2017,2018,2019,2020]
l2=[32,33,35,34]
l3=[20,22,21,23]
l4=[123,140,135,160]
Climate=pd.DataFrame({'Year':l1,'MaxTemp':l2,'MinTemp':l3,'Rainfall':l4})
#print(Climate)

print(Climate.iloc[1:3])
print(Climate.iloc[1:3,1:2])

print(Climate[['MaxTemp','Rainfall']][1:3])

print(Climate["MaxTemp"]-Climate["MinTemp"])

print(Climate.head(2))

print(Climate.count())
print(Climate.count(0))
print(Climate.count)
print(Climate.count(axis='index'))
'''
print(Climate.tail(2))

print(Climate.head())
'''
