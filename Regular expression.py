import re

pattern = r"Colour"

if re.match(pattern,"Red is a Colour, i love Blue Colour"):# stact matching at 1st.if dont,it will no matchied
    print("match")

else:
    print("Not matched")

if (re.findall(pattern, "Red is a Colour, i love Blue Colour")): # start matching & searching from 1st to last
    print("match")