class Employee:

    No_of_employees = 0
    increment = 2

    def __init__(self,ID,first_name,last_name,salary):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Employee.No_of_employees +=1
    def salary_increment(self):
        self.salary = int(self.salary * self.increment)
    @classmethod
    def change_salary_increment(cls,amount):
        cls.increment = amount


E01 = Employee('E01','Karam','G',55000)
E02 = Employee('E02','Param','G',65000)

E01.salary_increment()
print(E01.salary)
Employee.change_salary_increment(3)
E02.salary_increment()
print(E02.salary)
