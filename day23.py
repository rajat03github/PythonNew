# list methods
l = [1 ,2,  3, 4 ,5]
print(l)
# append adds in the end
# l.append(7)
l.sort()
# descnding order
l.sort(reverse=True)
# revert original list
l.reverse()
# value 3 is presnet at which indexs
print(l.index(3))
print(l.count(3))
# if we change m . l is changed
m = l
# this will make copy
m = l.copy()
m[0] = 0
# inserting 899 at index 1
l.insert(1,899)
m =[ 900,  1000, 11100]
# l.extend(m)
k = l + m
print(k)
print(l)
