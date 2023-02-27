# tuples oprtions
# this is how we can do mainpulations
# we convert in list and use list functions dircetly
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 2, 2, 31, 1, 3, 2, 3, 3)

# res= tuple1.count(3)

# print('count is ',res)
# res = tuple1.index(3)
# print('count is ',res)
# 4 to 7 slicing hogi fir usme 3 dundega 
# res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
print('count is ',res)
res = len(tuple1)
print('count is ',res)