class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * float(self.radius) * float(self.radius)
        print(area)

    def perimeter(self):
        perimeter = 2 * 3.14 * float(self.radius)
        print(perimeter)

class Main:

    r = int(input("Enter the radius: "))

    c = Circle(r)

    c.area()
    c.perimeter()