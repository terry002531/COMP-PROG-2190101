import math
def distance1(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def distance2(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return distance1(x1,y1,x2,y2)
def distance3(c1,c2):
    x1,y1,r1 = c1
    x2,y2,r2 = c2
    d = distance1(x1,y1,x2,y2)
    if abs(r1 - r2) <= d <= r1 + r2:
        return d,True
    else:
        return d,False
def perimeter(points):
    s = 0.0
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i+1) % len(points)]
        d = distance2(p1,p2)
        s += d
    return s

exec(input().strip())