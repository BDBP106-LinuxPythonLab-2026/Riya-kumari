#1
import numpy as np
arr = np.arange(10)
print(arr)
#2
import numpy as np
arr = np.full((3, 3), True)
print(arr)
#3
import numpy as np
arr = np.arange(1, 51)
prime = arr[
    (arr > 1) &
    np.array([all(i % j != 0 for j in range(2, int(i**0.5) + 1)) for i in arr])
]
print(prime)
#4
import numpy as np
arr = np.random.randint(1, 100, 20)
print("1D Array:")
print(arr)
new_arr = arr.reshape(4, 5)
print("2D Array:")
print(new_arr)
#5
import numpy as np
a = np.arange(10)
b = np.ones(10)
c = np.hstack((a, b))
print("Array a:", a)
print("Array b:", b)
print("Stacked array:", c)
#6
import numpy as np
a = np.arange(1, 101)
b = np.array([
    n for n in range(2, 600)
    if all(n % j != 0 for j in range(2, int(n**0.5) + 1))
])
b = b[:100]
c = np.intersect1d(a, b)
print(c)
#7
import numpy as np
c = np.setdiff1d(a, b)
print(c)
#8
import numpy as np
indices = np.where(np.isin(a, b))
print(indices)
#9
import numpy as np
a = np.arange(1, 101)
result = a[(a > 5) & (a < 20)]
print(result)