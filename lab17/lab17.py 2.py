#computer power raise the base to n-th power (2,5)
base=int(input("enter base:"))
n=int(input("enter power:"))
result=1
for i in range(n):
    result = result+base
    print("result=",result)