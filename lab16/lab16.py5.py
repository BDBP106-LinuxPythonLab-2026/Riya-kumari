import math
a=float(input("enter coefficient a"))
b=float(input("enter coefficient b "))
c=float(input("enter coefficient c"))

if a==0:
   print("this is not a quadratic equation.")
else:
    d= b**2 - 4*a*c

    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = ( -b - math.sqrt(d)) / (2*a)

    print("Root 1 =", root1)
    print("Root 2 =", root2)
    