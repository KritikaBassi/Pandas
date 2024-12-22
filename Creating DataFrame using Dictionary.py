#Creating DataFrame using dictionary
import pandas as pd
d={'Name':['Shreya','Rakshit','Srijan'],'Age':[20,22,18]}
df=pd.DataFrame(d,index=['R1','R2','R3'])
print(df)
