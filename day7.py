a= int (input("Enter the value of first number: "))
b= int (input("Enter the value of Second number "))

d= input("Enter the operators for calculation ")

if (d == "+"):
    print(a+b)
elif (d == "-"):
    print(a-b)
elif (d == "*"):
    print(a*b)
elif (d == "/"):
    print(a/b)
else:
    print("You have enter wrong operator, please renter coorect operator")