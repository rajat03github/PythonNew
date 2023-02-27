# strings slicing and oprtns
names = "rajat,Rohit"
# strings mei se index lelo
# 0 se 5 tk print krega 5th index ko nhi kia hai 

print(names[0:5])
# for length of string we use len
print(len(names))

fruit = "MANGO"
print(len(fruit))

# for slicing we use [ ] brackets

print(fruit[0:4])
print(fruit[2:4])
# automatically 0 lagalega
print(fruit[:4])
# kuch nhi toh lenth of fruit lag jaayegi 
print(fruit[:])
# print(fruit[0:-3])
print(fruit[0: len(fruit)-3])

print(fruit[-1:-3])
# 5-3:5-1 = 2:4  "NG"
# include 2 but not 4  
print(fruit[-3:-1])

# nm = "Harry"
# print(nm[-4:-2])