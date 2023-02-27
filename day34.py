# dic methods
ep1 = {
    122: 45, 123: 22, 223: 55, 323: 29
}

ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
print(ep1)

# ep1.clear(ep2)
print(ep1)

# empty
empt = {}

# ep1.pop(122)
print(ep1)

# last key value pair is removed
# ep1.popitem()
del ep1[123]
# this will give error
# del ep1["123"]
print(ep1)
