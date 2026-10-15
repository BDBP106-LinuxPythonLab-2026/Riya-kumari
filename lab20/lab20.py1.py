#number classifier
#check it is positive,negative or zero
#if it is non-zero,also print whether it is even or odd.
#if it is divisible by  both 3 and 5 ,print "FizzBuzz number!"
num=int(input("Enter a number"))
#positive , negative , zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("zero")
#even or odd
if num %2 ==0:
    print("even")
else:
    print("odd")
#FizzBuzz
if num % 3 == 0 and num % 5==0:
    print("FizzBuzz number")

