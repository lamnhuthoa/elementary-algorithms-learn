# Bai 2
# The Furthest Points
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __str__(self):
        return f"{self.x} {self.y}"
    
    
class FurthestPointFinder:
    def __init__(self, reference_point):
        self.reference_point = reference_point
        self.points = []
        
    def add_point(self, point):
        self.points.append(point)
        
        
    def find_furthest_point(self):
        if not self.points:
            return None
        
        max_distance = -1
        furthest_point = None
        
        for point in self.points:
            distance = self.reference_point.distance_to(point)
            if distance > max_distance:
                max_distance = distance
                furthest_point = point
        
        return furthest_point
    
    
def main():
    mx, my = map(int, input().split())
    point_m = Point(mx, my)
    
    n = int(input())
    
    finder = FurthestPointFinder(point_m)
    
    for _ in range(n):
        x, y = map(int, input().split())
        finder.add_point(Point(x, y))
        
        
    furthest = finder.find_furthest_point()
    if furthest:
        print(furthest)
        
        
if __name__ == "__main__":
    main()