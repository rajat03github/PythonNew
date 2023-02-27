# instance and class variables
class Employee:
    noOfEmployees = 0
    companyName = "Apple"  # this is class variable

    def __init__(self, name):
        self.name = name
        self.raiseAmount = 0.02
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(
            f"the name of the employee is {self.name} and the amonunt raise is {self.raiseAmount} and the company name is {self.companyName} employee no {self.noOfEmployees}"
        )


# Employee.showDetails(emp1)

emp1 = Employee("Harry")
emp1.raiseAmount = 0.44  # this is instance vairable

emp1.companyName = "APlleIndia"  # this will instance and change for emp1
emp1.showDetails()  #emp1 jaa rha hai as argument

Employee.companyName = "Google"  # this will change for class

emp2 = Employee("Rohan")
emp2.companyName = "NESTLE"

emp2.showDetails()  #emp1 jaa rha hai as argument
