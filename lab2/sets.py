a = {"apple", "banana", "cherry", True, 1, 2}
print(a)
print(type(a))
for i in a:
    print(i)
print("banana" in a)
b = ["kiwi", "watermelon"]
a.update(b)
a.add("orange")
a.discard("banana")
print(a)
s1 = {"a", "b", "c"}
s2 = {1, 2, 3}

s3 = s1.union(s2)
print(s3)
