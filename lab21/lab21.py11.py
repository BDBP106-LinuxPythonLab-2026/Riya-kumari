#program to concatenate a list strings to make a sentence using reduce function
from functools import reduce
words=["i","miss","my","home"]
sentence=reduce(lambda x,y:x+" "+y,words)
print("sentence:",sentence)