# Polymorphism
# Allows objects of different classes to be treated as objects of common superclass

# Method Overloading -> Does it exist in Python?
# Method Overriding
# Same name in parent and child
# child always override parent functions
# Super means call to parent function

# METHOD OVERRIDING
class Shape:
    def area(self):
        print("Area of the Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3, 4)
shape1.area()
print(f'Area of rectangle is(l=3,b=4): {shape1.area()}')

shape2 = Circle(2)
shape2.area()
print(f'Area of circle is(r=2): {shape2.area()}')

shape3 = Shape()
shape3.area()
