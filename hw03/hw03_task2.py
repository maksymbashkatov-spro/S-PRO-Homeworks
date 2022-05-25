class Point2D:
    __point_counter = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point2D.__point_counter += 1

    @staticmethod
    def get_point_counter():
        return Point2D.__point_counter

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def distance(self, point2d):
        return round(((self.__x - point2d.x) ** 2 + (self.__y - point2d.y) ** 2) ** 0.5, 3)


class Point3D(Point2D):
    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def distance(self, point3d):
        return round(((self.x - point3d.x) ** 2 +
                      (self.y - point3d.y) ** 2 +
                      (self.__z - point3d.z) ** 2) ** 0.5, 3)


print('Тестирование в 2х мерном пространстве.')
p2d1 = Point2D(0, 2)
p2d2 = Point2D(3, 4)
print(Point2D.get_point_counter())
print(p2d1.distance(p2d2))

print('\n', 'Тестирование в 3х мерном пространстве.', sep='')
p3d1 = Point3D(0, 2, 3)
p3d2 = Point3D(3, 4, 2)
print(Point3D.get_point_counter())
print(p3d1.distance(p3d2))
