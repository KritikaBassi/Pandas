#To perform Mathematical operations on two Series
import pandas as pd
ind=['a','b','c','d','e']
s1=pd.Series([10,20,30,40,50],index=ind)
print(s1)
s2=pd.Series([1,2,3,4,5],index=ind)
print(s2)
a=s1+s2
b=s1-s2
c=s1*s2
d=s1/s2
e=s1**s2
print("Sum:")
print(a)
print("Difference:")
print(b)
print("Multiple:")
print(c)
print("Division:")
print(d)
print("Exponent")
print(e)
#Here the index of two Series should be same

