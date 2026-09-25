element=int(input("enter a element you would like to find and remove:"))
L=[1,2,3,4,5,6,7,5,6,4,3,]
while element in L:
    L.remove(element)
print(L)