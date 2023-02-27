# seek

with open('sample.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    print(f.tell())  # will give position from where to read
    data = f.read(5)
    print(data)

with open('sample.txt2', 'w') as f:
    f.write('Hello World3!')
    # starting se kitna krna hai 5 ~ hello
    f.truncate(5)

with open('sample.txt2', 'r') as f:
    print(f.read())
