from .base import Shape

class Rectangle(Shape):

    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw(self, turtle):
        half_height = self.height/2
        half_width = self.width/2
        top = self.center_y + half_height
        left = self.center_x - half_width

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)

        for _ in range(4):
            if(_ % 2 == 0):
                turtle.forward(self.height)
                turtle.left(90)
            else:
                turtle.forward(self.width)
                turtle.left(90)