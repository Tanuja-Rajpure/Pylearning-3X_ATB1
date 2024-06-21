# tuple
x = 10
q, w, e = (45, 56, 67)  # Unpacking of the tuple
print(q)
print(w)
print(e)

# serach in tuple

# cities = ()"London" , "Paris", "Los ANgeles", "Tokyo")

t = (13, 23, 44)
# t.append() # tupes are immutable -> AttributeError: 'tuple' object has no attribute 'append'

new_t = t + (4,)
print(new_t)

# Convert to list- as list is muttable in nature

my_list = list(t)
print("Tyuple converted to list: ", my_list)
my_list.append(88)
print("Final List:", my_list)

