file = open("std.txt","r+")
print(file.readable())

text = file.read()
#text1 = file.readlines() # text1 = file.readlines()

print(text)
#print(text1)
size = len(text)
print(size)
file.close()