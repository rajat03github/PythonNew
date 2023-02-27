# lists
# ek naam ke under multiple rakhne ke liye
marks =[3,5,6,"Hrrry"]
# list allow every type
print(marks)
# print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
# print(marks[4])


# print(marks[-2]) 
# print(marks[-3]) 
# len(marks)-2

if 6 in marks:
    print("yes")
else:
    print("no")

# same thing applies for string
if "ry" in "Harry":
    print("yes")

# print[0:(len(marks))]
print(marks[1:len(marks)-1])
print(marks[1:4-1])
print(marks[1:-1])
# in this index 1 will be added and index 1 2 will be shown but index 3 will be exluded
print(marks[1:3])
# in down last 2 is jump index
print(marks[1:4:2])


lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(4) if i%2==0]
print(lst)