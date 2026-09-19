#write a program to check if an input string is palindrome
str = input("enter a string")
original_str = str
reversed_str = ""

for i in str:
    reversed_str = i + reversed_str

if original_str == reversed_str:
    print("yes, it is a palindrome")
else:
    print("no , it is not palindrome")


