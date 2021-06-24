from math import *
'''
num = float (input("Enter the number:"))
print(num)
'''
print(max(10,20))
print(min(20,30))
print(pow(2,3))
print(abs(-3))
print(sqrt(9))
print(floor(3.7))
print(ceil(2.6))

# string format
n1 = int(input("Enter 1st num:"))
n2 = int(input("Enter 2nd num:"))
print(f"{n1} + {n2} = {n1+n2}")
print(n1 + n2)
name = input("Enter your name :")
phn = input("Enter your phn :")
print(name +" " + phn)

# 2nd way
print(name ,end=" ")
print(phn)

# Relational Operator
n = 30>40
print(n)
print(20==80)
print(20!=30)
print(30<90)
print("Afrin"=="Afrin")
print("Afrin"=="Prova")