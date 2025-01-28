a = dict(name = "Ernar", age = 17, country = "Kazakhstan")
print(a)
print(type(a))
b = {
    "name":"Ernar",
    "age":17,
    "country":"Kazakhstan"
}
x = b["age"]
print(x)
b["age"] = 18
print(b["age"])
b.update({"country": "Germany"})
print(b["age"])
b["year"] = 2007
b.pop("country")
print(b)
for i in b.keys():
    print(i)

c = dict(b)
print(c)