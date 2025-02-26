import re
#1
text = "a,ab,abb,abbb"
pattern = r"a+b*"
print(re.findall(pattern,text))
#2
text = "a,ab,abb,abbb"
pattern = r"\ba+bb{1,2}\b"
print(re.findall(pattern,text))
#3
text = "Ernar,Berenbai,ernar,berenbai"
pattern = r"\b[A-Z][a-z]*\b"
print(re.findall(pattern,text))
#6
text = "Ernar,Berenbai get.100,points"
print(re.sub("[ .,]",":",text))
#7
text = "hello_world_example"
result = ''.join(word.capitalize() if i else word for i, word in enumerate(text.split('_')))
print(result) 
#8
text = "HelloWorldExample"
x = re.findall(r'[A-Z][a-z]*', text)
print(x)
#9
text = "ErnarBerenbaiKanatuly"
x = re.sub(r"([a-z])([A-Z])",r"\1 \2",text)
print(x)
#10
text = "ErnarBerenbaiKanatuly"
x = re.sub(r"([a-z])([A-Z])",r"\1_\2",text).lower()
print(x)
