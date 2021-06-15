import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        self.__x2 = x
        self.__y2 = y

        self.__dy = abs(self.__y2 - self.__y)
        self.__dx = abs(self.__x2 - self.__x)
        self.__distance = math.hypot(self.__dy, self.__dx)
        return self.__distance

    def distance_from_point(self, point):
        self.__x2 = point.getx()
        self.__y2 = point.gety()

        self.__dy = abs(self.__y2 - self.__y)
        self.__dx = abs(self.__x2 - self.__x)
        self.__distance = math.hypot(self.__dy, self.__dx)
        return self.__distance


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__face1 = vertice1.distance_from_point(vertice2)
        self.__face2 = vertice1.distance_from_point(vertice3)
        self.__face3 = vertice2.distance_from_point(vertice3)

    def perimeter(self):
        self.__perim = self.__face1 + self.__face2 + self.__face3
        return self.__perim


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
