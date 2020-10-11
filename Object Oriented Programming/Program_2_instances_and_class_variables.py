class Student:

    total_students = 0

    def __init__(self, firstname, lastname, rollno, math_marks,eng_marks, sci_marks):
        self.firstname = firstname
        self.lastname = lastname
        self.rollno = rollno
        self.math_marks = math_marks
        self.eng_marks = eng_marks
        self.sci_marks = sci_marks

        Student.total_students +=1

    def Percentage(self):
        self.percentage = (self.math_marks+self.eng_marks+self.sci_marks)*100/300
        return self.percentage


print("No of Students : {}".format(Student.total_students))

print("Adding students data")

student1 = Student("Karam", "Gajbhiye", "S21", 76, 80, 78)
student2 = Student("Param", "Gajbhiye", "S27", 85, 84, 75)


print("Full Name - {} {}, Roll No. - {}, Math Marks : {}, English Marks : {}, Science Marks : {}".format(student1.firstname,
                                                student1.lastname, student1.rollno,student1.math_marks,student1.eng_marks,student1.sci_marks))
print("Full Name - {} {}, Roll No. - {}, Math Marks : {}, English Marks : {}, Science Marks : {}".format(student2.firstname,
                                                student2.lastname, student2.rollno,student2.rollno,student2.math_marks,student2.eng_marks,student2.sci_marks))

S01_Perc = student1.Percentage()
S02_Perc = student2.Percentage()
'''
OR
S01_Perc = Student.Percentage(student1)
S02_Perc = Student.Percentage(student2)'''
print("Student {} {} has got {} %.".format(student1.firstname,student1.lastname, S01_Perc))
print("Student {} {} has got {} %.".format(student2.firstname,student2.lastname, S02_Perc))
#print(Student.__dict__)
#print(Student1.__dict__)

print("No of Students : {}".format(Student.total_students))