# type casting

n1 = input("Enter 1st num:")
n2 = input("Enter 2nd num : ")
s = int(n1) + int(n2) # without type casting, output will be error
print(s)

'''
Another way 
type cast
'''
n1 = int(input("Enter 1st num:")) # initially type cast
n2 = int(input("Enter 2nd num : "))
s = n1 + n2
r = n1 - n2
print("the Sum is : ",s) # use comma for integer num
print("the Sum is : ",r)