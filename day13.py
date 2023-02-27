# strings are immutable
a = "!!!haRry!!!!!! !!!!!!!! Harry"
print ( len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("haRry","John"))
print(a.split(" "))

blogHead= "introduction tO Js"
print(blogHead.capitalize())

str1 ="Welcone to console!!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 ="Welcone to console!!!!"
print(str1.endswith("!!!!"))

print(str1.endswith("to", 4, 10))

str1 = "He named DAN. HE cannot do this "
# find first occurence 
print(str1.find("iss"))
# index same as find but gives error if not found
print(str1.index("is"))

str1 = "WelcomeToTheConsole"
# alphanumeical
print(str1.isalnum())
print(str1.islower())


str1 = "We wish you a Merry Christmas\n"
# \n is not printable
print(str1.isprintable())

str1 = "       "       #using Spacebar
print(str1.isspace())
str2 = "                "       #using Tab
print(str2.isspace())


str1 = "World Health Organization"  #first word of title is capital
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
# lowercase to upper and vice versa
print(str1.swapcase())


# title method convert string into title case 
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())