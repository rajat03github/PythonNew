# classes and objects


# class defined
class Person:
    name = "Justin Bieber"  #default values ~
    occupation = "Singer"
    salary = 2000000

    # self keyword~

    def info(self):
        print(f"{self.name} is a {self.occupation}")


#self = woh object jispe yeh method call ho raha hiann

# objects
a = Person()
a.name = "Shubham"
a.occupation = "Side assistant"

b = Person()
b.name = "Panda"
b.occupation = "HR"

print(a.name)
print(b.name)

a.info()
b.info()