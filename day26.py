import time
hour = int(time.strftime('%H'))
name = input("Enter your name: ")
if (hour >= 5 and hour < 12):
  print("Good Morning", name)
elif (hour >= 12 and hour < 18):
  print("Good Afternoon", name)
elif (hour >= 18 and hour < 22):
  print("Good Evening", name)
else:
  print("Good Night", name)