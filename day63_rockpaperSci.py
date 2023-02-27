import random  #use to random integers


def check(comp, user):
    if (comp == user):
        return 0
    if (user == 2 and comp == 0):
        return -1
    if (user == 1 and comp == 2):
        return -1
    if (user == 1 and comp == 0):
        return -1

    return 1


comp = random.randint(0, 2)
user = int(input("0 for rock , 1 for paper and 2 for scissors :\n"))

score = check(comp, user)

print("You:", user)
print("Computer:", comp)

if (score == 0):
    print("its a draw")
elif (score == 1):
    print("You won")
else:
    print("you lose")

#
'''
0rock beats 2sci
2sci beats 1paper
1paper beats 0rock
'''