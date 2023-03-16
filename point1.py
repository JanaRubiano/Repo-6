import math
def volume(r1:float, r2:float, h:float) -> float:
    sphere = (4/3) * (r1**3) * math.pi
    cone = (h/3) * (r2**2) * math.pi
    return sphere + cone    

def area(r1:float, r2:float, h:float) -> float:
    sphere = 4 * math.pi * r1**2
    slant_height = math.sqrt(h**2 + r2**2)
    cone = (math.pi * r2 * slant_height) + (math.pi * r2**2)
    return sphere + cone

if __name__ == '__main__':
    r1 = float(input("Enter r1 in cm: "))
    r2 = float(input("Enter r2 in cm: "))
    h = float(input("Enter h in cm: "))
    vol = volume(r1, r2, h)
    a = area(r1, r2, h)
    print("The figure's volume is: " + str(vol))
    print("The figure's area is: " + str(a))



    

