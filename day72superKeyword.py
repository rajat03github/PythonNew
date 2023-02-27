# Super Method in class
class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):

    def __init__(self, name, id, lang):
        # super().__init__( name, id)
        self.lang = lang
        super().__init__(name, id)


rohan = Employee("ROHAN ", "3232")
ron = Programmer("RAN ", "3232", "Python")

print(ron.id)
print(ron.name)
print(ron.lang)