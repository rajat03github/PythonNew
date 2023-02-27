# MAP


def cube(x):
    return x * x * x


print(cube(3))

l = [1, 2, 3, 4, 5]
print(l)

newl = map(cube, l)
print(newl)  # will return map

newl = list(map(cube, l))
print(newl)


# FILTER
def filter_function(a):
    return a >= 4


# grater then 4 di toh true warna false

newnewl = list(filter(filter_function, l))
print(newnewl)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# numbers = [ 15]


# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
    return x + y


sum = reduce(mysum, numbers)
produce = reduce(lambda x, y: x * y, numbers)

# Print the sum
print("the sum is: ", sum)
print("the product is :", produce)
