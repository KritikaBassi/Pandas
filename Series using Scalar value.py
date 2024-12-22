#Series using Scalar value
import pandas as pd
S1=pd.Series(66,index=[100,200,300])
#Index is mandatory
print(S1)

print()
#OR

S2=pd.Series(66,index=range(1,10,3))
print(S2)
