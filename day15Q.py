import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if(hour<12):
    print("Good Morning Sir")
elif(hour>12 and hour<17):
    print("Good Afternoon Sir")
elif(hour>17 and hour<19):
    print("Good Evening Sir")
else:
    print("Good Night Sir")
