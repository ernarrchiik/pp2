#1
N = int(input())
class MyClass:
    def _iter_(self):
        self.a = 0
        return self
    def _next_(self):
        if self.a < N:
            self.a += 1
            return self.a**2
        else:
            raise StopIteration
p1 = MyClass()
result = iter(p1)
for i in result:
    print(i)
#2
N = int(input())
def generator_even(N):
    i = 0
    while i <=N:
        if i%2 == 0:
            yield i
        i+=1
for even in generator_even(N):
    print(even, end=', ' if even != N and even % 2 == 0 else '')
#3
N = int(input())
def gen(N):
    i = 0
    while i <= N:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i+=1
for i in gen(N):
    print(i)
#4
def generator(a,b):
    i = a
    while i <= b:
        yield i**2
        i+=1
a = int(input())
b = int(input())
for square in generator(a,b):
    print(square)
#5
N = int(input())
def reverse_num(n):
    i = n
    while i != 0:
        yield i
        i-=1
for rev in reverse_num(N):
    print(rev)