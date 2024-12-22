#Series using numpy array and arange
#Array is use to apply mathematical functions
import pandas as pd
import numpy as np
a1=np.array([1,2,3,4,5])
s1=pd.Series(a1+10)
s2=pd.Series(a1*10)
print(s1)
print()
print(s2)

a2=np.arange(10,16,2)
s3=pd.Series(a2)
print(s3)
s4=pd.Series(a2+2)
print(s4)
s5=pd.Series(a2*10)
print(s5)
