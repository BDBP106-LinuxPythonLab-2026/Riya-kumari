#duplicate element in a list
L=(1,2,2,3,4,5,5,6,6,7,8)
for x in L :
    if L.count(x) > 1:
        print(x)
