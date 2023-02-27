# INHERITANCE in python
class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee is: {self.id} is {self.name}")


# inheriting
class Programmer(Employee):

    def showLanguage(self):
        print("the default lang is python")


# class with inhertied class
class Programming(Programmer):

    def showLANG(self):
        print("the default lang is progam")


e = Employee("rohan das", 420)
e.showDetails()

e1 = Programmer("vodka ", 600)
e1.showDetails()
e1.showLanguage()

e2 = Programming("pista ", 999)
e2.showDetails()
e2.showLanguage()
e2.showLANG()
