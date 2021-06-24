# xargs
'''
def std(*details):
    print(details)
    print(details[0])

std(101,"Afrin")
std("Afrin",202,3.75)
'''
# addition
def std1(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return  sum

print(std1(10,20))
print(std1(10,20,30))

#xxargs(like dictionary)

def std2(**details):
    print(details)
    print(details["id"]) # id is a key
    print(details["name"])
    print(details["sec"])
    #print(details["sect"])

std2(id = 101,name = "Afrin",sec ="B") # just one call working
#std2(sect= "B")

