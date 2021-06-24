class std:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

prova = std()
a = input("Enter roll:")
b = input("Enter gpa:")
prova.set_value(a,b)
prova.display()

prova1 = std()
prova1.set_value(30,3.7)
prova1.display()
