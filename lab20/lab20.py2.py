#count the vowels,consonants,digit and spaces
text=input("enter a text")
vowel=0
consonants=0
digits=0
space=0
for ch in text.lower():
    if ch in "aeiou":
        vowel += 1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch == " ":
        space+= 1
print("vowel:", vowel)
print("consonants:",consonants)
print("digits:",digits)
print("space:",space)

