import math
class Area_Circle:
    def __init__(self, radius):
        self.radius = radius
    def areaofcircle(self):
        area = float(math.pi* self.radius * self.radius)
        return area
    def perimofcircle(self):
        perimeter = float(math.pi* 2 * self.radius)
        return perimeter

#take input from
radius1 = float(input("radius of circle:"))
p1_obj = Area_Circle(radius1)
area_res = p1_obj.areaofcircle()
print("Area of Circle", area_res)
perim_res = p1_obj.perimofcircle()
print("Perimeter of circle", perim_res)
