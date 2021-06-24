class std:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

a = input("Enter roll:")
b = input("Enter gpa:")
prova = std(a,b)
prova.display()
