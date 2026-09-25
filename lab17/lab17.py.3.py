#check number is prime or not
N=int(input("enter number"))
if N<2:
    print("not prime")
else:
    prime=True
for i in range(2,N):
    if N%i==0:
        prime=False
    break
    if prime :
        print("prime")
else:
    print("not prime")



