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

# Object
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