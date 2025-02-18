import math
#1
def radian(degree):
   radian = degree*(math.pi/180)
   return radian
n = float(input())
result = round(radian(n),6)
print(result)
#2
def area(height,first,second):
   s = ((first+second)/2)*height
   return s
h = int(input())
f = int(input())
s = int(input())
print(area(h,f,s))
#3
def area_polyg(n,s):
     A = (n*(s**2))/(4*math.tan(math.pi/n))
     return int(A)
n = int(input())
s = int(input())
print(area_polyg(n,s))
#4
def area_par(base,height):
     A = base*height
     return A
b = int(input())
h = int(input())
print(area_par(b,h))