
try:
   n1= int(input("Enter 1st number:"))
   n2= int(input("Enter 2nd number:"))

   r = n1/n2
   print(r)
except(ValueError,ZeroDivisionError):
    print("You have enter encorrect input.")

finally:
     print("Thanks!!!")


def voter(age):
    if age<18:
        raise ValueError("Invalid Voter")
    return "you are allowed to vote"
try:
    print(voter(19))
    print(voter(17))
except ValueError as e :
    print(e)