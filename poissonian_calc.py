import math as m

def calc_red():
    print("Enter upper bound of the series:")
    n = int(input())
    print("Enter the value of lambda:")
    l = int(input())
    e = m.e ** (-l)
    sum = 0
    for i in range(0, n+1):
        sum += (l ** i) / (m.factorial(i))

    print(sum * e)


def calc_value():
    print("Enter the value of lambda")
    l = int(input())
    print("Enter the value")
    v = float(input())

    e = m.e**(-l)
    print(((l**v)/(m.factorial(v))) * e)



if __name__ == "__main__":

    print("Choose your calculation of interest? \n 1 - Calculate Series \n 0 - Calculate for a given probability value ")
    choice = int(input())

    if choice == 1:
        calc_red()
    elif choice == 0:
        calc_value()
    else:
        print("Enter 1 or 0")




