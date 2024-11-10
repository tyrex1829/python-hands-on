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

