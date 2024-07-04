# File Handling
# Reading, writing file using file

# Pre defined function related to file in python
# 'r' for readig
# 'w' for writing
# 'a' for appending
# 'b' for binary mode. zoom.exe - binary
# '+' for updating (reading and writing)

# read and Write content
# Read a file
# reading entire content: content = file_object.read()
# line = file_object_readline() for a single line.
# lines = file.object.readiness()   for all lines in list.
# Close the file -
# Open file

file = open("text1.txt", "r")
content = file.read()
print(content)
file.close()

# Read file from another folder
file = open("C:\Users\Anna Rajpure\PycharmProjects\Pylearning 3XATB\ex02_July\Exercise 01072024\TestData2.txt", "r")
# file = open('testData2.txt', 'r')  # FileNotFoundError: [Errno 2] No such file or directory: 'testData2.txt'
content = file.read()
print(content)
file.close()
