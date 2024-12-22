import pandas as pd
list1=[1,2,3,4,5,6,7,8]
list2=['swimming','tt','skating','kho kho','bb','chess','football','cricket']
school=pd.Series(list1,index=list2)
school.name=('little')
print(school*2)
print(school.tail(3))
print(school['tt'])
print(school[2:4])
