#long format
import math
angle=(0,30,30)
def f (angle):
    x=math.sin(math.radians(angle))
    y=math.cos(math.radians(angle))
    return (x,y)
#short format
import math
angles = (0,30,45)
result=list(map(lambda x: (math.sin(math.radians(x)),math.cos(math.radians(x))),angles))
print(result)

