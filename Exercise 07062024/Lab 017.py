# List = Shopping List
# milk, butter, poha
# 1. Add list
# 2.  Remove list
# 3.   Update list
# 4.   View list
# 5.   Exit

shopping_list = ["milk" , "butter" , "poha"]
print (shopping_list)
print (len(shopping_list))
print (type(shopping_list))
print (shopping_list[0])

shopping_list.append("chocolate") # add item to list
print (shopping_list)

shopping_list.insert(2,"chips") # add item to list in between
print (shopping_list)

shopping_list.remove("chocolate") # remove item from list
print (shopping_list)

print(shopping_list.pop()) # remove last item from list
print(shopping_list)

print(shopping_list.index("butter")) # Index start from 0 , lenght start from 1

shopping_list.reverse()
print (shopping_list)