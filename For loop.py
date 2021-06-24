#Using for loop for Range
for x in range(10):
    print(x,end=' ')

for y in range(2,18):
    print(y,end="\n")


#series
# 1+2+.........+n
n = int(input("Enter the last Number:"))
s=0

for x in range(1,n+1,1):
    s+=x
print(s)

# 1+3+5..+n
s =0
for x in range(1,n+1,2):
    s+=x
print(s)

# 1*1 + 2*2 + ....... +n*n
s = 0
for x in range(1,n+1,1):
    s+=x*x
print(s)