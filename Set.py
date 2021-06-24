num = {1,2,3,4} # ussing 2nd bracket(called Curly braces)
num1 = set([4,5,6]) # list converted to set(called set function)
print(num1)
num1.add(7)
num.add(5)
print(num1)
print(num)
num1.remove(5)
print(num1)

print(num | num1) #union
print(num & num1) # Intersection
print(num - num1) # minus
