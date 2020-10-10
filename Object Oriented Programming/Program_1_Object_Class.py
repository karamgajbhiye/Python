class Student:
    def __init__(self, firstname, lastname, rollno):
        self.firstname = firstname
        self.lastname = lastname
        self.rollno = rollno


Student1 = Student("Karam", "Gajbhiye", 1000)
Student2 = Student("Param", "Gajbhiye", 1001)

print("Full Name - {} {}, Roll No. - {}".format(Student1.firstname,
                                                Student1.lastname, Student1.rollno))
print("Full Name - {} {}, Roll No. - {}".format(Student2.firstname,
                                                Student2.lastname, Student2.rollno))
