class Employee:
    name = "John"
    pay = "2000"


e1 = Employee()
e2 = Employee()

print(Employee.__dict__)

# modification of class variables w.r.t class name
Employee.name = "Tom"
print(Employee.__dict__)
print(e1.name)      # Tom

# modification of class variables w.r.t object
e1.name = "Ram"
print(e1.name)          # ram
print(Employee.name)    # Tom

# modification of class variables w.r.t class name
Employee.name = "Steve"
print(e1.name)          # ram
print(Employee.name)    # Steve
print(e2.name)

