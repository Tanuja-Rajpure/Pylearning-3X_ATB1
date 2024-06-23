t1 = tuple(["TheTestingAcademy", "For", "TheTestingAcademy"])
print(set(t1))


for i in t1:
    print(i)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print("Set after union:", my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print("SET intersection:", my_set)

my_set = set1.difference(set2)
print("set1.difference:", my_set)
my_set = set2.difference(set1)
print("set2.difference:", my_set)

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(set1)
print(len(set1))
set1.remove(5)
print(set1)
print(len(set1))

set1.add(100)
print(set1)
set1.pop()  # pop remove first item
print(set1)

