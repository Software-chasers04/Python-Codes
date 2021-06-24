
mark = int(input("Enter the mark: "))
if mark>=33:
    print("Pass")

else:
    print("Fail")

# max num
n1 = int(input("Enter the 1st num: "))
n2 = int(input("Enter the 2nd num: "))
if n1>n2:
    print(n1)
else:
    print(n2)

# even or ODD
n3 = int(input("Enter the a num: "))
if n3%2==0:
    print("Even")
else:
    print("Odd")

# Grade Result
marks = int(input("Enter a mark :"))

if marks >=80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
else:
    print("Fail")
