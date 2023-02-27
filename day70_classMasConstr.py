class Emploee:

    def __init__(self, name, salary):
        self.name = name
        self.salarty = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


string = "Rajat-120000"
e = Emploee.fromstr(string)

# e = Emploee(string.split("-")[0], string.split("-")[1])
print(e.name)
print(e.salarty)