#Creating DataFrame using list
import pandas as pd
l=[1,2,3,4]

df1=pd.DataFrame(l)
print(df1)
#0 is the column label
print()

df2=pd.DataFrame(l,index=['a','b','c','d'])
print(df2)
print()

df3=pd.DataFrame(l,index=['a','b','c','d'],columns=['Roll no.'])
print(df3)
print()

l1=['Shreya',20]
l2=['Rakshit',22]
l3=["Srijan",18]

df4=pd.DataFrame([l1,l2,l3],index=['R1','R2','R3'],columns=['Name','Age'])
print(df4)

