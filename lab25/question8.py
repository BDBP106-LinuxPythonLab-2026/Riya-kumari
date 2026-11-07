import re
text = input("Enter text containing an email address: ")

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}'

def mask_email(match):
 email = match.group()

 username, domain = email.split("@", 1)

 if len(username) <= 1:
    masked_username = username
 elif len(username) == 2:
    masked_username = username[0] + "*"
 else:
    masked_username = (
        username[0]
        + "*" * (len(username) - 2)
        + username[-1]
    )

 return masked_username + "@" + domain

masked_text = re.sub(pattern, mask_email, text)

print("Masked text:")
print(masked_text)