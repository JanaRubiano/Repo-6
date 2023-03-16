def covid_inf(D:int, C:int) -> float:
    return C*2**D

if __name__ == '__main__':
    D = int(input("Enter D number of days: "))
    C = int(input("Enter C number of initial people: "))
    infected = covid_inf(D, C)
    print(infected)
    