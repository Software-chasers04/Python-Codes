# largest num
n1 = int(input("Enter the 1st number :"))
n2 = int(input("Enter the 2nd number :"))
n3 = int(input("Enter the 3rd number :"))

if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)

# Vowel
ch = input("Enter a Char: ")
if ch=='a'or ch== 'e' or ch=='i' or ch=='o' or ch == 'u'or ch=='A'or ch== 'E' or ch=='I' or ch=='O' or ch == 'U' :
    print("vowel")
else:
    print("consonant")