# lambda

# def double(x):
#     return x * 2

# function in function


def appl(fx, value):
    return 6 + fx(value)


double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y: (x + y) / 2

print(double(5))
print(cube(4))
print(avg(3, 5))

print(appl(cube, 2))
# 6 + cube of 2

# can also be used as this as square ( ANONYMS )
print(appl(lambda x: x * x, 2))