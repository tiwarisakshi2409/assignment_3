# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)

area = circle.compute_area()
perimeter = circle.compute_perimeter()

print(f"The area of the circle is {area:.2f} square units.")
print(f"The perimeter (circumference) of the circle is {perimeter:.2f} units.")
