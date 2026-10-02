#lists and loops
#1

a=[i for i in range(1,51)]
sum = 0
for i in a:
    sum = sum + i
print(sum)
#2
#define another list b containing prime number 1 to 50

b=[i for i in range(2,51)
       if all(i % j !=0 for j in range(2 ,i))]
print(b)
#3
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)




