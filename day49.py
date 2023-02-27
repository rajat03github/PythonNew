# f = open('myfile.txt', 'r')
# # r is read 
# # rb is binary = jpg , etc
# #  w is write
# print(f)
# text = f.read()
# print(text)
# f.close()


# writing to a file 

# f = open('myfile.txt', 'w')
# f.write('Hello, world!')
# f.close()

f = open('myfile.txt', 'a')
f.write('\nHello, world!')
f.close()

with open('myfile.txt','a') as f:
    f.write("Hey i am inside with")