import re

pattern = r'^(?:[01][0-9]{2}|2[0-4][0-9]|25[0-5])$'

number = input("Enter a three-digit integer (000-255): ")

if re.fullmatch(pattern, number):
 print("Valid")
else:
 print("Invalid")