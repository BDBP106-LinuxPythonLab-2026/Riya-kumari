n=int(input("enter the number"))
total=0
while n > 0:
     digit = n % 10
     total += digit
     n= (n // 10 )

     print("sum of digits =", total )

