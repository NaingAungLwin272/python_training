#   1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def pname(self):
        print(self.firstname)


class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


p = Employee("Naing", "Aung Lwin")
p.pname()


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
