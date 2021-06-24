class shape:
    base = ''
    height = ''

    def __init__(self,base,height):
        self.base = base
        self.height = height
    #If i want ,i can use area method for overriding
    def area(self):
        print("I'm Area method of shape class")

class triangle(shape):
    #override methof(area)
   def area(self):

       a = 0.5* self.base*self.height
       print(a)

class Rectangle(shape):

    def area(self):
        a = self.base*self.height
        print(a)
#Object declearable of inherit class
s = shape(10,20)
s.shape()
t1 = triangle(10,20)
t1.area()
t2 = triangle(10,5)
t2.area()
r1 = Rectangle(10,20)
r1.area()