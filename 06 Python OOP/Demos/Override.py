class Figure:
    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def scale(self, scale_factor):
        # nothing to do here - scaling does not affect center coordinates
        pass


class Circle(Figure):
    def __init__(self, center_x, center_y, radius, color='black'):
        super().__init__(center_x, center_y, color)
        self.radius = radius

    def scale(self, scale_factor):
        super().scale(scale_factor)   # it is a GOOD idea to always call the super() method
        self.radius = self.radius * scale_factor