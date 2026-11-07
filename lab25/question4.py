import re

pattern = r'^(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

number = input("Enter an integer from 0 to 255: ")

if re.fullmatch(pattern, number):
 print("Valid")
else:
 print("Invalid")