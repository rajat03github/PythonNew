# break and continue
# for i in range(12):
#     # 0 se 10 tak i ki value hoga
#     if(i==10):
#         # break kahega is loop ko chorr kr nikl jaao
#         break
#     print("5 X " , i, " = ", 5 * (i))
# print("Loop ko chorrkr nikal gaya")

for j in range(12):
    # 0 se 10 tak i ki value hoga
    if(j==10):
        # continue kahega SKIP THE ITERTAION 
        continue
    # skip hogi pr next pe aajayega
    print("5 X " , j, " = ", 5 * (j))
print("ITERATION SKIPPED at i = 10")

# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")


i = 0;
while True:
    print(i)
    i = i + 1 
    if(i%100 == 0):
        break
