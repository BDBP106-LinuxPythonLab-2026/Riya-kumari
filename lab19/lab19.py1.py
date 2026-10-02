a=[i for i in range(1,51)]
print(a)
#q1(ii)
#1
print(a[1:5])
#2
print(a[3:20:2])
#3
print(a[::2])
#4
print(a[::])
#5
print(a[10::2])
#6
print(a[1:1:1])
#7
print(a[:0:])
#8
print(a[-7::1])
#9
print(a[-6:])
#10
print(a[0:-5])
#q1(iii)
#slicing with negative list
#1
print(a[::-1])
#2
print(a[::-3])
#3
print(a[:1:-2])
#4
print(a[-1:-1:-1])
#5
print(a[:-5:-1])
#6
print(a[:0:-1])
#7
print(a[:-1:-1])
#8
print(a[0:-5:-1])
#9
print(a[-1:5:-1])
#10
print(a[2:2:-1])
#11
print(a[2:1:-1])
#12
print(a[0:-5])
#q1(iv)
#modification of list using slicing
#create a list of even number
even=a[1::2]
print(even)
#create a new list from a by choosing the first 10 numbers
new_list=a[:10]=a[35::2]
print(new_list)