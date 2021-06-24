from random import randint
n = int(input("Enter the Test Num:"))
for i in range(1,n+1):

    guessNum = int(input("Enter the guess between 1 to 5 :"))
    randomNum = randint(1,5)
    if(guessNum == randomNum):
        print("You Won the game")
    else:
         print("You lost the game")
         print("The random Number was:", randomNum)
