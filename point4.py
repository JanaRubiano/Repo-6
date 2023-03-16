def change(P:int, M:int, H:int, B:float) -> float:
    difference = B - (P*300) - (M*3300) - (H*350)
    return difference

if __name__ == '__main__':
    P = int(input("Enter a number P of breads: "))
    M = int(input("Enter a number M of milk bags: "))
    H = int(input("Enter a number H of eggs: "))
    B = float(input("Enter a number B of pesos (money): "))
    ch = change(P, M, H, B)
    print("The difference, what was left or what is missing is: " + str(ch))