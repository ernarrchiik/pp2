#1
import math
a = [1,2,3,4,5,6]
print(math.prod(a))
#2
a = "ErnarBerenbai"
upp = 0
low = 0
for i in a:
    if i.islower():low+=1
    else:upp+=1
print(upp,low)
#3
a = "Ernar"

b = "".join(reversed(a))
if a == b:
    print("Palindrome")
else:
    print("Not polindrom")
#4
from math import sqrt
import time
a = int(input())
b = int(input())
time.sleep(b*0.001)
print("Square root of ",a," after ",b," miliseconds is ",sqrt(a))
#5
a = (1,0,"Ernar",True,False)
x = all(a)
print(x)