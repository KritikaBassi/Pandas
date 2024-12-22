#Creating DataFrame using list of dictionary
import pandas as pd
l1=[{'Name':'Shreya','Age':20},{'Name':'Rakshit','Age':22},{'Name':'Srijan','Age':18}]
df=pd.DataFrame(l1,index=['R1','R2','R3'])
print(df)
