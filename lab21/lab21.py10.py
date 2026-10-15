#program to extract all vowels in a given string using list comprehensions
text=input("enter a string:")
vowel=[ch for ch in text if ch.lower() in "aeiou"]
print("vowel:",vowel)