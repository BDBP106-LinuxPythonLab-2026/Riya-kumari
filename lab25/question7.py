import re

text = input("Enter a piece of text: ")

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}'

emails = re.findall(pattern, text)

unique_emails = sorted(set(emails))

if unique_emails:
 print("Unique email addresses:")
for email in unique_emails:
 print(email)
else:
 print("No email addresses found")