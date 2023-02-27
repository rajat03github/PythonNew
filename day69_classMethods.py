class Employee:
    company = "Apple"

    def show(self):  #instance var
        print(
            f"The name is {self.name} and the company name is {self.company}")

    #Lets change the company

    @classmethod  #this is a decorators
    def changeCompany(cls, newCompany):
        cls.company = newCompany

    # by default first argument is instance but with class method
    # the first method is now the class

    # now the real class component is changed


e1 = Employee()
e1.name = "Harry"
e1.company = "Daddy"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)