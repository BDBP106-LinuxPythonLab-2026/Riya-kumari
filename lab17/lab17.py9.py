#anagram check
s1=input("enter string")
s2=input("enter string")
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram")
    