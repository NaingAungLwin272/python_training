#   1
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def pname(self):
        print("First name of employee is " + self.fname)


emp = Person("Naing", "Aung Lwin")
emp.pname()


class Employee(Person):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)


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
