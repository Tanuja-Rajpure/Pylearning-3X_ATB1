# How to double values in list

list1 = [1, 2, 3, 4, 5]
# print(list*2)
temp_list = []
for i in list1:
    temp_variable = i * 2
    temp_list.append(temp_variable)
print(temp_list)

my_list = [1, 2, 3, 4, 5]
#***********************************************
#Use map() function to double each item from list
def double_item(num):
   return num * 2

#double_item = lambda num : num * 2  # Above def function can also be replcaed with lambda fun

# Map () function
# 1. Take each item form list
# 2. Execute function on it
# 3. Return same number of elements (list)

double_list = list(map(double_item, my_list))
print("Double item list is :", double_list)
