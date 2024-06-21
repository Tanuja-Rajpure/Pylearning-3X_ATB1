# List - COllection of items

my_list = [1, 2, 3]
my_list2 = [1, True, "Tanuja", 3.14]

print("Element at index 0 : ", my_list[0])

my_list[0] = 20
print("List after changing element at index 1:", my_list)

my_list.append(90)
print("List after appending a value is :", my_list)

my_list.extend([22, 90])
print("List after extend is : ", my_list)

my_list.insert(1, 'a')
print("List after insertion is :", my_list)

my_list.remove(90)  # It will remove only first found item
print("Final List after removal: ", my_list)

my_list.remove('a')
print(my_list)

my_copy_list = my_list.copy()
print("my_copy_list is:", my_copy_list)

my_list.clear()
print("Initial List", my_list)
print(my_copy_list)

#print("Index of 3 in the list: ", my_list.index(3))  #ValueError: 3 is not in list

my_copy_list.sort()
print("My sorted list", my_copy_list)