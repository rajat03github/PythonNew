# tuple
# similar tot list but cant be changed
tup=(1, 5, 6, "green", True)
print(type(tup), tup)
# list is brackets
# tup=[1, 5, 6]
# print(type(tup), tup)
# we have to put comma in tuple
# tup=(1, )
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

print(tup[-3])
print(len(tup))

if 342 in tup:
    print("presnt")
else:
    print("nos")

# tup slicing is also same first will be accesed and last will be sliced
tup2 = tup[1:4]
print(tup2)