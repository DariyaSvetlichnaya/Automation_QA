from lesson_8.my_classes.round.round import Round

class Circle(Round):
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle("Circle", 3)
print(circle.name)
print("Area:", circle.area())