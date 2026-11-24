name = input("Enter your name: ")
print(type(name))

age = input("Enter your age: ")
age = int(age)

height = input("Enter your height: ")
height = float(height)

print("----- User Information -----")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Next year age: {age + 1}")