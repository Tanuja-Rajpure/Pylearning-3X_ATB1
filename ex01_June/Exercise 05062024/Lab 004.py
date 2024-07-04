print("Hi, I am Tanuja", "Rajpure")
print("Hi, I am Tanuja", "Rajpure", sep=' - ')
print("Hi", "My name i Tanuja ", "Rajpure")
print("Hi", "My name i Tanuja ", "Rajpure")
#  above end is not used so by default end is '\n' i.e new line . now lets add end but empty

print("Hi", "My name i Tanuja ", "Rajpure", end='')
print("From Pune") # here as end is empty notyhing is added.

print("Hi", "My name i Tanuja ", "Rajpure", sep='-', end=' ')
print("From Pune") # here sep used for 1st print command only
# We can have only one sep, one end in one command