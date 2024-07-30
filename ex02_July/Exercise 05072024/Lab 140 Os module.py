# OS Module

# Used to interact multiple systems

# Get working dir, change dir, file exist? change file name, size file, env ariable available?

import os

print(os.name)
# nt -> windows system, posix- Unix system

print(os.getcwd())

print(os.listdir())

# os.mkdir("Tanuja")

# FOr read file, first check if already exist the file
size = os.path.getsize('testdata.txt')
print(size)

if size != 0:
    print("Exist")
else:
    print("No content")

mtime = os.path.getmtime('testdata.txt')
print(mtime)
