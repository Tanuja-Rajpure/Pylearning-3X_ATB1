# tuple
# Real time us-
#Tuples used for list of API Urls
API_URLS = ("www.gmail.com", "www.yahoo.com", "www.facebook.com")
print(API_URLS[0])
print(API_URLS[1])
print(API_URLS[2])

#*************************************************************

#tuple can also be created by using a function tuple
t = tuple()
print("This tuple is empty", t)

t1 = tuple(["Pramod", "Amit", "Rocky"])
print("This is conversion of list to tuple", t1)

del t
#print(t)



#*******************************************************************
x = 10
q, w, e = (45, 56, 67)  # Unpacking of the tuple
print(q)
print(w)
print(e)

# serach in tuple

# cities = ()"London" , "Paris", "Los ANgeles", "Tokyo")

t = (13, 23, 44)
# t.append() # tupes are immutable -> AttributeError: 'tuple' object has no attribute 'append'

new_t = t + (4,)  # , required- TypeError: can only concatenate tuple (not "int") to tuple
print(new_t)

# Convert to list- as list is muttable in nature

my_list = list(t)
print("Tuple converted to list: ", my_list)
my_list.append(88)
print("Final List:", my_list)
new_t2 = tuple(my_list)
print("New Tuple", new_t2)

