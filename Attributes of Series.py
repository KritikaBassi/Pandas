#Attributes of Series 
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)
print()

a=s.index
print("Index:",a)
print()

a1=s.index=['a','b','c','d','e']
print(s)
print()

V=s.values
print("Values:",V)
print()

s.name="information"
s.index.name='Marks'
print(s)
print()

b=s.dtype
print("Datatype",b)
print()

c=s.nbytes
print("Bytes",c)
print()

d=s.empty
print("Is the series Empty:",d)
print()

e=s.size
print("Size=",e)
print()

f=s.shape
print('Shape=',f)
print()

#Accessing elements
print(s['b'])
print()
print(s[['b','d','e']])
print()
print(s[0])
print()
print(s[0:4])
print()
print(s['a':'c'])
#here c will also get printed as this is a label and not a number index
print()
print(s.iloc[1:3])
#iloc is integer location
print()
print(s.loc['b':'d'])
#loc is label location
print()
print("Head:",s.head(2))
#It prints first two elements
print()
print("Tail:",s.tail(4))
#It prints 4 elements from the end



