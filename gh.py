class Student:
    def __init__(self, student_id):
        self.id = student_id
        print("Student ID: ", self.id)


class CSE(Student):
    cgpa = 0.0
    credit_hours_completed = 0.0
    number_of_courses = 0

    def __init__(self, student_id):
        super().__init__(student_id)
        self.cgpa
        self.credit_hours_completed
        print("Depertment: CSE")

    def calculate_completed_credit(self):
        number_of_courses = int(input("Enter no of courses: "))

        for i in range(number_of_courses):
            credit_hour = float(input("Enter credit hour %d : " % (i + 1)))
            credit_hours_completed = credit_hours_completed + credit_hour

        print("Total completed credit:", credit_hours_completed)

    def calculate_course_grade(self):
        for i in range(number_of_courses):
            credit = float(input("Enter course credit %d : " % (i + 1)))
            grade = float(input("Enter course grade %d : " % (i + 1)))
            print("Course ", (i + 1), " grade * hours : ", (credit * grade))


class SWE(Student):
    cgpa = 0
    credit_hours_completed = 0
    number_of_courses = 0

    def __init__(self, student_id):
        super().__init__(student_id)
        self.cgpa
        self.credit_hours_completed
        print("Depertment: SWE")

    def calculate_completed_credit(self):
        number_of_courses = int(input("Enter no of courses: "))

        for i in range(number_of_courses):
            credit_hour = float(input("Enter credit hour %d : " % (i + 1)))
            credit_hours_completed = credit_hours_completed + credit_hour

        print("Total completed credit:", credit_hours_completed)

    def calculate_course_grade(self):
        for i in range(number_of_courses):
            credit = float(input("Enter course credit %d : " % (i + 1)))
            grade = float(input("Enter course grade %d : " % (i + 1)))
            print("Course ", (i + 1), " grade * hours : ", (credit * grade))


ID = input("Enter ID: ")

cse = CSE(ID)
cse.calculate_completed_credit()
cse.calculate_course_grade()

ID = input("Enter ID: ")
swe = SWE(ID)
swe.calculate_completed_credit()
swe.calculate_course_grade()