#   1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


p = Employee("Naing", "Aung Lwin")
p.printname()


#   2
class Mynumbers:

    def __iter__(self):
        self.l = [*range(1, 11)]
        return self

    def __next__(self):

        value = self.l
        return value


myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
