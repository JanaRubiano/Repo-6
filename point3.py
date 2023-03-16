def kilograms_meat(N:int, M:int, K:int) -> int:
    return N*6 + M*7 + K*1

if __name__ == '__main__':
    N = int(input("Enter a number N of chickens: "))
    M = int(input("Enter a number M of roosters: "))
    K = int(input("Enter a number K of chicks: "))
    meat = kilograms_meat(N, M, K)
    print("Kilograms of meat is: " + str(meat))