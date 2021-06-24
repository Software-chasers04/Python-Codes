# Every function name must be different otherwise it will be error

def add(a,b):
    sum = a+b
    print(sum)

def sub(a,b):
    r = a-b
    print(r)

def add1(a,b,c):
    sum = a+b+c
    print(sum)

add(10,30)
add1(10,30,40)
sub(30,40)

def msg():
    print("Nothing")

def str(d,f):
    print(d+" "+f)
a =input("Enter 1st name:")
b =input("Enter 2nd name:")
str(a,b)
msg()

# using return
def large(a,b):
    if a>b:
        return a
    else:
        return b

r = large(30,40)
print(r)
print(large(20,90))

max = large
print(max(55,88))

