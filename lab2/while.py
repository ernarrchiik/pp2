a = 1234
x = 0
while a>0:
    x += a%10
    a//=10

print(x)