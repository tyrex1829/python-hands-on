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

account1 = BankAccount("John Doe", 1000);
print(account1.get_balance())
print(account1.deposite(500))