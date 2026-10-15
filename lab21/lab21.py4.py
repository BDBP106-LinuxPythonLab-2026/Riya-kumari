#odd element of fibonacci series for the first n terms
n=int(input("enter the number of terms:"))
fib = [0,1]
for i in range(2,n):
    fib.append(fib[i-1]+ fib[i-2])
fib =fib[:n]
odd =list(filter(lambda x:x%2!=0,fib))
print("fibonacci series:",fib)
print("odd elements:",odd)
