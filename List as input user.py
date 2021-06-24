n = input("Enter the text of numbers:")

list = n.split()
sum = 0;
for i in list :
    sum+= int(i)
print(sum)

# count the words, letters, digits in a text

numofDigits = 0
numofLetters = 0
numofWords = 0

text = input("Enter the text and numbers:")
for x in text:
    x = x.lower()
    if x>'a' and x<='z':
        numofLetters+=1
    if x>='0' and x<='9':
        numofDigits+=1
    elif x==' ':
        numofWords+=1

print(numofLetters)
print(numofDigits)
print(numofWords+1)

