class Figure:
    def __init__(self, position, color):
        print("Position: ", position)
        print("Color: ", color)

figure = Figure((0, 0), 'black')   # параметрите, подадени при създаване на инстанция, се предават на __init__()