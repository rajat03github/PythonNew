# dictonary

info = {"HARRY" : " HUMAN"}

print(info["HARRY"])

# here harry is key amnd value is human
info = {'name':'Karan', 'age':19, 'eligible':True}
# this will give error
# print(info['name2'])
# this will not give error
# print(info.get('name2'))

print(info.values())

# to get all keys 
for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")