# match case statements 

x = int(input("enter value of x"))
# x is the variable to match

# here we dont need an break statement
match x:

    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case _ if x == 90 :
        print("x is 90")
        
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")

    # default case(will only be matched if the above cases were not matched)

    # so it is basically just an else:
    case _:
        print(x)
