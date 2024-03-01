from hw_8.my_classes.polygon.polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, name, length, width):
        super().__init__(name, sides=4)
        self.length = length
        self.width = width

    # Encapsulation
    def area(self):
        return self.length * self.width


rectangle = Rectangle("Rectangle", 6, 4)
print(rectangle.display_info())
print("Area:", rectangle.area())
