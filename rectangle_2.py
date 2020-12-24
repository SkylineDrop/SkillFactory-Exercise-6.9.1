from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(3)
circle_2 = Circle(6)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_area())
    if isinstance(figure, Square):
        print(figure.get_squared_area())
    if isinstance(figure, Circle):
        print(figure.get_circle_area())
