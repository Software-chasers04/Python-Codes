class Bike :

    def __init__(self, name, color):
         self.name = name
         self.color = color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color


    def __str__(self):
        return (f"Name = {self.name}, color = {self.color}")

bike1 = Bike("Yahama R12","Blue")
bike2 = Bike("Yahama R2","Blue")
print(bike1)
print(bike1 == bike2)