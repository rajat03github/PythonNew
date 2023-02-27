# strings
name = "harry"
friend = " bieber "
anotherdost = ' justin '
apple = " he said, \"I want to eat an apple"
# this method of taking quote can also work
apple = 'he said, "I want to eat an apple'
print("hello "+ name)
print(apple)

# multiline ke liye ''' use krne hote hai
multiline = '''YEH HAI EK 

multiple

line ka 
example hai 
'''
print(multiline)
# here 0 is index
print(name[0]) 
print(name[1]) 
print(name[2]) 
print(name[3]) 
print(name[4]) 
# now there no 5th index so it will give error
# print(name[5]) 
# print(name[6]) 

# for in loop with strings

print("LETS USE A FOR LOOP\n")
for character in apple:
    print(character)

