
# Write a program to convert temperature in Celsius to Fahrenheit using map() function.
def convert(c):
    return(c*9/5)+32
celsius=[10,20,30,40]
fahrenheit=list(map(convert,celsius))
print(fahrenheit)