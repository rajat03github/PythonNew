

# reading lines

f = open('myfile.txt', 'r')
i = 0
while True:
    # read line reads by line by line
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"marks of student {i} is: {m1*2} ")
    print(f"marks of student {i} is: {m2*2} ")
    print(f"marks of student {i} is: {m3*3} ")
    print(line)

# WRITING 
    
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3']
f.writelines(lines)
f.close()