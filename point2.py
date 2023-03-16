import math
def perimeter(r:float, a:float, b:float) -> float:
    rectangle = 2*b + 2*a
    wheel = 2 * math.pi * r
    return rectangle + 2 * wheel    

def area(r:float, a:float, b:float) -> float:
    rectangle = a * b
    wheel = math.pi * r**2
    return rectangle + 2 * wheel 

if __name__ == '__main__':
    r = float(input("Enter r1 in cm: "))
    a = float(input("Enter r2 in cm: "))
    b = float(input("Enter h in cm: "))
    p = perimeter(r, a, b)
    a = area(r, a, b)
    print("The figure's perimeter: " + str(p))
    print("The figure's area is: " + str(a))