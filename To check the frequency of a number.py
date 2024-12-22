l=[1,2,3,4,2,5,3,4,6,3]
n=int(input("Enter the number:"))
if n in l:
    a=l.count(n)
    print("Frequency:",a)
else:
    print("Number not found")

