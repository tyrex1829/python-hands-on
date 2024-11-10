"""  Logic building file to get use to for python code  """

x = 0
y = "name"

x = y
y = x

print(x, y)

# 

def print_name ():
    a = ["name", "age", "post"]
    return a

ans = print_name()
ans[0] = "tyrex"
print(ans[0])

# 

object = {
    "name": "person",
    "age": "28"
}

print(list(object.keys())[0])

# Reverse a string

def reverseEachWordOfTheString(name):
    nameToList = list(name)
    nameToList.reverse()
    reversedName = "".join(nameToList)
    return reversedName

ans = reverseEachWordOfTheString("tyrex")
print(ans)

# read text file content

a = open("../txt.txt","r")
print(a.read())

# Write to a txt file

writeToFile = open("../txt.txt", "w")
writeToFile.write("because 10x aint enough")

# All methods of sets

my_set = {1, 2, 3}
my_set.pop()
print(my_set)

my_set.add(4)
print(my_set)

my_set.update([5])
print(my_set)

# 

# names=["Saksham", "Ankit", "Tyrex"]
# with open("./operations.py", "w") as file:
#     file.write('/n'.join(names) + '\n')

# 

with open("../txt.txt", "r") as input_file, open("../capitalized_names.txt", "w") as output_file:
    for line in input_file:
        capitalized_name = line.strip().capitalized()
        output_file.write(capitalized_name + "\n")
print("done")

# Classes

class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 
    def introduce(self):
        return f"Hey, this is {self.name}, age: {self.age}."

person1 = Person("Tyrex", 24)

print(person1.introduce())

# Encapsulation -> Data Hiding By Using underscore prefixes
# Single Underscore -> _ -> Protected Attribute -> no direct access
# Double Underscore -> __ -> Private Attribute -> no access directly outside of class

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._account_type = "Savings"
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposite(self, amount):
        if amount < 0:
            return "Invalid deposite amount"
        self.__balance += amount
        return f"{amount} deposited. New balance is {self.__balance}"

account1 = BankAccount("John Doe", 1000)
print(account1.get_balance())
print(account1.deposite(500))

# Class Variables and Instance Variable
# Class Variable -> Shared across all instances of a class, Defined outside of any method
# Instance Variables -> Specific to each instance object.

class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

human1 = Human("Tyrex")
human2 = Human("Saksham")

print(human1.species)
print(human2.species)

Human.species = "Homo sapiens sapiens"

print(human1.species)

# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "can speak"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
dog = Dog("Buddy")
print(dog.speak())

# Polymorphism -> Compile time polymorphism and Run time polymorphism

class Bird:
    def sound(self):
        return "Chirp Chirp"
    
class Dog:
    def sound(self):
        return "Bark Bark"
    
def make_sound(animal):
    print(animal.sound())

bird = Bird()
dog = Dog()

make_sound(bird)
make_sound(dog)

# Type hints with classes

class Student:
    def __init__(self, name: str, grade: float):
        self.name: str = name
        self.grade: float = grade

    def get_grade(self) -> float:
        return self.grade
    
student1 = Student("Tyrex", "9.5")
print(student1.get_grade())

# Type hints

def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("Tyrex"))
print(greet(123))

checkTypeHintInCompileTime: str = "My Name"
checkTypeHintInCompileTime = 123
print(checkTypeHintInCompileTime)

# map filter find

numberList = [1, 2, 3, 4]

# squaredList = map()

ress = map(str, numberList)
print(list(ress))

# Calculator class 

class Calculator:
    def __init__(self):
        pass
    
    def addition(self, a: int, b: int) -> int : 
        return a + b

    def subtraction(self, a: int, b: int) -> int :
        return a - b

    def multiplication(self, a: int, b: int) -> int :
        return a * b
    
    def division(self, a: int, b: int) -> int :
        if b == 0:
            return f"can't complete the operation because of {b}"
        return a / b

operation = Calculator()
add = operation.addition(5, 1)
sub = operation.subtraction(5, 1)
mul = operation.multiplication(5, 1)
div = operation.division(5, 1)
div2 = operation.division(5, 0)
print(add)
print(sub)
print(mul)
print(div)
print(div2)

# Inventory system

class Inventory:
    name: str
    quantity: int
    price: float

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def addMoreItem(self, name, quantity, price):
        pass

