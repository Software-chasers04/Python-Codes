# 1 to 19 output

i = 1
while i<=110:
    if i == 20 :
        break
    print(i)
    i+=1
print("Hello")

# Another way

i = 1
while i<=110:

    print(i)
    i+=1
    if i == 20:
        break
print("Hello")

# Using continue Keyword
i = 1
while i <= 110:
    if i == 20:
        continue
    print(i)
    i += 1
print("Hello")

# 1 to 110 print
i = 1
while i <= 110:
    print(i)
    i += 1
    if i == 20:
        continue
print("Hello")