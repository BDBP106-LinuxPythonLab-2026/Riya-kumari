

import re

data = "riya,22,world@gmail.com,ibab,Student"

fields = data.split(",")

pattern = r"^[\w.-]+@[\w.-]+.[A-Za-z]{2,}$"

if re.fullmatch(pattern, fields[2]):
     print("Third field is an email address")
else:
     print("Third field is not an email address")