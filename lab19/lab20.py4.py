#multiplication table grid
#print an n*n multiplication table
n=int(input("enter n:"))
print("    ",end="")
for j in range(1 , n + 1):
    print(str(j).rjust(4),end="")
print()
for i in range(1 , n + 1):
    print(str(i).rjust(4),end="")
    for j in range(1 , n + 1):
        print(str(i * j).rjust(4), end="")
    print()
