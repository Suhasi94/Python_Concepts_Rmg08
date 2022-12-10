# # executing instance methods
#
# class Employee:
#
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#
#     # instance methods
#     def create_email(self):
#         print(f"{self.fname}.{self.lname}@company.com")
#
#     def display_details(self):
#         print(f"Emp name: {self.fname} {self.lname}, pay: {self.pay}")
#
#
# emp1 = Employee("bill", "gates", 2000)
# emp1.create_email()
# emp1.display_details()
#
# Employee.display_details(emp1)
#
# ########################################################################################
# class Employee:
#     company = "Amazon"
#
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#
#     @classmethod
#     def display_company(cls):     # cls --> class' address
#         print(cls.company)
#
#     def display_employee_details(self):     # self -> address of currently invoking object's address
#         print(f"Emp name: {self.fname} {self.lname}, pay: {self.pay}")
#
#
# emp1 = Employee("bill", "gates", 2000)
# emp2 = Employee("bill", "gates", 20000)
# Employee.display_company()
# emp1.display_company()
#
#

#########################################################################################
# creating an alternate constructor using classmethod

class Employee:
    company = "Amazon"

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @classmethod
    def from_string(cls, string):
        details = string.split("-")     # ["steve", "jobs", "2000"]

        return cls(details[0], details[1], details[2])


    def display(self):
        print(self.fname, self.lname, self.pay)

s = "steve-jobs-2000"
print(Employee.from_string(s))
# print(Employee.__dict__)

# s1 = Employee.from_string(s)
# s1.display()
# print(s1.fname)














