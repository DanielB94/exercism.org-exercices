
def is_triangle(sides): # DRY PRINCIPLE
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c # COMPARISIONS returns BOOLEANS no need for if
    
def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3