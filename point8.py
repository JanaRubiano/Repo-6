import point7 


if __name__ == '__main__':
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))
    c = float(input("Enter a number: "))
    d = float(input("Enter a number: "))
    e = float(input("Enter a number: "))
    av = point7.average(a, b, c, d, e)
    med = point7.median(a, b, c, d, e)
    mult_av = point7.multiplicative_average(a, b, c, d, e) 
    asc = point7.ascending (a, b, c, d, e)
    desc = point7.descending(a, b, c, d, e)
    power = point7.fifth_to_the_power_of_first(a, b, c, d, e)
    cub = point7.cube_first(a, b, c, d, e)

    print("average: " + str(av))
    print ("median: " + str(med))
    print ("multiplicative average: " + str(mult_av))
    print("ascending: " + str(asc))
    print("descending: " + str(desc))
    print("largest value to the power of the smallest: " + str(power))
    print("The cube root of the smallest value: " + str(cub))
    