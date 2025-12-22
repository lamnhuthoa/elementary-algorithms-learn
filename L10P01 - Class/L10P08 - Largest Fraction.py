# Bai 8
# The largest fraction
# Given an array of N fractions, find the largest fraction (reduce the fractions if necessary).
# Input: The first line contains an integer n (0 < n <= 100) - the number of fractions.
# The next N lines, each contains numerator and denominator of a fraction.
# Numerators and denominators are non-negative integers that do not exceed 1.000. Denominators is not equal to 0.
# Output: A single line contains numerator and denominator of a the largest fraction.

class Fraction:
    def __init__(self, num = 0, denom = 1):
        self.num = num
        self.denom = denom
        
    def reduce_fraction(self):
        if self.num == 0:
            self.denom = 1
            return
        x = self.gcd(abs(self.num), abs(self.denom))
        self.num = self.num // x
        self.denom = self.denom // x
        
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def is_greater_than(self, reference_fraction):
        return (self.num / self.denom) > (reference_fraction.num / reference_fraction.denom)
    
        
class LargestFractionFinder:
    def __init__(self):
        self.fractions = []
        
    def add_fraction(self, fraction):
        self.fractions.append(fraction)
        
    def find_largest_fraction(self):
        if not self.fractions:
            return None
        
        largest_fraction = self.fractions[0]
        
        for fraction in self.fractions[1:]:
            if fraction.is_greater_than(largest_fraction):
                largest_fraction = fraction
                
        return largest_fraction
    
    
num_of_fractions = int(input())
finder = LargestFractionFinder()

for _ in range(num_of_fractions):
    num, denom = map(int, input().split())
    fraction = Fraction(num, denom)
    fraction.reduce_fraction()
    finder.add_fraction(fraction)
    
largest_fraction = finder.find_largest_fraction()
print(f"{largest_fraction.num} {largest_fraction.denom}")