from lesson_8.my_classes.shapes import Shapes


class Round(Shapes):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        pass
