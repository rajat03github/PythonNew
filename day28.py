# f strings
letter = " hey my name is {} and i am from {}"
country= "INDIA"
name = "harry "

# this is a feature of old python
print(letter.format(name,country))

# f string


print(f"hey my name is {name} and i am from {country}")

# as it is {{}}
print(f"We use f string like this hey my name is {{name}} and i am from {{country}}")

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))


price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))