# public private protected


class Employee:
    #by default ~ public
    def __init__(self):
        self.__name = "Harry"


# " __ " double underscores are used

a = Employee()
a.emp1 = 5
# print(a.__name) #cannot be accesed directly
print(a._Employee__name)  # can be accessed indirectly
print(a.__dir__())
