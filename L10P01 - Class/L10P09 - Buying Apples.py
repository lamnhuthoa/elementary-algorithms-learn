# Bai 9
# Buying Apples
'''
Imak wants to buy apples. Imak's critea: they have to be big and heavy. 
But in the shop, there are many apples with the same weight then they still have different prices. 
Imak thinks that the heaviest apple is the best. 
Therefore, he will choose the most expensive one out of apples with the same largest weight.

n apples are arranged along a line from left to right, numbered starting from 0. Each apple is labeled with its weight and price. Imak want to know which apple (counted from left) to choose.

Input:
First line is a positive integer n(n <= 1.000), the number of apples in the shop.

The next n lines, each contains 2 positive integers: weight w and price p of the i-th apple (0 <= i < n, 0 < w,p <= 1.000).

Ensure that no apples are the same.

Output:
A single line with the position of the apple Imak should buy.
'''
class Apple:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        
    
class AppleSelector:
    def __init__(self):
        self.apples = []
        
    def add_apple(self, apple):
        self.apples.append(apple)
        
    def select_apple(self):
        if not self.apples:
            return -1
        
        heaviest_weight = max(apple.weight for apple in self.apples)
        candidates = [apple for apple in self.apples if apple.weight == heaviest_weight]
        most_expensive_apple = max(candidates, key=lambda apple: apple.price)
        
        return self.apples.index(most_expensive_apple)
    
num_of_apples = int(input())
selector = AppleSelector()

for _ in range(num_of_apples):
    weight, price = map(int, input().split())
    apple = Apple(weight, price)
    selector.add_apple(apple)
    
selected_index = selector.select_apple()
print(selected_index)