from lesson_8.my_classes.polygon.polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, name, length, width):
        super().__init__(name, sides=4)
        self.length = length
        self.width = width

    # Encapsulation: Area is calculated internally without exposing details
    def area(self):
        return self.length * self.width
