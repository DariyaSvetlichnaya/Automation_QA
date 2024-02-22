from homework_8.my_classes.shapes import Shapes


class Polygon(Shapes):
    def __init__(self, name, sides):
        super().__init__(name)
        self.sides = sides

    def display_info(self):
        return f"{self.name} - Sides: {self.sides}"

    # Polymorphism
    def area(self):
        return "Cannot calculate area of a generic polygon."



