#1a
a= [ i for i in range(1,51)]
result = ",".join([str(i) for i in a])
print(result)
#1b
a= [ i for i in range(1,51)]
result = ",".join([str(i) for i in a])
print(result)
 #1c
a= [ i for i in range(1,51)]
result = "_".join([str(i) for i in a])
print(result)
#1d
a= [ i for i in range(1,51)]
result = "\n".join([f"{i} {i**2}"for i in a])
print(result)
#make a list of 10 people

#convert each element in the list to upper case using list comprehension
names = [ "maa papa","bhaiya didi","sir mam" ]
print(names)
#2a
names = [ "maa papa","bhaiya didi","sir mam" ]
upper_names = [ name.upper() for name in names]
print(upper_names)
#2b
names = [ "maa papa","bhaiya didi","sir mam" ]
swapped = [" ".join(name.split()[::-1]) for name in names]
print(swapped)
#2c
names = [ "maa papa","bhaiya didi","sir mam" ]
result = [name.title().replace(" ",".") for name in names]
print(result)
#3
s= "she sells sea shells that she collect from the sae floor"
w= s.split()
longest = [i for i in w if len(i) == max([len(j) for j in w])]
print(longest)
#4
s= "she sells sea shells that she collect from the sae floor"
w= s.lower().split()
duplicate = [ i for i in w if w.count(i) > 1]
print(set(duplicate))
