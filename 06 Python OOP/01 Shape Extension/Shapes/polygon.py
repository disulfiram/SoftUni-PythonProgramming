import math
from .base import Shape


class Polygon(Shape):

    def __init__(self, radius, n, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.n = n

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y + self.radius)
        turtle.pendown()
        turtle.color(self.color)

        rotation_angle = 360//self.n
        side = math.sqrt(2*math.pow(self.radius, 2) - 2*math.pow(self.radius, 2)*math.cos(math.radians(rotation_angle)))
        turtle.right(180-(rotation_angle/2))
        for _ in range(self.n):
            turtle.forward(side)
            turtle.left(rotation_angle)
