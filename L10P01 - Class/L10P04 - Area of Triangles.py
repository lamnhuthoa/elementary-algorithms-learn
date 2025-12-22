# Bai 4
# Area of the Triangles
import math

num_of_triangles = int(input())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __str__(self):
        return f"{self.x} {self.y}"

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calc_area(self):
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

class TrianglesAreaCalculator:
    def __init__(self):
        self.triangles = []

    def add_triangle(self, triangle):
        self.triangles.append(triangle)

    def total_area(self):
        total = 0
        for triangle in self.triangles:
            total += triangle.calc_area()
        return total
    
calculator = TrianglesAreaCalculator()

for _ in range(num_of_triangles):
    points = []
    for _ in range(3):
        x, y = map(float, input().split())
        points.append(Point(x, y))

    triangle = Triangle(points[0], points[1], points[2])
    calculator.add_triangle(triangle)

total = calculator.total_area()
print(f"{total:.2f}")