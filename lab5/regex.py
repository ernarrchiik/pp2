#4
import re
pattern = r"^[A-Z][a-z]+$"
x = ["ernar", "Berenbay"]
for i in x:
    if re.fullmatch(pattern, i):
        print(i)
#5
import re
pattern = r"^[a][b]$"
x = ["aeeb", "Berenbay"]
for i in x:
    if re.fullmatch(pattern, i):
        print(i)

