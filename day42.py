# Enumerate Function

marks= [12 , 56 , 32 ,98, 12 ,45]


# 98 k upar aane ke liye start =1 krdo 
for index , mark in enumerate( marks, start=1):
    print(mark)
    if(index == 3):
        print("Harry, awesome !")
    index = index+1