a = ("apple",)
print(type(a))
b = ("apple")
print(type(b))
c = ("apple", "banana", "cherry")
print(c[1])
y = list(c)
y[0] = "alma"
c = tuple(y)
print(c)
(green,yellow,red) = c
print(green,yellow,red)
for i in c:
    print(i)
z = c*2
print(z)