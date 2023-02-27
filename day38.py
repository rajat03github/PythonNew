# Raising custom errors

a = int(input("enter any value btwn 5 and 9"))

if (a < 5 or a > 9):
    raise ValueError("value should be btwn 5 and 9")

'''
class CustomError(Exception):
  # code ...
f  pass

try:
  # code ...

except CustomError:
  # code...
'''

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
