
list = [1, 2, 2, 3 ,4]
tuple = (1, 2, 2, 3, 4)
set = {1, 2, 2 ,3 ,4}
dict2 = {"key" : "value"}

print("List Syntax: ", list)
print("Tuple syntax: ", tuple)
print("Set syntax: ", set)
print("Dictionary syntax: ", dict2)

dict1 = {"name" : "Pramod", "age" : 45, "Address" : "Banglore"}
print(dict1)

print(dict1["name"])

Person_details = dict(name = "Pramod", age = 45, Address = "Banglore")
print(Person_details)

print(Person_details.get("Address"))
print(Person_details["Address"])
print(Person_details.keys())
print(Person_details.values())

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)

for k,v in dict1.items():
    print(k, ":" , v)