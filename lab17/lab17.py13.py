k=int(input("enter a no. how much times it repeated:"))
L=[2,2,4,4,4,4,5,5,6,6,6,7,8,8,8,8]
duplicates=[]
for i in L:
    if L.count(i) > k and i not in duplicates:
        duplicates.append(i)
print("duplicate:",duplicates)
