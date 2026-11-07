import re

text = input("Enter a string: ")

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}'

if re.search(pattern, text):
 print("Email address found")
else:
 print("No email address found")