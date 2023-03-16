
def ascending(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        first = a
    elif b <= a and b <= c and b <= d and b <= e :
        first  = b
    elif c <= a and c <= b and c <= d and c <= e :
        first  = c
    elif d <= a and d <= b and d <= c and d <= e :
        first  = d
    else :
        first  = e

    if a >= b and a >= c and a >= d and a >= e :
        fifth = a
    elif b >= a and b >= c and b >= d and b >= e :
        fifth = b
    elif c >= a and c >= b and c >= d and c >= e :
        fifth = c
    elif d >= a and d >= b and d >= c and d >= e :
        fifth = d
    else:
        fifth = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        second = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
     second = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        second = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        second = d
    else:
        second = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        forth = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        forth = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        forth = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        forth = d
    else:
        forth = e

    if second < a < forth :
        third = a
    elif second < b < forth :
        third = b
    elif second < c < forth :
        third = c
    elif second < d < forth :
        third = d
    else:
        third = e

    return first, second, third, forth, fifth
    
def descending(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        first = a
    elif b <= a and b <= c and b <= d and b <= e :
        first  = b
    elif c <= a and c <= b and c <= d and c <= e :
        first  = c
    elif d <= a and d <= b and d <= c and d <= e :
        first  = d
    else :
        first  = e

    if a >= b and a >= c and a >= d and a >= e :
        fifth = a
    elif b >= a and b >= c and b >= d and b >= e :
        fifth = b
    elif c >= a and c >= b and c >= d and c >= e :
        fifth = c
    elif d >= a and d >= b and d >= c and d >= e :
        fifth = d
    else:
        fifth = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        second = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
     second = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        second = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        second = d
    else:
        second = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        forth = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        forth = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        forth = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        forth = d
    else:
        forth = e

    if second < a < forth :
        third = a
    elif second < b < forth :
        third = b
    elif second < c < forth :
        third = c
    elif second < d < forth :
        third = d
    else:
        third = e

    return fifth, forth, third, second, first

def average(a:float, b:float, c:float, d:float, e:float) -> float:
    return (a + b + c + d + e)/5

def median(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        first = a
    elif b <= a and b <= c and b <= d and b <= e :
        first  = b
    elif c <= a and c <= b and c <= d and c <= e :
        first  = c
    elif d <= a and d <= b and d <= c and d <= e :
        first  = d
    else :
        first  = e

    if a >= b and a >= c and a >= d and a >= e :
        fifth = a
    elif b >= a and b >= c and b >= d and b >= e :
        fifth = b
    elif c >= a and c >= b and c >= d and c >= e :
        fifth = c
    elif d >= a and d >= b and d >= c and d >= e :
        fifth = d
    else:
        fifth = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        second = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
     second = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        second = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        second = d
    else:
        second = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        forth = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        forth = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        forth = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        forth = d
    else:
        forth = e

    if second < a < forth :
        third = a
    elif second < b < forth :
        third = b
    elif second < c < forth :
        third = c
    elif second < d < forth :
        third = d
    else:
        third = e

    return third

def multiplicative_average(a:float, b:float, c:float, d:float, e:float) -> float:
    return (a*b*c*d*e)**0.20

def fifth_to_the_power_of_first(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        first = a
    elif b <= a and b <= c and b <= d and b <= e :
        first  = b
    elif c <= a and c <= b and c <= d and c <= e :
        first  = c
    elif d <= a and d <= b and d <= c and d <= e :
        first  = d
    else :
        first  = e

    if a >= b and a >= c and a >= d and a >= e :
        fifth = a
    elif b >= a and b >= c and b >= d and b >= e :
        fifth = b
    elif c >= a and c >= b and c >= d and c >= e :
        fifth = c
    elif d >= a and d >= b and d >= c and d >= e :
        fifth = d
    else:
        fifth = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        second = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
     second = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        second = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        second = d
    else:
        second = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        forth = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        forth = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        forth = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        forth = d
    else:
        forth = e

    if second < a < forth :
        third = a
    elif second < b < forth :
        third = b
    elif second < c < forth :
        third = c
    elif second < d < forth :
        third = d
    else:
        third = e

    return fifth**first

def cube_first(a:float, b:float, c:float, d:float, e:float) -> float:
    if a <= b and a <= c and a <= d and a <= e :
        first = a
    elif b <= a and b <= c and b <= d and b <= e :
        first  = b
    elif c <= a and c <= b and c <= d and c <= e :
        first  = c
    elif d <= a and d <= b and d <= c and d <= e :
        first  = d
    else :
        first  = e

    if a >= b and a >= c and a >= d and a >= e :
        fifth = a
    elif b >= a and b >= c and b >= d and b >= e :
        fifth = b
    elif c >= a and c >= b and c >= d and c >= e :
        fifth = c
    elif d >= a and d >= b and d >= c and d >= e :
        fifth = d
    else:
        fifth = e

    if (a >= b and a <= c and a <= d and a <= e) or (a >= c and a <= b and a <= d and a <= e) or (a >= d and a <= b and a <= c and a <= e) or (a >= e and a <= b and a <= c and a <= d) :
        second = a
    elif (b >= a and b <= c and b <= d and b <= e) or (b >= c and b <= a and b <= d and b <= e) or (b >= d and b <= c and b <= a and b <= e) or (b >= e and b <= c and b <= d and b <= a) :
     second = b
    elif (c >= a and c <= a and c <= d and c <= e) or (c >= b and c <= a and c <= d and c <= e) or (c >= d and c <= a and c <= b and c <= e) or (c >= e and c <= a and c <= d and c <= b) :
        second = c
    elif (d >= b and d <= c and d <= a and d <= e) or (d >= c and d <= b and d <= a and d <= e) or (d >= a and d <= c and d <= b and d <= e) or (d >= e and d <= c and d <= a and d <= b) :
        second = d
    else:
        second = e

    if (a <= b and a >= c and a >= d and a >= e) or (a <= c and a >= b and a >= d and a >= e) or (a <= d and a >= c and a >= b and a >= e) or (a <= e and a >= c and a >= d and a >= b) :
        forth = a
    elif (b <= a and b >= c and b >= d and b >= e) or (b <= c and b >= a and b >= d and b >= e) or (b <= d and b >= c and b >= a and b >= e) or (b <= e and b >= c and b >= d and b >= a) :
        forth = b
    elif (c <= a and c >= a and c >= d and c >= e) or (c <= b and c >= a and c >= d and c >= e) or (c <= d and c >= a and c >= b and c >= e) or (c <= e and c >= a and c >= d and c >= b) :
        forth = c
    elif (d <= b and d >= c and d >= a and d >= e) or (d <= c and d >= b and d >= a and d >= e) or (d <= a and d >= c and d >= b and d >= e) or (d <= e and d >= c and d >= a and d >= b) :
        forth = d
    else:
        forth = e

    if second < a < forth :
        third = a
    elif second < b < forth :
        third = b
    elif second < c < forth :
        third = c
    elif second < d < forth :
        third = d
    else:
        third = e

    return first**(1/3)


if __name__ == '__main__':
    a = float (input("Enter a number: "))
    b = float (input("Enter a number: "))
    c = float (input("Enter a number: "))
    d = float (input("Enter a number: "))
    e = float (input("Enter a number: "))
    av = average(a, b, c, d, e)
    med = median(a, b, c, d, e)
    mult_av = multiplicative_average(a, b, c, d, e) 
    asc = ascending (a, b, c, d, e)
    desc = descending(a, b, c, d, e)
    power = fifth_to_the_power_of_first(a, b, c, d, e)
    cub = cube_first(a, b, c, d, e)

    print("average: " + str(av))
    print ("median: " + str(med))
    print ("multiplicative average: " + str(mult_av))
    print("ascending: " + str(asc))
    print("descending: " + str(desc))
    print("largest value to the power of the smallest: " + str(power))
    print("The cube root of the smallest value: " + str(cub))
    