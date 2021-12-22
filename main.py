# # C = 2πR
# from math import pi
#
#
# class Circle:
#     all_circles = []
#
#     def __init__(self, rad):
#         self.raduis = rad
#         self.__class__.all_circles.append(self)
#
#     def circle_len(self):
#         return 2 * pi * self.raduis
#
#     @classmethod
#     def total_len(cls):
#         total = 0
#         for circle in cls.all_circles:
#             total += circle.circle_len()
#         return print(total)
#
#
# val = Circle(2)
# val.circle_len()
# val.total_len()

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, delta_x, delta_y):
#         self.x = self.x + delta_x
#         self.y = self.y + delta_y
#
#
# class Square(Shape):
#     def __init__(self, side=1, x=0, y=0):
#         super().__init__(x, y)
#         self.side = side
#
#
# class Circle(Shape):
#     pi = 3.14159
#     all_circles = []
#
#     def __init__(self, radius=1, x=0, y=0):
#         super().__init__(x, y)
#         self.radius = radius
#         self.all_circles.append(self)
#
#     @classmethod
#     def total_area(cls):
#         area = 0
#         for circle in cls.all_circles:
#             area += cls.circle_area(circle.radius)
#         return area
#
#     @staticmethod
#     def circle_area(radius):
#         return __class__.pi * radius * radius


# class Rectangle():
#     def __init__(self, x, y):
#             self.x = x
#             self.y = y
#
#     @staticmethod
#     def area(x, y):
#         return x * y
#
# class Square(Rectangle):
#     def __init__(self, x):
#         self.y = y
#
#
#
#
# rec = Rectangle(3, 2)
# print(rec.area(3, 2))
# sq = Square(3)
# print(sq.area(3))


class Rectangle():
    all_rectangle = []                                     с

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.all_rectangle.append(self)

    @classmethod
    def total_area(cls):
        area = 0
        for rectangle in cls.all_rectangle:
            area += cls.area(rectangle.a, rectangle.b)
        return area

    @staticmethod
    def area(a, b):
        return a * b


class Square(Rectangle):
    all_square = []

    def __init__(self, a):
        super().__init__(a, b=a)
        self.all_square.append(self)

    @classmethod
    def total_area(cls):
        area = 0
        for square in cls.all_square:
            area += cls.area(square.a, square.b)
        return area


rec = Rectangle(3, 2)
print(rec.area(3, 2))
sq = Square(3)
print(sq.area(3, 3))