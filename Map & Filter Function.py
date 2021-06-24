def square(x):
    return x*x
num = [1,2,3,4]
r = list(map(square,num))
print(r)


# filter function
def sub(a):
    if a%2==0:
     return a

result = list(filter(sub,num))
print(result)

#same code bt using lambda function
re = list(filter(lambda x: x%2==0,num))
print(re)