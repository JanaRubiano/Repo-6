def loan(c:float, i:float, n:int) -> float:
    interest = i * c / 100
    return c + n * interest

if __name__ == '__main__':
    c = float(input("Enter a value c in pesos: "))
    i = float(input("Enter a value i '%' of interest: "))
    n = float(input("Enter a value n of months: "))
    l = loan(c, i, n)
    print("The value to be payed is: " + str(l))