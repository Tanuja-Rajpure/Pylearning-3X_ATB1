# Strings- set of characters enclosed in quotes
# '' , "" , ''' , """

name = "Amit"
print(name)

name = 'Amit'
print(name)

name = """AMit is good person
he has a dog
...
...
"""
# raw string -
dir = 'C:\nomedir\some dir'
print(dir)
dir = "C:\nomedir\some dir"
print(dir)
# with '' or "" we can use \n as new line, to print dir we need to use it as raw string
# raw string - C:\nomedir\some dir
dir = r'C:\nomedir\some dir'
print(dir)

# format of the string
first_name = "Tanuja"
last_name = "Rajpure"
print(first_name + " " + last_name)
print(first_name, last_name)

address = "Pune"

# f-> string - format string-used for formatting,
# {}-> Placeholder-It wll replace the value of the variables
print(f'My full name is {first_name} {last_name}' +  f'I live in {address}')
