class Math:

    def __init__(self, num):
        self.num = num

    def addToNum(self, num2):
        self.num = self.num + num2

    @staticmethod  #no self is needed
    def add(a, b):
        return a + b


# result = Math.add(1, 2)
# print(result)

a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)

print(Math.add(6, 12))
print(a.add(65, 12))
