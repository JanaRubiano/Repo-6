# Repo-6
1. Calculate the surface area and volume of the the figure.

2. Calculate the perimeter and area of the the figure.

3.  Calculate the meat in kilograms of N chickens, M rooster and K chicks.

4. Calcultae the diference if I have to buy P breads of $300, M milk bags of 3300 and H eggs of 350 each one, and I am given B pesos. 

5. Make a function to calculate the value of a loan c with compound interest of i for n months.

6. Find the number of Covid-19 infected people after D days, with C initial infected people, given that the number of infections doubles every day.

7. Write a program that given 5 numbers calculates: Average, median, multiplicative average, numbers in acending order, numbers in descending order, the largest value to the power of the smallest value, and the cubic root of the smallest value. (Each function in an independent file.)

8. For the previous point, import them to a file for their use.

9. Research what pip is in python and how it works.

10. Make a list of popular python modules that can be installed with pip and how to install them.


def covid_inf(D:int, C:int) -> float:
    return C*2**D
if __name__ == '__main__':
    D = int(input("Enter D number of days: "))
    C = int(input("Enter C number of initial people: "))
    infected = covid_inf(D, C)
    print(infected)
