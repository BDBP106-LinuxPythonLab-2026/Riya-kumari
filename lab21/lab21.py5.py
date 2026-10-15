#find the sum of all the elements in a list using lamda and reduce
from functools import reduce
number= [10,20,30,40,50]
total=reduce(lambda a,b:a+b,number)
print("sum:",total)