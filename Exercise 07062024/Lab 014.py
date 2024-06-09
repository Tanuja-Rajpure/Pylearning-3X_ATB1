#strings
# Bunch of characters
# In built functions
# If want to repeat a task- use function
# we have used still - print , sum, input, type, max, input, format,
# In python String are immutable

# Important string fuctions

name = "Amit"  # it is indexed from 0 to leng-1
print(name)
print(f'Name is = {name}')

print(type(name))
print(f'Type of Name is = {type(name)}')

print(id(name))  # id- given memory location of the variable
print(f'Id of name is = {id(name)}')

print(len(name))  # length of the string always start from 1 and not from 0
print(f'Length of name is = {len(name)}')

name = name.upper()
print(f'Upper case name= {name}')

a = name.count('a')
print(f'Count of a= {a}')

a = name.count('A')
print(f'Count of A= {a}')

name = name.lower()
print(f'Lower case name= {name}')

name = "Amit"

namei0 = name.index('A')
namei1 = name.index('m')
namei2 = name.index('i')
namei3 = name.index('t')
print(f'Index of A= {namei0}',  f'Index of m= {namei1}', f'Index of i= {namei2}', f'Index of t= {namei3}')

name = "Amit"
a = name.count('M') # Python is case sensative language
a1 = name.count('m')
a3 = name.count('A')
print(f'Count of M = {a}')
print(f'Count of m = {a1}')
print(f'Count of A = {a3}')

#index of name
print(name[0])
print(f'Value at index 0 is = {name[0]}')
print(f'Value at index 1 is = {name[1]}')
print(f'Value at index 2 is = {name[2]}')
print(f'Value at index 3 is = {name[3]}')
#print(f'Value at index 4 is = {name[4]}') IndexError: string index out of range

#Strings are immutable- can't be chaanged
name = "Amit"
name[0] = "P"
print(name[0]) #TypeError: 'str' object does not support item assignment

