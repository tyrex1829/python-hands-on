# Variables
x = 5
y = "hello"

print(x)
print(y)

# Data Types
name = "Tyrex"
age = 30
isVote = True

print(name)
print(age)
print(isVote)

# If Else
if x > 1:
    print("Big")
elif x > 0:
    print("Positive")
else:
    print("negative")

# Functions
def greet(name):
    return f"Hello! {name}"

print(greet(name))

# Object -> Dictonaries
person = {
    "name": "tyrex",
    "age": 24
}

print(person)
print(person["name"])
print(person["age"])

# Classes
class Car:
    def __init__(self, model):
        self.model = model

myCar = Car("Benz")
print(myCar.model)

# Arrays
fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])

# Scope of variable
x = 10

def my_function():
    y = 5
    print(y)

my_function()
print(x)

# Floor division
result = 10 // 3
print(result)

# List
numberss = [1, 2, 3]
numberss.append(4)
numberss.insert(1, 9)
print(numberss[-1]) # Last element
print(numberss[-2]) # Second last element
print(numberss)

# Set
unique_values = {1, 2, 2, 2, 3, 3, 3}
unique_values.discard(10)
print(unique_values)