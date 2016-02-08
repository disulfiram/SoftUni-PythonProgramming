class Figure:
    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def __str__(self):
        return "Figure - center_x={} , center_y={}, color={}".format(
            self.center_x,
            self.center_y,
            self.color
        )

f = Figure(10, 20, 'red')
print(str(f))
print(f)
print("This is a {}".format(f))