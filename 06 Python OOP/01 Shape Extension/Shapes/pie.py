from .circle import Circle


class Pie(Circle):

    def __init__(self, arg_degrees, **kwargs):
        super().__init__(**kwargs)
        self.arg_degrees = arg_degrees

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x,self.center_y-self.radius)
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(self.radius, self.arg_degrees)
        turtle.goto(self.center_x, self.center_y)
        turtle.goto(self.center_x, self.center_y - self.radius)
