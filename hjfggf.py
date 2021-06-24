import random
import datetime

# Global List Declaration
name = []
phno = []
add = []
check_in = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

# Global Vaariable Declaration

i = 0


# Home Function
def Home():
    print("""
                                Welcome to Hotel Daffodil

                                      1.Booking
                                      2.Room Info
                                      3.Menu Card
                                      4.Payment
                                      5.Record
                                      0.Exit
    """)

    choice = int(input("                Enter the choice->   "))

    if choice == 1:
        print(" ")
        Booking()

    elif choice == 2:
        print(" ")
        Rooms_Info()

    elif choice == 3:
        print(" ")
        restaurant()

    elif choice == 4:
        print(" ")
        Payment()

    elif choice == 5:
        print(" ")
        Record()

    else:
        exit()

    # Function used in booking


def date(c):
    if c[2] >= 2019 and c[2] <= 2020:

        if c[1] != 0 and c[1] <= 12:

            if c[1] == 2 and c[0] != 0 and c[0] <= 31:

                if c[2] % 4 == 0 and c[0] <= 29:
                    pass

                elif c[0] < 29:
                    pass

                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    check_in.pop(i)
                    checkout.pop(i)
                    Booking()

                    # if month is odd & less than equal
            # to 7th  month
            elif c[1] <= 7 and c[1] % 2 != 0 and c[0] <= 31:
                pass

            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1] % 2 == 0 and c[0] <= 30 and c[1] != 2:
                pass

            # if month is even & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1] % 2 == 0 and c[0] <= 31:
                pass

            # if month is odd & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1] % 2 != 0 and c[0] <= 30:
                pass

            else:
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                check_in.pop(i)
                checkout.pop(i)
                Booking()

        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            check_in.pop(i)
            checkout.pop(i)
            Booking()

    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        check_in.pop(i)
        checkout.pop(i)
        Booking()

    # Booking fucntion


def Booking():
    # used global keyword to
    # use global variable 'i'
    global i
    print(" BOOKING ROOMS")
    print(" ")

    while 1:
        n = str(input("Name: "))
        p1 = str(input("Phone No.: "))
        a = str(input("Address: "))

        # checks if any field is not empty
        if n != "" and p1 != "" and a != "":
            name.append(n)
            add.append(a)
            break

        else:
            print("\tName, Phone no. & Address cannot be empty..!!")

    cii = str(input("Check-In: "))
    check_in.append(cii)
    cii = cii.split('-')
    ci = cii
    ci[0] = int(ci[0])
    ci[1] = int(ci[1])
    ci[2] = int(ci[2])
    date(ci)

    coo = str(input("Check-Out: "))
    checkout.append(coo)
    coo = coo.split('-')
    co = coo
    co[0] = int(co[0])
    co[1] = int(co[1])
    co[2] = int(co[2])

    # checks if check-out date falls after
    # check-in date
    if co[1] < ci[1] and co[2] < ci[2]:

        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        name.pop(i)
        add.pop(i)
        check_in.pop(i)
        checkout.pop(i)
        Booking()
    elif co[1] == ci[1] and co[2] >= ci[2] and co[0] <= ci[0]:

        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        name.pop(i)
        add.pop(i)
        check_in.pop(i)
        checkout.pop(i)
        Booking()
    else:
        pass

    date(co)
    d1 = datetime.datetime(ci[2], ci[1], ci[0])
    d2 = datetime.datetime(co[2], co[1], co[0])
    d = (d2 - d1).days
    day.append(d)

    print("""
                          ----SELECT ROOM TYPE----
                           1. Standard Non-AC  
                           2. Standard AC    
                           3. 3-Bed Non-AC
                           4. 3-Bed AC
                           1\tPress 0 for Room Prices
    """)

    choice = int(input("->"))

    # if-conditions to display alloted room
    # type and it's price
    if choice == 0:
        print("""
                               1. Standard Non-AC - TK. 3500
                               2. Standard AC - Tk. 4000
                               3. 3-Bed Non-AC - Tk. 4500
                               4. 3-Bed AC - Tk. 5000
        """)
        choice = int(input("                      ->"))
    if choice == 1:
        room.append('Standard Non-AC')
        print("Room Type- Standard Non-AC")
        price.append(3500)
        print("Price- 3500")
    elif choice == 2:
        room.append('Standard AC')
        print("Room Type- Standard AC")
        price.append(4000)
        print("Price- 4000")
    elif choice == 3:
        room.append('3-Bed Non-AC')
        print("Room Type- 3-Bed Non-AC")
        price.append(4500)
        print("Price- 4500")
    elif choice == 4:
        room.append('3-Bed AC')
        print("Room Type- 3-Bed AC")
        price.append(5000)
        print("Price- 5000")
    else:
        print(" Wrong choice..!!")

        # randomly generating room no. and customer
    # id for customer
    rn = random.randrange(40) + 300
    cid = random.randrange(40) + 10

    # checks if alloted room no. & customer
    # id already not alloted
    while rn in roomno or cid in custid:
        rn = random.randrange(60) + 300
        cid = random.randrange(60) + 10

    rc.append(0)
    p.append(0)

    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 1:
                    phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 0:
                    print("\tPhone no. already exists and payment yet not done..!!")
                    name.pop(i)
                    add.pop(i)
                    check_in.pop(i)
                    checkout.pop(i)
                    Booking()
    print("")
    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("Room No. - ", rn)
    print("Customer Id - ", cid)
    roomno.append(rn)
    custid.append(cid)
    i = i + 1
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()

    # ROOMS INFO


def Rooms_Info():
    print("""
                                      ------ HOTEL ROOMS INFO ------

                                            STANDARD NON-AC
                        ---------------------------------------------------------------
                               1 Double Bed, Television, Telephone,
                               1 Coffee table with 2 sofa, Balcony and
                               an attached washroom with hot/cold water.

                                            STANDARD NON-AC
                        ---------------------------------------------------------------
                              1 Double Bed, Television, Telephone,
                           Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
                           an attached washroom with hot/cold water + Window/Split AC.

                                            3-Bed NON-AC
                        ---------------------------------------------------------------
                                  1 Double Bed + 1 Single Bed, Television,
                                  Telephone, 1 Coffee table with 2 sofa,
                                 1 Side table, Balcony with 2 Chair and an
                                 attached washroom with hot/cold water.\n
                                              3-Bed AC
                        ---------------------------------------------------------------
                                   1 Double Bed + 1 Single Bed, Television,
                                   Telephone, 1 Coffee table with 2 sofa,
                               1 Side table, Balcony table with 2 Chair and an
                          attached washroom with hot/cold water + Window/Split AC.\n\n
    """)
    print()
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()

    # RESTAURANT FUNCTION


def restaurant():
    ph = int(input("Customer Id: "))
    global i
    f = 0
    r = 0
    for n in range(0, i):
        if custid[n] == ph and p[n] == 0:
            f = 1
            print("""

                       ------------------------------------------------------------------------- 
                                                  Hotel Daffodil 
                       ------------------------------------------------------------------------- 
                                                   Menu Card 
                       ------------------------------------------------------------------------- 
                         BEVARAGES                             26 Dal Fry................ 140.00
                       ----------------------------------      27 Dal Makhani............ 150.00
                        1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00
                        2  Masala Tea.............. 25.00")
                        3  Coffee.................. 25.00      ROTI
                        4  Cold Drink.............. 25.00     ---------------------------------- 
                        5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00 
                        6  Bread Jam............... 30.00      30 Butter Roti............. 15.00 
                        7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00 
                        8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00 
                        9  Cheese Toast Sandwich... 70.00")
                       10 Grilled Sandwich........ 70.00      RICE
                                                              ----------------------------------
                         SOUPS                                  33 Plain Rice............. 90.00 
                        ----------------------------------      34 Jeera Rice............. 90.00 
                       11 Tomato Soup............ 110.00        35 Veg Pulao.............. 110.00 
                       12 Hot & Sour............. 110.00        36 Ilish Pulao............ 110.00 
                       13 Veg. Noodle Soup....... 110.00")
                       14 Sweet Corn............. 110.00      CHINESE ")
                       15 Veg. Munchow........... 110.00     ---------------------------------- 
                                                                37 Dim Sums................. 100.00   
                     MAIN COURSE                                38 Fried Rice with Veg...... 110.00 
                   ----------------------------------           39 F.Rice with Chicken & Veg 130.00 
                      16 Morog Polaw............ 110.00         40 Chicken with Chestnuts... 130.00 
                      17 Kacchi(Beef)........... 110.00         41 Chow Mein................ 130.00 
                      18 Kacchi(Mutton)......... 120.00         42 Dumplings................ 140.00 
                      19 Tehari................. 120.00")
                      20 Khichuri(Egg).......... 140.00      ICE CREAM 
                      21 Kala Vuna(Beef)........ 140.00      ---------------------------------- 
                      22 Kala Vuna(Mutton)...... 140.00         43 Vanilla................. 60.00  
                      23 Hydrabadi Biryani...... 140.00         44 Strawberry.............. 60.00 
                      24 Dom Biriyani........... 140.00         45 Pineapple............... 60.00 
                      25 Handi Biriyani......... 140.00         46 Butter Scotch........... 60.00 
                                              Press 0 -to end  
            """)
            choice = 1
            while (choice != 0):

                choice = int(input(" -> "))

                # if-elif-conditions to assign item
                # prices listed in menu card
                if choice == 1 or choice == 31 or choice == 32:
                    tk = 20
                    r = r + tk
                elif choice <= 4 and choice >= 2:
                    tk = 25
                    r = r + tk
                elif choice <= 6 and choice >= 5:
                    tk = 30
                    r = r + tk
                elif choice <= 8 and choice >= 7:
                    tk = 50
                    r = r + tk
                elif choice <= 10 and choice >= 9:
                    tk = 70
                    r = r + tk
                elif (choice <= 17 and choice >= 11) or choice == 35 or choice == 36 or choice == 38:
                    tk = 110
                    r = r + tk
                elif choice <= 19 and choice >= 18:
                    tk = 120
                    r = r + tk
                elif (choice <= 26 and choice >= 20) or choice == 42:
                    tk = 140
                    r = r + tk
                elif choice <= 28 and choice >= 27:
                    tk = 150
                    r = r + tk
                elif choice <= 30 and choice >= 29:
                    tk = 15
                    r = r + tk
                elif choice == 33 or choice == 34:
                    tk = 90
                    r = r + tk
                elif choice == 37:
                    tk = 100
                    r = r + tk
                elif choice <= 41 and choice >= 39:
                    tk = 130
                    r = r + tk
                elif choice <= 46 and choice >= 43:
                    tk = 60
                    r = r + tk
                elif choice == 0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ", r)

            # updates restaurant charges and then
            # appends in 'rc' list
            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()

    # PAYMENT FUNCTION


def Payment():
    ph = str(input("Phone Number: "))
    global i
    f = 0

    for n in range(0, i):
        if ph == phno[n]:

            # checks if payment is
            # not already done
            if p[n] == 0:
                f = 1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")

                print("  1- Credit/Debit Card")
                print("  2- bKash")
                print("  3- Rocket")
                print("  4- Nogod")
                x = int(input("-> "))
                print("\n  Amount: ", (price[n] * day[n]) + rc[n])
                print("\n            Pay For Daffodil")
                print("  (y/n)")
                choice = str(input("->"))

                if choice == 'y' or choice == 'Y':
                    print("\n\n --------------------------------")
                    print("           Hotel Daffodil")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ", name[n], "\t\n Phone No.: ", phno[n], "\t\n Address: ", add[n], "\t")
                    print("\n Check-In: ", check_in[n], "\t\n Check-Out: ", checkout[n], "\t")
                    print("\n Room Type: ", room[n], "\t\n Room Charges: ", price[n] * day[n], "\t")
                    print(" Restaurant Charges: \t", rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ", (price[n] * day[n]) + rc[n], "\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)

                    # pops room no. and customer id from list and
                    # later assigns zero at same position
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n, 0)
                    custid.insert(n, 0)

            else:

                for j in range(n + 1, i):
                    if ph == phno[j]:
                        if p[j] == 0:
                            pass

                        else:
                            f = 1
                            print("\n\tPayment has been Made :)\n\n")
    if f == 0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()

    # RECORD FUNCTION


def Record():
    # checks if any record exists or not
    if phno != []:
        print("        *** HOTEL RECORD ***\n")
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |")
        print(
            "----------------------------------------------------------------------------------------------------------------------")

        for n in range(0, i):
            print("|", name[n], "\t |", phno[n], "\t|", add[n], "\t|", check_in[n], "\t|", checkout[n], "\t|", room[n],
                  "\t|", price[n])

        print(
            "----------------------------------------------------------------------------------------------------------------------")

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()

    else:
        exit()

    # Driver Code


Home()