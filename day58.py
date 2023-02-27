# constructors
class Person:

    # constructor
    def __init__(self, n, o):
        print("hey this is constructor")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Harry ", "rocket")
b = Person("DIVYA ", "Hr")
# print(a.name)
# a.name = "DIVYA"
# a.occ = "HR"
# a.info()
a.info()
# b.occ

c = Person("mera", "kaam")
