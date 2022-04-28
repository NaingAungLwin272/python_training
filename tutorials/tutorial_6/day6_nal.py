#   1
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def pname(self):
        print("First name of employee is " + self.fname)


p = Person("Aung", "Naing Lwin")
p.pname()


class Employee(Person):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)


emp = Employee("Naing", "Aung Lwin")
emp.pname()


#   2
l = [*range(1, 11)]
numbers = l.__iter__()
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
