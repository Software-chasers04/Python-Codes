def std1(*numbers):
    sum = 0
    for i in numbers:
        sum += i
        return  sum

print(std1(10,20))
print(std1(10,20,30))