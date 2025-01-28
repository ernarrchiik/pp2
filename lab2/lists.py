a = ["my","name","is","Ernar","my"]
print(a)
print(len(a))
print(type(a))
print(a[::-1])
a.insert(2,"Is")
a.pop()
a[0] = "My"
print(a)
if "Ernar" in a:
    print("Ernar is in the list")
for i in a:
    print(i)
a.sort
print(a)
mylist = a.copy()
print(mylist)
list = a +mylist
print(list)