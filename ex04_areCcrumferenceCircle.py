# Description: This program calculates the area and circumference of a circle given the radius.

import math

radius = float(input("Please input the radius of the circle: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print("The area of the circle is: ", round(area,2))
print("The cirumference of the circle is: ", round(circumference,2))