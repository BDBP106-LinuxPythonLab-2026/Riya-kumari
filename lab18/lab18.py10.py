n = int(input("Enter number:"))
def nexprime(n):
    n=n+1

     while True:
         for 1 in range(2,n):
             if n % 1==0:
                 break
         else:
             return n

         n= n + 1
print(f"First prime number larger than {n} is", nextprime(n))



