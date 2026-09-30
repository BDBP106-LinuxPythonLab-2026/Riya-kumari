import math
def triangle_areas(a,b,c):
    s=(a+b+c)/2
    a=2
    b=3
    c=4
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)

