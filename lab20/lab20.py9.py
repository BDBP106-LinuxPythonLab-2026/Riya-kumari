Special_ch={"!","@","$","^","%","&","*"}
while True:
    error=[]
    P=input("Enter Password:",)
    if len(P)<8:
        error.append("At least 8 characters password is required")
    u=False
    l=False
    digit=False
    special=False
    for i in P:
        if i.isupper():
            u=True
        if i.islower():
            l=True
        if i.isdigit():
            digit=True
        if i in Special_ch:
            special=True
    if u==False:
        error.append("Missing Uppercase Letter")
    if l==False:
        error.append("Missing Lowercase Letter")
    if digit==False:
        error.append("Missing Digit")
    if special==False:
        error.append("Missing Special Characters")
    if " " in P:
        error.append("No Space Allowed")
    if "password" in P:
        error.append("It cannot contain 'password'")
    if len(error)==0:
        break
    else:
        print("Invalid Password")
        for i in error:
            print(i)