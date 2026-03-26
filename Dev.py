new_dict = {}
for i in range (5):
    x = input("Create a key: ").lower()
    y = input("Create a value for that key: ").lower()
    new_dict[x]=y
print(new_dict)
z = input("Call a key: ")
print(new_dict[z])
a = input("What key and value would you like to delete: ").lower()
del new_dict[a]
print(new_dict)
print(len(new_dict))
check = input("Tell me a key and I shall check if it exits").lower()
if check not in list:
    print(new_dict)

second.update(new_dict)
