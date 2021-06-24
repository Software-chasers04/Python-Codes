# Using some library functions
s =["C","C++","Java","Python","Basic"]
print(len(s))

s.append("toc")
print(s)

s.insert(2,"os")
print(s)

s.remove("Basic")
print(s)

s.sort()
print(s)

s.reverse()
print(s)

s.pop()
s.pop()
print(s)

s.clear()
print(s)

p = [20,10,3,3,399]

p2 = p.copy()
print(p2)

pos = p.index(10)
print(pos)

pos = p.count(4)
print(pos)