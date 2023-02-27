#for 73
#DUNDER METHODS


class Employee:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):  #Super Method
        return f"The name of employee is {self.name}"

    def __call__(self):
        print("Hey I am good")