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