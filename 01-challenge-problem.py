class Point:
    # coordX -> x, coordY -> y
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    # starting_point -> origin, broad -> width, high -> height
    def __init__(self, starting_point, broad, high):
        self.starting_point = starting_point
        self.broad = broad
        self.high = high

    # area -> get_area
    def area(self):
        return self.broad * self.high

    # end_points -> print_coordinates
    def end_points(self):
        top_right = self.starting_point.coordX + self.broad
        bottom_left = self.starting_point.coordY + self.high
        print('Starting Point (X)): ' + str(self.starting_point.coordX))
        print('Starting Point (Y)): ' + str(self.starting_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))

# build_stuff -> build_rectangle
def build_stuff():
    # main_point -> rectangle_origin
    main_point = Point(50, 100)
    # rect -> rectangle
    rect = Rectangle(main_point, 90, 10)

    return rect


# my_rect -> rectangle
my_rect = build_stuff()

print(my_rect.area())
my_rect.end_points()
