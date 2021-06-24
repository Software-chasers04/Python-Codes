import re

pattern = r"Colour"

text = "My favourite Colour is Red.I love Blue Colour"
text2 = re.sub(pattern,"Color",text)
text3 = re.sub(pattern,"Color",text,count=1)

print(text2)
print(text3)