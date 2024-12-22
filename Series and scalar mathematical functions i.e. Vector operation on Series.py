#Series and scalar mathematical functions
import pandas as pd
ind=['a','b','c','d','e']
s=pd.Series([10,20,30,40,50],index=ind)
print(s)
print(s*2)
print(s+10)
print(s>30)#To check whether number is greater than 30
print(s[s>30])#To print the numbers greater than 30
