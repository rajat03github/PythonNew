#global and local variables

x = 4
print(x)

def hello():
    x=5
    print(f"the global x is {x}")
    print(x)
    print("hello harry")


print(f"the global x is {x}")
hello()
print(f"the global x is {x}")



def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function