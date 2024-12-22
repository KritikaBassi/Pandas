import pandas as pd
d={'Company':['Hyundai','Bmw','Honda','Tata','Toyota','Mahindra'],
   'Bodystyle':['Sedan','Sedan','Sedan','Sedan','Hatchback','SUV'],
   'domanu':['2000-10-01','1998-01-04','1999-03-01','2000-04-01','1998-08-05','2000-03-10'],
   'Price':[25783,30172,20679,24458,18549,50000]}
auto=pd.DataFrame(d,index=[1001,1002,1003,1004,1005,1006])
print(auto)
print()

print('(a)')
auto['Cyinders']=[4,6,4,4,4,6]
print(auto)
print()

print('(b)')
auto.loc[1007]=['Maruti','Hatchback','1999-06-12',10873,4]
print(auto)
print()

print('(c)')
auto.loc[auto["Company"]=='Bmw','Price']=39085
print(auto)
print()

print('(d)')
print(auto[(auto.Company=='Tata') | (auto.Company=='Honda')])
print()

print('(e)')
print(auto.loc[(auto['Price']>20000) & (auto['Price']<27000),['Company']])
print()

print('(f)')
del auto['domanu']
print(auto)
print()

print('(g)')
print(auto[['Company','Bodystyle']])
                                    

