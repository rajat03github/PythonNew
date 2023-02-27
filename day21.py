# def average(a, b):
#     print("The average is ", (a+b)/2)

# average(4,6)

# average(b =9 , a= 21)

def average(*numbers):
    # this is tuple no matter how much we pass
    # print(type(numbers))
    sum = 0;
    for i in numbers:
        sum = sum + i;
    # print("average is " , sum / len(numbers))
    return  sum / len(numbers)

c = average(4,6)
print(c)

def name(**name):
    # this is dictionary
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")