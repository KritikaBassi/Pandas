#Series with range and for loop
import pandas as pd
S1=pd.Series(range(1,10,2),index=(x for x in 'abcde'))
print(S1)

print()
#OR

l=range(1,10,2)
ind=(x for x in 'abcde')
S2=pd.Series(l,index=ind)
print(S2)
