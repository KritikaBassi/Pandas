#Deleting elements from a Series
import pandas as pd
s=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(s)
print("Deleting element:")
print(s.drop("b"))
#print(s.drop[1]) this will not work as drop works only with the assigned index

