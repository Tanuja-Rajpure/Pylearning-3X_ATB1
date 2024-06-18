# WATCHING 14 June recording:
# For loops used for range (Range will be given till n-1

for counter in range(0, 100):
    print(counter)

for even_number in range(0, 100, 2): # here 2 is range , it can be -ve as well
    print(even_number)

for i in range(20,0,-5):
    print(i)

for odd_number in range(1, 100, 2):
    print(odd_number)

for i in range(0, 100):
    print(i)
    if i == 5:
        break # When used- Logic to get out from loop break used
print("Outside of the programme")
