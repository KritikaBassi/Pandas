#Series using range() function
import pandas as pd
S1=pd.Series(range(1,10,2))
print(S1)

print()
#OR

S2=pd.Series(range(1,10,2),index=range(100,150,10))
print(S2)

print()
#OR

l=range(1,10,2)
ind=range(100,150,10)
S3=pd.Series(l,index=ind)
print(S3)
