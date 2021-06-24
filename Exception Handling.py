try:

   n1 = (input("Enter a number:"))
   r = 20/n1
   print(r)
   print("Done")
   list =[10,0,30]
   r1= list[0]/list[1]
   print(r1)
except TypeError:
   print("Type Error")
except IndexError:
    print("Index error")
try:
    list = [10, 0, 30]
    r1 = list[0] / list[1] # this is a Zero divission error
    print(r1)
#except ZeroDivisionError:
 #   print(" error")
except IndexError:
    print("Index error")
finally: # print all statements under finally keyword
    print("Successful")