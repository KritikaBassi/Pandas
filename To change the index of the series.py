#To change the index of the series
import pandas as pd
L=[10,20,30,40]
ind=["Rollno 1","Rollno 2","Rollno 3","Rollno 4"]
S1=pd.Series(L,index=ind)
print(S1)

print()

#OR
S2=pd.Series([10,20,30,40],index=["Rollno 1","Rollno 2","Rollno 3","Rollno 4"])
print(S2)

print()

#OR
S3=pd.Series([10,20,30,40],index=["Rollno 1","Rollno 2",3,"Rollno 4"])
print(S3)
#It is not necessary to make index list homogeneous
