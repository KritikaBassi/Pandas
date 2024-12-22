#To convert list into series
import pandas as pd
L=[10,20,30,40]
S1=pd.Series(L)
print(S1)

print()#For leaving a blank line
#OR
S2=pd.Series([10,20,30,40])
print(S2)

print()
#OR
S3=pd.Series(['a','b','c','d'])
print(S3)

