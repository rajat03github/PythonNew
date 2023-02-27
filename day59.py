#DECORATORS
# take function as argument then decorate as modified returned
def greet(fx):

    def mfx(*args, **kwargs):
        # args takes argument as tuple
        #kwargs takes argument as dictonary
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


# def greet(fx):

#     def mfx():
#         print("good morning")
#         fx()
#         print("thanks for using this function")

#     return mfx

# @greet  # decorator
# def hello():
#     print("hello world")

# greet(hello()) this is same thing as @


def add(a, b):
    print(a + b)


greet(add)(1, 2)

# hello()
